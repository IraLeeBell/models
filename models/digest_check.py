"""Validate, normalize, and render model digests (digest.json schema_version 2).

digest.json is the authored source of each digest. digest.md is rendered from it and catalog.json, so the two
always agree. See DIGESTS.md for the rules.

    python3 digest_check.py [<slug> ...]            # validate (default: every model)
    python3 digest_check.py --write <slug> ...      # normalize digest.json, render digest.md, then validate
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCHEMA_VERSION = 2
HEADINGS = [
    "At a glance", "Capabilities", "Evaluations", "Safety findings",
    "Limitations and caveats", "Practical implications for Copilot users", "Document coverage",
]
COPY_WINDOW = 12
LONG_DOCUMENT_PAGES = 20
MD_MARKER = ("<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run "
             "`python3 digest_check.py --write {slug}`. -->")
# Pricing, billing, and cost-management language stays out of digests. "Thinking budget" and similar phrases
# are model or harness terminology, so those compounds are allowed.
FORBIDDEN = re.compile(
    r"(?i)premium request|multiplier|finops|cost center|\bbill(?:s|ed|ing)?\b|\bpric(?:e|es|ed|ing)\b|"
    r"\bcosts?\b|\bcheap(?:er|est)?\b|"
    r"(?<!thinking )(?<!token )(?<!reasoning )(?<!compute )(?<!context )(?<!time )(?<!step )(?<!turn )"
    r"(?<!search )(?<!tool-call )(?<!inference )budget")
DATE = r"^[0-9]{4}(-(0[1-9]|1[0-2])(-(0[1-9]|[12][0-9]|3[01]))?)?$"
DAY = r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$"
VOCAB_ID = re.compile(r"[a-z0-9]+(?:[-.][a-z0-9]+)*")
SLUG = r"^[a-z0-9]+(?:[.-][a-z0-9]+)*$"
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]

# Facts in display order: (key, label, kind). The kind selects the value schema and formatting.
FACTS = [
    ("release_date", "Release date", "date"),
    ("knowledge_cutoff", "Knowledge cutoff", "date"),
    ("context_window_tokens", "Context window", "tokens"),
    ("max_output_tokens", "Maximum output", "tokens"),
    ("input_modalities", "Input modalities", "modalities"),
    ("output_modalities", "Output modalities", "modalities"),
    ("reasoning_controls", "Reasoning controls", "reasoning_controls"),
    ("effort_levels", "Effort levels", "strings"),
    ("tool_use", "Tool use", "tools"),
    ("open_weights", "Open weights", "bool"),
    ("architecture", "Architecture", "architectures"),
    ("parameters_total", "Total parameters", "count"),
    ("parameters_active", "Active parameters", "count"),
]
CITE = ["pages", "document", "section", "source"]
KEYS = {
    "top": ["schema_version", "slug", "model", "publisher", "lifecycle", "retired_on", "document", "supplements",
            "sources", "coverage", "summary", "at_a_glance", "facts", "capabilities", "evaluations",
            "safety_classification", "agentic_risks", "safety_findings", "limitations", "choose_for", "avoid_for",
            "practical_implications"],
    "document": ["id", "title", "publisher", "date", "format", "pages"],
    "supplement": ["id", "label", "title", "date", "pages"],
    "source": ["title", "url"],
    "coverage": ["card_type", "document_model_names", "model_pages", "note"],
    "glance": ["choose_it_for", "watch_out_for", "points"],
    "text": ["text"] + CITE,
    "fact": ["value", "as_stated", "note"] + CITE,
    "evaluation": ["benchmark_id", "benchmark", "variant", "metric", "value", "unit", "higher_is_better", "effort",
                   "harness", "setting", "run_by", "comparators", "headline", "note"] + CITE,
    "comparator": ["model", "value", "setting"],
    "safety": ["framework", "framework_name", "overall", "summary", "domains"] + CITE,
    "domain": ["domain", "determination", "level", "text"] + CITE,
    "risk": ["topic", "status", "text"] + CITE,
    "choice": ["use", "rationale"] + CITE,
    "implication": ["text"],
}
# Minimum and maximum item counts: (with a publisher document, without one).
COUNTS = {
    "capabilities": ((3, 8), (1, 8)),
    "safety_findings": ((3, 10), (0, 10)),
    "limitations": ((3, 8), (2, 8)),
    "choose_for": ((2, 4), (1, 4)),
    "avoid_for": ((2, 4), (1, 4)),
    "practical_implications": ((3, 7), (2, 7)),
}
MAX_EVALUATIONS, MAX_HEADLINE, MIN_HEADLINE = 30, 6, 3


# ---------------------------------------------------------------------------------------------------- vocabulary

def load_vocab(extra=(), root=ROOT):
    """Load vocabulary.json, adding entries from proposal files (which may only add new identifiers)."""
    vocab = json.loads((root / "vocabulary.json").read_text(encoding="utf-8"))
    for path in extra:
        for key, value in json.loads(Path(path).read_text(encoding="utf-8")).items():
            if isinstance(value, dict) and isinstance(vocab.get(key), dict):
                for ident, entry in value.items():
                    if ident in vocab[key] and vocab[key][ident] != entry:
                        raise ValueError(f"{path}: {key}.{ident} already exists in vocabulary.json")
                    vocab[key][ident] = entry
            elif isinstance(value, list) and isinstance(vocab.get(key), list):
                vocab[key] += [v for v in value if v not in vocab[key]]
            else:
                raise ValueError(f"{path}: cannot merge vocabulary key {key!r}")
    return vocab


def vocab_problems(vocab):
    """Return problems with the vocabulary itself."""
    problems = []
    sections = ["benchmark_categories", "benchmarks", "metrics", "units", "modalities", "reasoning_controls", "tools",
                "architectures", "use_cases", "safety_frameworks", "safety_domains", "safety_determinations",
                "risk_topics", "risk_statuses", "run_by", "card_types"]
    for section in sections:
        if not isinstance(vocab.get(section), dict) or not vocab[section]:
            problems.append(f"vocabulary: {section} must be a non-empty object")
            continue
        for ident, entry in vocab[section].items():
            if not VOCAB_ID.fullmatch(ident) or "internal" in ident:
                problems.append(f"vocabulary: {section} id {ident!r} is not a lowercase hyphenated identifier")
            if not isinstance(entry, dict) or not (entry.get("label") or entry.get("name")):
                problems.append(f"vocabulary: {section}.{ident} needs a label")
    names = {}
    for ident, entry in vocab.get("benchmarks", {}).items():
        if entry.get("category") not in vocab.get("benchmark_categories", {}):
            problems.append(f"vocabulary: benchmark {ident} has unknown category {entry.get('category')!r}")
        metric = entry.get("default_metric")
        if metric is not None and not metric_known(metric, vocab):
            problems.append(f"vocabulary: benchmark {ident} has unknown default_metric {metric!r}")
        for name in [entry.get("name")] + list(entry.get("aliases", [])):
            key = (name or "").casefold()
            if not key:
                problems.append(f"vocabulary: benchmark {ident} has an empty name or alias")
            elif names.setdefault(key, ident) != ident:
                problems.append(f"vocabulary: name or alias {name!r} is used by {names[key]} and {ident}")
    for category in vocab.get("headline_categories", []):
        if category not in vocab.get("benchmark_categories", {}):
            problems.append(f"vocabulary: headline category {category!r} is not a benchmark category")
    for domain, entry in vocab.get("safety_domains", {}).items():
        if not entry.get("group"):
            problems.append(f"vocabulary: safety domain {domain} needs a group")
    if not any(t.get("required") for t in vocab.get("risk_topics", {}).values()):
        problems.append("vocabulary: risk_topics needs required topics")
    return problems


def metric_known(metric, vocab):
    return metric in vocab["metrics"] or any(re.fullmatch(p["pattern"].strip("^$"), metric)
                                             for p in vocab.get("metric_patterns", []))


def metric_label(metric, vocab):
    if metric in vocab["metrics"]:
        return vocab["metrics"][metric]["label"]
    match = re.fullmatch(r"([a-z]+)-at-([0-9]+)", metric or "")
    return f"{match.group(1)}@{match.group(2)}" if match else str(metric)


def label(vocab, section, ident):
    entry = vocab.get(section, {}).get(ident)
    return (entry.get("label") or entry.get("name")) if isinstance(entry, dict) else str(ident)


# ---------------------------------------------------------------------------------------------------- JSON Schema

def json_schema(vocab):
    """Build the digest.json JSON Schema (draft 2020-12) from the vocabulary."""
    def ids(section):
        return list(vocab[section])

    def text(low, high):
        return {"type": "string", "minLength": low, "maxLength": high}

    def nullable(schema):
        out = dict(schema)
        out["type"] = [schema["type"], "null"]
        return out

    def obj(properties, optional=()):
        return {"type": "object", "required": [k for k in properties if k not in optional],
                "properties": properties, "additionalProperties": False}

    cite = {"pages": {"$ref": "#/$defs/pages"}, "document": {"type": ["string", "null"]},
            "section": text(1, 200), "source": {"type": "string", "pattern": "^https://"}}
    optional = ("section", "source")

    def fact(value):
        return obj({"value": value, "as_stated": nullable(text(1, 120)), "note": nullable(text(1, 300)), **cite},
                   optional)

    def id_list(section):
        return {"type": ["array", "null"], "items": {"enum": ids(section)}, "minItems": 1, "uniqueItems": True}

    value_schemas = {
        "date": {"type": ["string", "null"], "pattern": DATE},
        "tokens": {"type": ["integer", "null"], "minimum": 1},
        "count": {"type": ["integer", "null"], "minimum": 1},
        "bool": {"type": ["boolean", "null"]},
        "strings": {"type": ["array", "null"], "items": {"type": "string", "pattern": "^[a-z0-9][a-z0-9 -]*$"},
                    "minItems": 1, "uniqueItems": True},
        "architectures": {"enum": ids("architectures") + [None]},
    }
    for section in ("modalities", "reasoning_controls", "tools"):
        value_schemas[section] = id_list(section)
    metric = {"type": "string", "anyOf": [{"enum": ids("metrics")}] +
              [{"pattern": p["pattern"]} for p in vocab.get("metric_patterns", [])]}
    defs = {
        "pages": {"type": "array", "items": {"type": "integer", "minimum": 1}, "uniqueItems": True},
        "citedText": obj({"text": text(10, 600), **cite}, optional),
        "comparator": obj({"model": text(1, 80), "value": {"type": "number"}, "setting": nullable(text(1, 120))}),
        "evaluation": obj({
            "benchmark_id": {"enum": ids("benchmarks")}, "benchmark": text(1, 80),
            "variant": nullable(text(1, 80)), "metric": metric, "value": {"type": "number"},
            "unit": {"enum": ids("units")}, "higher_is_better": {"type": "boolean"},
            "effort": nullable(text(1, 40)), "harness": nullable(text(1, 120)), "setting": nullable(text(1, 160)),
            "run_by": {"enum": ids("run_by")},
            "comparators": {"type": "array", "items": {"$ref": "#/$defs/comparator"}, "maxItems": 6},
            "headline": {"type": "boolean"}, "note": nullable(text(1, 240)),
            **cite, "document": {"type": "string"}}, optional),
        "domain": obj({"domain": {"enum": ids("safety_domains")}, "determination": {"enum": ids("safety_determinations")},
                       "level": nullable(text(1, 40)), "text": text(10, 400), **cite}, optional),
        "risk": obj({"topic": {"enum": ids("risk_topics")}, "status": {"enum": ids("risk_statuses")},
                     "text": text(10, 500), **cite}, optional),
        "choice": obj({"use": {"enum": ids("use_cases")}, "rationale": text(10, 400), **cite}, optional),
    }

    def items(ref, low=0, high=None):
        out = {"type": "array", "items": {"$ref": f"#/$defs/{ref}"}, "minItems": low}
        if high:
            out["maxItems"] = high
        return out

    properties = {
        "schema_version": {"const": SCHEMA_VERSION},
        "slug": {"type": "string", "pattern": SLUG},
        "model": text(1, 120),
        "publisher": text(1, 80),
        "lifecycle": {"enum": ["current", "limited", "utility", "retired"]},
        "retired_on": {"type": ["string", "null"], "pattern": DAY},
        "document": nullable(obj({
            "id": text(1, 80), "title": text(1, 300), "publisher": text(1, 80),
            "date": {"type": ["string", "null"], "pattern": DATE}, "format": {"enum": ["pdf", "markdown"]},
            "pages": {"type": ["integer", "null"], "minimum": 1}})),
        "supplements": {"type": "array", "items": obj({
            "id": text(1, 80), "label": text(1, 40), "title": text(1, 300),
            "date": {"type": ["string", "null"], "pattern": DATE}, "pages": {"type": ["integer", "null"], "minimum": 1}})},
        "sources": {"type": "array", "uniqueItems": True,
                    "items": obj({"title": text(1, 200), "url": {"type": "string", "pattern": "^https://"}})},
        "coverage": obj({
            "card_type": {"enum": ids("card_types")},
            "document_model_names": {"type": "array", "items": text(1, 80), "uniqueItems": True},
            "model_pages": {"$ref": "#/$defs/pages"}, "note": text(80, 900)}),
        "summary": text(80, 600),
        "at_a_glance": obj({"choose_it_for": text(20, 240), "watch_out_for": text(20, 240),
                            "points": items("citedText", 3, 6)}),
        "facts": obj({key: fact(value_schemas[kind]) for key, _, kind in FACTS}),
        "capabilities": items("citedText", 1, 8),
        "evaluations": items("evaluation", 0, MAX_EVALUATIONS),
        "safety_classification": obj({
            "framework": {"enum": ids("safety_frameworks")}, "framework_name": nullable(text(1, 120)),
            "overall": nullable(text(1, 160)), "summary": text(20, 700),
            "domains": items("domain", 0, 12), **cite}, optional),
        "agentic_risks": items("risk", sum(1 for t in vocab["risk_topics"].values() if t.get("required")),
                               len(vocab["risk_topics"])),
        "safety_findings": items("citedText", 0, 10),
        "limitations": items("citedText", 2, 8),
        "choose_for": items("choice", 1, 4),
        "avoid_for": items("choice", 1, 4),
        "practical_implications": {"type": "array", "minItems": 2, "maxItems": 7,
                                   "items": obj({"text": text(10, 500)})},
    }
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://github.com/IraLeeBell/models/blob/main/models/digest.schema.json",
        "title": "Model digest (digest.json, schema_version 2)",
        "description": "Generated by models/generate.py from models/vocabulary.json. See models/DIGESTS.md.",
        "type": "object",
        "required": list(properties),
        "properties": properties,
        "additionalProperties": False,
        "$defs": defs,
    }


def _is(value, kind):
    if kind == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if kind == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return isinstance(value, {"object": dict, "array": list, "string": str, "boolean": bool,
                              "null": type(None)}[kind])


def _same(a, b):
    return type(a) is type(b) and a == b


def validate(value, schema, root, path="$"):
    """A small JSON Schema validator covering the keywords json_schema() uses. Returns error strings."""
    if "$ref" in schema:
        schema = root["$defs"][schema["$ref"].rsplit("/", 1)[1]]
    errors = []
    if "type" in schema:
        kinds = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(_is(value, k) for k in kinds):
            got = "boolean" if isinstance(value, bool) else type(value).__name__
            return [f"{path} must be {' or '.join(kinds)} (got {got})"]
    if "const" in schema and not _same(value, schema["const"]):
        errors.append(f"{path} must be {schema['const']!r}")
    if "enum" in schema and not any(_same(value, e) for e in schema["enum"]):
        errors.append(f"{path} value {value!r} is not in the vocabulary")
    if "anyOf" in schema and all(validate(value, s, root, path) for s in schema["anyOf"]):
        errors.append(f"{path} value {value!r} is not an allowed form")
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{path} is shorter than {schema['minLength']} characters")
        if len(value) > schema.get("maxLength", 10 ** 9):
            errors.append(f"{path} is longer than {schema['maxLength']} characters")
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append(f"{path} value {value!r} does not match {schema['pattern']}")
    if _is(value, "number") and value < schema.get("minimum", float("-inf")):
        errors.append(f"{path} must be at least {schema['minimum']}")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path} needs at least {schema['minItems']} items")
        if len(value) > schema.get("maxItems", 10 ** 9):
            errors.append(f"{path} allows at most {schema['maxItems']} items")
        if schema.get("uniqueItems"):
            seen = [json.dumps(v, sort_keys=True) for v in value]
            if len(seen) != len(set(seen)):
                errors.append(f"{path} has duplicate items")
        if "items" in schema:
            for index, item in enumerate(value):
                errors += validate(item, schema["items"], root, f"{path}[{index}]")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}.{key} is required")
        for key, item in value.items():
            if key in schema.get("properties", {}):
                errors += validate(item, schema["properties"][key], root, f"{path}.{key}")
            elif schema.get("additionalProperties") is False:
                errors.append(f"{path}.{key} is not an allowed key")
    return errors


# ---------------------------------------------------------------------------------------------------- normalize

def _pages(value):
    if isinstance(value, list) and all(_is(p, "integer") for p in value):
        return sorted(set(value))
    return value


def _ordered(item, kind, defaults=None):
    if not isinstance(item, dict):
        return item
    out, defaults = {}, defaults or {}
    for key in KEYS[kind]:
        if key in item:
            out[key] = item[key]
        elif key in defaults:
            out[key] = defaults[key]
    for key in item:
        out.setdefault(key, item[key])
    if "pages" in out:
        out["pages"] = _pages(out["pages"])
    return out


def _cited(item, kind, primary, extra=None):
    if not isinstance(item, dict):
        return item
    defaults = {"pages": [], "document": None if "source" in item else primary}
    defaults.update(extra or {})
    return _ordered(item, kind, defaults)


def _list(value, func):
    return [func(v) for v in value] if isinstance(value, list) else value


def normalize(data, model, catalog, vocab):
    """Return digest.json in canonical form: catalog-derived fields filled in, defaults added, keys ordered."""
    if not isinstance(data, dict):
        return data
    documents = catalog["documents"]
    primary = model.get("document")
    d = dict(data)
    d["slug"], d["model"], d["publisher"] = model["slug"], model["name"], model["provider"]
    d["lifecycle"], d["retired_on"] = model["lifecycle"], model.get("retired_on")
    if primary:
        doc = documents[primary]
        d["document"] = {"id": primary, "title": doc["title"], "publisher": doc["publisher"], "date": doc.get("date"),
                         "format": doc["format"], "pages": doc.get("pages")}
    else:
        d["document"] = None
    labels = {s.get("id"): s.get("label") for s in d.get("supplements") or [] if isinstance(s, dict)}
    d["supplements"] = [{"id": s, "label": labels.get(s), "title": documents[s]["title"],
                         "date": documents[s].get("date"), "pages": documents[s].get("pages")}
                        for s in model.get("supplements", [])]
    d.setdefault("sources", [])
    d["sources"] = _list(d["sources"], lambda s: _ordered(s, "source"))
    if isinstance(d.get("coverage"), dict):
        d["coverage"] = _ordered(d["coverage"], "coverage", {"document_model_names": [], "model_pages": []})
    if isinstance(d.get("at_a_glance"), dict):
        glance = _ordered(d["at_a_glance"], "glance")
        glance["points"] = _list(glance.get("points"), lambda i: _cited(i, "text", primary))
        d["at_a_glance"] = glance
    if isinstance(d.get("facts"), dict):
        order = [key for key, _, _ in FACTS] + [k for k in d["facts"] if k not in {f[0] for f in FACTS}]
        d["facts"] = {k: _cited(d["facts"][k], "fact", primary, {"as_stated": None, "note": None})
                      for k in order if k in d["facts"]}
    for key in ("capabilities", "safety_findings", "limitations"):
        d[key] = _list(d.get(key), lambda i: _cited(i, "text", primary))

    def evaluation(item):
        if not isinstance(item, dict):
            return item
        item = dict(item)
        entry = vocab["benchmarks"].get(item.get("benchmark_id"))
        if entry:
            item["benchmark"] = entry["name"]
        item["comparators"] = _list(item.get("comparators", []),
                                    lambda c: _ordered(c, "comparator", {"setting": None}))
        defaults = {k: None for k in ("variant", "effort", "harness", "setting", "note")}
        defaults["headline"] = False
        return _cited(item, "evaluation", primary, defaults)

    d["evaluations"] = _list(d.get("evaluations"), evaluation)
    if isinstance(d.get("safety_classification"), dict):
        safety = _cited(d["safety_classification"], "safety", primary,
                        {"framework_name": None, "overall": None, "domains": []})
        safety["domains"] = _list(safety["domains"], lambda i: _cited(i, "domain", primary, {"level": None}))
        d["safety_classification"] = safety
    if isinstance(d.get("agentic_risks"), list):
        order = list(vocab["risk_topics"])
        risks = [_cited(i, "risk", primary) for i in d["agentic_risks"]]
        d["agentic_risks"] = sorted(risks, key=lambda r: order.index(r.get("topic")) if isinstance(r, dict)
                                    and r.get("topic") in order else len(order))
    for key in ("choose_for", "avoid_for"):
        d[key] = _list(d.get(key), lambda i: _cited(i, "choice", primary))
    d["practical_implications"] = _list(d.get("practical_implications"), lambda i: _ordered(i, "implication"))
    return _ordered(d, "top")


def dumps(value, indent=0):
    """Deterministic JSON: two-space indentation, with lists of scalars kept on one line."""
    pad = "  " * indent
    if isinstance(value, dict):
        if not value:
            return "{}"
        body = ",\n".join(f"{pad}  {json.dumps(k, ensure_ascii=False)}: {dumps(v, indent + 1)}" for k, v in value.items())
        return "{\n" + body + "\n" + pad + "}"
    if isinstance(value, list):
        if not value:
            return "[]"
        if not any(isinstance(v, (dict, list)) for v in value):
            return "[" + ", ".join(json.dumps(v, ensure_ascii=False) for v in value) + "]"
        return "[\n" + ",\n".join(f"{pad}  {dumps(v, indent + 1)}" for v in value) + "\n" + pad + "]"
    return json.dumps(value, ensure_ascii=False)


def canonical(data):
    return dumps(data) + "\n"


# ---------------------------------------------------------------------------------------------------- render

def human_date(value):
    if not value:
        return "undated"
    parts = value.split("-")
    if len(parts) == 1:
        return parts[0]
    month = MONTHS[int(parts[1]) - 1]
    return f"{month} {int(parts[2])}, {parts[0]}" if len(parts) == 3 else f"{month} {parts[0]}"


def compress(pages):
    ranges = []
    for page in sorted(set(pages)):
        if ranges and page == ranges[-1][1] + 1:
            ranges[-1][1] = page
        else:
            ranges.append([page, page])
    return ", ".join(f"{a}-{b}" if a != b else str(a) for a, b in ranges)


def cite(item, data, bare=False):
    """Render an item's citation: (p. 5), (pp. 5-7), (August update, p. 3), (§ Heading), or a source link."""
    doc_id = item.get("document")
    if doc_id is None:
        url = item.get("source")
        if not url:
            return ""
        title = next((s["title"] for s in data.get("sources", []) if s.get("url") == url), url)
        text = f"[{title}]({url})"
    else:
        primary = (data.get("document") or {}).get("id")
        supplement = next((s.get("label") or s["id"] for s in data.get("supplements", []) if s["id"] == doc_id), None)
        prefix = "" if doc_id == primary else f"{supplement or doc_id}, "
        pages = item.get("pages") or []
        if pages:
            text = prefix + ("p. " if len(pages) == 1 else "pp. ") + compress(pages)
        elif item.get("section"):
            text = prefix + f"§ {item['section']}"
        else:
            return ""
    return text if bare else f"({text})"


