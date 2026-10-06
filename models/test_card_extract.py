"""Tests for card_extract.py: page markers, plain-text fallback, and TeX delimiter mapping."""

import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

import pymupdf

import card_extract


def page_record(number, markdown, status="ok", extra=None):
    return {"page": number, "tokens": 5, "coverage": 1.0 if status == "ok" else 0.5, "images": 0,
            "markdown": markdown, "status": status, "extra": extra, "delimiters": 0}


class RenderTest(unittest.TestCase):
    def test_markers_and_fallback(self):
        pages = [page_record(1, "# Title"), page_record(2, "partial", "fallback", "full page two text")]
        text = card_extract.render(pages, ["Title: Example"])
        self.assertTrue(card_extract.check_markdown(text, 2))
        self.assertIn("````text\nfull page two text\n````", text)
        self.assertIn("1 pages also carry their verbatim plain text", text)
        self.assertFalse(card_extract.check_markdown(text, 3))
        self.assertFalse(card_extract.check_markdown(text.replace("<!-- page 2 of 2 -->", ""), 2))

    def test_extract_real_pdf(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "a.pdf"
            with pymupdf.open() as document:
                for word in ("alpha", "beta", "gamma"):
                    document.new_page().insert_text((40, 60), f"Section {word} has selectable text.")
                document.save(path)
            with pymupdf.open(path) as document:
                pages = card_extract.extract_pages(document)
        self.assertEqual([p["page"] for p in pages], [1, 2, 3])
        self.assertTrue(all(p["status"] == "ok" for p in pages))
        self.assertEqual(card_extract.summary(pages)["pages_ok"], 3)


class CmexTest(unittest.TestCase):
    def fake_page(self, spans):
        blocks = [{"lines": [{"spans": [{"font": font, "text": text} for font, text in spans]}]}]
        return SimpleNamespace(get_text=lambda kind="text": {"blocks": blocks})

    def test_maps_only_codes_from_cmex_spans(self):
        page = self.fake_page([("ABCDEF+CMEX10", "\x00\x01\x12\x13"), ("Times", "text\x05")])
        table = card_extract.cmex_table(page)
        self.assertEqual("\x00x\x01 \x12y\x13".translate(table), "(x) (y)")
        self.assertNotIn(0x05, table)

    def test_newline_is_never_remapped(self):
        page = self.fake_page([("CMEX10", "\x0a\x0d\x08")])
        self.assertEqual(card_extract.cmex_table(page), {0x08: "{"})


if __name__ == "__main__":
    unittest.main()
