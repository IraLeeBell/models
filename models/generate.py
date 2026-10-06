"""Render the public model catalog from catalog.json (Python standard library only)."""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent
DOCS = "https://docs.github.com/en/copilot/reference/ai-models/supported-models"
COMPARISON = "https://docs.github.com/en/copilot/reference/ai-models/model-comparison"
ALLOWED_HOSTS = {
    "OpenAI": {"deploymentsafety.openai.com", "cdn.openai.com", "openai.com"},
    "Anthropic": {"www-cdn.anthropic.com", "assets.anthropic.com", "anthropic.com"},
    "Google": {"storage.googleapis.com"},
    "Microsoft": {"microsoft.ai"},
    "Moonshot AI": {"raw.githubusercontent.com"},
    "xAI": {"media.x.ai"},
}


def load_catalog():
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    models = catalog["models"]
    if len(models) != catalog["expected_model_count"]:
        raise ValueError("Model count does not match expected_model_count")
    if len({model["name"] for model in models}) != len(models):
        raise ValueError("Duplicate model name")
    if len({model["slug"] for model in models}) != len(models):
        raise ValueError("Duplicate model slug")
    for model in models:
        if not re.fullmatch(r"[a-z0-9]+(?:[.-][a-z0-9]+)*", model["slug"]):
            raise ValueError(f"Unsafe model slug: {model['slug']}")
        if model["provider"] not in ALLOWED_HOSTS:
            raise ValueError(f"Unknown publisher: {model['provider']}")
        if model["cli_source"] not in ("per-client", "auto-only"):
            raise ValueError(f"Unknown CLI evidence: {model['name']}")
        card = model["card"]
        if card is None:
            if not model.get("card_note"):
                raise ValueError(f"Missing explanation for absent document: {model['name']}")
            continue
        url = urlparse(card["url"])
        if url.scheme != "https" or url.hostname not in ALLOWED_HOSTS[model["provider"]]:
            raise ValueError(f"Non-publisher card URL: {model['name']}")
        if model["provider"] == "Google" and not url.path.startswith("/deepmind-media/"):
            raise ValueError(f"Not a Google DeepMind card: {model['name']}")
        if model["provider"] == "Moonshot AI" and not url.path.startswith("/MoonshotAI/Kimi-K3/"):
            raise ValueError(f"Not an owner-published Moonshot report: {model['name']}")
        if url.path.lower().endswith(".pdf") != bool(card.get("sha256")):
            raise ValueError(f"PDF needs a verified hash; HTML must not have one: {model['name']}")
        if card.get("sha256") and not re.fullmatch(r"[0-9a-f]{64}", card["sha256"]):
            raise ValueError(f"Invalid SHA-256: {model['name']}")
    return catalog


def source(model, catalog):
    card = model["card"]
    tables = f"https://github.com/github/docs/blob/{catalog['docs_revision']}/data/tables/copilot"
    lines = [
        f"# Sources: {model['name']}",
        "",
        f"- Publisher: {model['provider']}",
        f"- Checked: {catalog['checked_at']}",
        "- GitHub release status: GA",
        f"- Copilot CLI: {'listed in the per-client table' if model['cli_source'] == 'per-client' else 'listed for CLI Auto; not yet in the per-client table'}",
        f"- Copilot app manual picker: {'observed' if model['app_picker_observed'] else 'not observed (not a claim of unavailability)'} on {catalog['checked_at']}",
        f"- Copilot app Auto selection: {'included' if model['app_auto'] else 'not listed'}",
        f"- GitHub availability: {DOCS}",
        f"- GitHub model comparison: {COMPARISON}",
        f"- Frozen release table: {tables}/model-release-status.yml",
        f"- Frozen CLI evidence: {tables}/{'model-supported-clients' if model['cli_source'] == 'per-client' else 'auto-model-selection'}.yml",
        f"- Frozen app Auto table: {tables}/auto-model-selection.yml",
        f"- Frozen model comparison: {tables}/model-comparison.yml",
        "",
    ]
    if model.get("status"):
        lines.insert(5, f"- Availability qualification: {model['status']}")
        lines.insert(-1, f"- Frozen retirement history: {tables}/model-deprecation-history.yml")
    if model.get("note"):
        lines.insert(-1, f"- Note: {model['note']}")
    if card:
        kind = "PDF" if card.get("sha256") else "HTML"
        lines += [
            f"## Publisher document ({kind})",
            "",
            f"- Title: {card['title']}",
            f"- Owner URL: {card['url']}",
            f"- Scope verified: {card['scope']}",
        ]
        if card.get("sha256"):
            lines.append(f"- SHA-256 of PDF retrieved {catalog['checked_at']}: `{card['sha256']}`")
    else:
        lines += ["## Publisher document", "", f"No matching publisher card confirmed. {model['card_note']}"]
    lines += [
        "",
        ("The publisher document is linked, not reproduced here."
         if card else "No publisher card or full-text extraction is supplied here."),
        "This repository's MIT license does not grant redistribution rights to",
        "third-party system cards, PDFs, or their full text.",
        "",
    ]
    return "\n".join(lines)