def with_cite(text, item, data):
    citation = cite(item, data)
    return f"{text} {citation}" if citation else text


def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def number(value):
    return f"{value:,}"


def result(value, unit, vocab):
    n = number(abs(value)) if unit == "usd" else number(value)
    formats = {"percent": "{}%", "fraction": "{}", "score": "{}", "count": "{}", "elo": "{} Elo",
               "usd": ("-" if value < 0 else "") + "${}", "ratio": "{}×", "hours": "{} h", "minutes": "{} min",
               "tokens": "{} tokens", "rank": "#{}"}
    return formats.get(unit, "{} " + label(vocab, "units", unit)).format(n)


def human_count(value):
    for scale, word in ((10 ** 12, "trillion"), (10 ** 9, "billion"), (10 ** 6, "million")):
        if value >= scale:
            return f"{value / scale:g} {word}"
    return number(value)


def fact_value(key, kind, fact, vocab):
    value = fact.get("value")
    if value is None:
        text = "Not stated"
    elif kind == "date":
        text = human_date(value)
    elif kind == "tokens":
        text = f"{number(value)} tokens"
    elif kind == "count":
        text = human_count(value)
    elif kind == "bool":
        text = "Yes" if value else "No"
    elif kind == "strings":
        text = ", ".join(value)
    elif kind == "architectures":
        text = label(vocab, "architectures", value)
    else:
        text = ", ".join(label(vocab, kind, v) for v in value)
    if fact.get("as_stated"):
        text += f" (stated as {fact['as_stated']})"
    if fact.get("note"):
        text += f". {fact['note']}"
    return text


