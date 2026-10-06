# Gemini 2.5 Pro

> Original digest of *Gemini 2.5 Pro Model Card* (Google DeepMind, 2025-06-27; 21 pages). Page references are PDF
> page numbers. This summary paraphrases the publisher's document and is not a substitute for it;
> see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance
- Updated June 27, 2025 card for Gemini 2.5 Pro; GitHub retired the model on 2026-07-31 and did not list it for the CLI.
- The card covers Gemini 2.5 Pro GA while also retaining earlier Experimental (03-25) and Preview (05-06) results where relevant (p. 2).
- Gemini 2.5 Pro is described as a sparse mixture-of-experts multimodal reasoning model with text, audio, image, and video inputs (p. 2).
- The model has a 1M-token input context window and 64K-token text output limit (p. 2).
- Capability tables cover reasoning, science, coding, factuality, multimodal, video, long-context, and multilingual benchmarks (pp. 5-6).
- The safety sections report improved tone and instruction-following relative to Gemini 1.5 Pro 002, but note over-refusal and tone as ongoing safety limitations (pp. 9-10).
- Frontier Safety results say no Critical Capability Level was reached, while cyber uplift reached an alert threshold that led Google to increase testing and mitigations (pp. 10-21).

## Capabilities
- Gemini 2.5 Pro is presented as a multimodal reasoning model for complex tasks across text, audio, images, video, and code repositories. (p. 2)
- The architecture is described as sparse mixture-of-experts transformers with native multimodal support. (p. 2)
- The model supports a 1M-token context window and text outputs up to 64K tokens. (p. 2)
- Training data included public web documents, code in multiple programming languages, images, audio, video, instruction tuning data, preferences, and tool-use data. (p. 3)
- Data processing included deduplication, safety filtering, and quality filtering. (p. 3)
- The intended-use section emphasizes enhanced reasoning, advanced coding, multimodal understanding, and long-context applications. (p. 7)

## Evaluations
| Benchmark | Result | Context | Pages |
|---|---|---|---|
| Humanity's Last Exam | 21.6% for Gemini 2.5 Pro GA | Reasoning and knowledge benchmark; prior preview and experimental values are also listed. | p. 5 |
| GPQA diamond | 86.4% single-attempt pass@1 | Science benchmark for Gemini 2.5 Pro GA. | p. 5 |
| AIME 2025 | 88.0% single-attempt pass@1 | Mathematics benchmark; the chart also lists higher comparison-model values. | p. 5 |
| LiveCodeBench (Oct 2024-Feb 2025 window) | 75.6% for Preview 05-06; GA not reported | Code-generation row retained for the earlier preview version. | p. 5 |
| LiveCodeBench (Jan-May 2025 window) | 69.0% single attempt for GA | Code-generation row for the newer UI date range. | p. 5 |
| Aider Polyglot | 82.2% diff-fenced for GA | Code-editing benchmark; chart also shows prior Gemini 2.5 versions. | p. 5 |
| SWE-bench verified | 59.6% single attempt; 67.2% multiple attempts for GA | Agentic coding benchmark. | p. 5 |
| SimpleQA | 54.0% for GA | Factuality benchmark. | p. 5 |
| FACTS Grounding | 87.8% for GA | Grounded factuality benchmark. | p. 5 |
| MMMU | 82.0% single-attempt pass@1 for GA | Visual reasoning benchmark. | p. 5 |
| Vibe-Eval (Reka) | 67.2% for GA | Image-understanding benchmark. | p. 5 |
| VideoMME | 86.9% for GA | Video benchmark using audio, visuals, and subtitles. | p. 6 |
| VideoMMMU | 83.6% for GA | Video-understanding benchmark. | p. 6 |
| MRCR | Preview 05-06: 93.0% at 128K average and 82.9% at 1M pointwise; Experimental 03-25: 94.5% and 83.1% | Earlier long-context MRCR row; GA is not reported in that row. | p. 6 |
| MRCR v2 (8-needle) | 58.0% at 128K average; 16.4% at 1M pointwise for GA | Harder long-context benchmark version. | p. 6 |
| Global MMLU (Lite) | 89.2% for GA | Multilingual performance benchmark. | p. 6 |

