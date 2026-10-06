# Kimi K2.7 Code

> Original digest of *Kimi K2.7 Code (Hugging Face model card)* (Moonshot AI; Hugging Face Markdown model card, no PDF exists). Citations use README section headings rather than page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and [model-card.md](model-card.md) for the full text.

## At a glance

- Kimi K2.7 Code is described as a coding-focused agentic model built on Kimi K2.6, with improved long-horizon software-engineering performance and about 30% lower thinking-token use than K2.6 (§ 1. Model Introduction).
- The model summary lists a Mixture-of-Experts architecture with 1T total parameters, 32B activated parameters, 61 layers, 384 experts, 8 selected experts per token, and a 256K context length (§ 2. Model Summary).
- The card reports a MoonViT vision encoder with 400M parameters and an image-text-to-text pipeline tag, plus examples for image and video inputs (§ 2. Model Summary; § 6. Model Usage).
- Evaluation results cover six coding and agentic benchmarks; Kimi K2.7 Code improves over Kimi K2.6 on every listed benchmark but trails GPT-5.5 or Claude Opus 4.8 on several rows (§ 3. Evaluation Results).
- Deployment guidance recommends vLLM, SGLang, or KTransformers, gives a `transformers` version range, and says deployment can reuse K2.5/K2.6 architecture assumptions (§ 5. Deployment).
- Usage guidance says thinking mode and preserve-thinking behavior are forced; instant mode is not supported, and video input is experimental outside the official API (§ 6. Model Usage).
- The Hugging Face card has little safety content: it does not report harmful-content, cyber, jailbreak, or other behavioral safety evaluations (§ 3. Evaluation Results).

## Capabilities

- Kimi K2.7 Code is presented as a coding-specialized model for real-world, long-horizon agentic software tasks, built on Kimi K2.6 (§ 1. Model Introduction).
- The architecture table lists 1T total parameters, 32B activated parameters, 61 layers, 384 experts, 8 selected experts per token, a 256K context, MLA attention, SwiGLU activation, and MoonViT vision support (§ 2. Model Summary).
- Benchmark coverage includes coding-agent tasks, program reconstruction, ML-systems tasks, persistent professional scenarios, MCP tool use, and verified MCP tasks (§ 3. Evaluation Results).
- The model supports official API chat examples with text, image, and video content, while third-party serving is framed around vLLM and SGLang with caveats (§ 6. Model Usage).
- Preserve-thinking behavior is enabled by default and cannot be disabled, which the card links to multi-turn coding-agent performance (§ 6. Model Usage).

## Evaluations

| Benchmark | Result | Context | Pages |
| --- | --- | --- | --- |
| Kimi Code Bench v2 | 62.0 | Coding benchmark; Kimi K2.6 is listed at 50.9, GPT-5.5 at 69.0, Claude Opus 4.8 at 67.4 | § 3. Evaluation Results |
| Program Bench | 53.6 | Code-generation-agent benchmark; K2.6 is listed at 48.3 | § 3. Evaluation Results |
| MLS Bench Lite | 35.1 | ML-systems subset; close to GPT-5.5's 35.5 and below Claude Opus 4.8's 42.8 | § 3. Evaluation Results |
| Kimi Claw 24/7 Bench | 46.9 | Persistent long-horizon professional tasks; averaged over three runs according to the footnote | § 3. Evaluation Results |
| MCP Atlas | 76.0 | MCP tool-use benchmark with a 100 tool-call limit and 32k max tokens per step | § 3. Evaluation Results |
| MCP Mark Verified | 81.1 | Human-verified MCP tool-use benchmark across multiple server environments | § 3. Evaluation Results |

## Safety findings

- The card does not include a dedicated safety section; its reported measurements are capability and agentic benchmarks rather than behavioral-safety evaluations (§ 3. Evaluation Results).
- Deployment guidance narrows supported serving paths to specific inference engines and a `transformers` version range, which helps operational reproducibility but is not a safety evaluation (§ 5. Deployment).
- Usage notes flag video input as experimental and supported only by the official API, and state that instant mode is unavailable (§ 6. Model Usage).
- The Modified MIT license governs the repository and weights, but the card does not describe acceptable-use rules or safety mitigations (§ 7. License).

## Limitations and caveats

- The card says Kimi K2.7 Code is built on Kimi K2.6, but it does not provide training data, training dates, or a full technical-report lineage for this specific checkpoint (§ 1. Model Introduction).
- Comparisons use different products and settings: Kimi models run through Kimi Code CLI with thinking mode, GPT-5.5 uses Codex xhigh, and Claude Opus 4.8 uses Claude Code xhigh (§ 3. Evaluation Results).
- Safety coverage is very thin; no harmful-content, cyber, jailbreak, or prompt-injection robustness scores are reported (§ 3. Evaluation Results).
- Third-party deployments have feature limits: video is experimental outside the official API, instant mode is unsupported, and preserve-thinking is forced (§ 6. Model Usage).
- The GitHub catalog marks this Copilot model retired on 2026-10-02, so the card is mainly useful for historical comparison (§ 1. Model Introduction).

## Practical implications for Copilot users

- GitHub retired the model on 2026-10-02; the remaining bullets are for historical comparison and for understanding the successor model's lineage.
- Use the README's benchmarks to understand why it was positioned for coding-agent workflows, not to infer broad chat or safety behavior.
- The 256K context and forced thinking behavior fit multi-step coding tasks, but generated changes still need tests, review, and careful tool permissions.
- Because the card lacks safety evaluations, do not treat Kimi K2.7 Code as vetted for harmful-content refusal, cyber misuse resistance, or prompt-injection robustness.
- The model card states that K2.7 Code is built on K2.6; do not import claims from older Kimi reports unless they are repeated in this README.
- For multimodal use, remember that video input was described as experimental and tied to the official API.

## Document coverage

This digest uses only the Hugging Face Markdown model card for Kimi K2.7 Code. It covers the introduction, architecture table, benchmark table and footnotes, deployment instructions, usage notes, and license section. It does not import facts from Kimi K2, K2.5, K2.6, or K3 reports beyond the README's statement that K2.7 Code is built on Kimi K2.6.
