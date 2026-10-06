# Gemini 3.6 Flash

> Original digest of *Gemini 3.6 Flash — Model Card* (Google DeepMind, 2026-07; 7 pages). Page references are PDF
> page numbers. This summary paraphrases the publisher's document and is not a substitute for it;
> see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance
- Dedicated July 2026 Google DeepMind card for Gemini 3.6 Flash; GitHub retired the model on 2026-10-02.
- Google calls it a Gemini 3-series workhorse with better coding, knowledge-work, multimodal, and token-efficiency behavior than Gemini 3.5 Flash (p. 2).
- Inputs span text, image, audio, and video with a 1M-token context window; outputs are text up to 64K tokens (p. 2).
- The headline benchmark chart covers SWE-Bench Pro, DeepSWE, Terminal-bench, MLE-Bench, OSWorld, CharXiv, and GDM-MRCR v2 (p. 4).
- Safety testing shows better text and multilingual safety than Gemini 3.5 Flash, with a tone regression and low unjustified refusals in Google’s summary (p. 6).
- The Frontier Safety section says 3.6 Flash remains below the cyber critical capability level and is unlikely to reach critical levels assessed for Gemini 3.1 Pro (p. 7).

## Capabilities
- Google describes 3.6 Flash as a highly capable, natively multimodal reasoning model in the Gemini 3 series. (p. 2)
- The model is based on Gemini 3.5 Flash and is positioned as improving coding, knowledge work, multimodal performance, and token efficiency. (p. 2)
- The card lists text, image, audio, and video inputs, with a context window of up to 1M tokens. (p. 2)
- The output format is text with a 64K-token output limit. (p. 2)
- Google says the model fits agent workflows, video-heavy reasoning, coding assistance, and enterprise work patterns. (p. 5)
- Google lists Gemini App, Gemini Enterprise App, Gemini Enterprise Agent Platform, Google AI Studio, Gemini API, and Google Antigravity as distribution channels. (pp. 3-4)

## Evaluations
| Benchmark | Result | Context | Pages |
|---|---|---|---|
| SWE-Bench Pro (Public) | 58.7% | Diverse agentic coding tasks; higher than Gemini 3.5 Flash in the chart. | p. 4 |
| DeepSWE v1.1 | 49% | Long-horizon software engineering; below GPT-5.6 Luna in the row. | p. 4 |
| Terminal-bench 2.1 | 78.0% | Agentic terminal coding benchmark. | p. 4 |
| MLE-Bench | 63.9% | Machine-learning engineering; close to the strongest listed score. | p. 4 |
| GDPVal-AA v2 | 1421 Elo | Knowledge-work benchmark. | p. 4 |
| OSWorld-Verified | 83.0% | Computer-use benchmark; highest value shown in the row. | p. 4 |
| CharXiv Reasoning | 85.2% without tools; 89.4% with tools | Information synthesis from complex charts. | p. 4 |
| GDM-MRCR v2 (8-needle) | 91.8% at 128K average; 54.0% at 1M pointwise | Long-context performance rows. | p. 4 |

## Safety findings
- Automated safety results versus Gemini 3.5 Flash report text-to-text safety down 1.35 percentage points and multilingual safety down 5.45 points, where lower is better. (p. 6)
- Image-to-text safety is unchanged, tone is down 3.31 percentage points, and unjustified refusals are up 0.25 points in the automated table. (p. 6)
- Google says manual review of automated losses did not find egregious issues. (p. 6)
- Human red teaming reports child-safety launch thresholds met, content safety similar or improved versus Gemini 3.5 Flash, and no egregious concerns in broader probing. (p. 7)
- For Frontier Safety, the card relies on Gemini 3.1 Pro as the most capable assessed model and says 3.6 Flash is unlikely to reach critical capability levels. (p. 7)
- Additional cyber testing found Gemini 3.6 Flash below the cyber critical capability level. (p. 7)

## Limitations and caveats
- Hallucinations are explicitly named as a remaining foundation-model limitation. (p. 5)
- Google says jailbreak resistance is still being improved and Frontier Safety mitigations were strengthened. (p. 5)
- The card warns about occasional slow responses or timeouts. (p. 5)
- The knowledge cutoff is March 2026 overall, while some domains may only reflect January 2025 knowledge. (p. 5)
- Automated safety scores are development evaluations, not human evaluation or red-teaming results. (pp. 5-6)
- The evaluation methodology for capability benchmarks is mainly pointed to an external page rather than detailed in this short card. (p. 4)

## Practical implications for Copilot users
- GitHub retired Gemini 3.6 Flash on 2026-10-02; the remaining bullets are for historical comparison and for understanding the successor model's lineage.
- The card explains why 3.7 and 3.8 Flash inherit a fast multimodal, long-context design, so it remains useful background when comparing newer Flash models.
- For historical CLI work, its OSWorld and MRCR rows suggest it was suitable for UI and long-context tasks, but users should still reproduce results with currently available models.
- The cyber mitigation language supports keeping agent shells and network-sensitive tasks constrained even for fast models.
- Because safety results are relative to Gemini 3.5 Flash and not a full standalone FSF table, avoid treating this card as exhaustive dangerous-capability evidence.

## Document coverage
This digest uses pages 2-4 for model description, modalities, distribution, and the benchmark chart; pages 5-6 for limitations and automated safety; and page 7 for red teaming, Frontier Safety, and mitigations. The card is dedicated to Gemini 3.6 Flash, while architecture, data, acceptable-use, safety-policy, and deeper Frontier Safety details are delegated to earlier Gemini cards. External methodology and the Gemini 3.1 Pro model card are noted but not expanded beyond this document.
