"""Download verified publisher PDFs and extract Markdown for local use only."""

import argparse
import hashlib
import os
import re
import subprocess
import sys
import tempfile
import unicodedata
from contextlib import ExitStack
from pathlib import Path
from urllib.parse import urlparse

import pymupdf
import pymupdf4llm

from generate import ALLOWED_HOSTS, ROOT, load_catalog


class CardError(Exception):
    """A download or document did not match the catalog entry."""


def normalized(text):
    return " ".join(re.findall(r"[a-z0-9]+", unicodedata.normalize("NFKC", text).casefold()))


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def download(model, path):
    url = model["card"]["url"]
    command = [
        "curl", "--fail", "--location", "--silent", "--show-error",
        "--proto", "=https", "--proto-redir", "=https",
        "--connect-timeout", "20", "--max-time", "240",
        "--output", str(path), "--write-out", "%{http_code}\n%{content_type}\n%{url_effective}",
        url,
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=250, check=False)
    except FileNotFoundError as error:
        raise CardError("curl is required to download publisher PDFs") from error
    except subprocess.TimeoutExpired as error:
        raise CardError(f"Timed out downloading {url}") from error
    if result.returncode:
        raise CardError(f"Download failed for {url}: {result.stderr.strip()}")
    response = result.stdout.strip().splitlines()
    if len(response) != 3:
        raise CardError(f"Unexpected HTTP response for {url}: {result.stdout!r}")
    status, content_type, final_url = response
    final = urlparse(final_url)
    if status not in ("200", "206") or final.scheme != "https":
        raise CardError(f"Invalid publisher response for {url}: HTTP {status}, {final_url}")
    if final.hostname not in ALLOWED_HOSTS[model["provider"]]:
        raise CardError(f"Publisher URL redirected outside its owner domain: {final_url}")
    media_type = content_type.split(";", 1)[0].lower()
    if (model["provider"] == "Moonshot AI"
            and (not final.path.startswith("/MoonshotAI/Kimi-K3/")
                 or media_type not in ("application/pdf", "application/octet-stream"))):
        raise CardError(f"Unexpected Moonshot PDF response: {content_type}, {final_url}")
    if model["provider"] != "Moonshot AI" and media_type != "application/pdf":
        raise CardError(f"Expected application/pdf, got {content_type} from {final_url}")


def verified_document(path, model):
    card = model["card"]
    with path.open("rb") as stream:
        if stream.read(5) != b"%PDF-":
            raise CardError(f"Not a PDF: {path}")
    actual_hash = sha256(path)
    if actual_hash != card["sha256"]:
        raise CardError(
            f"PDF hash mismatch for {model['name']}: expected {card['sha256']}, "
            f"got {actual_hash}; publisher may have revised the file"
        )
    try:
        document = pymupdf.open(path)
    except (pymupdf.FileDataError, pymupdf.EmptyFileError) as error:
        raise CardError(f"Unreadable PDF: {path}") from error
    with ExitStack() as stack:
        stack.enter_context(document)
        if not document.page_count:
            raise CardError(f"PDF has no pages: {path}")
        front = " ".join(page.get_text() for page in document[:2])
        if len(normalized(front)) < 80:
            raise CardError(f"PDF has no usable cover text: {path}")
        candidate = normalized(f"{document.metadata.get('title') or ''} {front}")
        title = normalized(card.get("title_check", card["title"]))
        if title not in candidate:
            raise CardError(
                f"PDF title does not match {model['name']}: expected {card['title']}"
            )
        model_name = model["name"].split(" (fast mode)", 1)[0]
        full_text = normalized(" ".join(page.get_text() for page in document))
        if normalized(model_name) not in full_text:
            # The 5.6 card names the family once, then names Sol, Terra and Luna.
            if not (model_name.startswith("GPT-5.6 ")
                    and "gpt 5 6" in candidate
                    and normalized(model_name.split()[-1]) in full_text):
                raise CardError(f"PDF does not identify the selected model: {model['name']}")
        stack.pop_all()
        return document


def replace_file(path, contents):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".system-card-", suffix=".tmp", dir=path.parent)
    temp = Path(name)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(contents)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp, path)
    finally:
        temp.unlink(missing_ok=True)


def build(model, output_root, refresh):
    card = model["card"]
    if card is None:
        raise CardError(f"{model['name']}: no matching publisher PDF is confirmed")
    if not card.get("sha256"):
        raise CardError(f"{model['name']}: publisher document is HTML, not a PDF")
    folder = output_root / model["slug"]
    pdf_path = folder / "system-card.pdf"
    md_path = folder / "system-card.md"
    if pdf_path.exists() and not pdf_path.is_file():
        raise CardError(f"Local PDF path is not a regular file: {pdf_path}")
    with tempfile.TemporaryDirectory(prefix="copilot-model-card-") as scratch:
        if refresh or not pdf_path.exists():
            source = Path(scratch) / "system-card.pdf"
            print(f"{model['slug']}: fetching {card['url']}", flush=True)
            download(model, source)
        else:
            source = pdf_path
        with verified_document(source, model) as document:
            markdown = pymupdf4llm.to_markdown(
                document, use_ocr=False, write_images=False, embed_images=False,
                show_progress=False,
            )
        if not isinstance(markdown, str) or len(normalized(markdown)) < 80:
            raise CardError(f"PDF extraction returned no usable Markdown for {model['name']}")
        if source != pdf_path:
            replace_file(pdf_path, source.read_bytes())
        replace_file(md_path, (markdown.rstrip() + "\n").encode("utf-8"))
    print(f"{model['slug']}: verified PDF and extracted local Markdown ({pdf_path}, {md_path})", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument("--model", action="append", metavar="SLUG", help="Model folder (repeatable)")
    choice.add_argument("--all", action="store_true", help="All models with verified publisher PDFs")
    parser.add_argument(
        "--output-root", type=Path, default=ROOT,
        help="Local parent of model folders (default: models/ in this checkout)",
    )
    parser.add_argument("--refresh", action="store_true", help="Re-download a cached, verified PDF")
    args = parser.parse_args()
    output_root = args.output_root.resolve()
    if output_root != ROOT and output_root.is_relative_to(ROOT.parent):
        parser.error("--output-root inside the checkout must be the models/ directory (Git-ignored)")
    models = load_catalog()["models"]
    by_slug = {model["slug"]: model for model in models}
    if args.model:
        missing = sorted(set(args.model) - by_slug.keys())
        if missing:
            parser.error(f"unknown model folder(s): {', '.join(missing)}")
        selected = [by_slug[slug] for slug in dict.fromkeys(args.model)]
    else:
        selected = [model for model in models if model["card"] and model["card"].get("sha256")]
    for model in selected:
        try:
            build(model, output_root, args.refresh)
        except CardError as error:
            print(f"ERROR: {error}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
