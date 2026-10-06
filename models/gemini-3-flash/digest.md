# Gemini 3 Flash

> Original digest of *Gemini 3 Flash Model Card* (Google DeepMind, 2025-12; 6 pages). Page references are PDF
> page numbers. This summary paraphrases the publisher's document and is not a substitute for it;
> see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance
- Dedicated December 2025 card for Gemini 3 Flash; GitHub retired the model on 2026-07-31 and did not list it for the CLI.
- Google describes the model as built from the Gemini 3 Pro reasoning foundation with thinking levels for task control (p. 2).
- Inputs include text, images, audio, and video up to 1M tokens; outputs are text up to 64K tokens (p. 2).
- The benchmark chart reports reasoning, coding, tool-use, factuality, multilingual, multimodal, and long-context scores (p. 4).
- Automated safety metrics improve over Gemini 2.5 Flash for text safety, image safety, tone, and unjustified refusals, while multilingual safety rises slightly but is labeled non-egregious (p. 5).
- The Frontier Safety assessment relies on Gemini 3 Pro Preview and says Gemini 3 Flash was acceptable for deployment under the framework criteria used by Google (p. 6).

## Capabilities
- Gemini 3 Flash is described as a highly capable, natively multimodal reasoning model in the Gemini 3 series. (p. 2)
- The model is based on Gemini 3 Pro and includes thinking levels for different task demands. (p. 2)
- The card lists text, image, audio, and video inputs with context up to 1M tokens. (p. 2)
- Text output can be up to 64K tokens. (p. 2)
- Training hardware is described as Google TPUs, and training software as JAX and ML Pathways. (p. 3)
- Google lists agentic workflows, everyday coding, reasoning and planning, and multimodal analysis as intended use cases. (p. 5)

## Evaluations
| Benchmark | Result | Context | Pages |
|---|---|---|---|
| Humanity's Last Exam | 33.7% without tools; 43.5% with search and code execution | Academic reasoning on full-set text and multimodal tasks. | p. 4 |
| ARC-AGI-2 | 33.6% | ARC Prize Verified visual reasoning puzzles. | p. 4 |
| GPQA Diamond | 90.4% | Scientific-knowledge benchmark without tools. | p. 4 |
| AIME 2025 | 95.2% without tools; 99.7% with code execution | Mathematics benchmark. | p. 4 |
| MMMU-Pro | 81.2% | Multimodal understanding and reasoning. | p. 4 |
| ScreenSpot-Pro | 69.1% | Screen-understanding benchmark. | p. 4 |
| CharXiv Reasoning | 80.3% | Information synthesis from complex charts without tools. | p. 4 |
| OmniDocBench 1.5 | 0.121 | OCR overall edit distance; lower values are better. | p. 4 |
| Video-MMMU | 86.9% | Knowledge acquisition from videos. | p. 4 |
| LiveCodeBench Pro | 2316 Elo | Competitive coding problems. | p. 4 |
| Terminal-bench 2.0 | 47.6% | Agentic terminal coding on the Terminus-2 harness. | p. 4 |
| SWE-bench Verified | 78.0% | Single-attempt agentic coding benchmark. | p. 4 |
| t2-bench | 90.2% | Agentic tool-use benchmark. | p. 4 |
| Toolathlon | 49.4% | Long-horizon real-world software tasks. | p. 4 |
| MCP Atlas | 57.4% | Multi-step workflows using MCP. | p. 4 |
| FACTS Benchmark Suite | 61.9% | Factuality across grounding, parametric, search, and multimodal settings. | p. 4 |
| SimpleQA Verified | 68.7% | Parametric-knowledge benchmark. | p. 4 |
| MMMLU | 91.8% | Multilingual question answering. | p. 4 |
| Global PIQA | 92.8% | Commonsense reasoning across 100 languages and cultures. | p. 4 |
| MRCR v2 (8-needle) | 67.2% at 128K average; 22.1% at 1M pointwise | Long-context performance rows. | p. 4 |

## Safety findings
- Automated safety testing versus Gemini 2.5 Flash reports text-to-text safety down 3.1%, multilingual safety up 0.1% with a non-egregious label, image-to-text safety down 2.3%, tone up 3.8%, and unjustified refusals down 10.4%. (p. 5)
- Google summarizes the development results as better safety and tone than Gemini 2.5 Flash while keeping unjustified refusals low. (p. 5)
- Manual red teams found child-safety thresholds met, content safety similar or improved against Gemini 2.5 Flash, and no egregious concerns in broader probing. (p. 6)
- Frontier Safety conclusions are based on Gemini 3 Pro Preview, which did not reach critical capability levels in Google’s reported framework analysis. (p. 6)
- Because Google considers Gemini 3 Flash less capable than Gemini 3 Pro, the card relies on the Pro results to judge Flash unlikely to reach critical capability levels. (p. 6)

## Limitations and caveats
- Known limitations are not restated; the card directs readers to the Gemini 3 Pro model card. (p. 5)
- Acceptable-use, safety evaluation approach, and safety-policy details are also delegated to the Gemini 3 Pro card. (p. 5)
- The evaluation methodology is referred to an external page, and the short card mainly shows headline results. (p. 4)
- Training and development safety results are automated tests, not human evaluation or red teaming. (p. 5)
- Google cautions that refined safety evaluations make these results unsuitable for direct comparison with older Gemini model cards. (p. 6)
- Risk and mitigation details are deferred to Gemini 3 Pro rather than explained in this card. (p. 6)

## Practical implications for Copilot users
- GitHub retired Gemini 3 Flash on 2026-07-31; the remaining bullets are for historical comparison and for understanding the successor model's lineage.
- GitHub listed this model for app and IDE surfaces rather than the Copilot CLI, so CLI users should treat it as catalog history, not a past CLI option.
- Its benchmark chart is useful for understanding the first Flash baseline that later 3.5 and 3.6 Flash cards compare against.
- For old generated code or plans, rerun modern tests because many limitations and mitigations are only referenced through Gemini 3 Pro.
- The Pro-derived Frontier Safety rationale is not the same as a dedicated Flash dangerous-capability evaluation, so use it cautiously in comparisons.

## Document coverage
This digest uses pages 2-3 for model identity, modalities, training hardware/software, and dependencies; page 4 for the headline benchmark chart; page 5 for intended use and automated safety; and page 6 for red teaming, Frontier Safety, and risk references. The card is dedicated to Gemini 3 Flash, but distribution, architecture details, limitations, policies, and risk mitigations are largely pointed to Gemini 3 Pro. The external evaluation methodology page and Gemini 3 Pro Frontier Safety report are noted but not summarized beyond the text here.
