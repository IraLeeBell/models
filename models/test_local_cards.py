"""Local-only download guard and conversion checks; no publisher files are used."""

import hashlib
import tempfile
import textwrap
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import pymupdf

import local_cards


def make_pdf(path, title, body, *, metadata_title=""):
    with pymupdf.open() as document:
        document.set_metadata({"title": metadata_title})
        page = document.new_page()
        page.insert_text((30, 50), title + "\n" + textwrap.fill(body, width=75), fontsize=11)
        document.save(path)
    return hashlib.sha256(path.read_bytes()).hexdigest()


def entry(sha, title="Model Card: Grok 4.7", name="Grok 4.7"):
    return {
        "slug": "grok-4.7", "name": name, "provider": "xAI",
        "card": {"url": "https://media.x.ai/v1/website/4p7card-5eccc980.pdf",
                 "title": title, "sha256": sha},
    }


class LocalCardsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.card = self.root / "original.pdf"
        self.body = "This original test PDF checks that content is selected and rendered to Markdown. " * 4
        self.hash = make_pdf(self.card, "Model Card: Grok 4.7", self.body)
        self.model = entry(self.hash)

    def test_cached_pdf_is_verified_and_extracted(self):
        folder = self.root / "grok-4.7"
        folder.mkdir()
        pdf = folder / "system-card.pdf"
        pdf.write_bytes(self.card.read_bytes())
        with patch.object(local_cards, "download", side_effect=AssertionError("no download")):
            local_cards.build(self.model, self.root, refresh=False)
            first = (folder / "system-card.md").read_bytes()
            local_cards.build(self.model, self.root, refresh=False)
        self.assertEqual(pdf.read_bytes(), self.card.read_bytes())
        self.assertEqual((folder / "system-card.md").read_bytes(), first)
        self.assertIn("Model Card: Grok 4.7", (folder / "system-card.md").read_text())

    def test_bad_cached_hash_does_not_replace_markdown(self):
        folder = self.root / "grok-4.7"
        folder.mkdir()
        (folder / "system-card.pdf").write_bytes(b"%PDF-bad")
        md = folder / "system-card.md"
        md.write_text("existing local notes")
        with self.assertRaisesRegex(local_cards.CardError, "hash mismatch"):
            local_cards.build(self.model, self.root, refresh=False)
        self.assertEqual(md.read_text(), "existing local notes")

    def test_refresh_replaces_invalid_cache_only_after_verification(self):
        folder = self.root / "grok-4.7"
        folder.mkdir()
        pdf = folder / "system-card.pdf"
        pdf.write_bytes(b"%PDF-bad")

        def mock_download(_model, destination):
            destination.write_bytes(self.card.read_bytes())

        with patch.object(local_cards, "download", side_effect=mock_download):
            local_cards.build(self.model, self.root, refresh=True)
        self.assertEqual(pdf.read_bytes(), self.card.read_bytes())
        self.assertIn("Grok 4.7", (folder / "system-card.md").read_text())

    def test_refresh_failure_preserves_existing_cache(self):
        folder = self.root / "grok-4.7"
        folder.mkdir()
        pdf = folder / "system-card.pdf"
        md = folder / "system-card.md"
        pdf.write_bytes(self.card.read_bytes())
        md.write_text("existing extraction")

        def mock_download(_model, destination):
            destination.write_bytes(b"not a PDF")

        with patch.object(local_cards, "download", side_effect=mock_download):
            with self.assertRaisesRegex(local_cards.CardError, "Not a PDF"):
                local_cards.build(self.model, self.root, refresh=True)
        self.assertEqual(pdf.read_bytes(), self.card.read_bytes())
        self.assertEqual(md.read_text(), "existing extraction")

    def test_wrong_title_with_valid_hash_fails(self):
        sha = make_pdf(self.card, "Model Card: Grok 4.6", self.body)
        with self.assertRaisesRegex(local_cards.CardError, "title does not match"):
            local_cards.verified_document(self.card, entry(sha))

    def test_shared_card_without_model_fails(self):
        sha = make_pdf(self.card, "GPT-6 Astra System Card", self.body)
        model = entry(sha, title="GPT-6 Astra System Card", name="GPT-6 Luna")
        with self.assertRaisesRegex(local_cards.CardError, "does not identify"):
            local_cards.verified_document(self.card, model)

    def test_non_pdf_with_matching_hash_fails(self):
        self.card.write_bytes(b"<!doctype html>Login required")
        with self.assertRaisesRegex(local_cards.CardError, "Not a PDF"):
            local_cards.verified_document(self.card, entry(local_cards.sha256(self.card)))

    def test_download_rejects_html_content_type(self):
        result = SimpleNamespace(
            returncode=0, stderr="",
            stdout="200\ntext/html\nhttps://media.x.ai/v1/website/4p7card-5eccc980.pdf",
        )
        with patch.object(local_cards.subprocess, "run", return_value=result):
            with self.assertRaisesRegex(local_cards.CardError, "Expected application/pdf"):
                local_cards.download(self.model, self.card)

    def test_download_rejects_redirect_to_non_publisher(self):
        result = SimpleNamespace(
            returncode=0, stderr="", stdout="200\napplication/pdf\nhttps://example.com/card.pdf"
        )
        with patch.object(local_cards.subprocess, "run", return_value=result):
            with self.assertRaisesRegex(local_cards.CardError, "redirected outside"):
                local_cards.download(self.model, self.card)

    def test_moonshot_octet_stream_is_allowed_only_for_owner(self):
        model = {
            "provider": "Moonshot AI",
            "card": {"url": "https://raw.githubusercontent.com/MoonshotAI/Kimi-K3/main/k3_tech_report.pdf"},
        }
        result = SimpleNamespace(
            returncode=0, stderr="",
            stdout="206\napplication/octet-stream\n"
            "https://raw.githubusercontent.com/MoonshotAI/Kimi-K3/main/k3_tech_report.pdf",
        )
        with patch.object(local_cards.subprocess, "run", return_value=result):
            local_cards.download(model, self.card)
            result.stdout = result.stdout.replace("MoonshotAI/Kimi-K3/", "another-org/another-repo/")
            with self.assertRaisesRegex(local_cards.CardError, "Unexpected Moonshot"):
                local_cards.download(model, self.card)

    def test_missing_and_html_only_documents_fail(self):
        model = {**self.model, "card": None}
        with self.assertRaisesRegex(local_cards.CardError, "no matching publisher PDF"):
            local_cards.build(model, self.root, refresh=False)
        model["card"] = {"url": "https://deploymentsafety.openai.com/gpt-6-1-sol"}
        with self.assertRaisesRegex(local_cards.CardError, "HTML, not a PDF"):
            local_cards.build(model, self.root, refresh=False)

    def test_download_failure_does_not_leave_local_artifact(self):
        folder = self.root / "grok-4.7"
        with patch.object(
            local_cards.subprocess, "run",
            return_value=SimpleNamespace(returncode=22, stderr="HTTP 404", stdout=""),
        ):
            with self.assertRaisesRegex(local_cards.CardError, "HTTP 404"):
                local_cards.build(self.model, self.root, refresh=False)
        self.assertFalse(folder.exists())


if __name__ == "__main__":
    unittest.main()