def copilot_status(model, catalog):
    from generate import CLI, LIFECYCLE  # generate imports this module, so import lazily

    if model["lifecycle"] == "retired":
        text = (f"**Copilot status:** Retired from GitHub Copilot on {model['retired_on']}. This digest is kept "
                "for historical comparison and model lineage.")
    else:
        parts = [f"{LIFECYCLE[model['lifecycle']]}; GitHub release status {model['release_status']}.",
                 f"CLI: {CLI[model['cli']]}."]
        if model.get("app_picker_observed") is not None:
            parts.append("App model picker: " + ("listed." if model["app_picker_observed"] else
                                                 "not listed on the check date."))
        if model.get("app_reasoning_efforts"):
            parts.append(f"App reasoning efforts: {', '.join(model['app_reasoning_efforts'])}.")
        if model.get("app_auto") is not None:
            parts.append(f"App Auto: {'yes' if model['app_auto'] else 'no'}.")
        if model.get("app_long_context") is not None:
            parts.append(f"App long-context option: {'yes' if model['app_long_context'] else 'no'}.")
        checked = catalog.get("app_picker_checked_at") or catalog["checked_at"]
        text = f"**Copilot status** (catalog checked {checked}): " + " ".join(parts)
    if model.get("note"):
        text += f" {model['note']}"
    return text


