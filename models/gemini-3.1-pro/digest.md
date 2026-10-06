# Gemini 3.1 Pro

> Original digest of *Gemini 3.1 Pro Model Card* (Google DeepMind, 2026-02; 9 pages). Page references are PDF
> page numbers. This summary paraphrases the publisher's document and is not a substitute for it;
> see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance
- Dedicated February 2026 card for Gemini 3.1 Pro; GitHub offered it in public preview and retired it on 2026-09-01.
- Google describes it as the most advanced Google model for complex tasks at publication time (p. 2).
- It can take text, audio, images, video, and whole code repositories, with a 1M-token context window and 64K-token text output (p. 2).
- The benchmark chart includes reasoning, coding, agentic tool use, browser/search, multimodal, multilingual, and long-context tasks (p. 4).
- Automated safety comparisons against Gemini 3.0 Pro show small text and multilingual regressions marked non-egregious, image-safety and refusal improvements, and nearly flat tone (p. 6).
- The Frontier Safety section reports no critical capability level reached across CBRN, cyber, harmful manipulation, ML R&D, or misalignment (pp. 7-9).

## Capabilities
- Gemini 3.1 Pro is presented as a natively multimodal reasoning model for complex tasks. (p. 2)
- The card says it can handle large multimodal sources, including audio, images, video, and entire code repositories. (p. 2)
- Inputs have a context window up to 1M tokens and outputs are text up to 64K tokens. (p. 2)
- The model is based on Gemini 3 Pro, with additional architecture details deferred to that card. (p. 2)
- Google lists agentic performance, advanced coding, long context, multimodal understanding, and algorithmic development as especially relevant uses. (p. 5)
- Distribution channels named include Gemini App, Google Cloud or Vertex AI, Google AI Studio, Gemini API, Google Antigravity, Gemini Enterprise, and NotebookLM. (p. 3)

## Evaluations
| Benchmark | Result | Context | Pages |
|---|---|---|---|
| Humanity's Last Exam | 44.4% without tools; 51.4% with search and code | Academic reasoning on full-set text and multimodal tasks. | p. 4 |
| ARC-AGI-2 | 77.1% | ARC Prize Verified abstract-reasoning puzzles. | p. 4 |
| GPQA Diamond | 94.3% | Scientific knowledge without tools. | p. 4 |
| Terminal-Bench 2.0 | 68.5% | Agentic terminal coding on the Terminus-2 harness. | p. 4 |
| SWE-Bench Verified | 80.6% | Single-attempt agentic coding benchmark. | p. 4 |
| SWE-Bench Pro (Public) | 54.2% | Single-attempt diverse agentic coding tasks. | p. 4 |
| LiveCodeBench Pro | 2887 Elo | Competitive coding problems from Codeforces, ICPC, and IOI. | p. 4 |
| SciCode | 59% | Scientific research coding benchmark. | p. 4 |
| APEX-Agents | 33.5% | Long-horizon professional tasks. | p. 4 |
| GDPval-AA | 1317 Elo | Expert-task benchmark. | p. 4 |
| t2-bench | 90.8% retail; 99.3% telecom | Agentic tool-use benchmark with two sectors reported. | p. 4 |
| MCP Atlas | 69.2% | Multi-step workflows using MCP. | p. 4 |
| BrowseComp | 85.9% | Agentic web search using search, Python, and browsing. | p. 4 |
| MMMU Pro | 80.5% | Multimodal understanding and reasoning without tools. | p. 4 |
| MMMLU | 92.6% | Multilingual question answering. | p. 4 |
| MRCR v2 (8-needle) | 84.9% at 128K average; 26.3% at 1M pointwise | Long-context performance rows. | p. 4 |

## Safety findings
- Automated safety results versus Gemini 3.0 Pro report text-to-text safety up 0.10% and multilingual safety up 0.11%, both labeled non-egregious, plus image-to-text safety down 0.33%. (p. 6)
- The same table reports tone up 0.02% and unjustified refusals down 0.08%. (p. 6)
- Human red teams found child-safety thresholds satisfied and content-safety performance broadly similar to Gemini 3.0 Pro. (p. 7)
- The Frontier Safety summary says the model remains below alert thresholds for CBRN, harmful manipulation, ML R&D, and misalignment, and below the cyber critical capability level after additional testing. (p. 7)
- In CBRN testing with Deep Think mode, Google says the model can give accurate and actionable information but not sufficiently novel or complete instructions for critical stages needed to meet the critical level. (p. 8)
- Cyber testing shows an increase over Gemini 3 Pro and reaches an alert threshold, but still falls short of Uplift Level 1 critical capability. (p. 8)
- Harmful-manipulation testing reports a maximum belief-change odds ratio of 3.6x versus a non-AI baseline but below the alert threshold. (p. 8)
- ML R&D testing reports a RE-Bench human-normalized average of 1.27 versus Gemini 3 Pro at 1.04, yet the average remains below alert level. (p. 9)
- Misalignment evaluations show almost 100% success on three situational-awareness challenges but inconsistent results elsewhere, so the alert threshold is not met. (p. 9)

## Limitations and caveats
- The card does not restate known limitations in detail and points to the Gemini 3 Pro model card. (p. 5)
- Acceptable-use, safety evaluation approach, safety-policy, and risk-mitigation details are mostly delegated to Gemini 3 Pro. (pp. 5-7)
- Capability benchmark methodology is referred to an external page rather than described fully in the model card. (p. 4)
- The development safety table is automated testing rather than human evaluation or red teaming. (p. 6)
- Google says safety results are consistent with the original Gemini 3.0 Pro safety assessment, limiting what can be inferred about novel safety behavior. (p. 6)
- Deep Think mode did not provide a cyber advantage over the standard model in the reported tests. (p. 8)

## Practical implications for Copilot users
- GitHub retired Gemini 3.1 Pro on 2026-09-01; the remaining bullets are for historical comparison and for understanding the successor model's lineage.
- The high coding and reasoning rows make it a useful baseline for understanding why later Flash cards compare themselves to 3.1 Pro on red teaming and Frontier Safety.
- For any historical output, treat the model as capable but not self-verifying: rerun tests, inspect code changes, and confirm long-context references.
- The cyber alert-threshold result supports strict review before using similar models for offensive-security, exploit, or autonomous terminal workflows.
- Because many limitations are delegated to Gemini 3 Pro, this card should not be read as a complete standalone safety manual.

## Document coverage
This digest draws on pages 2-5 for model identity, modalities, distribution, intended uses, and headline benchmarks; pages 6-7 for automated safety, human red teaming, and the Frontier Safety setup; and pages 8-9 for the domain-specific Frontier Safety table. The card is dedicated to Gemini 3.1 Pro, but repeatedly refers architecture, data, acceptable-use, limitations, and risk-mitigation detail to Gemini 3 Pro. It mentions external methodology and the Gemini 3 Pro Frontier Safety Framework Report but does not reproduce their contents.
