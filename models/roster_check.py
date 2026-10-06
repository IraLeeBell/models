"""Compare catalog.json with GitHub's Copilot model tables in github/docs.

    python3 roster_check.py                 # compare with github/docs main
    python3 roster_check.py --ref <commit>  # compare with a specific revision
    python3 roster_check.py --tables-dir DIR  # use downloaded copies of the YAML tables

Exit status 0 means the catalog agrees with the tables; 1 lists what to update. The Copilot app's
model picker is not published in these tables; re-check it in the app and update catalog.json by hand.
"""

import argparse
import json
import subprocess
import sys
import urllib.request
from pathlib import Path

from generate import load_catalog

TABLES = ("model-supported-clients", "auto-model-selection", "model-release-status", "model-deprecation-history")
RAW = "https://raw.githubusercontent.com/github/docs/{ref}/data/tables/copilot/{name}.yml"
COMMIT_API = "https://api.github.com/repos/github/docs/commits/{ref}"
CLIENT_COLUMNS = ("dotcom", "cli", "vscode", "vs", "eclipse", "xcode", "jetbrains")


def scalar(value):
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
        return value[1:-1]
    return {"true": True, "false": False}.get(value, value)


def parse_rows(text):
    """Parse the flat list-of-mappings YAML used by these tables (no nesting)."""
    rows = []
    for raw in text.splitlines():
        line = raw.split(" #", 1)[0].rstrip() if not raw.lstrip().startswith("#") else ""
        if not line.strip():
            continue
        if line.startswith("- "):
            rows.append({})
            line = line[2:]
        elif not rows or not line.startswith("  "):
            raise ValueError(f"unexpected line in table: {raw!r}")
        key, sep, value = line.strip().partition(":")
        if not sep:
            raise ValueError(f"unexpected line in table: {raw!r}")
        rows[-1][key.strip()] = scalar(value)
    return rows


def fetch(url):
    """Fetch with curl (system certificate store), falling back to urllib."""
    agent = "copilot-model-cards-roster-check"
    try:
        result = subprocess.run(["curl", "--fail", "--silent", "--show-error", "--location", "--proto", "=https",
                                 "--max-time", "60", "--user-agent", agent, url],
                                capture_output=True, check=False, timeout=90)
        if result.returncode == 0:
            return result.stdout.decode("utf-8")
        raise OSError(f"curl failed for {url}: {result.stderr.decode().strip()}")
    except FileNotFoundError:
        request = urllib.request.Request(url, headers={"User-Agent": agent})
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.read().decode("utf-8")


def load_tables(ref, tables_dir):
    tables = {}
    for name in TABLES:
        text = (Path(tables_dir) / f"{name}.yml").read_text(encoding="utf-8") if tables_dir \
            else fetch(RAW.format(ref=ref, name=name))
        tables[name] = {row["name"]: row for row in parse_rows(text)}
    return tables


def expected(name, tables):
    """Derive lifecycle and CLI availability for a model name from the tables."""
    clients = tables["model-supported-clients"].get(name)
    auto = tables["auto-model-selection"].get(name)
    retired = tables["model-deprecation-history"].get(name)
    if clients:
        lifecycle = "limited" if retired else (
            "utility" if not any(clients.get(c) for c in CLIENT_COLUMNS) else "current")
        return lifecycle, bool(clients.get("cli"))
    if auto:
        return ("limited" if retired else "current"), ("auto-only" if auto.get("cli") else False)
    if retired:
        return "retired", None
    return None, None


def compare(catalog, tables):
    problems = []
    by_name = {m["name"]: m for m in catalog["models"]}
    listed = set(tables["model-supported-clients"]) | set(tables["auto-model-selection"]) | \
        set(tables["model-release-status"])
    for name in sorted(listed - set(by_name)):
        problems.append(f"NEW   {name}: listed by GitHub but missing from catalog.json")
    for name, model in by_name.items():
        lifecycle, cli = expected(name, tables)
        if lifecycle is None:
            problems.append(f"GONE  {name}: no longer in any GitHub table; record its status")
            continue
        if lifecycle != model["lifecycle"]:
            problems.append(f"STATE {name}: catalog says {model['lifecycle']}, tables imply {lifecycle}")
        if lifecycle != "retired" and cli != model["cli"]:
            problems.append(f"CLI   {name}: catalog says {model['cli']!r}, tables imply {cli!r}")
        retired = tables["model-deprecation-history"].get(name)
        if retired and model.get("retired_on") != retired.get("retirement_date"):
            problems.append(f"DATE  {name}: retirement date {retired.get('retirement_date')} "
                            f"(catalog: {model.get('retired_on')})")
        status = tables["model-release-status"].get(name)
        if status and status.get("release_status") != model["release_status"]:
            problems.append(f"REL   {name}: release status {status.get('release_status')} "
                            f"(catalog: {model['release_status']})")
        if lifecycle in ("current", "limited") and "app_auto" in model:
            auto = bool(tables["auto-model-selection"].get(name, {}).get("app"))
            if auto != model["app_auto"]:
                problems.append(f"AUTO  {name}: app Auto eligibility {auto} (catalog: {model['app_auto']})")
    return problems


def docs_commit(ref):
    try:
        return json.loads(fetch(COMMIT_API.format(ref=ref)))["sha"]
    except (OSError, ValueError, KeyError):
        return None


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--ref", default="main", help="github/docs branch or commit (default: main)")
    parser.add_argument("--tables-dir", type=Path, help="read <table>.yml files from this directory instead")
    args = parser.parse_args(argv)
    catalog = load_catalog()
    tables = load_tables(args.ref, args.tables_dir)
    if not args.tables_dir:
        sha = docs_commit(args.ref)
        same = " (same as catalog)" if sha == catalog["docs_revision"] else f" (catalog: {catalog['docs_revision']})"
        print(f"github/docs {args.ref} = {sha or 'unknown'}{same if sha else ''}")
    problems = compare(catalog, tables)
    print("\n".join(problems) or f"roster OK: {len(catalog['models'])} catalog models agree with GitHub's tables")
    print("Reminder: re-check the Copilot app model picker by hand; it is not published in these tables.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
