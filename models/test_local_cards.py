"""Download guard, verification, and extraction tests for local_cards.py (synthetic PDFs only)."""

import hashlib
import tempfile
import textwrap
import unittest
from pathlib import Path
from unittest.mock import patch

import pymupdf

import card_extract
import local_cards


def make_pdf(path, title, body, pages=1):
    with pymupdf.open() as document:
        for number in range(pages):
            page = document.new_page()
            page.insert_text((30, 50), (title if number == 0 else f"Page {number + 1}") + "\n"
                             + textwrap.fill(body, width=75), fontsize=11)
        document.save(path)
    data = path.read_bytes()
    return hashlib.sha256(data).hexdigest(), len(data)


def pdf_doc(sha, size, pages=2, **extra):
    return {"publisher": "xAI", "title": "Grok 4.7 Model Card", "title_check": "Grok 4.7 Model Card",
            "date": "2026-08-01", "format": "pdf", "url": "https://media.x.ai/v1/website/card.pdf",
            "bytes": size, "pages": pages, "sha256": sha, "retrieved": "2026-10-06", "rights": "not-granted",
            **extra}


class LocalCardsTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.out = Path(tmp.name) / "out"
        self.card = Path(tmp.name) / "card.pdf"
        body = "This synthetic card describes Grok 4.7 evaluations and safety mitigations in plain words. " * 3
        sha, size = make_pdf(self.card, "Grok 4.7 Model Card", body, pages=2)
        self.doc = pdf_doc(sha, size)
        self.base = local_cards.ROOT / "grok-4.7" / "system-card"
        self.folder = self.out / "grok-4.7"

    def build(self, **kwargs):
        return local_cards.build("xai-grok-4-7", self.doc, self.base, ["Grok 4.7"], output_root=self.out, **kwargs)

    def test_existing_pdf_is_verified_and_extracted_without_download(self):
        self.folder.mkdir(parents=True)
        (self.folder / "system-card.pdf").write_bytes(self.card.read_bytes())
        with patch.object(local_cards, "download", side_effect=AssertionError("no download expected")):
            report = self.build()
        text = (self.folder / "system-card.md").read_text(encoding="utf-8")
        self.assertTrue(card_extract.check_markdown(text, 2))
        self.assertIn(self.doc["sha256"], text[:3000])
        self.assertIn("not licensed for redistribution", text)
        self.assertEqual(report["pages"], 2)

    def test_pdf_cache_is_used_and_copied(self):
        cache = self.out / "cache"
        cache.mkdir(parents=True)
        (cache / f"{self.doc['sha256']}.pdf").write_bytes(self.card.read_bytes())
        with patch.object(local_cards, "download", side_effect=AssertionError("no download expected")):
            self.build(cache=cache)
        self.assertEqual((self.folder / "system-card.pdf").read_bytes(), self.card.read_bytes())

    def test_hash_mismatch_preserves_existing_files(self):
        self.folder.mkdir(parents=True)
        (self.folder / "system-card.pdf").write_bytes(b"%PDF-1.7 not the cataloged file")
        (self.folder / "system-card.md").write_text("existing notes")
        with self.assertRaisesRegex(local_cards.CardError, "SHA-256 mismatch"):
            self.build()
        self.assertEqual((self.folder / "system-card.md").read_text(), "existing notes")

    def test_refresh_downloads_and_failure_keeps_previous_copy(self):
        self.folder.mkdir(parents=True)
        pdf = self.folder / "system-card.pdf"
        pdf.write_bytes(b"%PDF-old")
        with patch.object(local_cards, "download", side_effect=local_cards.CardError("offline")):
            with self.assertRaises(local_cards.CardError):
                self.build(refresh=True)
        self.assertEqual(pdf.read_bytes(), b"%PDF-old")
        with patch.object(local_cards, "download",
                          side_effect=lambda _doc, path: path.write_bytes(self.card.read_bytes())):
            self.build(refresh=True)
        self.assertEqual(pdf.read_bytes(), self.card.read_bytes())

    def test_scope_terms_and_title_are_required(self):
        self.folder.mkdir(parents=True)
        (self.folder / "system-card.pdf").write_bytes(self.card.read_bytes())
        with self.assertRaisesRegex(local_cards.CardError, "does not mention"):
            local_cards.build("x", self.doc, self.base, ["Grok 9"], output_root=self.out)
        with self.assertRaisesRegex(local_cards.CardError, "front matter"):
            local_cards.build("x", {**self.doc, "title_check": "Other Card"}, self.base, [], output_root=self.out)

    def test_page_count_must_match(self):
        self.folder.mkdir(parents=True)
        (self.folder / "system-card.pdf").write_bytes(self.card.read_bytes())
        with self.assertRaisesRegex(local_cards.CardError, "pages"):
            local_cards.build("x", {**self.doc, "pages": 3}, self.base, [], output_root=self.out)

    def test_granted_header_names_license(self):
        granted = {**self.doc, "rights": "granted", "copyright": "Copyright (c) 2026 Example",
                   "license_name": "Example License", "license_file": "LICENSE-Example.txt"}
        lines = local_cards.header("doc", granted)
        self.assertIn("Copyright (c) 2026 Example. Redistributed under the Example License "
                      "(LICENSE-Example.txt in this folder).", lines)

    def test_markdown_owner_document_is_written_verbatim(self):
        source = self.out / "owner.md"
        source.parent.mkdir(parents=True)
        source.write_text("# Example Model Card\n\nDetails.\n", encoding="utf-8")
        data = source.read_bytes()
        doc = {**self.doc, "format": "markdown", "pages": None, "title_check": "Example Model Card",
               "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
        base = local_cards.ROOT / "example" / "model-card"
        with patch.object(local_cards, "download", side_effect=lambda _doc, path: path.write_bytes(data)):
            local_cards.build("doc", doc, base, [], output_root=self.out)
        self.assertEqual((self.out / "example" / "model-card.md").read_bytes(), data)


class ResponseCheckTest(unittest.TestCase):
    doc = {"publisher": "xAI", "format": "pdf", "url": "https://media.x.ai/a.pdf"}
    moonshot = {"publisher": "Moonshot AI", "format": "pdf", "url": "https://raw.githubusercontent.com/MoonshotAI/x.pdf"}

    def test_accepts_owner_pdf(self):
        local_cards.check_response(self.doc, "200", "application/pdf", "https://media.x.ai/a.pdf")

    def test_rejects_redirect_off_owner_host(self):
        with self.assertRaisesRegex(local_cards.CardError, "outside"):
            local_cards.check_response(self.doc, "200", "application/pdf", "https://media.x.ai.example.com/a.pdf")

    def test_rejects_wrong_type_and_status(self):
        with self.assertRaisesRegex(local_cards.CardError, "expected"):
            local_cards.check_response(self.doc, "200", "text/html", "https://media.x.ai/a.pdf")
        with self.assertRaisesRegex(local_cards.CardError, "HTTP 404"):
            local_cards.check_response(self.doc, "404", "application/pdf", "https://media.x.ai/a.pdf")

    def test_octet_stream_only_from_raw_github(self):
        local_cards.check_response(self.moonshot, "200", "application/octet-stream",
                                   "https://raw.githubusercontent.com/MoonshotAI/x.pdf")
        with self.assertRaises(local_cards.CardError):
            local_cards.check_response(self.doc, "200", "application/octet-stream", "https://media.x.ai/a.pdf")


if __name__ == "__main__":
    unittest.main()
