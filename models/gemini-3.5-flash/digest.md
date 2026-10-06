# Gemini 3.5 Flash

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write gemini-3.5-flash`. -->

> Original digest of *Gemini 3.5 Flash Model Card* (Google DeepMind, May 2026; 7 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

**Copilot status:** Retired from GitHub Copilot on 2026-10-02. This digest is kept for historical comparison and model lineage.

## At a glance

Gemini 3.5 Flash is a retired Google Flash model built on Gemini 3 Flash, mainly useful for comparing the Flash lineage. Its chart emphasizes terminal, MCP-style, computer-use, finance, multimodal, and long-context tasks. Safety coverage is short: automated rows compare to Gemini 3 Flash, while Frontier Safety relies on 3.1 Pro and a separate cyber check.

- **Choose it for:** Historical comparison for Flash agentic-tool, terminal, and computer-use gains over Gemini 3 Flash.
- **Watch out for:** Most architecture, limitation, acceptable-use, and risk detail is delegated to other Gemini cards.
- The chart’s strongest agentic rows are MCP Atlas at 83.6%, Toolathlon at 56.5%, Terminal-Bench 2.1 at 76.2%, OSWorld-Verified at 78.4%, and SWE-bench Pro at 53.9%. (p. 4)
- The card presents 3.5 Flash as a 3 Flash successor with thinking levels, 1M-token multimodal input, and 64K-token text output. (p. 2)
- Safety comparisons improve text, multilingual, and tone rows versus Gemini 3 Flash, while unjustified refusals rise 0.8 percentage points. (p. 6)
- Frontier Safety is inherited from 3.1 Pro; Google says 3.5 Flash is unlikely to reach any CCL and stays below the cyber CCL. (p. 7)
- Most underlying detail is delegated to Gemini 3 Flash or Gemini 3.1 Pro, so the card is a lineage snapshot rather than a standalone system card. (pp. 5, 7)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The card is dated 2026-05, but it does not state a separate model release date. | — |
| Knowledge cutoff | Not stated. The card does not state a knowledge cutoff for this model. | — |
| Context window | 1,000,000 tokens (stated as up to 1M tokens) | p. 2 |
| Maximum output | 64,000 tokens (stated as 64K token output) | p. 2 |
| Input modalities | Text, Image, Audio, Video | p. 2 |
| Output modalities | Text | p. 2 |
| Reasoning controls | Effort levels. The card says thinking levels control quality, latency, and token usage, but does not list level names. | p. 2 |
| Effort levels | Not stated. The card does not name the individual effort or thinking levels. | — |
| Tool use | Terminal, Computer use, MCP, Function calling. The benchmark chart includes terminal, OSWorld, Toolathlon, and MCP Atlas rows; no product tool surface is specified. | p. 4 |
| Open weights | Not stated. The card does not say the weights are open. | — |
| Architecture | Not stated. Architecture details are deferred to a predecessor or sibling card. | — |
| Total parameters | Not stated. The card does not state a parameter count. | — |
| Active parameters | Not stated. The card does not state active parameters. | — |

### Capability notes

- The card frames 3.5 Flash as a Gemini 3 Flash successor with thinking levels for task-dependent behavior. (p. 2)
- Inputs are text, images, audio, and video with up to 1M tokens of context; outputs are text up to 64K tokens. (p. 2)
- The publisher lists Gemini app, Gemini Enterprise App, Gemini API, Google AI Studio, Search AI Mode, Antigravity, and an enterprise agent platform as distribution channels. (p. 3)
- Google names agentic workflows, coding, and multi-week enterprise processes as intended uses. (p. 5)
- The chart reports strong gains over Gemini 3 Flash on MCP Atlas, Toolathlon, Finance Agent v2, GDPval-AA, and the MRCR v2 long-context row. (p. 4)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Terminal-Bench 2.1 | — | success rate | 76.2% | Terminus-2 | Gemini 3 Flash 58.0%; Gemini 3.1 Pro 70.3%; Claude Opus 4.7 66.1%; GPT-5.5 78.2% | p. 4 |
| SWE-bench Pro | Public | pass@1 | 53.9% | — | Gemini 3 Flash 48.4%; Gemini 3.1 Pro 54.2%; Claude Sonnet 4.6 53.0%; Claude Opus 4.7 64.3%; GPT-5.5 58.6% | p. 4 |
| MCP Atlas | — | success rate | 83.6% | — | Gemini 3 Flash 62.0%; Gemini 3.1 Pro 78.2%; Claude Sonnet 4.6 69.5%; Claude Opus 4.7 79.1%; GPT-5.5 75.3% | p. 4 |
| Toolathlon | — | pass@1 | 56.5% | — | Gemini 3 Flash 49.4%; GPT-5.5 55.6% | p. 4 |
| OSWorld-Verified | — | pass@1 | 78.4% | — | Gemini 3 Flash 65.1%; Gemini 3.1 Pro 76.2%; Claude Sonnet 4.6 72.5%; Claude Opus 4.7 78.0%; GPT-5.5 78.7% | p. 4 |

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Finance Agent v2 | — | accuracy | 57.9% | — | Gemini 3 Flash 42.6%; Gemini 3.1 Pro 43.0%; Claude Sonnet 4.6 51.0%; Claude Opus 4.7 51.5%; GPT-5.5 51.8% | p. 4 |
| GDPval-AA | — | Elo | 1,656 Elo | — | Gemini 3 Flash 1,204 Elo; Gemini 3.1 Pro 1,314 Elo; Claude Sonnet 4.6 1,674 Elo; Claude Opus 4.7 1,753 Elo; GPT-5.5 1,773 Elo | p. 4 |
| CharXiv Reasoning | No tools | accuracy | 84.2% | — | Gemini 3 Flash 80.3%; Gemini 3.1 Pro 83.3%; Claude Sonnet 4.6 70.5%; Claude Opus 4.7 82.1%; GPT-5.5 84.1% | p. 4 |
| MMMU-Pro | No tools | accuracy | 83.6% | — | Gemini 3 Flash 81.2%; Gemini 3.1 Pro 80.5%; Claude Sonnet 4.6 74.5%; Claude Opus 4.7 75.2%; GPT-5.5 81.2% | p. 4 |
| MRCR v2 | 8-needle; 128K average | accuracy | 77.3% | — | Gemini 3 Flash 67.2%; Gemini 3.1 Pro 84.9%; Claude Sonnet 4.6 84.9%; Claude Opus 4.7 59.3%; GPT-5.5 94.8% | p. 4 |
| MRCR v2 | 8-needle; 1M pointwise | accuracy | 26.6% | — | Gemini 3 Flash 22.1%; Gemini 3.1 Pro 26.3% | p. 4 |
| Humanity's Last Exam | — | accuracy | 40.2% | — | Gemini 3 Flash 33.7%; Gemini 3.1 Pro 44.4%; Claude Sonnet 4.6 33.2%; Claude Opus 4.7 46.9%; GPT-5.5 41.4% | p. 4 |
| ARC-AGI-2 | — | accuracy | 72.1% | — | Gemini 3 Flash 33.6%; Gemini 3.1 Pro 77.1%; Claude Sonnet 4.6 58.3%; Claude Opus 4.7 75.8%; GPT-5.5 85.0% | p. 4 |

## Safety findings

### Safety classification

- **Framework:** Google DeepMind Frontier Safety Framework
- **Overall determination:** Unlikely to reach any CCL based on Gemini 3.1 Pro; cyber CCL below threshold

Google bases the Frontier Safety conclusion on 3.1 Pro, says 3.5 Flash has no meaningful new Frontier Safety capability increase, and adds that additional cyber testing kept the model below the cyber CCL. (p. 7)

| Domain | Determination | Level | Finding | Source |
| --- | --- | --- | --- | --- |
| Overall deployment standard | Below threshold | CCLs not reached | Based on Gemini 3.1 Pro results, Google assesses 3.5 Flash as unlikely to reach any CCL. | p. 7 |
| Cybersecurity | Below threshold | Cyber CCL not reached | Additional cyber testing found Gemini 3.5 Flash below the cyber critical capability level. | p. 7 |

### Agentic-coding risks

- **Reward hacking** (not reported): The card reports no evaluation of grader gaming or reward exploitation.
- **Test tampering** (not reported): The card reports no test editing, deletion, or weakening evaluation.
- **Destructive or overeager actions** (not reported): The card reports no evaluation of irreversible or unrequested tool actions.
- **Sabotage** (not reported): The card does not report a sabotage or task-undermining evaluation for this model.
- **Prompt injection** (not reported): The card reports jailbreak and content-safety work, but not injected instructions from files, tools, or web content.
- **Honesty** (not reported): The card reports no honesty, deception, or false-task-success evaluation.
- **Sycophancy** (not reported): The card reports no sycophancy evaluation.
- **Over-refusal** (reported): Automated unjustified refusals worsen by 0.8 percentage points versus Gemini 3 Flash, with a non-egregious note. (p. 6)

### Other safety findings

- Automated safety against Gemini 3 Flash improves text-to-text safety by 3.9 points and multilingual safety by 2.6 points; image-to-text is unchanged. (p. 6)
- Tone improves by 8.9 points, while unjustified refusals worsen by 0.8 points and are labeled non-egregious. (p. 6)
- Manual review of automated losses found false positives or non-egregious cases. (p. 6)
- Specialist red teams found child-safety thresholds satisfied, content safety similar or improved versus Gemini 3 Flash, and no egregious concerns. (p. 6)
- Frontier Safety relies on 3.1 Pro and adds that 3.5 Flash remains below the cyber CCL. (p. 7)

## Limitations and caveats

- Known limitations are not restated; the card points to Gemini 3 Flash. (p. 5)
- Acceptable-use, evaluation-approach, and safety-policy details are delegated to Gemini 3 Flash. (p. 5)
- Capability methods are external, and benchmark values are in an image. (p. 4)
- The safety table is automated development testing, not human evaluation or red teaming. (p. 6)
- Risk and mitigation details are mostly deferred to Gemini 3.1 Pro. (p. 7)

## Practical implications for Copilot users

### Choose it for

- **Historical comparison:** The model is a direct predecessor to 3.6 Flash, and later Flash cards compare against this era of benchmarks and safety tests. (pp. 2, 4)
- **Agentic coding:** The chart includes 76.2% on Terminal-Bench 2.1, 53.9% on SWE-bench Pro, and 83.6% on MCP Atlas. (p. 4)
- **Computer use:** OSWorld-Verified is 78.4%, close to the strongest values in the chart. (p. 4)

### Avoid it for

- **Untrusted input:** Prompt-injection testing is not reported, while tool and agentic rows imply exposure to external content. (pp. 4, 7)
- **High-stakes domains:** The card omits detailed limitations and relies on other documents for risk mitigations. (pp. 5, 7)

### Guidance

- GitHub retired Gemini 3.5 Flash from Copilot on 2026-10-02; the guidance below serves historical comparison and the lineage of later models.
- Use this digest as historical context; GitHub retired the model and newer Gemini entries supersede it.
- For old agent outputs, rerun tests because the card does not report reward-hacking or test-tampering evaluations.
- When comparing Flash generations, account for methodology changes called out in the safety section.
- Do not infer current Copilot app or CLI availability from a retired model.

## Document coverage

The whole 7-page document is dedicated to Gemini 3.5 Flash. It has one benchmark image and one safety-table image; many underlying details are delegated to Gemini 3 Flash and Gemini 3.1 Pro. This digest records only what this short card states and treats the model as a retired historical comparison point.

- **Card type:** Dedicated. The document is about this model; it may include short sibling sections.
- **Pages specific to this model:** the whole document
- **Names the document uses for this model:** Gemini 3.5 Flash
- **Catalog scope:** Dedicated publisher card for this model.
