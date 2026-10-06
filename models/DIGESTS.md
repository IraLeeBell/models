# Writing digests

Each model folder has an original `digest.md` and a structured `digest.json` that summarize the publisher's document. They are this repository's own writing (MIT license), not extracts. `digest_check.py` enforces the rules below. `generate.py --check` runs it for every folder.

## Before writing

1. Create the local extraction: `python3 local_cards.py --model <slug>` writes `system-card.md`, plus `supplements/<document-id>.md` when the model has supplements. Each PDF page begins with `<!-- page N of M -->`. Cite these PDF page numbers N, not the page numbers printed in the document's footers. A ````text block on a page holds that page's complete plain text; treat it as part of the page.
2. Read the model's entry in `catalog.json`, including its `scope`, `card_note`, `note`, `lifecycle`, and `supplements`. Then read the document's entry for the exact title, publisher, date, and page count.
3. Read the document broadly: the table of contents, then capabilities and benchmarks, then the safety, preparedness, and responsible-scaling evaluations, then alignment and model welfare where present, then agentic, coding, and cyber sections, then limitations. Verify every number against the page you cite.

## `digest.md` layout

```text
# <exact catalog model name>

> Original digest of *<document title>* (<publisher>, <date>; <N> pages). Page references are PDF
> page numbers. This summary paraphrases the publisher's document and is not a substitute for it;
> see [source.md](source.md) for provenance and <FULL TEXT CLAUSE>

## At a glance
## Capabilities
## Evaluations
## Safety findings
## Limitations and caveats
## Practical implications for Copilot users
## Document coverage
```

Link only to files that are committed. Replace `<FULL TEXT CLAUSE>` with `[system-card.md](system-card.md) for the full text.` when the PDF's rights are `granted`, `[model-card.md](model-card.md) for the full text.` for a granted Markdown card, and otherwise ``for the local workflow that produces the full text, `system-card.md`.`` `generate.py --check` rejects relative links to files that would not be committed.

Use exactly these seven `##` headings, in this order, and no other `##` headings. Use `###` or bold text for sub-structure.

- **At a glance:** 5–8 bullets. Cover what the model is, its release date, how the document covers this specific model, headline capability claims, the headline safety determination (for example, an ASL level, Preparedness categories rated High, or Frontier Safety Framework thresholds), and deployment notes.
- **Capabilities:** architecture, context, modalities, and tools where stated, plus coding and agentic strengths. End each claim with a citation such as `(p. 12)` or `(pp. 12-14)`.
- **Evaluations:** a table with the columns `| Benchmark | Result | Context | Pages |`. Use at least 8 rows for long cards and at least 3 for short ones. Include comparison models only where the document gives them.
- **Safety findings:** whatever the document covers, with citations. This may include dangerous-capability evaluations (CBRN, cyber, autonomy and AI R&D), alignment audits, reward hacking, sabotage, prompt injection, honesty and sycophancy, harmful-content metrics, jailbreak robustness, and welfare.
- **Limitations and caveats:** known weaknesses, evaluation caveats, what the document says it did not test, regressions, and residual risks.
- **Practical implications for Copilot users:** 4–7 bullets of your own reasoning about what the findings mean when using the model in the Copilot CLI or app. Cover task fit, when to prefer the model, review and verification practices, agentic safety practices (permissions, sandboxing, prompt-injection exposure), and failure modes to watch. Do not invent Copilot features. Leave out pricing, billing, and cost management entirely.
- **Document coverage:** 2–4 sentences on which sections and pages the digest draws on and what it omits. For family or joint cards, say exactly which parts apply to this model and which to sibling models.

### Lifecycle

- **Retired models:** the first implications bullet states GitHub's retirement date and says the remaining bullets serve historical comparison and the successor's lineage.
- **Limited models:** say who still has access, as GitHub documents it.

### Supplements and non-PDF documents

- Cite a supplement page as `(August update, p. 5)`.
- For an owner document in Markdown, cite `(§ <section heading>)` instead of page numbers.

### Folders without a publisher card

These folders use four headings: `At a glance`, `What the publisher documents`, `Practical implications for Copilot users`, and `Document coverage`. The block quote under the title states that no publisher system card or model card exists and links the closest owner documentation.

## `digest.json` (schema_version 1)

```json
{
  "schema_version": 1,
  "slug": "<slug>",
  "model": "<exact catalog model name>",
  "publisher": "<catalog provider>",
  "document": {"id": "<document id>", "title": "<exact catalog title>", "pages": 0},
  "summary": "<2-4 sentence original summary>",
  "capabilities": [{"text": "...", "pages": [12, 13]}],
  "evaluations": [{"benchmark": "...", "result": "...", "context": "...", "pages": [20]}],
  "safety_findings": [{"text": "...", "pages": [40]}],
  "limitations": [{"text": "...", "pages": [55]}],
  "practical_implications": [{"text": "..."}],
  "coverage_notes": "..."
}
```

- **Minimum item counts:** capabilities 3, evaluations 3, safety_findings 3, limitations 3, and practical_implications 3. The JSON must agree with `digest.md`. Its evaluations may be the most important subset of the table.
- **Pages:** integers within the cited document's page range.
- **Supplement items:** add `"document": "<supplement id>"` to an item that cites a supplement.
- **Markdown owner documents:** items use `"pages": []` and add `"section": "<heading>"`.
- **No-card folders:** `"document": null`. These need at least 1 capability, 2 limitations, and 2 practical implications. `evaluations` and `safety_findings` may be empty. Each capability and limitation uses `"pages": []` and adds `"source": "<owner URL>"`.

## Originality and accuracy

- **Paraphrase, don't copy.** The checker rejects any run of 12 or more consecutive words that also appears in the source. Text inside double quotes is exempt; keep such quotations short, rare, and under 15 words.
- **Facts may be reproduced.** Benchmark names, model names, and numbers are facts.
- **Do not overstate scope.** For a family or joint card, never attribute a sibling model's results to this model.
- **Stick to the public document.** If the document does not report something, say so; do not fill the gap. Leave out internal identifiers, customer information, and billing or cost-management language.
- **Style:** neutral, precise American English with no marketing tone.

## Check

```sh
python3 digest_check.py <slug>      # uses the folder's local extraction for the copy check
python3 generate.py --check         # every folder, plus generated files and rights rules
```