def eval_table(rows, data, vocab):
    lines = ["| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |",
             "| --- | --- | --- | --- | --- | --- | --- |"]
    for e in rows:
        metric = metric_label(e["metric"], vocab) + ("" if e["higher_is_better"] else " (lower is better)")
        setting = "; ".join(s for s in [f"{e['effort']} effort" if e.get("effort") else None, e.get("harness"),
                                        e.get("setting"), "third-party run" if e.get("run_by") == "third-party"
                                        else None] if s)
        if e.get("note"):
            setting = f"{setting}. {e['note']}" if setting else e["note"]
        comparators = "; ".join(f"{c['model']} {result(c['value'], e['unit'], vocab)}" +
                                (f" ({c['setting']})" if c.get("setting") else "") for c in e["comparators"])
        lines.append("| " + " | ".join(cell(x) for x in [
            e["benchmark"], e.get("variant") or "—", metric, result(e["value"], e["unit"], vocab),
            setting or "—", comparators or "—", cite(e, data, bare=True) or "—"]) + " |")
    return lines


def render_markdown(data, model, catalog, vocab):
    """Render digest.md from a normalized, schema-valid digest.json."""
    doc = data["document"]
    lines = [f"# {model['name']}", "", MD_MARKER.format(slug=model["slug"]), ""]
    if doc:
        record = catalog["documents"][doc["id"]]
        if doc["format"] == "pdf":
            what = (f"*{doc['title']}* ({doc['publisher']}, {human_date(doc['date'])}; {doc['pages']} pages). "
                    "Page references are PDF page numbers.")
            full = "system-card.md"
        else:
            what = (f"*{doc['title']}* ({doc['publisher']}, {human_date(doc['date'])}; Markdown model card, no PDF). "
                    "Citations use the card's section headings.")
            full = "model-card.md"
        clause = (f"[{full}]({full}) for the full text." if record["rights"] == "granted" else
                  "for the local workflow that produces the full text, `system-card.md`.")
        quote = [f"Original digest of {what} This summary paraphrases the publisher's document and is not a "
                 f"substitute for it; see [source.md](source.md) for provenance and {clause}"]
        for s in data["supplements"]:
            publisher = catalog["documents"][s["id"]]["publisher"]
            quote.append(f"Also cited: *{s['title']}* ({publisher}, {human_date(s['date'])}; {s['pages']} pages), "
                         f"cited as \"{s['label']}\".")
        if data["sources"]:
            quote.append("Additional owner documentation cited: " +
                         "; ".join(f"[{s['title']}]({s['url']})" for s in data["sources"]) + ".")
    else:
        quote = [f"No publisher system card or model card exists for {model['name']}. This digest summarizes the "
                 "closest owner documentation: " + "; ".join(f"[{s['title']}]({s['url']})" for s in data["sources"]) +
                 ". See [source.md](source.md) for provenance."]
    lines += [line for i, q in enumerate(quote) for line in ([">"] if i else []) + [f"> {q}"]]
    lines += ["", copilot_status(model, catalog), ""]

    glance = data["at_a_glance"]
    lines += ["## At a glance", "", data["summary"], "",
              f"- **Choose it for:** {glance['choose_it_for']}",
              f"- **Watch out for:** {glance['watch_out_for']}"]
    lines += [f"- {with_cite(p['text'], p, data)}" for p in glance["points"]]

    lines += ["", "## Capabilities", "", "### Key facts", "", "| Fact | Value | Source |", "| --- | --- | --- |"]
    for key, name, kind in FACTS:
        fact = data["facts"][key]
        lines.append(f"| {name} | {cell(fact_value(key, kind, fact, vocab))} | {cell(cite(fact, data, bare=True) or '—')} |")
    lines += ["", "### Capability notes", ""]
    lines += [f"- {with_cite(c['text'], c, data)}" for c in data["capabilities"]]

    lines += ["", "## Evaluations", ""]
    evaluations = data["evaluations"]
    if evaluations:
        headline = [e for e in evaluations if e["headline"]]
        other = [e for e in evaluations if not e["headline"]]
        lines += ["Results are as the document reports them. Scores from different publishers, harnesses, effort "
                  "levels, or tool settings are often not directly comparable; the Setting column records those "
                  "conditions.", "", "### Headline coding and agentic results", ""]
        lines += eval_table(headline, data, vocab) if headline else ["The document reports no coding or agentic "
                                                                     "benchmark results for this model."]
        lines += ["", "### Other reported results", ""]
        lines += eval_table(other, data, vocab) if other else ["None beyond the headline results."]
    else:
        lines.append("The owner documentation reports no benchmark results for this model.")

    safety = data["safety_classification"]
    framework = label(vocab, "safety_frameworks", safety["framework"])
    if safety.get("framework_name"):
        framework += f" (named \u201c{safety['framework_name']}\u201d in the document)"
    lines += ["", "## Safety findings", "", "### Safety classification", "",
              f"- **Framework:** {framework}",
              f"- **Overall determination:** {safety.get('overall') or 'Not stated'}", "",
              with_cite(safety["summary"], safety, data), ""]
    if safety["domains"]:
        lines += ["| Domain | Determination | Level | Finding | Source |", "| --- | --- | --- | --- | --- |"]
        lines += ["| " + " | ".join(cell(x) for x in [
            label(vocab, "safety_domains", d["domain"]), label(vocab, "safety_determinations", d["determination"]),
            d.get("level") or "—", d["text"], cite(d, data, bare=True) or "—"]) + " |" for d in safety["domains"]]
    else:
        lines.append("The document states no per-domain determinations.")
    lines += ["", "### Agentic-coding risks", ""]
    for risk in data["agentic_risks"]:
        status = label(vocab, "risk_statuses", risk["status"]).lower()
        lines.append(f"- **{label(vocab, 'risk_topics', risk['topic'])}** ({status}): "
                     f"{with_cite(risk['text'], risk, data)}")
    lines += ["", "### Other safety findings", ""]
    lines += ([f"- {with_cite(s['text'], s, data)}" for s in data["safety_findings"]] or
              ["The owner documentation reports no other safety findings."])

    lines += ["", "## Limitations and caveats", ""]
    lines += [f"- {with_cite(x['text'], x, data)}" for x in data["limitations"]]

    lines += ["", "## Practical implications for Copilot users", ""]
    for key, heading in (("choose_for", "Choose it for"), ("avoid_for", "Avoid it for")):
        lines += [f"### {heading}", ""]
        lines += [f"- **{label(vocab, 'use_cases', c['use'])}:** {with_cite(c['rationale'], c, data)}" for c in data[key]]
        lines.append("")
    lines += ["### Guidance", ""]
    if model["lifecycle"] == "retired":
        lines.append(f"- GitHub retired {model['name']} from Copilot on {model['retired_on']}; the guidance below "
                     "serves historical comparison and the lineage of later models.")
    lines += [f"- {p['text']}" for p in data["practical_implications"]]

    coverage = data["coverage"]
    card_type = coverage["card_type"]
    if coverage["model_pages"]:
        pages = ("p. " if len(coverage["model_pages"]) == 1 else "pp. ") + compress(coverage["model_pages"])
    else:
        pages = {"dedicated": "the whole document", "same-weights": "the whole document",
                 "none": "not applicable"}.get(card_type, "not separated by page")
    lines += ["", "## Document coverage", "", coverage["note"], "",
              f"- **Card type:** {label(vocab, 'card_types', card_type)}. "
              f"{vocab['card_types'][card_type].get('description', '')}.".rstrip(". ") + ".",
              f"- **Pages specific to this model:** {pages}"]
    if coverage["document_model_names"]:
        lines.append("- **Names the document uses for this model:** " + ", ".join(coverage["document_model_names"]))
    lines.append(f"- **Catalog scope:** {model['scope']}")
    if model.get("card_note"):
        lines.append(f"- **Catalog note:** {model['card_note']}")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------------------------------- checks

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


