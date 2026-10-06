# Gemini 3.6 Flash

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write gemini-3.6-flash`. -->

> Original digest of *Gemini 3.6 Flash — Model Card* (Google DeepMind, July 2026; 7 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

**Copilot status:** Retired from GitHub Copilot on 2026-10-02. This digest is kept for historical comparison and model lineage.

## At a glance

Gemini 3.6 Flash is a retired Google Flash model built on 3.5 Flash, mainly useful now for lineage against later Flash releases. Its short card reports strong chart results on terminal, coding, computer-use, and long-context tasks, but inherits architecture, data, acceptable-use, and most Frontier Safety detail. Google says it is unlikely to reach any CCL and separately reports cyber below the CCL.

- **Choose it for:** Historical comparison for the Flash line, especially terminal, coding, OSWorld, and long-context baselines.
- **Watch out for:** Most safety and architecture detail is inherited, and the chart includes numbers that are not usable as current Copilot availability guidance.
- The chart shows a fast long-context predecessor with 58.7% on SWE-bench Pro, 49% on DeepSWE v1.1, 78.0% on Terminal-Bench 2.1, and 83.0% on OSWorld-Verified. (p. 4)
- Google describes it as based on 3.5 Flash, improving coding, knowledge work, multimodal performance, and token efficiency. (p. 2)
- It keeps the Flash multimodal interface: text, image, audio, and video inputs, 1M-token context, text output, and 64K-token output. (p. 2)
- Frontier Safety conclusions are inherited from 3.1 Pro; Google adds only that 3.6 Flash stays below the cyber CCL. (p. 7)
- Automated safety improves on text and multilingual rows against 3.5 Flash, while tone regresses and unjustified refusals rise slightly. (p. 6)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The card is dated 2026-07, but it does not state a separate model release date. | — |
| Knowledge cutoff | March 2026 (stated as knowledge cutoff date for Gemini 3.6 Flash is March 2026) | p. 5 |
| Context window | 1,000,000 tokens (stated as up to 1M tokens) | p. 2 |
| Maximum output | 64,000 tokens (stated as 64K token output) | p. 2 |
| Input modalities | Text, Image, Audio, Video | p. 2 |
| Output modalities | Text | p. 2 |
| Reasoning controls | Always reasons. The card calls it a reasoning model but does not describe adjustable levels. | p. 2 |
| Effort levels | Not stated. The card does not name the individual effort or thinking levels. | — |
| Tool use | Terminal, Computer use. The benchmark chart includes terminal and computer-use rows; no product tool interface is specified. | p. 4 |
| Open weights | Not stated. The card does not say the weights are open. | — |
| Architecture | Not stated. Architecture details are deferred to a predecessor or sibling card. | — |
| Total parameters | Not stated. The card does not state a parameter count. | — |
| Active parameters | Not stated. The card does not state active parameters. | — |

### Capability notes

- Google presents 3.6 Flash as a workhorse model with better coding, knowledge-work, multimodal performance, and token efficiency than 3.5 Flash. (p. 2)
- Inputs cover text, image, audio, and video, with up to 1M tokens of context and text output up to 64K tokens. (p. 2)
- The benchmark chart reports improvements over its predecessor on SWE-bench Pro, DeepSWE v1.1, MLE-Bench, OSWorld-Verified, and MRCR v2. (p. 4)
- The intended-use section names agent workflows, video-heavy reasoning, coding help, and enterprise workflows. (p. 5)
- Publisher distribution channels include Gemini apps, Gemini API, Google AI Studio, Antigravity, and an enterprise agent platform. (pp. 3-4)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| SWE-bench Pro | Public | pass@1 | 58.7% | — | Gemini 3.5 Flash 55.1%; Gemini 3.1 Pro 54.2%; GPT-5.6 Luna 62.7%; Grok 4.5 64.7%; Claude Sonnet 5 63.2% | p. 4 |
| DeepSWE v1.1 | — | pass@1 | 49.0% | — | Gemini 3.5 Flash 37.0%; Gemini 3.1 Pro 12.0%; GPT-5.6 Luna 67.0%; Grok 4.5 54.0%; Claude Sonnet 5 54.0% | p. 4 |
| Terminal-Bench 2.1 | — | success rate | 78.0% | Terminus-2 | Gemini 3.5 Flash 76.2%; Gemini 3.1 Pro 73.8%; GPT-5.6 Luna 84.7%; Grok 4.5 83.3%; Claude Sonnet 5 80.4% | p. 4 |
| OSWorld-Verified | — | pass@1 | 83.0% | — | Gemini 3.5 Flash 78.4%; Gemini 3.1 Pro 76.2%; GPT-5.6 Luna 72.6%; Claude Sonnet 5 81.2% | p. 4 |

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| MLE-bench | — | pass@1 | 63.9% | — | Gemini 3.5 Flash 49.7%; Gemini 3.1 Pro 42.6%; GPT-5.6 Luna 47.6%; Grok 4.5 43.2%; Claude Sonnet 5 66.9% | p. 4 |
| GDPval-AA v2 | — | Elo | 1,421 Elo | — | Gemini 3.5 Flash 1,349 Elo; Gemini 3.1 Pro 965 Elo; GPT-5.6 Luna 1,584 Elo; Grok 4.5 1,535 Elo; Claude Sonnet 5 1,607 Elo | p. 4 |
| CharXiv Reasoning | No tools | accuracy | 85.2% | — | Gemini 3.5 Flash 84.2%; Gemini 3.1 Pro 83.3%; GPT-5.6 Luna 82.7%; Grok 4.5 81.6%; Claude Sonnet 5 77.0% | p. 4 |
| CharXiv Reasoning | With tools | accuracy | 89.4% | — | Gemini 3.5 Flash 84.9%; Gemini 3.1 Pro 83.2%; Claude Sonnet 5 88.3% | p. 4 |
| MRCR v2 | 8-needle; 128K average | accuracy | 91.8% | — | Gemini 3.5 Flash 77.3%; Gemini 3.1 Pro 84.9%; GPT-5.6 Luna 74.8%; Grok 4.5 81.4%; Claude Sonnet 5 71.6% | p. 4 |
| MRCR v2 | 8-needle; 1M pointwise | accuracy | 54.0% | — | Gemini 3.5 Flash 26.6%; Gemini 3.1 Pro 26.3% | p. 4 |

## Safety findings

### Safety classification

- **Framework:** Google DeepMind Frontier Safety Framework
- **Overall determination:** Unlikely to reach any CCL based on Gemini 3.1 Pro; cyber CCL below threshold

Google relies on Gemini 3.1 Pro as the most capable assessed model and says 3.6 Flash has no meaningful new Frontier Safety capability increase. It adds that extra cyber testing kept 3.6 Flash below the cyber critical capability level. (p. 7)

| Domain | Determination | Level | Finding | Source |
| --- | --- | --- | --- | --- |
| Overall deployment standard | Below threshold | CCLs not reached | Based on Gemini 3.1 Pro results, Google assesses 3.6 Flash as unlikely to reach any Critical Capability Level. | p. 7 |
| Cybersecurity | Below threshold | Cyber CCL not reached | Additional cyber testing found Gemini 3.6 Flash below the cyber critical capability level. | p. 7 |

### Agentic-coding risks

- **Reward hacking** (not reported): The card reports no evaluation of grader gaming or reward exploitation.
- **Test tampering** (not reported): The card reports no test editing, deletion, or weakening evaluation.
- **Destructive or overeager actions** (not reported): The card reports no evaluation of irreversible or unrequested tool actions.
- **Sabotage** (not reported): The card does not report a sabotage or task-undermining evaluation for this model.
- **Prompt injection** (not reported): The card reports jailbreak and content-safety work, but not injected instructions from files, tools, or web content.
- **Honesty** (not reported): The card reports no honesty, deception, or false-task-success evaluation.
- **Sycophancy** (not reported): The card reports no sycophancy evaluation.
- **Over-refusal** (reported): Automated unjustified refusals worsen by 0.25 percentage points versus 3.5 Flash, with lower values preferred. (p. 6)

### Other safety findings

- Automated results versus 3.5 Flash improve text-to-text safety by 1.35 points and multilingual safety by 5.45 points, with lower values preferred. (p. 6)
- Tone worsens by 3.31 points and unjustified refusals worsen by 0.25 points in the same automated table. (p. 6)
- Manual review of automated losses found false positives or non-egregious cases. (p. 6)
- Specialist red teams found child-safety thresholds met, content safety similar or improved versus 3.5 Flash, and no egregious concerns. (p. 7)
- The Frontier Safety section relies on 3.1 Pro and adds that 3.6 Flash remains below the cyber CCL. (p. 7)

## Limitations and caveats

- Architecture, training data, training processing, hardware, and software are referred to the 3.5 Flash card. (pp. 2-3)
- Known limitations include hallucinations, continuing jailbreak-resistance work, strengthened Frontier Safety mitigations, occasional slowness or timeouts, and uneven knowledge recency. (p. 5)
- Capability methods are mostly external, with the main results embedded in a chart image. (p. 4)
- Automated safety scores are development evaluations rather than human evaluation or red teaming. (pp. 5-6)
- The Frontier Safety assessment is not a full per-domain table for this model. (p. 7)

## Practical implications for Copilot users

### Choose it for

- **Historical comparison:** The card is a direct predecessor reference for 3.7 and 3.8 Flash, with the chart showing the baseline those later cards compare against. (pp. 2, 4)
- **Terminal workflows:** Terminal-Bench 2.1 is 78.0%, making it a useful historical terminal-agent baseline. (p. 4)
- **Long context:** MRCR v2 is 91.8% at 128K average and 54.0% at 1M pointwise, higher than 3.5 Flash in the same chart. (p. 4)

### Avoid it for

- **Untrusted input:** Prompt-injection robustness is not reported, and risk detail is delegated to other cards. (pp. 5, 7)
- **High-stakes domains:** The card names hallucination and provides only inherited Frontier Safety conclusions for most domains. (pp. 5, 7)

### Guidance

- GitHub retired Gemini 3.6 Flash from Copilot on 2026-10-02; the guidance below serves historical comparison and the lineage of later models.
- Use this digest for lineage against later Flash cards; choose an available successor for new Copilot work.
- When comparing later Flash models, separate benchmark gains from changes in safety-evaluation methodology.
- Historical outputs from this model should be rechecked with current tests and sources.
- Do not infer current Copilot model-picker behavior from this retired entry.
- The inherited FSF treatment means later cards may be better sources for per-domain safety comparisons.

## Document coverage

The whole 7-page document is dedicated to Gemini 3.6 Flash. Its capability numbers come from a rendered benchmark image on page 4, while safety sections compare mostly against 3.5 Flash and rely on 3.1 Pro for Frontier Safety. The digest does not import the predecessor cards that the document repeatedly references.

- **Card type:** Dedicated. The document is about this model; it may include short sibling sections.
- **Pages specific to this model:** the whole document
- **Names the document uses for this model:** Gemini 3.6 Flash
- **Catalog scope:** Dedicated publisher card for this model.
