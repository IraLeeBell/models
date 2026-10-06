"""Catalog, generator, digest, and roster checks (standard library only)."""

import copy
import json
import tempfile
import unittest
from pathlib import Path

import digest_check
import generate
import roster_check

CATALOG = generate.load_catalog()


def write_catalog(data):
    tmp = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8")
    json.dump(data, tmp)
    tmp.close()
    return Path(tmp.name)


class CatalogTest(unittest.TestCase):
    def assert_rejected(self, mutate, message):
        data = copy.deepcopy(CATALOG)
        mutate(data)
        path = write_catalog(data)
        self.addCleanup(path.unlink)
        with self.assertRaisesRegex(generate.CatalogError, message):
            generate.load_catalog(path)

    def test_owner_urls(self):
        self.assertTrue(generate.owner_url("https://media.x.ai/v1/website/4p7card-5eccc980.pdf", "xAI"))
        self.assertFalse(generate.owner_url("http://media.x.ai/a.pdf", "xAI"))
        self.assertFalse(generate.owner_url("https://media.x.ai.example.com/a.pdf", "xAI"))
        self.assertFalse(generate.owner_url("https://storage.googleapis.com/other-bucket/a.pdf", "Google DeepMind"))

    def test_rejects_non_owner_url(self):
        def mutate(data):
            data["documents"]["xai-grok-4-7"]["url"] = "https://example.com/grok.pdf"
        self.assert_rejected(mutate, "not an owner URL")

    def test_rejects_grant_without_license(self):
        def mutate(data):
            data["documents"]["xai-grok-4-7"]["rights"] = "granted"
        self.assert_rejected(mutate, "granted rights need")

    def test_rejects_unexplained_missing_card(self):
        def mutate(data):
            next(m for m in data["models"] if m["slug"] == "raptor-mini").pop("card_note")
        self.assert_rejected(mutate, "card_note")

    def test_counts_and_mapping(self):
        slugs = [m["slug"] for m in CATALOG["models"]]
        self.assertEqual(len(slugs), len(set(slugs)))
        folders = {p.name for p in generate.ROOT.iterdir() if p.is_dir() and not p.name.startswith((".", "_"))}
        self.assertEqual(folders, set(slugs))

    def test_generated_text_is_public_safe(self):
        for path, text in generate.outputs(CATALOG).items():
            self.assertIsNone(generate.BANNED.search(text), path)

    def test_relative_link_pattern_skips_code(self):
        text = "[a](x.md) [b](https://example.com) [c](#h) `[d](y.md)` ``[e](z.md) `q` `` \n```\n[f](w.md)\n```\n"
        prose = generate.CODE_SPAN.sub("", generate.FENCE.sub("", text))
        self.assertEqual(generate.RELATIVE_LINK.findall(prose), ["x.md"])

    def test_digests_link_only_to_committed_full_text(self):
        for model in CATALOG["models"]:
            text = (generate.ROOT / model["slug"] / "digest.md").read_text(encoding="utf-8")
            doc = CATALOG["documents"].get(model.get("document") or "")
            granted = doc and doc["rights"] == "granted"
            self.assertEqual("](system-card.md)" in text, bool(granted and doc["format"] == "pdf"), model["slug"])
            self.assertEqual("](model-card.md)" in text, bool(granted and doc["format"] != "pdf"), model["slug"])


class DigestCheckTest(unittest.TestCase):
    def test_copied_runs(self):
        source = "the quick brown fox jumps over the lazy dog while seven cats watch from the old fence"
        self.assertTrue(digest_check.copied_runs(f"Intro. {source}.", source))
        self.assertFalse(digest_check.copied_runs(f'Intro "{source}".', source))
        self.assertFalse(digest_check.copied_runs("the quick brown fox jumps over a sleeping dog", source))

    def test_real_digest_passes_and_detects_tampering(self):
        model = next(m for m in CATALOG["models"] if m["slug"] == "grok-4.7")
        self.assertEqual(digest_check.check(model, CATALOG["documents"]), [])
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "grok-4.7"
            folder.mkdir()
            md = (generate.ROOT / "grok-4.7" / "digest.md").read_text(encoding="utf-8")
            data = json.loads((generate.ROOT / "grok-4.7" / "digest.json").read_text(encoding="utf-8"))
            data["capabilities"][0]["pages"] = [9999]
            (folder / "digest.md").write_text(md.replace("## Evaluations", "## Benchmarks"), encoding="utf-8")
            (folder / "digest.json").write_text(json.dumps(data), encoding="utf-8")
            problems = digest_check.check(model, CATALOG["documents"], Path(tmp))
        self.assertTrue(any("headings" in p for p in problems))
        self.assertTrue(any("outside" in p for p in problems))


class RosterCheckTest(unittest.TestCase):
    def test_parse_rows(self):
        rows = roster_check.parse_rows("# comment\n\n- name: 'Model A'\n  cli: true\n  app: false\n")
        self.assertEqual(rows, [{"name": "Model A", "cli": True, "app": False}])

    def test_detects_new_and_changed_models(self):
        tables = {name: {} for name in roster_check.TABLES}
        tables["model-supported-clients"]["Brand New"] = {"name": "Brand New", "cli": True}
        problems = roster_check.compare(CATALOG, tables)
        self.assertIn("NEW   Brand New: listed by GitHub but missing from catalog.json", problems)
        self.assertTrue(any(p.startswith("GONE  Grok 4.7") for p in problems))


if __name__ == "__main__":
    unittest.main()
