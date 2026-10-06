# MAI-Code-1.1-Flash

> Original digest of *MAI-Code-1.1-Flash model card* (Microsoft, 2026-08-11; 6 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance

- MAI-Code-1.1-Flash is a dedicated Microsoft coding-model card for a transformer sparse-MoE model with 138B total parameters, 5B active parameters, text and image inputs, text output, and a 256K-token context window (p. 1).
- The card gives an August 11, 2026 release date, March-August 2026 training dates, English language support, and a December 2025 pretraining cut-off (pp. 1, 3).
- Microsoft positions the model for agentic coding, repository Q&A, refactoring, and tool-using developer work in GitHub Copilot (p. 2).
- The training disclosure says it starts from a compressed MAI-Thinking-1 checkpoint, adds supervised tuning, a two-stage synthetic agentic phase with about 2 million tasks, and reinforcement learning across more than 150,000 environments (p. 3).
- The benchmark table reports 72.6% on SWE-Bench Verified and 62.9% on Terminal Bench 2.1, with lower average token use than several listed comparison models on SWE-Bench Verified (p. 5).
- Vision-oriented coding evaluations include 74.1% on internal Text2WebApp, 42.1% on ScreenShot2WebApp, and 11.5% on Vision2Web Level3 (p. 5).
- Safety coverage consists of training-time filtering/alignment, cybersecurity and secure-coding evaluations, and release checks with classifiers and filters; the card does not publish numeric safety scores (p. 4).

## Capabilities

- The model accepts text prompts and images and returns text, with the card listing a 256K-token context length for repository-scale interactions (p. 1).
- Its architecture is a transformer using sparse Mixture-of-Experts layers; the model summary lists 138B total parameters with 5B active for each token (p. 1).
- Microsoft describes agentic coding in real developer environments, concise-to-expanded answer length control, single- and multi-turn instruction following, and reasoning over math, science, and visual coding tasks (p. 2).
- The intended Copilot scenarios include code generation, code completion, repository questions, refactoring, telemetry-informed coding tasks, and tool use (p. 2).
- Training and validation are tied to the production GitHub Copilot harness, with internal tests built from software-engineering, repository Q&A, refactoring, and real-usage-derived tasks (p. 4).
- Compared with MAI-Code-1-Flash, the 1.1 card adds image-input capability and reports web-app and vision-to-code evaluations rather than a broad general-reasoning table (pp. 1, 5).

## Evaluations

| Benchmark | Result | Context | Pages |
| --- | --- | --- | --- |
| SWE-Bench Verified | 72.6% pass rate; 8.6K average tokens | Same VS Code-based production harness; compared with MAI-Code-1-Flash, Haiku 4.5, and GPT 5.4 mini | p. 5 |
| Terminal Bench 2.1 | 62.9% pass rate; 17.0K average tokens | Same harness comparison; MAI-Code-1-Flash is listed at 51.7% | p. 5 |
| Text2WebApp | 74.1% pass rate; 17.1K average tokens | Internal WebApp development evaluation against Haiku 4.5 and GPT 5.4 mini | p. 5 |
| ScreenShot2WebApp | 42.1% pass rate; 10.5K average tokens | Internal image-to-web-app task, using screenshot input | p. 5 |
| Vision2Web Level3 | 11.5% pass rate; 15.1K average tokens | Vision-to-web benchmark where the card reports Haiku 4.5 at 13.7% and GPT 5.4 mini at 10.1% | p. 5 |

## Safety findings

- Microsoft says harmful content is filtered out or down-ranked during pretraining to reduce base-model exposure (p. 4).
- Later training stages, including supervised tuning and reinforcement learning, are described as alignment points for encouraging helpful behavior and discouraging unsafe outputs (p. 4).
- The card names CyberBench, CyberSecEval, and SecRepo as security-oriented tests used to assess cyber robustness, vulnerability introduction, and secure-coding alignment (p. 4).
- A separate release process used production model APIs with safety classifiers and filters before deployment (p. 4).
- Use is bounded by GitHub and Microsoft acceptable-use terms that restrict harmful or unlawful content, but the model card does not enumerate category-level pass rates (pp. 2, 5).

## Limitations and caveats

- The card warns against treating generated code or explanations as authoritative; human review and project tests remain necessary before consequential use (p. 4).
- Safety evaluations are described by benchmark family and release process, but the card provides no quantitative cyber, secure-coding, jailbreak, or harmful-content results (p. 4).
- For broader general benchmarks, the 1.1 card points readers back to the MAI-Code-1-Flash card rather than reproducing those results for this checkpoint (p. 5).
- Client-availability wording is not perfectly uniform: one use-case section still focuses on Visual Studio Code with CLI rollout later, while the distribution section says the model is available for all Copilot clients (pp. 2, 4).
- The supported-language field lists English only, so the card does not establish performance for multilingual developer interactions (p. 3).

## Practical implications for Copilot users

- The card makes MAI-Code-1.1-Flash look best suited to everyday coding-agent work where repository context, tool use, and short feedback loops matter.
- Use the image input path for UI or screenshot-grounded coding only with verification, because the reported vision-to-code scores are useful but uneven.
- Treat the security evaluation as evidence of release diligence, not as a guarantee that generated patches are vulnerability-free.
- Keep agent permissions narrow, run tests, and inspect diffs, especially when prompts or repository content may contain instructions from untrusted files.
- If comparing it with MAI-Code-1-Flash, expect the clearest reported gains on Terminal Bench 2.1 and image/web-app tasks, not a full replacement for application-specific validation.
- Check current Copilot product documentation for client availability because the card mixes a VS Code-focused use-case passage with broader distribution wording.

## Document coverage

This digest uses the six-page Microsoft model card, emphasizing the model summary, training disclosure, responsible-AI section, and benchmark tables. It omits the administrative publisher table details and does not reproduce personal names or postal addresses. The document is dedicated to MAI-Code-1.1-Flash; references to MAI-Code-1-Flash are used only as the publisher's comparison baseline.