def markdown_sections(text):
    return {re.sub(r"\s+", " ", m.group(1)).strip() for m in re.finditer(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.M)}


def cited_items(data):
    """Yield (path, item, citation_required) for every citable item."""
    for i, item in enumerate(data["at_a_glance"]["points"]):
        yield f"at_a_glance.points[{i}]", item, True
    for key, fact in data["facts"].items():
        yield f"facts.{key}", fact, fact["value"] is not None
    for key in ("capabilities", "evaluations", "safety_findings", "limitations", "choose_for", "avoid_for"):
        for i, item in enumerate(data[key]):
            yield f"{key}[{i}]", item, True
    safety = data["safety_classification"]
    yield "safety_classification", safety, safety["framework"] != "none-stated"
    for i, item in enumerate(safety["domains"]):
        yield f"safety_classification.domains[{i}]", item, item["determination"] != "not-stated"
    for i, item in enumerate(data["agentic_risks"]):
        yield f"agentic_risks[{i}]", item, item["status"] in ("reported", "family-level")


def semantic_problems(data, model, catalog, vocab, root=ROOT):
    """Rules beyond the JSON Schema. `data` must be normalized and schema-valid."""
    slug, problems = model["slug"], []
    documents = catalog["documents"]
    primary = model.get("document")
    allowed = {doc_id: documents[doc_id] for doc_id in ([primary] if primary else []) + model.get("supplements", [])}
    urls = [s["url"] for s in data["sources"]]
    sections = None
    if primary and documents[primary]["format"] != "pdf" and (root / slug / "model-card.md").is_file():
        sections = markdown_sections((root / slug / "model-card.md").read_text(encoding="utf-8"))

    def p(message):
        problems.append(f"{slug}: {message}")

    for path, item, required in cited_items(data):
        doc_id, pages, section, source = item.get("document"), item.get("pages", []), item.get("section"), item.get("source")
        if doc_id is None:
            if source is None and required:
                p(f"{path} needs a citation (document pages, a section, or a listed source)")
            if source is not None and source not in urls:
                p(f"{path} source {source} is not listed in sources")
            if pages:
                p(f"{path} has pages but no document")
            continue
        if doc_id not in allowed:
            p(f"{path} cites unknown document {doc_id!r}")
            continue
        if source is not None:
            p(f"{path} cites both a document and a source; split it")
        target = allowed[doc_id]
        if target["format"] == "pdf":
            bad = [n for n in pages if not 1 <= n <= target["pages"]]
            if bad:
                p(f"{path} pages {bad} outside 1..{target['pages']}")
            if required and not pages:
                p(f"{path} needs at least one page of {doc_id}")
        else:
            if pages:
                p(f"{path} cites pages of a Markdown document; use section instead")
            if required and not section:
                p(f"{path} needs a section heading of the Markdown document")
            if section and sections is not None and section not in sections:
                p(f"{path} section {section!r} is not a heading in model-card.md")

    counts = 1 if primary else 0
    for key, limits in COUNTS.items():
        low, high = limits[1 - counts]
        if not low <= len(data[key]) <= high:
            p(f"{key} needs {low}-{high} items (has {len(data[key])})")
    if primary and not data["coverage"]["document_model_names"]:
        p("coverage.document_model_names needs the name(s) the document uses for this model")
    card_type = data["coverage"]["card_type"]
    if (card_type == "none") != (primary is None):
        p("coverage.card_type must be 'none' exactly when the catalog maps no document")
    if primary and documents[primary].get("pages"):
        bad = [n for n in data["coverage"]["model_pages"] if n > documents[primary]["pages"]]
        if bad:
            p(f"coverage.model_pages {bad} outside 1..{documents[primary]['pages']}")
    if not primary and not data["sources"]:
        p("sources must list the closest owner documentation when there is no publisher card")
    for s in data["supplements"]:
        if not s["label"]:
            p(f"supplements: {s['id']} needs a short citation label, such as 'August update'")

    facts = data["facts"]
    total, active = facts["parameters_total"]["value"], facts["parameters_active"]["value"]
    if total and active and active > total:
        p("facts.parameters_active exceeds parameters_total")

    evaluations = data["evaluations"]
    pages = (documents[primary].get("pages") or 0) if primary else 0
    minimum = 0 if not primary else 8 if pages >= LONG_DOCUMENT_PAGES else 3
    if len(evaluations) < minimum:
        p(f"evaluations needs at least {minimum} rows for this document (has {len(evaluations)})")
    headline_categories = set(vocab["headline_categories"])
    eligible = [e for e in evaluations if vocab["benchmarks"][e["benchmark_id"]]["category"] in headline_categories]
    headline = [e for e in evaluations if e["headline"]]
    for i, e in enumerate(evaluations):
        if e["headline"] and e not in eligible:
            p(f"evaluations[{i}] {e['benchmark_id']} is headline but not a coding or agentic benchmark")
        if not metric_known(e["metric"], vocab):
            p(f"evaluations[{i}] metric {e['metric']!r} is not in the vocabulary")
        if e["unit"] == "percent" and not -100 <= e["value"] <= 100:
            p(f"evaluations[{i}] percent value {e['value']} is outside -100..100")
        if e["unit"] == "fraction" and not -1 <= e["value"] <= 1:
            p(f"evaluations[{i}] fraction value {e['value']} is outside -1..1")
        if any(c["model"] in (model["name"], *data["coverage"]["document_model_names"]) for c in e["comparators"]):
            p(f"evaluations[{i}] lists this model as its own comparator; use a separate row")
    if len(headline) > MAX_HEADLINE:
        p(f"evaluations: at most {MAX_HEADLINE} headline rows (has {len(headline)})")
    if len(headline) < min(MIN_HEADLINE, len(eligible)):
        p(f"evaluations: mark at least {min(MIN_HEADLINE, len(eligible))} coding or agentic rows as headline")
    keys = [(e["benchmark_id"], e["variant"], e["metric"], e["effort"], e["harness"], e["setting"], e["document"])
            for e in evaluations]
    for key in sorted({k for k in keys if keys.count(k) > 1}, key=str):
        p(f"evaluations: duplicate row {key[0]} (variant {key[1]!r}, effort {key[3]!r}); distinguish or merge")

    safety = data["safety_classification"]
    if not primary and (safety["framework"] != "none-stated" or safety["domains"]):
        p("safety_classification must use framework 'none-stated' and no domains without a publisher card")
    publisher = vocab["safety_frameworks"][safety["framework"]].get("publisher")
    if publisher and publisher != model["provider"]:
        p(f"safety_classification.framework {safety['framework']} belongs to {publisher}, not {model['provider']}")

    topics = [r["topic"] for r in data["agentic_risks"]]
    for topic, entry in vocab["risk_topics"].items():
        if entry.get("required") and topic not in topics:
            p(f"agentic_risks is missing required topic {topic!r} (use status 'not-reported' if absent)")
    for topic in sorted({t for t in topics if topics.count(t) > 1}):
        p(f"agentic_risks lists {topic!r} more than once")

    for key in ("choose_for", "avoid_for"):
        uses = [c["use"] for c in data[key]]
        if len(uses) != len(set(uses)):
            p(f"{key} repeats a use case")
    both = {c["use"] for c in data["choose_for"]} & {c["use"] for c in data["avoid_for"]}
    if both:
        p(f"choose_for and avoid_for both list {sorted(both)}")
    return problems


