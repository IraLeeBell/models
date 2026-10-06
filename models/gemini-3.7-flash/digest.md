# Gemini 3.7 Flash

> Original digest of *Gemini 3.7 Flash — Model Card* (Google DeepMind, 2026-08; 9 pages). Page references are PDF
> page numbers. This summary paraphrases the publisher's document and is not a substitute for it;
> see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance
- Dedicated August 2026 card for Gemini 3.7 Flash, a current GitHub Copilot model.
- Google describes it as a Gemini 3.6 Flash successor with stronger core reasoning and agentic video understanding (p. 2).
- It supports text, image, audio, and video inputs up to 1M tokens and text output up to 64K tokens (p. 2).
- The benchmark chart covers coding, agent, knowledge-work, long-context, biology, PDF, and desktop/OS tasks (p. 5).
- Automated safety results are mostly close to Gemini 3.6 Flash, with low unjustified refusals in Google’s summary (pp. 6-7).
- The Frontier Safety table says no tracked or critical capability level is reached, though cyber and some CBRN results are near alert concepts (pp. 8-9).

## Capabilities
- The card attributes 3.7 Flash to algorithmic improvements over 3.6 Flash and adds support for agentic video understanding. (p. 2)
- Inputs include text, images, audio, and video with a context window of up to 1M tokens. (p. 2)
- The output channel is text with a 64K-token maximum. (p. 2)
- Thinking configurations can be customized to tune answer quality and latency for different workloads. (p. 2)
- The intended-use section names agentic workflows, complex video reasoning, coding, and enterprise workflows. (p. 5)
- The distribution list includes Gemini App, Gemini Enterprise App, Gemini Enterprise Agent Platform, Google AI Studio, Gemini API, Google AI Mode, and Google Antigravity. (p. 3)

## Evaluations
| Benchmark | Result | Context | Pages |
|---|---|---|---|
| Artificial Analysis Intelligence Index | 56 | Composite intelligence score; one point below the highest values shown. | p. 5 |
| FrontierCode 1.1 Main | 43.6% | Production-code quality score; above the comparison models with reported values. | p. 5 |
| DeepSWE v1.1 | 65.3% | Long-horizon software engineering; higher than Gemini 3.6 Flash. | p. 5 |
| Code Arena | 1588 Elo | Web-development benchmark; highest row value in the chart. | p. 5 |
| Terminal-bench 2.1 | 85.8% | Agentic terminal coding benchmark. | p. 5 |
| Terminal-bench 3.0 | 14.9% | General agent capabilities; below GPT-5.6 Terra in the chart. | p. 5 |
| AutomationBench | 30.4% | Private enterprise workflow automation set. | p. 5 |
| GDPVal-AA v2 | 1525 Elo | Knowledge-work benchmark. | p. 5 |
| Harvey LAB-AA | 90.7% | Complex legal workflows; above all listed comparisons with values. | p. 5 |
| GDP.pdf | 34.0% | Expert PDF document comprehension. | p. 5 |
| CharXiv Reasoning | 84.5% without tools; 88.7% with tools | Information synthesis from complex charts. | p. 5 |
| LVBench | 85.4% | Long-video understanding benchmark. | p. 5 |
| GDM-MRCR v2 (8-needle) | 97.0% at 128K average | Long-context performance row; chart does not list a 1M value for 3.7 Flash. | p. 5 |
| OSWorld-2.0 | 47.9% | Agentic computer-use benchmark. | p. 5 |
| Agent's Last Exam | 26.3% pass rate | Multimodal desktop and OS-agent tasks. | p. 5 |
| HLE-Verified | 53.6% | Multidisciplinary expert reasoning. | p. 5 |
| BioMysteryBench | 87.1% human-solvable; 43.5% human-difficult | Bioinformatics research reasoning benchmark. | p. 5 |
| LABBench2 | 82.1% | Biology real-world research tasks. | p. 5 |

## Safety findings
- Automated safety results versus Gemini 3.6 Flash show text-to-text safety up 1.17 percentage points, multilingual safety down 0.48 points, image-to-text unchanged, tone down 0.47 points, and unjustified refusals up 0.84 points. (p. 7)
- Google summarizes the automated development results as similar to 3.6 Flash on safety and tone, with low unjustified refusals. (p. 6)
- Manual red teaming found required child-safety thresholds met and similar or better content-safety behavior relative to Gemini 3.6 Flash. (pp. 7-8)
- The CBRN Frontier Safety row rules out both the tracked level and the critical level, while noting high theoretical ability and some actionable expert-elicited answers. (p. 8)
- The cybersecurity row says the model reaches an alert threshold for Uplift Level 1 but remains below the critical capability level. (p. 8)
- The ML R&D and misalignment row says the model can solve individual coding tasks and recognize some testing settings, but it cannot bypass restrictions or carry out an independent end-to-end research workflow. (p. 9)

## Limitations and caveats
- Google flags hallucination as a remaining foundation-model limitation. (p. 6)
- The card says jailbreak resistance and Frontier Safety mitigations continue to be improved. (p. 6)
- Occasional slowness or timeouts are listed as possible operational issues. (p. 6)
- The knowledge cutoff is March 2026 overall, with some areas potentially limited to January 2025 knowledge. (p. 6)
- The safety table is automated development testing rather than human evaluation or red-team measurement. (pp. 6-7)
- Google cautions that the improved safety evaluations are not directly comparable with older Gemini model-card results. (p. 7)

## Practical implications for Copilot users
- 3.7 Flash is a good fit for quick agentic coding, video, and document-understanding questions when users still plan to verify final outputs.
- For terminal or automation tasks, keep tool permissions narrow because the card reports material agent capability without claiming autonomous reliability.
- The Frontier Safety cyber alert-threshold note supports sandboxing commands, reviewing network access, and avoiding uncontrolled exploit-development workflows.
- Use citations, tests, and source files for knowledge-heavy answers because the card still identifies hallucination and uneven recency as risks.
- If safety behavior matters in non-English settings, compare outputs carefully because automated safety metrics move in different directions by category.

## Document coverage
This digest uses pages 2-4 for model setup, modalities, distribution, and evaluation scope; page 5 for the benchmark chart; pages 6-7 for limitations and automated safety; and pages 8-9 for human red teaming and Frontier Safety. The card is dedicated to Gemini 3.7 Flash, but architecture, data, and several policy details are referred back to the Gemini 3.6 Flash card. It mentions an external evaluation methodology page and a separate Frontier Safety Framework report without reproducing their contents.