## Safety findings
- The safety approach included development evaluations, human and automated red teaming, assurance evaluations, governance review, and Frontier Safety Framework testing. (pp. 7-8)
- For Gemini 2.5 Pro GA versus Gemini 1.5 Pro 002, the automated table reports text-to-text safety down 0.9%, multilingual safety down 3.5%, image-to-text safety up 1.8% with a non-egregious label, tone up 18.4%, and instruction following up 14.8%. (p. 9)
- Assurance evaluations found low safety-policy violation rates across modalities for the experimental, preview, and GA versions. (pp. 9-10)
- No Frontier Safety critical capability level is reported as reached for Gemini 2.5 Pro GA in the summary table. (pp. 11-12)
- CBRN evaluation says the model can provide detailed technical knowledge but does not consistently or completely move through key bottleneck stages needed for the Uplift Level 1 critical level. (pp. 12-13)
- Cyber key-skills results for GA are 7/8 easy, 10/28 medium, and 1/12 hard, and the card says the model remains below both cyber critical capability levels. (pp. 11, 14, 15)
- Cyber uplift reached an alert threshold, prompting Google to accelerate mitigations and increase testing frequency. (pp. 10, 11, 14, 21)
- ML R&D testing says the best GA RE-Bench agent solutions achieve between 50% and 125% of strong human-written reference solutions, while the alert threshold is still not reached. (pp. 11, 17, 19)
- Deceptive-alignment evaluations for GA were not completed when the card was updated; earlier experimental results make Google judge it unlikely that GA reached either instrumental-reasoning critical level. (pp. 20-21)
- Correctness checks on RE-Bench, cyber, and alignment-style environments found no errors that Google believed invalidated the benchmark results. (p. 21)

## Limitations and caveats
- The card names hallucinations as a general limitation. (p. 7)
- It also lists limitations around causal understanding, complex logical deduction, and counterfactual reasoning. (p. 7)
- The knowledge cutoff is January 2025. (p. 7)
- The main safety limitations identified are over-refusals and tone, including answers that can still sound preachy. (p. 10)
- Capability comparisons include methodological caveats about provider-reported numbers, thinking versus non-thinking variants, single versus multiple attempts, and leaderboard sources. (p. 4)
- For MRCR v2, Google says the methodology changed from prior reports by focusing on a harder eight-needle version. (p. 4)
- Deceptive-alignment testing for the GA model was not yet complete in the updated card. (pp. 20-21)
- RE-Bench is described as only a subset of the skills required for the full AI R&D pipeline. (pp. 17-18)

## Practical implications for Copilot users
- GitHub retired Gemini 2.5 Pro on 2026-07-31; the remaining bullets are for historical comparison and for understanding the successor model's lineage.
- GitHub did not list this model for the Copilot CLI, so CLI users should treat it as predecessor context for later Gemini models rather than a direct CLI option.
- The GA capability table remains useful for comparing later model-card claims in coding, factuality, multimodal, and long-context tasks.
- For historical outputs, revalidate code and factual statements because the card explicitly lists hallucination, reasoning, and recency limits.
- The cyber alert-threshold finding supports strict sandboxing, approval gates, and audit logs for agentic security tasks with successor models.
- Because GA deceptive-alignment testing was incomplete, avoid using this card alone to conclude that later models have covered all situational-awareness or stealth risks.

## Document coverage
This digest uses pages 2-3 for model architecture, modalities, data, and processing; pages 4-6 for capability methodology and benchmark tables; pages 7-10 for intended use, general limitations, safety policy, and automated or assurance evaluations; and pages 10-21 for Frontier Safety details. The document covers Gemini 2.5 Pro GA while retaining preview and experimental data; evaluation rows in this digest identify when the GA number is absent and an earlier version is the one reported. The Gemini 2.5 technical report, external methodology sources, and cited research are mentioned only to the extent summarized in the card.