def identity_problems(raw, model, catalog):
    slug, problems = model["slug"], []
    expected = {"slug": slug, "model": model["name"], "publisher": model["provider"],
                "lifecycle": model["lifecycle"], "retired_on": model.get("retired_on")}
    for key, value in expected.items():
        if raw.get(key) != value:
            problems.append(f"{slug}: digest.json {key}={raw.get(key)!r} disagrees with catalog.json ({value!r})")
    doc_id = (raw.get("document") or {}).get("id") if isinstance(raw.get("document"), dict) else None
    if doc_id != model.get("document"):
        problems.append(f"{slug}: digest.json document id {doc_id!r} disagrees with catalog.json "
                        f"({model.get('document')!r})")
    return problems


def load_normalized(model, catalog, vocab, root=ROOT):
    """Return (normalized digest, schema errors), or (None, [reason]) when digest.json cannot be used."""
    path = root / model["slug"] / "digest.json"
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return None, [f"digest.json cannot be read ({error})"]
    if not isinstance(raw, dict) or raw.get("schema_version") != SCHEMA_VERSION:
        return None, [f"digest.json must be an object with schema_version {SCHEMA_VERSION} (see DIGESTS.md)"]
    data = normalize(raw, model, catalog, vocab)
    schema = json_schema(vocab)
    return data, validate(data, schema, schema)


