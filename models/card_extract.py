"""Page-by-page PDF to Markdown conversion with a completeness check."""

import re
import shutil
import unicodedata
from collections import Counter

import pymupdf
import pymupdf4llm

COVERAGE_FLOOR = 0.98
EXTRACTOR = f"pymupdf4llm {pymupdf4llm.__version__} (PyMuPDF {pymupdf.__version__})"
PAGE_MARKER = re.compile(r"^<!-- page (\d+) of (\d+) -->$", re.MULTILINE)


# TeX's CMEX fonts place large delimiters at code points 0x00-0x1F with no Unicode mapping, so text
# extraction yields control characters. Map them to the delimiter each glyph draws.
CMEX_DELIMITERS = dict(enumerate("()[]⌊⌋⌈⌉{}⟨⟩|‖/\\()()[]⌊⌋⌈⌉{}⟨⟩/\\"))
NEVER_REMAP = {0x0A, 0x0D}


class ExtractionError(Exception):
    """The PDF could not be converted faithfully."""


def tokens(text):
    return re.findall(r"[a-z0-9]+", unicodedata.normalize("NFKC", text).casefold())


def ocr_available():
    return shutil.which("tesseract") is not None


def cmex_table(page):
    """Translation table for the control characters that CMEX-font spans produce on this page."""
    codes = set()
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line["spans"]:
                if "CMEX" in span["font"].upper():
                    codes.update(ord(c) for c in span["text"] if ord(c) < 0x20)
    return {code: CMEX_DELIMITERS[code] for code in codes - NEVER_REMAP}


def extract_pages(document, ocr=False):
    """Return one record per page; low-coverage pages carry their verbatim plain text."""
    if ocr and not ocr_available():
        raise ExtractionError("--ocr needs the Tesseract binary on PATH")
    chunks = pymupdf4llm.to_markdown(
        document, page_chunks=True, use_ocr=False, write_images=False,
        embed_images=False, show_progress=False,
    )
    if len(chunks) != document.page_count:
        raise ExtractionError(f"Converter returned {len(chunks)} of {document.page_count} pages")
    pages = []
    for number, (page, chunk) in enumerate(zip(document, chunks), start=1):
        table = cmex_table(page)
        raw_plain, raw_markdown = page.get_text(), chunk["text"].strip()
        plain, markdown = raw_plain.translate(table), raw_markdown.translate(table)
        expected = Counter(tokens(plain))
        total = sum(expected.values())
        coverage = sum((expected & Counter(tokens(markdown))).values()) / total if total else 1.0
        record = {"page": number, "tokens": total, "coverage": round(coverage, 4),
                  "images": len(page.get_images()), "markdown": markdown,
                  "status": "ok", "extra": None,
                  "delimiters": sum(raw_markdown.count(chr(code)) for code in table)}
        if total == 0:
            record["status"] = "no-text"
            if ocr:
                text = page.get_text(textpage=page.get_textpage_ocr(full=True, dpi=300)).strip()
                if text:
                    record["status"], record["extra"] = "ocr", text
        elif coverage < COVERAGE_FLOOR:
            record["status"], record["extra"] = "fallback", plain.strip()
            record["delimiters"] += sum(raw_plain.count(chr(code)) for code in table)
        pages.append(record)
    return pages


def summary(pages):
    count = Counter(page["status"] for page in pages)
    return {
        "pages": len(pages),
        "pages_ok": count["ok"],
        "pages_with_plain_text_fallback": count["fallback"],
        "pages_without_selectable_text": count["no-text"],
        "pages_ocr": count["ocr"],
        "min_layout_coverage": min((p["coverage"] for p in pages if p["tokens"]), default=1.0),
        "selectable_tokens": sum(p["tokens"] for p in pages),
        "tex_delimiters_mapped": sum(p.get("delimiters", 0) for p in pages),
        "unmapped_glyphs": sum(p["markdown"].count("\ufffd") + (p["extra"] or "").count("\ufffd") for p in pages),
    }


def render(pages, header):
    """Render the pages with explicit markers; header is a list of comment lines."""
    total = len(pages)
    stats = summary(pages)
    lines = ["<!--", *header,
             f"Converter: {EXTRACTOR}. One marker precedes each of the {total} PDF pages.",
             f"Completeness: {stats['pages_ok']} pages converted with >= {COVERAGE_FLOOR:.0%} of their "
             f"selectable-text tokens; {stats['pages_with_plain_text_fallback']} pages also carry their "
             f"verbatim plain text; {stats['pages_without_selectable_text']} pages have no selectable "
             f"text (image only){'; ' + str(stats['pages_ocr']) + ' pages OCR' if stats['pages_ocr'] else ''}.",
             "Figures, charts, and text inside images are not reproduced; consult the original PDF.",
             *([f"{stats['tex_delimiters_mapped']} large TeX delimiter glyphs (CMEX font, no Unicode mapping in "
                "the PDF) are written as the bracket, brace, or parenthesis they draw."]
               if stats["tex_delimiters_mapped"] else []),
             *([f"{stats['unmapped_glyphs']} glyphs have no Unicode mapping in the PDF and appear as U+FFFD."]
               if stats["unmapped_glyphs"] else []),
             "-->", ""]
    for page in pages:
        lines += [f"<!-- page {page['page']} of {total} -->", ""]
        if page["markdown"]:
            lines += [page["markdown"], ""]
        if page["status"] == "fallback":
            lines += [f"<!-- page {page['page']}: layout conversion matched {page['coverage']:.1%} of the "
                      "selectable-text tokens; the complete selectable text of this page follows -->",
                      "", "````text", page["extra"], "````", ""]
        elif page["status"] == "no-text":
            lines += [f"<!-- page {page['page']}: no selectable text (image-only page); "
                      "see the original PDF -->", ""]
        elif page["status"] == "ocr":
            lines += [f"<!-- page {page['page']}: no selectable text; Tesseract OCR output follows "
                      "and may contain recognition errors -->", "", "````text", page["extra"], "````", ""]
    return "\n".join(lines).rstrip() + "\n"


def check_markdown(text, page_count):
    """Confirm an extraction has exactly one ordered marker for every PDF page."""
    markers = [(int(a), int(b)) for a, b in PAGE_MARKER.findall(text)]
    return markers == [(n, page_count) for n in range(1, page_count + 1)]
