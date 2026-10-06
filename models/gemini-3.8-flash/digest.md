# Gemini 3.8 Flash

> Original digest of *Gemini 3.8 Flash — Model Card* (Google DeepMind, 2026-09; 8 pages). Page references are PDF
> page numbers. This summary paraphrases the publisher's document and is not a substitute for it;
> see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance
- Dedicated September 2026 Google DeepMind card for Gemini 3.8 Flash, a current GitHub Copilot model.
- The model is described as a Gemini 3.7 Flash successor aimed at software engineering and agentic knowledge workflows (p. 2).
- It accepts text, image, audio, and video inputs up to a 1M-token context window and produces text up to 64K tokens (p. 2).
- The public benchmark chart reports stronger DeepSWE, Terminal-bench, LVBench, OSWorld, BioMysteryBench, and LABBench2 results than Gemini 3.7 Flash (p. 5).
- Google reports broadly similar safety and tone to Gemini 3.7 Flash, with a non-English safety regression in automated testing (p. 7).
- Frontier Safety conclusions are inherited from Gemini 3.7 Flash because Google says 3.8 Flash does not add material capability in those domains (p. 8).

## Capabilities
- Google positions 3.8 Flash as an iteration on 3.7 Flash with improvements for software engineering and agentic knowledge workflows. (p. 2)
- The input interface covers text, images, audio, and video, and the context window is listed as up to 1M tokens. (p. 2)
- Text output can be as long as 64K tokens, supporting extended coding and analysis responses. (p. 2)
- The card says effort levels can be adjusted to trade response quality and latency for a task. (p. 2)
- Intended uses include production-ready agents, software engineering, agent tasks, and complex knowledge workflows. (p. 6)
- Distribution channels named in the card include the Gemini app, Google AI Studio, Gemini API, Google AI Mode, Google Antigravity, and the Gemini Enterprise Agent Platform. (pp. 3-4)

## Evaluations
| Benchmark | Result | Context | Pages |
|---|---|---|---|
| DeepSWE v1.1 | 73.7% | Long-horizon software engineering; chart also lists Gemini 3.7 Flash at 65.3%. | p. 5 |
| GDPVal-AA v2 | 1545 Elo | Knowledge-work benchmark; lower than Claude Opus 5 in the same chart. | p. 5 |
| Vals Finance Agent v2 | 61.4% | Financial analyst task benchmark; highest value shown in the row. | p. 5 |
| Harvey's Legal Agent Benchmark | 10.0% all-pass rate | Complex legal workflow benchmark; above the other listed models. | p. 5 |
| Terminal-bench 2.1 | 89.4% | Agentic terminal coding; slightly ahead of the listed GPT-5.6 variants. | p. 5 |
| Terminal-bench 4.0 | 19.1% | General agent capability benchmark; below Claude Opus 5 and GPT-5.6 Sol. | p. 5 |
| GDP.PDF | 35.0% all-pass rate | Expert PDF comprehension; below the GPT-5.6 Sol value shown. | p. 5 |
| CharXiv Reasoning | 86.2% | Information synthesis from complex charts without tools. | p. 5 |
| LVBench | 87.8% agentic; 87.1% static | Long-video understanding; both modes are reported in the model column. | p. 5 |
| HLE-Verified | 54.9% | Multidisciplinary expert reasoning; close to the GPT-5.6 Sol value. | p. 5 |
| OSWorld-2.0 | 59.0% | Agentic computer-use partial score with batch tool enabled. | p. 5 |
| BioMysteryBench | 88.8% human-solvable; 56.5% human-difficult | Bioinformatics research workflow benchmark with two difficulty slices. | p. 5 |
| LABBench2 | 86.2% | Biology real-world research tasks; above Gemini 3.7 Flash in the chart. | p. 5 |

## Safety findings
- Automated development evaluations compare 3.8 Flash with 3.7 Flash and report text-to-text safety down 0.4 percentage points, image-to-text unchanged, tone up 0.2 points, and unjustified refusals up 1.1 points. (p. 7)
- The multilingual safety metric moved 5.4 percentage points in the unfavorable direction relative to Gemini 3.7 Flash, while the card still summarizes overall safety and tone as similar. (p. 7)
- Google says manual review of automated safety losses did not identify egregious content problems. (p. 7)
- Specialist red teams found required child-safety thresholds satisfied, content safety similar or improved versus Gemini 3.7 Flash, and no egregious issues outside strict policy areas. (p. 8)
- For Frontier Safety, Google did not run a new full table in this card; it relies on 3.7 Flash results and says 3.8 Flash is unlikely to reach any tracked or critical capability level. (p. 8)

## Limitations and caveats
- The card warns that hallucinations remain a general foundation-model failure mode. (p. 6)
- Jailbreak resistance and Frontier Safety mitigations are described as areas of continuing work rather than finished guarantees. (p. 6)
- Users may see occasional slow responses or timeouts. (p. 6)
- Higher effort settings can consume more tokens to pursue better answers. (p. 6)
- The knowledge cutoff is March 2026 for the model overall, but Google says some domains may only be current to January 2025. (p. 6)
- Benchmark methodology is mostly delegated to an external evaluation-methodology page rather than reproduced in the card. (pp. 4-5)

## Practical implications for Copilot users
- Use 3.8 Flash when quick iteration and agentic coding performance matter, but still require review for patches, commands, and long generated plans.
- The strong terminal, DeepSWE, and OSWorld numbers make it a plausible default for lightweight CLI investigations; multi-step repository changes still need tests and human oversight.
- Because Frontier Safety conclusions are inherited from 3.7 Flash, do not treat this short card as a full new dangerous-capability assessment.
- The multilingual safety regression is a reason to be more conservative with non-English sensitive prompts and to check refusals or unsafe completions manually.
- The long context window is useful for large files and logs, but hallucination risk means users should ground requests in exact file paths and verify quoted details.

## Document coverage
This digest draws on pages 2-4 for model identity, modalities, dependencies, distribution, and the evaluation approach; page 5 for the headline benchmark chart; and pages 6-8 for limitations, safety, red teaming, and Frontier Safety. The card is dedicated to Gemini 3.8 Flash, but several architecture, data, policy, and Frontier Safety details are explicitly referred back to Gemini 3.7 Flash rather than restated here. The external evaluation-methodology page and the Gemini 3.7 Frontier Safety material are noted but not summarized beyond what this card says.