def check(model, catalog, root=ROOT, extraction=None, vocab=None):
    """Return a list of problems for one catalog model."""
    vocab = vocab or load_vocab(root=root if (root / "vocabulary.json").is_file() else ROOT)
    slug = model["slug"]
    folder = root / slug
    md_path, json_path = folder / "digest.md", folder / "digest.json"
    if not md_path.is_file() or not json_path.is_file():
        return [f"{slug}: digest.md and digest.json are required"]
    raw_text, md = json_path.read_text(encoding="utf-8"), md_path.read_text(encoding="utf-8")
    data, errors = load_normalized(model, catalog, vocab, root)
    if data is None:
        return [f"{slug}: {e}" for e in errors]
    problems = identity_problems(json.loads(raw_text), model, catalog)
    problems += [f"{slug}: digest.json {e}" for e in errors]
    if not errors:
        problems += semantic_problems(data, model, catalog, vocab, root)
    if raw_text != canonical(data):
        problems.append(f"{slug}: digest.json is not in canonical form; run python3 digest_check.py --write {slug}")
    found = re.findall(r"^## (.+?)\s*$", md, re.MULTILINE)
    if found != HEADINGS:
        problems.append(f"{slug}: digest.md headings {found} != {HEADINGS}")
    if not errors and md != render_markdown(data, model, catalog, vocab):
        problems.append(f"{slug}: digest.md does not match digest.json; run python3 digest_check.py --write {slug}")
    match = FORBIDDEN.search(md) or FORBIDDEN.search(raw_text)
    if match:
        problems.append(f"{slug}: digest mentions pricing or billing ({match.group(0)!r}); keep it out")
    if extraction is not None:
        for run in copied_runs(md + "\n" + raw_text, extraction):
            problems.append(f"{slug}: copies {len(run.split())} consecutive source words: '{run[:90]}...'")
    return problems