def digest(model):
    card = model["card"]
    lines = [
        f"# {model['name']}",
        "",
        f"- **Publisher:** {model['provider']}",
        f"- **Copilot status:** {model.get('status', 'GA')}",
        f"- **Use case:** {model['summary']}",
        "",
        "This is an original short orientation, not a benchmark, endorsement, or a",
        "verbatim extraction of a publisher document. Availability depends on plan,",
        "organization policy, client, and the publisher.",
        "",
    ]
    if model.get("note"):
        lines += [model["note"], ""]
    if card:
        lines += [
            f"**Publisher reading:** [{card['title']}]({card['url']}).",
            f"**Document scope:** {card['scope']}",
        ]
    else:
        lines += [f"**Document status:** {model['card_note']}"]
    lines += ["", "See [source.md](source.md) for provenance and availability evidence.", ""]
    return "\n".join(lines)


def index(catalog):
    models = catalog["models"]
    cli_per_client = sum(m["cli_source"] == "per-client" for m in models)
    observed = sum(m["app_picker_observed"] for m in models)
    app_auto = sum(m["app_auto"] for m in models)
    with_card = sum(m["card"] is not None for m in models)
    lines = [
        "# GitHub Copilot model catalog",
        "",
        f"Checked **{catalog['checked_at']}** against [GitHub's supported-model tables]({DOCS})",
        f"([frozen docs revision](https://github.com/github/docs/tree/{catalog['docs_revision']}/data/tables/copilot)).",
        f"**{len(models)} folders**: {cli_per_client} listed for CLI in the per-client table;",
        "GPT-6.1 Sol is additionally listed for CLI Auto but not yet in that table.",
        f"The app manual picker was observed to list {observed} of these publicly",
        f"documented models; {app_auto} appear in GitHub's separate app Auto table.",
        "One model, Claude Sonnet 4.6, has a documented annual-plan exception",
        "despite an earlier retirement date. GPT-5.4 nano is a non-selectable",
        "utility model and has no folder.",
        "",
        "The **app picker** observation is local to the checked date and account;",
        "a blank observation does not mean a model is unavailable to every user.",
        "The **app Auto** column means eligible for *automatic selection*, not",
        "necessarily selectable manually. Neither is the GitHub.com browser column.",
        "CLI evidence is from the per-client table except where explicitly noted.",
        "Plan, policies, region, and rollout can alter actual availability.",
        "",
        "| Model | Publisher | CLI evidence | App picker observed | App Auto | Owner document |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for model in models:
        card = model["card"]
        kind = "PDF" if card and card.get("sha256") else "HTML" if card else "none confirmed"
        status = " (limited)" if model.get("status") else ""
        lines.append(
            f"| [{model['name']}](./{model['slug']}/digest.md){status} "
            f"| {model['provider']} | {'per-client' if model['cli_source'] == 'per-client' else 'Auto only'} "
            f"| {'yes' if model['app_picker_observed'] else 'not observed'} "
            f"| {'yes' if model['app_auto'] else 'not listed'} "
            f"| [{kind}](./{model['slug']}/source.md) |"
        )
    lines += [
        "",
        f"**Documentation:** [Supported models]({DOCS}) (release status, CLI, app Auto,",
        f"retirement history); [model comparison]({COMPARISON}) (use cases and",
        "publisher links). The per-client GitHub.com column is **not** app evidence.",
        "The release-status and retirement tables disagree for Claude Sonnet 4.6;",
        "the retirement footnote preserves access for annual individual subscribers.",
        "The catalog labels this restricted exception rather than calling it",
        "universally available.",
        "For GPT-6.1 Sol and Claude Sonnet 5.5, GitHub's comparison still says",
        "\"Coming soon\"; the publisher documents linked here were verified",
        "independently on the checked date.",
        "",
        "**Licensing:** Publisher PDFs and full-text extractions are *not* committed.",
        "An official public download URL is not a redistribution license. The",
        "repository's MIT license covers only its own code and original summaries.",
        f"{with_card} entries link to a matching owner document;",
        (f"the remaining one explains the missing dedicated card."
         if len(models) - with_card == 1
         else f"the remaining {len(models) - with_card} explain missing dedicated cards."),
        "A PDF hash in `source.md` identifies the publisher file downloaded for",
        "verification on the checked date; it does not imply a local PDF is shipped.",
        "",
        "**Updating:** Edit `catalog.json` with public evidence, update the checked",
        "date and docs revision, verify owner URL, title and scope, then run",
        "`python3 models/generate.py --write` and",
        "`python3 models/generate.py --check`. Do not assign a family card to a",
        "new variant unless the publisher document explicitly covers it.",
        "",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true", help="Regenerate checked-in documents")
    group.add_argument("--check", action="store_true", help="Check documents match catalog.json")
    args = parser.parse_args()
    catalog = load_catalog()
    rendered = {ROOT / "README.md": index(catalog)}
    for model in catalog["models"]:
        folder = ROOT / model["slug"]
        rendered[folder / "source.md"] = source(model, catalog)
        rendered[folder / "digest.md"] = digest(model)

    if args.check:
        wrong = [str(p.relative_to(ROOT)) for p, content in rendered.items()
                 if not p.is_file() or p.read_text(encoding="utf-8") != content]
        actual = {p.name for p in ROOT.iterdir() if p.is_dir()
                  and not p.name.startswith(".") and p.name != "__pycache__"}
        expected = {model["slug"] for model in catalog["models"]}
        wrong.extend(f"unexpected folder: {name}" for name in sorted(actual - expected))
        if wrong:
            print("Catalog out of date:\n" + "\n".join(wrong), file=sys.stderr)
            return 1
        print(f"Catalog OK: {len(expected)} model folders, {len(rendered)} generated files")
        return 0
    for path, content in rendered.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"Generated {len(rendered)} files for {len(catalog['models'])} models")
    return 0


if __name__ == "__main__":
    sys.exit(main())
