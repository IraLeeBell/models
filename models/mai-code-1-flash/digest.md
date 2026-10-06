# MAI-Code-1-Flash

> Original digest of *MAI-Code-1-Flash model card* (Microsoft, 2026-06-02; 6 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance

- MAI-Code-1-Flash is Microsoft's dedicated card for a text-only coding model released on June 2, 2026, with a 256K-token context window (p. 1).
- The model summary lists a transformer with sparse Mixture-of-Experts layers, 137B total parameters, and 5B active parameters (p. 1).
- Microsoft frames the model around fast developer assistance, including agentic coding, repository Q&A, refactoring, and tool-using workflows in Copilot (pp. 1-2).
- Training ran from March to May 2026, with a December 2025 pretraining cut-off and English listed as the supported language (pp. 1, 3).
- The training section says the pipeline includes pretraining, midtraining, supervised tuning, a synthetic agentic phase of about 2 million tasks, and reinforcement learning over more than 150,000 environments (p. 3).
- At launch, distribution language limited availability to GitHub Copilot in Visual Studio Code, with Copilot CLI described as a later rollout (pp. 2, 4).
- Safety coverage is qualitative: filtering, alignment during tuning/RL, named cyber and secure-coding benchmarks, and release checks are described, but no safety score table is provided (p. 4).

## Capabilities

- The model is a text-to-text coding system with a 256K-token context window and sparse-MoE transformer architecture (p. 1).
- Microsoft lists agentic coding, adaptive response length, instruction following across single and multi-turn settings, and math/science/visual-coding reasoning as core capabilities (p. 2).
- Intended Copilot use cases include code generation, completion, repository questions, refactoring, telemetry-grounded tasks, and agentic tool use (p. 2).
- Offline evaluation and validation use the same production GitHub Copilot harness that serves users, including software-engineering, repository Q&A, refactoring, and real-usage-derived tasks (p. 3).
- The card reports both coding-agent benchmarks and more general reasoning, instruction-following, and tool-use benchmarks (pp. 5-6).

## Evaluations

| Benchmark | Result | Context | Pages |
| --- | --- | --- | --- |
| SWE-Bench Verified | 71.6% pass rate; 10.8K average tokens | Production VS Code-based harness; Claude Haiku 4.5 listed at 66.6% | p. 5 |
| SWE-Bench Pro | 51.2% pass rate; 28.0K average tokens | Diverse agentic coding comparison with Claude Haiku 4.5 | p. 5 |
| SWE-Bench Multilingual | 65.5% pass rate; 15.3K average tokens | Multilingual coding benchmark; Claude Haiku 4.5 listed at 62.7% | p. 5 |
| Terminal Bench 2 | 54.8% pass rate; 21.6K average tokens | Agentic terminal coding; Claude Haiku 4.5 listed at 41.6% | p. 5 |
| AIME 2026 | 92.5% accuracy; 23.6K average tokens | Competitive math comparison against Claude Haiku 4.5 | p. 5 |
| AMO Bench | 40.0% accuracy; 56.0K average tokens | Olympiad math comparison | p. 5 |
| GPQA Diamond | 84.6% accuracy; 9.6K average tokens | Biology, chemistry, and physics questions | p. 5 |
| Frontier Science | 58.2% accuracy; 20.5K average tokens | Scientific reasoning comparison | p. 5 |
| IF Bench | 75.0 average | Precise instruction following | p. 5 |
| Advanced IF | 71.4 average | Rubric-based instruction following | pp. 5-6 |
| Robust IF Bench | 61.2 average | Internal diverse hard instruction-following set | p. 6 |
| τ²-Bench | 71.7 on telecom | Agentic tool-use benchmark | p. 6 |

## Safety findings

- Pretraining includes filtering or demotion of harmful content in the data mixture (p. 4).
- Later training stages use alignment techniques during supervised tuning and reinforcement learning to promote safer responses (p. 4).
- Microsoft names CyberBench, CyberSecEval, and SecRepo as the cyber and secure-coding evaluation sources (p. 4).
- The release process additionally used production model APIs with safety classifiers and filters (p. 4).
- Commercial use is subject to applicable Copilot terms and Microsoft's acceptable-use rules for harmful or unlawful content (pp. 4-5).

## Limitations and caveats

- GitHub retired this model on 2026-09-10; the digest therefore describes historical behavior rather than current selection guidance.
- The card lists text as the only input modality, so image-grounded tasks are outside the model summary's stated interface (p. 1).
- Launch distribution was limited to Visual Studio Code, and the card describes CLI support as planned rather than available at release (pp. 2, 4).
- The known-limitations section warns that generated text and code can be wrong, incomplete, or unsuitable without review and testing (p. 4).
- Safety evaluation details are high level: the document names security benchmarks and release checks but does not publish pass rates or failure categories (p. 4).
- The benchmark comparisons mainly use Claude Haiku 4.5 as the named comparator, so they do not characterize the full frontier model set (pp. 5-6).

## Practical implications for Copilot users

- GitHub retired the model on 2026-09-10; the remaining bullets are for historical comparison and for understanding the successor model's lineage.
- Treat this card as the baseline for MAI-Code-1.1-Flash: the later model keeps the same broad coding focus but adds image input and updated benchmark results.
- For historical evaluations, its strongest reported areas were SWE-style coding, instruction following, and tool-use tasks, but local repository tests remain decisive.
- Because the card describes text input only, do not infer screenshot or image-to-code behavior from this model's results.
- The safety section supports cautious use rather than blind trust: review generated diffs, run tests, and apply normal secure-development checks.
- The launch notes were VS Code-specific, so old availability statements should not be used to infer current Copilot client behavior.

## Document coverage

This digest covers the complete six-page Microsoft card, including the model summary, capability description, training disclosure, safety section, distribution notes, and evaluation tables. It omits administrative contact details and does not reproduce personal names or postal addresses. The card is dedicated to MAI-Code-1-Flash; later MAI-Code-1.1-Flash behavior should be evaluated from its own card.