def write(model, catalog, vocab, root=ROOT):
    """Normalize digest.json and render digest.md. Returns problems that prevented rendering."""
    path = root / model["slug"] / "digest.json"
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return [f"{model['slug']}: digest.json cannot be read ({error})"]
    data = normalize(raw, model, catalog, vocab)
    path.write_text(canonical(data), encoding="utf-8")
    schema = json_schema(vocab)
    errors = validate(data, schema, schema)
    if errors:
        return [f"{model['slug']}: digest.md not rendered until digest.json is schema-valid"]
    (root / model["slug"] / "digest.md").write_text(render_markdown(data, model, catalog, vocab), encoding="utf-8")
    return []


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("slugs", nargs="*", help="models to check (default: all)")
    parser.add_argument("--write", action="store_true", help="normalize digest.json and render digest.md first")
    parser.add_argument("--vocab-extra", action="append", default=[], type=Path,
                        help="vocabulary proposal file whose new identifiers are accepted (repeatable)")
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
    vocab = load_vocab(args.vocab_extra)
    problems = vocab_problems(vocab)
    source = "\n".join(Path(p).read_text(encoding="utf-8") for p in args.extraction) if args.extraction else None
    for slug in args.slugs or models:
        model = models[slug]
        if args.write:
            problems += write(model, catalog, vocab)
        text = source
        if text is None:
            from generate import load_catalog, local_sources
            text = local_sources(model, load_catalog(), args.extraction_dir)
        problems += check(model, catalog, extraction=text, vocab=vocab)
    print("\n".join(problems) or "digests OK")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
