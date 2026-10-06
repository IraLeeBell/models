# Gemini 3.5 Flash

> Original digest of *Gemini 3.5 Flash Model Card* (Google DeepMind, 2026-05; 7 pages). Page references are PDF
> page numbers. This summary paraphrases the publisher's document and is not a substitute for it;
> see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance
- Dedicated May 2026 card for Gemini 3.5 Flash; GitHub retired the model on 2026-10-02.
- The model is described as a Gemini 3 Flash successor using thinking levels to tune answer quality and latency (p. 2).
- It supports text, image, audio, and video inputs with a 1M-token context window and text output up to 64K tokens (p. 2).
- The evaluation chart reports headline coding, agentic, UI-control, expert-task, multimodal, long-context, and reasoning results (p. 4).
- Automated safety rows improve on Gemini 3 Flash for text and multilingual safety and tone, while unjustified refusals rise slightly but are described as non-egregious (p. 6).
- The Frontier Safety discussion relies on Gemini 3.1 Pro and adds that 3.5 Flash stayed below the cyber critical capability level (p. 7).

## Capabilities
- Gemini 3.5 Flash is framed as a natively multimodal reasoning model in the Gemini 3 series. (p. 2)
- The model builds on Gemini 3 Flash and adds thinking levels for task-dependent behavior. (p. 2)
- The card lists text, images, audio, and video as input types, with context up to 1M tokens. (p. 2)
- Outputs are text and can reach 64K tokens. (p. 2)
- Distribution channels include Gemini App, Gemini Enterprise App, Gemini Enterprise Agent Platform, Google AI Studio, Gemini API, Google Search AI Mode, and Google Antigravity. (p. 3)
- Google names agentic workflows, coding tasks, and multi-week enterprise processes as intended use cases. (p. 5)

## Evaluations
| Benchmark | Result | Context | Pages |
|---|---|---|---|
| Terminal-bench 2.1 | 76.2% | Agentic terminal coding on the Terminus-2 harness. | p. 4 |
| SWE-Bench Pro (Public) | 53.9% | Single-attempt diverse agentic coding tasks. | p. 4 |
| MCP Atlas | 83.6% | Multi-step workflows using MCP; highest row value shown. | p. 4 |
| Toolathlon | 56.5% | Real-world general tool-use benchmark. | p. 4 |
| OSWorld-Verified | 78.4% | Agentic computer-use benchmark. | p. 4 |
| Finance Agent v2 | 57.9% | Financial analysis and decision-making tasks. | p. 4 |
| GDPval-AA | 1656 Elo | Economically valuable knowledge-work benchmark. | p. 4 |
| CharXiv Reasoning | 84.2% | Information synthesis from complex charts without tools. | p. 4 |
| MMMU-Pro | 83.6% | Multimodal understanding and reasoning without tools. | p. 4 |
| Blueprint-Bench 2 | 33.6% | Agentic spatial reasoning normalized score. | p. 4 |
| MRCR v2 (8-needle) | 77.3% at 128K average; 26.6% at 1M pointwise | Long-context performance rows. | p. 4 |
| Humanity's Last Exam | 40.2% | Academic reasoning across full-set text and multimodal tasks. | p. 4 |
| ARC-AGI-2 | 72.1% | Abstract reasoning puzzles. | p. 4 |

## Safety findings
- Automated safety testing versus Gemini 3 Flash reports text-to-text safety down 3.9%, multilingual safety down 2.6%, image-to-text safety unchanged, tone up 8.9%, and unjustified refusals up 0.8% with a non-egregious note. (p. 6)
- Google characterizes the development results as better safety and tone than Gemini 3 Flash while maintaining low unjustified refusals. (p. 6)
- Manual red teams found child-safety launch thresholds met, similar or improved content safety versus Gemini 3 Flash, and no egregious concerns in broader probing. (p. 6)
- For Frontier Safety, Google relies on Gemini 3.1 Pro results and says Gemini 3.5 Flash is also unlikely to reach critical capability levels. (p. 7)
- Extra cyber testing found Gemini 3.5 Flash below the cyber critical capability level. (p. 7)

## Limitations and caveats
- Known limitations are not restated in detail; the card points readers to the Gemini 3 Flash model card. (p. 5)
- Acceptable-use, safety evaluation approach, and safety policy details are also delegated to the Gemini 3 Flash card. (p. 5)
- Capability-benchmark methodology is referred to an external methodology page rather than explained in this short card. (p. 4)
- The safety table is automated development testing rather than human evaluation or red-teaming. (p. 6)
- Google cautions that its refined automated safety evaluations make these safety results unsuitable for direct comparison with older Gemini model-card numbers. (p. 6)
- Risk and mitigation details are mostly deferred to the Gemini 3.1 Pro model card. (p. 7)

## Practical implications for Copilot users
- GitHub retired Gemini 3.5 Flash on 2026-10-02; the remaining bullets are for historical comparison and for understanding the successor model's lineage.
- Its benchmark mix helps explain why later Flash models emphasized terminal coding, MCP-style workflows, and long-context use.
- For old outputs produced by this model, re-check factual claims and code because this short card does not restate the detailed limitations it inherits from Gemini 3 Flash.
- The mild unjustified-refusal increase means historical comparisons should separate safety improvements from potential answer-availability changes.
- The cyber testing note reinforces that agent tool access should remain constrained even when a model is positioned as a faster Flash variant.

## Document coverage
This digest uses pages 2-3 for model identity, modalities, and distribution; page 4 for the benchmark chart; page 5 for intended use and delegated limitations; and pages 6-7 for safety, red teaming, Frontier Safety, and risk references. The card is dedicated to Gemini 3.5 Flash, but it sends readers to Gemini 3 Flash and Gemini 3.1 Pro for many underlying details. The external evaluation methodology page is mentioned but not summarized beyond the card.
