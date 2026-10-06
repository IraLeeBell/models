# Gemini 3 Flash

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write gemini-3-flash`. -->

> Original digest of *Gemini 3 Flash Model Card* (Google DeepMind, December 2025; 6 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

**Copilot status:** Retired from GitHub Copilot on 2026-07-31. This digest is kept for historical comparison and model lineage. GitHub listed it for VS Code and other IDEs but not for the CLI.

## At a glance

Gemini 3 Flash is a retired early Flash model built on Gemini 3 Pro and offered historically outside the Copilot CLI. Its short card reports broad reasoning, coding, tool-use, multimodal, factuality, multilingual, and long-context results in a single chart image. Safety and limitations are mostly inherited from Gemini 3 Pro, with direct automated comparisons against Gemini 2.5 Flash.

- **Choose it for:** Historical comparison for the first Gemini 3 Flash baseline across coding, terminal, tool-use, MCP, and multimodal rows.
- **Watch out for:** No dedicated per-domain Frontier Safety table, and most risk and limitation details are delegated to Gemini 3 Pro.
- The chart image reports strong tool and coding results for its era: 78.0% on SWE-bench Verified, 47.6% on Terminal-Bench 2.0, 90.2% on τ²-bench, 49.4% on Toolathlon, and 57.4% on MCP Atlas. (p. 4)
- It is an early Flash model based on Gemini 3 Pro, with thinking levels, 1M-token multimodal input, and 64K-token text output. (p. 2)
- Frontier Safety is not evaluated directly for Flash; Google relies on Gemini 3 Pro Preview and says Flash is less capable and unlikely to reach any CCL. (p. 6)
- Automated safety improves versus Gemini 2.5 Flash on text-to-text safety, image-to-text safety, tone, and unjustified refusals, while multilingual safety worsens slightly but is labeled non-egregious. (p. 5)
- Most distribution, known limitations, acceptable-use, safety-policy, and risk-mitigation details are deferred to Gemini 3 Pro. (pp. 3, 5-6)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The card is dated 2025-12, but it does not state a separate model release date. | — |
| Knowledge cutoff | Not stated. The card does not state a knowledge cutoff for this model. | — |
| Context window | 1,000,000 tokens (stated as up to 1M tokens) | p. 2 |
| Maximum output | 64,000 tokens (stated as 64K token output) | p. 2 |
| Input modalities | Text, Image, Audio, Video | p. 2 |
| Output modalities | Text | p. 2 |
| Reasoning controls | Effort levels. The card says thinking levels control quality, latency, and token usage, but it does not list the level names. | p. 2 |
| Effort levels | Not stated. The card does not name the individual effort or thinking levels. | — |
| Tool use | Terminal, MCP, Function calling, Web search, Code execution. The chart includes terminal, tool-use, MCP, and search plus code execution rows; no product tool surface is specified. | p. 4 |
| Open weights | Not stated. The card does not say the weights are open. | — |
| Architecture | Not stated. Architecture details are deferred to a predecessor or sibling card. | — |
| Total parameters | Not stated. The card does not state a parameter count. | — |
| Active parameters | Not stated. The card does not state active parameters. | — |

### Capability notes

- Google describes Gemini 3 Flash as an early fast Gemini 3 reasoning model based on Gemini 3 Pro. (p. 2)
- The model accepts text, images, audio, and video, with up to 1M tokens of context and 64K tokens of text output. (p. 2)
- Training used Google TPUs and JAX plus ML Pathways. (p. 3)
- Intended uses include agentic workflows, everyday coding, reasoning and planning, and multimodal analysis. (p. 5)
- The chart covers reasoning, coding, tool use, factuality, multilingual, multimodal, video, and long-context benchmarks. (p. 4)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| LiveCodeBench Pro | — | Elo | 2,316 Elo | — | Gemini 3 Pro 2,439 Elo; Gemini 2.5 Flash 1,143 Elo; Gemini 2.5 Pro 1,775 Elo; Claude Sonnet 4.5 1,418 Elo; GPT-5.2 2,393 Elo | p. 4 |
| Terminal-Bench 2.0 | — | success rate | 47.6% | Terminus-2 | Gemini 3 Pro 54.2%; Gemini 2.5 Flash 16.9%; Gemini 2.5 Pro 32.6%; Claude Sonnet 4.5 42.8% | p. 4 |
| SWE-bench Verified | Single attempt | pass@1 | 78.0% | — | Gemini 3 Pro 76.2%; Gemini 2.5 Flash 60.4%; Gemini 2.5 Pro 59.6%; Claude Sonnet 4.5 77.2%; GPT-5.2 80.0%; Grok 4.1 Fast 50.6% | p. 4 |
| τ²-bench | — | success rate | 90.2% | — | Gemini 3 Pro 90.7%; Gemini 2.5 Flash 79.5%; Gemini 2.5 Pro 77.8%; Claude Sonnet 4.5 87.2% | p. 4 |
| Toolathlon | — | pass@1 | 49.4% | — | Gemini 3 Pro 36.4%; Gemini 2.5 Flash 3.7%; Gemini 2.5 Pro 10.5%; Claude Sonnet 4.5 38.9%; GPT-5.2 46.3% | p. 4 |
| MCP Atlas | — | success rate | 57.4% | — | Gemini 3 Pro 54.1%; Gemini 2.5 Flash 3.4%; Gemini 2.5 Pro 8.8%; Claude Sonnet 4.5 43.8%; GPT-5.2 60.6% | p. 4 |

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Humanity's Last Exam | No tools | accuracy | 33.7% | — | Gemini 3 Pro 37.5%; Gemini 2.5 Flash 11.0%; Gemini 2.5 Pro 21.6%; Claude Sonnet 4.5 13.7%; GPT-5.2 34.5%; Grok 4.1 Fast 17.6% | p. 4 |
| Humanity's Last Exam | Search and code execution | accuracy | 43.5% | — | Gemini 3 Pro 45.8%; GPT-5.2 45.5% | p. 4 |
| ARC-AGI-2 | — | accuracy | 33.6% | — | Gemini 3 Pro 31.1%; Gemini 2.5 Flash 2.5%; Gemini 2.5 Pro 4.9%; Claude Sonnet 4.5 13.6%; GPT-5.2 52.9% | p. 4 |
| GPQA Diamond | No tools | accuracy | 90.4% | — | Gemini 3 Pro 91.9%; Gemini 2.5 Flash 82.8%; Gemini 2.5 Pro 86.4%; Claude Sonnet 4.5 83.4%; GPT-5.2 92.4%; Grok 4.1 Fast 84.3% | p. 4 |
| AIME 2025 | No tools | accuracy | 95.2% | — | Gemini 3 Pro 95.0%; Gemini 2.5 Flash 72.0%; Gemini 2.5 Pro 88.0%; Claude Sonnet 4.5 87.0%; GPT-5.2 100.0%; Grok 4.1 Fast 91.9% | p. 4 |
| AIME 2025 | With code execution | accuracy | 99.7% | — | Gemini 3 Pro 100.0%; Gemini 2.5 Flash 75.7%; Claude Sonnet 4.5 100.0% | p. 4 |
| MMMU-Pro | — | accuracy | 81.2% | — | Gemini 3 Pro 81.0%; Gemini 2.5 Flash 66.7%; Gemini 2.5 Pro 68.0%; Claude Sonnet 4.5 68.0%; GPT-5.2 79.5%; Grok 4.1 Fast 63.0% | p. 4 |
| ScreenSpot-Pro | No tools unless specified | accuracy | 69.1% | — | Gemini 3 Pro 72.7%; Gemini 2.5 Flash 3.9%; Gemini 2.5 Pro 11.4%; Claude Sonnet 4.5 36.2%; GPT-5.2 86.3% (with Python) | p. 4 |
| CharXiv Reasoning | No tools | accuracy | 80.3% | — | Gemini 3 Pro 81.4%; Gemini 2.5 Flash 63.7%; Gemini 2.5 Pro 69.6%; Claude Sonnet 4.5 68.5%; GPT-5.2 82.1% | p. 4 |
| Video-MMMU | — | accuracy | 86.9% | — | Gemini 3 Pro 87.6%; Gemini 2.5 Flash 79.2%; Gemini 2.5 Pro 83.6%; Claude Sonnet 4.5 77.8%; GPT-5.2 85.9% | p. 4 |
| FACTS Benchmark Suite | — | score | 61.9% | — | Gemini 3 Pro 70.5%; Gemini 2.5 Flash 50.4%; Gemini 2.5 Pro 63.4%; Claude Sonnet 4.5 48.9%; GPT-5.2 61.4%; Grok 4.1 Fast 42.1% | p. 4 |
| SimpleQA Verified | — | accuracy | 68.7% | — | Gemini 3 Pro 72.1%; Gemini 2.5 Flash 28.1%; Gemini 2.5 Pro 54.5%; Claude Sonnet 4.5 29.3%; GPT-5.2 38.0%; Grok 4.1 Fast 19.5% | p. 4 |
| MMMLU | — | accuracy | 91.8% | — | Gemini 3 Pro 91.8%; Gemini 2.5 Flash 86.6%; Gemini 2.5 Pro 89.5%; Claude Sonnet 4.5 89.1%; GPT-5.2 89.6%; Grok 4.1 Fast 86.8% | p. 4 |
| MRCR v2 | 8-needle; 128K average | accuracy | 67.2% | — | Gemini 3 Pro 77.0%; Gemini 2.5 Flash 54.3%; Gemini 2.5 Pro 58.0%; Claude Sonnet 4.5 47.1%; GPT-5.2 81.9%; Grok 4.1 Fast 54.6% | p. 4 |
| MRCR v2 | 8-needle; 1M pointwise | accuracy | 22.1% | — | Gemini 3 Pro 26.3%; Gemini 2.5 Flash 21.0%; Gemini 2.5 Pro 16.4%; Grok 4.1 Fast 6.1% | p. 4 |

## Safety findings

### Safety classification

- **Framework:** Google DeepMind Frontier Safety Framework
- **Overall determination:** Unlikely to reach any CCL based on Gemini 3 Pro Preview

Google did not run a dedicated Flash FSF table in this card. It relies on Gemini 3 Pro Preview, which did not reach CCLs, and says Gemini 3 Flash is less capable and therefore unlikely to reach any CCL. (p. 6)

| Domain | Determination | Level | Finding | Source |
| --- | --- | --- | --- | --- |
| Overall deployment standard | Below threshold | CCLs not reached | Based on Gemini 3 Pro Preview, Google deems Gemini 3 Flash acceptable for deployment and unlikely to reach any Critical Capability Level. | p. 6 |

### Agentic-coding risks

- **Reward hacking** (not reported): The card reports no evaluation of grader gaming or reward exploitation.
- **Test tampering** (not reported): The card reports no test editing, deletion, or weakening evaluation.
- **Destructive or overeager actions** (not reported): The card reports no evaluation of irreversible or unrequested tool actions.
- **Sabotage** (not reported): The card does not report a sabotage or task-undermining evaluation for this model.
- **Prompt injection** (not reported): The card reports jailbreak and content-safety work, but not injected instructions from files, tools, or web content.
- **Honesty** (not reported): The card reports no honesty, deception, or false-task-success evaluation.
- **Sycophancy** (not reported): The card reports no sycophancy evaluation.
- **Over-refusal** (reported): Automated unjustified refusals improve by 10.4 percentage points versus Gemini 2.5 Flash, with lower values preferred. (p. 5)

### Other safety findings

- Automated safety versus Gemini 2.5 Flash improves text-to-text safety by 3.1 points, image-to-text safety by 2.3 points, tone by 3.8 points, and unjustified refusals by 10.4 points. (p. 5)
- Multilingual safety worsens by 0.1 points but is labeled non-egregious. (p. 5)
- Manual review of automated losses found false positives or non-egregious cases. (p. 6)
- Specialist red teams found child-safety thresholds satisfied, content safety similar or improved versus Gemini 2.5 Flash, and no egregious concerns. (p. 6)
- Google relies on Gemini 3 Pro Preview Frontier Safety results and says Flash is less capable and unlikely to reach any CCL. (p. 6)

## Limitations and caveats

- Known limitations are not restated; the card directs readers to Gemini 3 Pro. (p. 5)
- Acceptable use, safety evaluation approach, and safety policies are also delegated to Gemini 3 Pro. (p. 5)
- The capability methodology is external, with most numbers in a chart image. (p. 4)
- Training and development safety results are automated tests rather than human evaluation or red teaming. (p. 5)
- Risk and mitigation details are deferred to Gemini 3 Pro. (p. 6)

## Practical implications for Copilot users

### Choose it for

- **Historical comparison:** The model is the baseline that later Flash cards build on, and its chart supplies the first Gemini 3 Flash tool-use and coding comparison set. (pp. 2, 4)
- **Agentic coding:** SWE-bench Verified is 78.0%, Terminal-Bench 2.0 is 47.6%, and Toolathlon is 49.4%. (p. 4)
- **Vision:** The card reports MMMU-Pro at 81.2%, ScreenSpot-Pro at 69.1%, and Video-MMMU at 86.9%. (p. 4)

### Avoid it for

- **Untrusted input:** The card reports no prompt-injection evaluation and delegates risk mitigations to Gemini 3 Pro. (pp. 5-6)
- **High-stakes domains:** Limitations and safety policies are not detailed in this card, so it is a weak standalone source for high-stakes use. (p. 5)

### Guidance

- GitHub retired Gemini 3 Flash from Copilot on 2026-07-31; the guidance below serves historical comparison and the lineage of later models.
- Use this digest as historical lineage only; GitHub retired this model and did not list it for the Copilot CLI.
- For old outputs, rerun current tests and factual checks because the card delegates limitations.
- Do not compare its automated safety rows directly to later cards without considering Google’s methodology caveat.
- Agentic tool rows are useful for lineage, but reward-hacking, test-tampering, and prompt injection are not tested.

## Document coverage

The whole 6-page document is dedicated to Gemini 3 Flash. Page 4 is a rendered benchmark image and page 5 includes a rendered safety table. The document points to Gemini 3 Pro for many limitations, policies, distribution, risk, and Frontier Safety details; this digest records only what the Flash card itself states.

- **Card type:** Dedicated. The document is about this model; it may include short sibling sections.
- **Pages specific to this model:** the whole document
- **Names the document uses for this model:** Gemini 3 Flash
- **Catalog scope:** Dedicated publisher card for this model.
