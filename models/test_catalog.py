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
    MODEL = next(m for m in CATALOG["models"] if m["slug"] == "grok-4.7")
    VOCAB = digest_check.load_vocab()

    def tampered(self, mutate=None, mutate_md=None):
        """Check a modified copy of the grok-4.7 digest in a temporary root and return the problems."""
        data = json.loads((generate.ROOT / "grok-4.7" / "digest.json").read_text(encoding="utf-8"))
        md = (generate.ROOT / "grok-4.7" / "digest.md").read_text(encoding="utf-8")
        if mutate:
            mutate(data)
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "grok-4.7"
            folder.mkdir()
            (folder / "digest.json").write_text(json.dumps(data), encoding="utf-8")
            (folder / "digest.md").write_text(mutate_md(md) if mutate_md else md, encoding="utf-8")
            return digest_check.check(self.MODEL, CATALOG, Path(tmp))

    def assert_flags(self, needle, mutate=None, mutate_md=None):
        problems = self.tampered(mutate, mutate_md)
        self.assertTrue(any(needle in p for p in problems), problems)

    def test_copied_runs(self):
        source = "the quick brown fox jumps over the lazy dog while seven cats watch from the old fence"
        self.assertTrue(digest_check.copied_runs(f"Intro. {source}.", source))
        self.assertFalse(digest_check.copied_runs(f'Intro "{source}".', source))
        self.assertFalse(digest_check.copied_runs("the quick brown fox jumps over a sleeping dog", source))

    def test_vocabulary_is_valid(self):
        self.assertEqual(digest_check.vocab_problems(self.VOCAB), [])

    def test_vocabulary_proposals_cannot_redefine(self):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as tmp:
            json.dump({"benchmarks": {"swe-bench-pro": {"name": "Other", "category": "coding", "aliases": []}}}, tmp)
        self.addCleanup(Path(tmp.name).unlink)
        with self.assertRaisesRegex(ValueError, "already exists"):
            digest_check.load_vocab([tmp.name])

    def test_committed_schema_is_current(self):
        committed = json.loads((generate.ROOT / "digest.schema.json").read_text(encoding="utf-8"))
        self.assertEqual(committed, digest_check.json_schema(self.VOCAB))

    def test_real_digest_passes(self):
        self.assertEqual(digest_check.check(self.MODEL, CATALOG, vocab=self.VOCAB), [])

    def test_normalize_and_render_are_deterministic(self):
        raw = json.loads((generate.ROOT / "grok-4.7" / "digest.json").read_text(encoding="utf-8"))
        once = digest_check.normalize(raw, self.MODEL, CATALOG, self.VOCAB)
        twice = digest_check.normalize(copy.deepcopy(once), self.MODEL, CATALOG, self.VOCAB)
        self.assertEqual(digest_check.canonical(once), digest_check.canonical(twice))
        self.assertEqual(digest_check.render_markdown(once, self.MODEL, CATALOG, self.VOCAB),
                         digest_check.render_markdown(twice, self.MODEL, CATALOG, self.VOCAB))

    def test_every_digest_uses_schema_version_2(self):
        for model in CATALOG["models"]:
            data = json.loads((generate.ROOT / model["slug"] / "digest.json").read_text(encoding="utf-8"))
            self.assertEqual(data.get("schema_version"), digest_check.SCHEMA_VERSION, model["slug"])

    def test_detects_structural_tampering(self):
        self.assert_flags("headings", mutate_md=lambda md: md.replace("## Evaluations", "## Benchmarks"))
        self.assert_flags("does not match digest.json", mutate_md=lambda md: md.replace("xAI's", "xAI\u2019s", 1))
        self.assert_flags("schema_version 2", lambda d: d.update(schema_version=1))
        self.assert_flags("facts.open_weights is required", lambda d: d["facts"].pop("open_weights"))
        self.assert_flags("disagrees with catalog", lambda d: d.update(lifecycle="retired"))

    def test_detects_value_and_vocabulary_errors(self):
        self.assert_flags("must be number", lambda d: d["evaluations"][0].update(value="46.3"))
        self.assert_flags("not in the vocabulary", lambda d: d["evaluations"][0].update(benchmark_id="no-such-bench"))
        self.assert_flags("does not match", lambda d: d["facts"]["knowledge_cutoff"].update(value="June 2026"))
        self.assert_flags("not a coding or agentic benchmark",
                          lambda d: [e.update(headline=True) for e in d["evaluations"]])

    def test_detects_citation_and_coverage_errors(self):
        self.assert_flags("outside", lambda d: d["capabilities"][0].update(pages=[9999]))
        self.assert_flags("needs at least one page", lambda d: d["facts"]["knowledge_cutoff"].update(pages=[]))
        self.assert_flags("missing required topic 'sabotage'",
                          lambda d: d.update(agentic_risks=[r for r in d["agentic_risks"] if r["topic"] != "sabotage"]))
        self.assert_flags("both list", lambda d: d["avoid_for"].append(dict(d["choose_for"][0])))
        self.assert_flags("pricing or billing", lambda d: d["limitations"][0].update(text="It has a lower price than "
                                                                                          "Grok 4.6 on most tasks."))

    def test_aggregate_joins_catalog_and_digests(self):
        aggregate = json.loads((generate.ROOT / "digests.json").read_text(encoding="utf-8"))
        self.assertEqual([m["slug"] for m in aggregate["models"]], [m["slug"] for m in CATALOG["models"]])
        grok = next(m for m in aggregate["models"] if m["slug"] == "grok-4.7")
        self.assertEqual(grok["catalog"]["provider"], "xAI")
        self.assertEqual(grok["digest"]["slug"], "grok-4.7")
        self.assertNotIn("rights", grok["catalog"])


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
