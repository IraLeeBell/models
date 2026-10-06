"""Validate hand-written digest.md / digest.json files against the catalog and, when available, the local extraction."""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CARD_HEADINGS = [
    "At a glance", "Capabilities", "Evaluations", "Safety findings",
    "Limitations and caveats", "Practical implications for Copilot users", "Document coverage",
]
NO_CARD_HEADINGS = [
    "At a glance", "What the publisher documents", "Practical implications for Copilot users",
    "Document coverage",
]
MINIMUMS = {"capabilities": 3, "evaluations": 3, "safety_findings": 3, "limitations": 3,
            "practical_implications": 3}
NO_CARD_MINIMUMS = {"capabilities": 1, "limitations": 2, "practical_implications": 2}
COPY_WINDOW = 12
# Billing and cost-management language stays out of digests; "thinking/token budget" is model terminology.
FORBIDDEN = re.compile(r"(?i)premium request|multiplier|finops|cost center|"
                       r"(?<!thinking )(?<!token )(?<!reasoning )(?<!compute )(?<!context )budget")


def words(text):
    return re.findall(r"[a-z0-9]+(?:[.'][a-z0-9]+)*", text.casefold())


def copied_runs(digest_text, source_text, window=COPY_WINDOW):
    """Return digest word runs of `window` or more words that also appear verbatim in the source."""
    body = re.sub(r'"[^"\n]{0,200}"|“[^”\n]{0,200}”', " ", digest_text)
    source = words(source_text)
    grams = {tuple(source[i:i + window]) for i in range(len(source) - window + 1)}
    found, tokens, i = [], words(body), 0
    while i <= len(tokens) - window:
        if tuple(tokens[i:i + window]) in grams:
            j = i + window
            while j < len(tokens) and tuple(tokens[j - window + 1:j + 1]) in grams:
                j += 1
            found.append(" ".join(tokens[i:j]))
            i = j
        else:
            i += 1
    return found


def page_list(item, field="pages"):
    value = item.get(field, [])
    return value if isinstance(value, list) else None


def check(model, documents, root=ROOT, extraction=None):
    """Return a list of problems for one catalog model."""
    slug, problems = model["slug"], []
    folder = root / slug
    md_path, json_path = folder / "digest.md", folder / "digest.json"
    if not md_path.is_file() or not json_path.is_file():
        return [f"{slug}: digest.md and digest.json are required"]
    md = md_path.read_text(encoding="utf-8")
    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        return [f"{slug}: digest.json is not valid JSON ({error})"]

    document = documents.get(model.get("document")) if model.get("document") else None
    headings = CARD_HEADINGS if document else NO_CARD_HEADINGS
    found = re.findall(r"^## (.+?)\s*$", md, re.MULTILINE)
    if found != headings:
        problems.append(f"{slug}: digest.md headings {found} != {headings}")
    if not md.startswith(f"# {model['name']}"):
        problems.append(f"{slug}: digest.md must start with '# {model['name']}'")
    if FORBIDDEN.search(md) or FORBIDDEN.search(json.dumps(data)):
        problems.append(f"{slug}: digest mentions billing/FinOps terms; keep them out")

    expected = {"schema_version": 1, "slug": slug, "model": model["name"], "publisher": model["provider"]}
    for key, value in expected.items():
        if data.get(key) != value:
            problems.append(f"{slug}: digest.json {key}={data.get(key)!r}, expected {value!r}")
    if not isinstance(data.get("summary"), str) or len(data["summary"]) < 80:
        problems.append(f"{slug}: digest.json summary is missing or too short")
    if not isinstance(data.get("coverage_notes"), str) or not data["coverage_notes"]:
        problems.append(f"{slug}: digest.json coverage_notes is required")

    allowed_docs = {}
    if document:
        allowed_docs[model["document"]] = document
        if data.get("document") != {"id": model["document"], "title": document["title"], "pages": document.get("pages")}:
            problems.append(f"{slug}: digest.json document must be "
                            f"{{'id': {model['document']!r}, 'title': {document['title']!r}, 'pages': {document.get('pages')!r}}}")
    elif data.get("document") is not None:
        problems.append(f"{slug}: digest.json document must be null when the catalog has no card")
    for supplement in model.get("supplements", []):
        allowed_docs[supplement] = documents[supplement]

    for field, minimum in (MINIMUMS if document else NO_CARD_MINIMUMS).items():
        items = data.get(field)
        if not isinstance(items, list) or len(items) < minimum:
            problems.append(f"{slug}: digest.json {field} needs at least {minimum} items")
    for field in ("capabilities", "evaluations", "safety_findings", "limitations", "practical_implications"):
        for index, item in enumerate(data.get(field) or []):
            label = f"{slug}: {field}[{index}]"
            if not isinstance(item, dict):
                problems.append(f"{label} must be an object")
                continue
            text_key = "benchmark" if field == "evaluations" else "text"
            if not isinstance(item.get(text_key), str) or not item[text_key].strip():
                problems.append(f"{label} needs {text_key}")
            if field == "evaluations" and not str(item.get("result", "")).strip():
                problems.append(f"{label} needs result")
            if field == "practical_implications":
                continue
            doc_id = item.get("document", model.get("document"))
            if doc_id not in allowed_docs:
                if document:
                    problems.append(f"{label} cites unknown document {doc_id!r}")
                continue
            target = allowed_docs[doc_id]
            pages = page_list(item)
            if pages is None:
                problems.append(f"{label} pages must be a list")
            elif target.get("format") == "pdf":
                if not pages:
                    problems.append(f"{label} needs at least one PDF page")
                bad = [p for p in pages if not isinstance(p, int) or not 1 <= p <= target["pages"]]
                if bad:
                    problems.append(f"{label} pages {bad} outside 1..{target['pages']}")
            elif not item.get("section"):
                problems.append(f"{label} needs a section for a non-PDF document")

    if extraction is not None:
        for run in copied_runs(md + "\n" + json.dumps(data, ensure_ascii=False), extraction):
            problems.append(f"{slug}: copies {len(run.split())} consecutive source words: '{run[:90]}...'")
    return problems


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slugs", nargs="*", help="models to check (default: all)")
    parser.add_argument("--extraction", action="append", default=[],
                        help="extraction or owner Markdown to test for verbatim copying (repeatable)")
    parser.add_argument("--extraction-dir", type=Path,
                        help="directory of <document-id>.md extractions (used when a folder has no local copy)")
    args = parser.parse_args(argv)
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    models = {m["slug"]: m for m in catalog["models"]}
    unknown = sorted(set(args.slugs) - set(models))
    if unknown:
        parser.error(f"unknown slugs: {', '.join(unknown)}")
    source = "\n".join(Path(p).read_text(encoding="utf-8") for p in args.extraction) if args.extraction else None
    problems = []
    for slug in args.slugs or models:
        model = models[slug]
        text = source
        if text is None:
            from generate import load_catalog, local_sources
            text = local_sources(model, load_catalog(), args.extraction_dir)
        problems += check(model, catalog["documents"], extraction=text)
    print("\n".join(problems) or "digests OK")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
