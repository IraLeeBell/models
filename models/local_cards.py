"""Download publisher documents, verify them against catalog.json, and extract page-marked Markdown.

    python3 local_cards.py --all                  # every model's primary PDF and supplements
    python3 local_cards.py --model grok-4.7       # one folder (repeatable)
    python3 local_cards.py --check-urls           # confirm each owner URL still serves the expected type

Outputs are written into the model folders. They are Git-ignored unless the catalog records a
redistribution grant for the document (see RIGHTS.md).
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path
from urllib.parse import urlparse

from generate import ROOT, load_catalog, owner_url

PDF_TYPES = {"application/pdf"}
# raw.githubusercontent.com serves binary files as octet-stream.
OCTET_HOSTS = {"raw.githubusercontent.com"}


class CardError(Exception):
    """A download or document did not match the catalog entry."""


def normalized(text):
    return " ".join(re.findall(r"[a-z0-9]+", unicodedata.normalize("NFKC", text).casefold()))


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fetch(url, path, *, head_only=False):
    """Fetch an HTTPS URL with curl; return (status, media type, final URL)."""
    command = ["curl", "--fail", "--location", "--silent", "--show-error", "--proto", "=https",
               "--proto-redir", "=https", "--connect-timeout", "20", "--max-time", "300",
               "--user-agent", "copilot-model-cards/2 (+https://github.com/IraLeeBell/models)",
               "--output", str(path), "--write-out", "%{http_code}\n%{content_type}\n%{url_effective}"]
    if head_only:
        command += ["--range", "0-1023"]
    try:
        result = subprocess.run(command + [url], capture_output=True, text=True, timeout=320, check=False)
    except FileNotFoundError as error:
        raise CardError("curl is required to download publisher documents") from error
    except subprocess.TimeoutExpired as error:
        raise CardError(f"timed out fetching {url}") from error
    if result.returncode:
        raise CardError(f"download failed for {url}: {result.stderr.strip()}")
    response = result.stdout.strip().splitlines()
    if len(response) != 3:
        raise CardError(f"unexpected HTTP response for {url}: {result.stdout!r}")
    status, content_type, final = response
    return status, content_type.split(";", 1)[0].strip().lower(), final


def check_response(doc, status, media_type, final):
    if status not in ("200", "206"):
        raise CardError(f"HTTP {status} from {final}")
    if not owner_url(final, doc["publisher"]):
        raise CardError(f"{doc['url']} redirected outside {doc['publisher']}'s hosts: {final}")
    host = urlparse(final).hostname
    if doc["format"] == "pdf":
        allowed = PDF_TYPES | ({"application/octet-stream"} if host in OCTET_HOSTS else set())
    else:
        allowed = {"text/plain", "text/markdown"}
    if media_type not in allowed:
        raise CardError(f"expected {' or '.join(sorted(allowed))} from {final}, got {media_type}")


def download(doc, path):
    status, media_type, final = fetch(doc["url"], path)
    check_response(doc, status, media_type, final)
    return final


def verify(doc, path, scope_terms=()):
    """Check signature, SHA-256, title and scope terms; return an open PyMuPDF document (PDFs only)."""
    data_start = Path(path).read_bytes()[:5]
    if doc["format"] == "pdf" and data_start != b"%PDF-":
        raise CardError(f"not a PDF: {path}")
    actual = sha256(path)
    if actual != doc["sha256"]:
        raise CardError(f"SHA-256 mismatch for {doc['title']}: expected {doc['sha256']}, got {actual}. "
                        "The publisher may have revised the document; verify its scope and update catalog.json.")
    if doc["format"] != "pdf":
        text = Path(path).read_text(encoding="utf-8")
        if normalized(doc["title_check"]) not in normalized(text):
            raise CardError(f"owner document does not name {doc['title_check']!r}")
        return None
    import pymupdf

    try:
        document = pymupdf.open(path)
    except (pymupdf.FileDataError, pymupdf.EmptyFileError) as error:
        raise CardError(f"unreadable PDF: {path}") from error
    try:
        if document.page_count != doc["pages"]:
            raise CardError(f"{doc['title']}: {document.page_count} pages, catalog says {doc['pages']}")
        front = " ".join(page.get_text() for page in document[:2])
        if normalized(doc["title_check"]) not in normalized(f"{document.metadata.get('title') or ''} {front}"):
            raise CardError(f"PDF front matter does not contain {doc['title_check']!r}")
        text = normalized(" ".join(page.get_text() for page in document))
        missing = [term for term in scope_terms if normalized(term) not in text]
        if missing:
            raise CardError(f"PDF text does not mention {missing}")
    except Exception:
        document.close()
        raise
    return document


def replace_file(path, contents):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".card-", suffix=".tmp", dir=path.parent)
    temp = Path(name)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(contents)
            stream.flush()
            os.fsync(stream.fileno())
        temp.chmod(0o644)
        os.replace(temp, path)
    finally:
        temp.unlink(missing_ok=True)


def header(doc_id, doc):
    lines = [f"Title: {doc['title']}", f"Publisher: {doc['publisher']}",
             f"Document date: {doc['date'] or 'undated'}", f"Owner URL: {doc['url']}"]
    if doc.get("resolved_url"):
        lines.append(f"Resolved URL: {doc['resolved_url']}")
    lines += [f"Catalog document: {doc_id}; retrieved {doc['retrieved']}; SHA-256 verified against the catalog",
              f"PDF: {doc['bytes']:,} bytes, {doc['pages']} pages, SHA-256 {doc['sha256']}"]
    if doc["rights"] == "granted":
        lines.append(f"{doc['copyright']}. Redistributed under the {doc['license_name']} "
                     f"({doc['license_file']} in this folder).")
    else:
        lines.append(f"Copyright {doc['publisher']}. Local copy for private reference; this file is not "
                     "licensed for redistribution and is Git-ignored (see RIGHTS.md).")
    lines.append("This is a verbatim text extraction of the PDF; headings and tables are reconstructed from layout.")
    return lines


def targets(model, catalog, include_supplements=True):
    """Yield (doc_id, doc, base path without suffix, scope terms) for a model."""
    folder = ROOT / model["slug"]
    if model.get("document"):
        doc = catalog["documents"][model["document"]]
        base = folder / ("system-card" if doc["format"] == "pdf" else "model-card")
        yield model["document"], doc, base, model.get("scope_terms", [])
    if include_supplements:
        for doc_id in model.get("supplements", []):
            yield doc_id, catalog["documents"][doc_id], folder / "supplements" / doc_id, []


def build(doc_id, doc, base, scope_terms, *, output_root=ROOT, cache=None, refresh=False, ocr=False):
    """Download (or reuse), verify, and extract one document. Return a report dict."""
    import card_extract

    base = output_root / base.relative_to(ROOT)
    if doc["format"] != "pdf":
        target = base.with_suffix(".md")
        with tempfile.TemporaryDirectory(prefix="model-card-") as scratch:
            source = target if target.is_file() and not refresh else Path(scratch) / "card.md"
            if source != target:
                download(doc, source)
            verify(doc, source)
            if source != target:
                replace_file(target, source.read_bytes())
        return {"document": doc_id, "path": str(target), "format": doc["format"], "verbatim": True}

    pdf_path, md_path = base.with_suffix(".pdf"), base.with_suffix(".md")
    with tempfile.TemporaryDirectory(prefix="model-card-") as scratch:
        cached = Path(cache) / f"{doc['sha256']}.pdf" if cache else None
        if pdf_path.is_file() and not refresh:
            source = pdf_path
        elif cached and cached.is_file() and not refresh:
            source = cached
        else:
            source = Path(scratch) / "card.pdf"
            print(f"{doc_id}: fetching {doc['url']}", flush=True)
            download(doc, source)
        document = verify(doc, source, scope_terms)
        try:
            pages = card_extract.extract_pages(document, ocr=ocr)
        finally:
            document.close()
        text = card_extract.render(pages, header(doc_id, doc))
        if not card_extract.check_markdown(text, doc["pages"]):
            raise CardError(f"{doc_id}: extraction lacks one ordered marker per page")
        if source != pdf_path:
            replace_file(pdf_path, source.read_bytes())
        replace_file(md_path, text.encode("utf-8"))
    stats = card_extract.summary(pages)
    low = [p["page"] for p in pages if p["status"] != "ok"]
    print(f"{doc_id}: {stats['pages']} pages -> {md_path.relative_to(output_root)} "
          f"({stats['pages_with_plain_text_fallback']} with plain-text fallback, "
          f"{stats['pages_without_selectable_text']} without selectable text)", flush=True)
    return {"document": doc_id, "path": str(md_path), **stats, "pages_not_ok": low}


def check_urls(catalog):
    problems = 0
    for doc_id, doc in catalog["documents"].items():
        with tempfile.TemporaryDirectory(prefix="model-card-") as scratch:
            probe = Path(scratch) / "head"
            try:
                status, media_type, final = fetch(doc["url"], probe, head_only=True)
                check_response(doc, status, media_type, final)
                if doc["format"] == "pdf" and probe.read_bytes()[:5] != b"%PDF-":
                    raise CardError("response does not start with %PDF-")
                if doc.get("resolved_url") and final != doc["resolved_url"]:
                    print(f"NOTE {doc_id}: now redirects to {final} (catalog: {doc['resolved_url']}); "
                          "run local_cards.py --refresh to compare SHA-256")
                print(f"ok   {doc_id}: HTTP {status} {media_type}")
            except CardError as error:
                problems += 1
                print(f"FAIL {doc_id}: {error}")
    return problems


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument("--model", action="append", metavar="SLUG", help="model folder (repeatable)")
    choice.add_argument("--all", action="store_true", help="every model with a publisher document")
    choice.add_argument("--check-urls", action="store_true", help="probe every owner URL and exit")
    parser.add_argument("--output-root", type=Path, default=ROOT, help="parent of the model folders (default: here)")
    parser.add_argument("--pdf-cache", type=Path, help="directory of previously downloaded <sha256>.pdf files")
    parser.add_argument("--refresh", action="store_true", help="re-download even when a verified copy exists")
    parser.add_argument("--no-supplements", action="store_true", help="skip supplement documents")
    parser.add_argument("--ocr", action="store_true", help="OCR pages without selectable text (needs Tesseract)")
    parser.add_argument("--report", type=Path, help="write per-document conversion statistics as JSON")
    args = parser.parse_args(argv)
    catalog = load_catalog()
    if args.check_urls:
        return 1 if check_urls(catalog) else 0
    output_root = args.output_root.resolve()
    if output_root != ROOT and output_root.is_relative_to(ROOT.parent):
        parser.error("--output-root inside the checkout must be the models/ directory")
    by_slug = {m["slug"]: m for m in catalog["models"]}
    if args.model:
        unknown = sorted(set(args.model) - set(by_slug))
        if unknown:
            parser.error(f"unknown model folder(s): {', '.join(unknown)}")
        selected = [by_slug[slug] for slug in dict.fromkeys(args.model)]
        missing = [m["slug"] for m in selected if not m.get("document")]
        if missing:
            parser.error(f"no publisher document exists for: {', '.join(missing)} (see their source.md)")
    else:
        selected = [m for m in catalog["models"] if m.get("document")]
    reports, failures = [], 0
    for model in selected:
        for doc_id, doc, base, terms in targets(model, catalog, not args.no_supplements):
            try:
                report = build(doc_id, doc, base, terms, output_root=output_root, cache=args.pdf_cache,
                               refresh=args.refresh, ocr=args.ocr)
                reports.append({"model": model["slug"], **report})
            except CardError as error:
                failures += 1
                print(f"ERROR {model['slug']}: {error}", file=sys.stderr)
    if args.report:
        args.report.write_text(json.dumps(reports, indent=2) + "\n", encoding="utf-8")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
