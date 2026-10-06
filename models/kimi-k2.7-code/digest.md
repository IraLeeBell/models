# Kimi K2.7 Code

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write kimi-k2.7-code`. -->

> Original digest of *Kimi K2.7 Code (Hugging Face model card)* (Moonshot AI, undated; Markdown model card, no PDF). Citations use the card's section headings. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and [model-card.md](model-card.md) for the full text.

**Copilot status:** Retired from GitHub Copilot on 2026-10-02. This digest is kept for historical comparison and model lineage.

## At a glance

Kimi K2.7 Code is a retired Moonshot AI coding-agent model carded as built on Kimi K2.6. The card lists a 1T-parameter MoE with 32B active parameters, 256K context, forced thinking, preserve-thinking, image/video input examples, and six coding or agentic benchmark rows. It gives almost no behavioral-safety evidence, so its main value is historical comparison and lineage.

- **Choose it for:** Historical comparison of the Kimi coding-agent lineage and the K2.6-to-K2.7 Code benchmark step.
- **Watch out for:** Retired in GitHub's catalog and missing safety, release-date, training-data, and prompt-injection results.
- The card says Kimi K2.7 Code is a coding-focused agentic model built on Kimi K2.6 and uses about 30% fewer thinking tokens than K2.6. (§ 1. Model Introduction)
- The summary table lists a MoE architecture with 1T total parameters, 32B active parameters, 384 experts, 8 selected experts per token, MoonViT vision, and 256K context. (§ 2. Model Summary)
- It improves over Kimi K2.6 on all six listed rows, including 62.0 on Kimi Code Bench v2, 53.6 on Program Bench, 76.0 on MCP Atlas, and 81.1 on MCPMark Verified. (§ 3. Evaluation Results)
- The card says thinking and preserve-thinking are forced, instant mode is unsupported, and video input is experimental outside the official API. (§ 6. Model Usage)
- No dedicated safety section or safety benchmark table appears; the reported measurements are coding and agentic capability rows. (§ 3. Evaluation Results)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The model card is undated and does not state a release date. | — |
| Knowledge cutoff | Not stated. The model card does not state a knowledge cutoff. | — |
| Context window | 262,144 tokens (stated as 262,144-token context length). The architecture table says 256K; the evaluation footnote spells out 262,144 tokens. | § 3. Evaluation Results |
| Maximum output | Not stated. Examples set max_tokens to 4096 or 8192, but the card does not state a model maximum. | — |
| Input modalities | Text, Image, Video (stated as K2.7-Code supports Image and Video input) | § Chat Completion with visual content |
| Output modalities | Text. Examples print reasoning content and response text; no non-text output modality is stated. | § Chat Completion |
| Reasoning controls | Always reasons, Extended thinking (stated as forces thinking and preserve_thinking as True) | § 6. Model Usage |
| Effort levels | Not stated. The card names thinking mode but does not list selectable effort levels for Kimi K2.7 Code. | — |
| Tool use | Function calling, MCP. The card points to interleaved thinking with multi-step tool calls and reports MCP tool-use benchmarks. | § Interleaved Thinking and Multi-Step Tool Call |
| Open weights | Yes (stated as model weights are released under the Modified MIT License) | § 7. License |
| Architecture | Mixture of experts (stated as Mixture-of-Experts (MoE)) | § 2. Model Summary |
| Total parameters | 1 trillion (stated as 1T) | § 2. Model Summary |
| Active parameters | 32 billion (stated as 32B) | § 2. Model Summary |

### Capability notes

- Kimi K2.7 Code is described as a coding-focused agentic model built on Kimi K2.6 for complex long-horizon software workflows. (§ 1. Model Introduction)
- The architecture table lists MoE, MLA attention, SwiGLU activation, one dense layer, 61 total layers, 384 experts, and one shared expert. (§ 2. Model Summary)
- The card reports MoonViT with 400M parameters and a Hugging Face image-text-to-text pipeline tag, with examples for image and video calls. (§ 2. Model Summary)
- Official examples run in thinking mode, show reasoning content separately from the final response, and set recommended temperature and top-p for thinking mode. (§ 6. Model Usage)
- Preserve-thinking is enabled by default, cannot be disabled, and is presented as useful for multi-turn coding-agent scenarios. (§ Preserve Thinking)
- The card says it works best with Kimi Code CLI as its coding-agent framework. (§ Coding Agent Framework)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Kimi Code Bench v2 | — | score | 62.0% | Kimi Code CLI; thinking mode; temperature 1.0; top-p 0.95; 262,144-token context | Kimi K2.6 50.9% (thinking); GPT-5.5 69.0% (Codex xhigh); Claude Opus 4.8 67.4% (Claude Code xhigh) | § 3. Evaluation Results |
| ProgramBench | — | success rate | 53.6% | Kimi Code CLI; thinking mode; 200 tasks; no source, decompilation, or internet; behavioral tests | Kimi K2.6 48.3% (thinking); GPT-5.5 69.1% (Codex xhigh); Claude Opus 4.8 63.8% (Claude Code xhigh) | § 3. Evaluation Results |
| Kimi Claw 24/7 Bench | — | score | 46.9% | OpenClaw; thinking mode; 17 professional scenarios; 610 evaluation points; averaged over 3 runs | Kimi K2.6 42.9% (thinking); GPT-5.5 52.8% (Codex xhigh); Claude Opus 4.8 50.4% (Claude Code xhigh) | § 3. Evaluation Results |
| MCP Atlas | — | success rate | 76.0% | Kimi Code CLI; thinking mode; official configuration; 100 tool-call limit; 32k max tokens per step; averaged over 3 runs | Kimi K2.6 69.4% (thinking); GPT-5.5 79.4% (Codex xhigh); Claude Opus 4.8 81.3% (Claude Code xhigh) | § 3. Evaluation Results |
| MCPMark Verified | — | score | 81.1% | Kimi Code CLI; thinking mode; five server environments; 100-step tool-call limit; 32k max tokens per step; averaged over 3 runs | Kimi K2.6 72.8% (thinking); GPT-5.5 92.9% (Codex xhigh); Claude Opus 4.8 76.4% (Claude Code xhigh) | § 3. Evaluation Results |

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| MLS Bench Lite | — | score | 35.1% | Kimi Code CLI; thinking mode; 30-task MLS-Bench subset; 5 hours before submission | Kimi K2.6 26.7% (thinking); GPT-5.5 35.5% (Codex xhigh); Claude Opus 4.8 42.8% (Claude Code max) | § 3. Evaluation Results |

## Safety findings

### Safety classification

- **Framework:** No safety framework stated
- **Overall determination:** Not stated

The Hugging Face model card does not state a safety framework or overall safety classification. It provides capability benchmarks, deployment notes, usage examples, and license information, but no formal risk level or safety-threshold determination.

The document states no per-domain determinations.

### Agentic-coding risks

- **Reward hacking** (not reported): The card reports capability benchmarks and footnotes, but no reward-hacking or grader-gaming evaluation.
- **Test tampering** (not reported): The card does not evaluate editing or weakening tests.
- **Destructive or overeager actions** (not reported): The card does not report destructive or over-eager action testing.
- **Sabotage** (not reported): The card does not report sabotage, monitor evasion, or oversight-evasion tests.
- **Prompt injection** (not reported): The card includes MCP tool-use benchmarks but no prompt-injection or instruction-hierarchy evaluation.
- **Honesty** (not reported): The card does not report honesty, deception, hallucinated success, or calibration results.
- **Sycophancy** (not reported): The card does not report sycophancy testing.

### Other safety findings

- The card has no dedicated safety-evaluation section; all reported benchmark rows are capability results for coding or agentic work. (§ 3. Evaluation Results)
- Deployment guidance lists recommended inference engines and says Kimi-K2.7-Code has the same architecture as Kimi-K2.5 and Kimi-K2.6, but this is operational guidance rather than safety evidence. (§ 5. Deployment)
- Usage notes make video experimental outside the official API, force thinking and preserve-thinking, and say instant mode is unsupported. (§ 6. Model Usage)
- The license section states that both the repository code and model weights are under the Modified MIT License; it does not add a safety policy. (§ 7. License)

## Limitations and caveats

- The card says Kimi K2.7 Code is built on Kimi K2.6, but does not provide training data, training dates, knowledge cutoff, or a full technical report for this checkpoint. (§ 1. Model Introduction)
- Comparisons mix Kimi Code CLI thinking mode, Codex xhigh for GPT-5.5, and Claude Code xhigh or max for Claude Opus 4.8. (§ 3. Evaluation Results)
- No harmful-content, cyber, jailbreak, prompt-injection, honesty, or sycophancy scores are reported. (§ 3. Evaluation Results)
- Third-party serving has feature limits: video is experimental outside the official API, preserve-thinking is forced, and instant mode is unavailable. (§ 6. Model Usage)
- The card gives examples with 4096 and 8192 max_tokens settings but does not state the model's maximum output limit. (§ 6. Model Usage)

## Practical implications for Copilot users

### Choose it for

- **Historical comparison:** The model is retired in GitHub's catalog, and the card is most useful for comparing the Kimi K2.6 to K2.7 Code coding-agent step. (§ 1. Model Introduction)
- **Agentic coding:** All six listed rows are coding or agentic benchmarks, and Kimi K2.7 Code improves over Kimi K2.6 on every row. (§ 3. Evaluation Results)
- **Long-horizon autonomy:** The introduction and Kimi Claw 24/7 Bench position it for persistent, multi-day agentic workflows, though only as historical guidance now. (§ 1. Model Introduction)

### Avoid it for

- **Untrusted input:** MCP and multi-step tool use are reported, but no prompt-injection robustness result is provided. (§ 3. Evaluation Results)
- **High-stakes domains:** The card lacks harmful-content, cyber-safety, medical, legal, or broader behavioral-safety measurements. (§ 3. Evaluation Results)
- **Low latency:** The card forces thinking and preserve-thinking and explicitly says instant mode is not supported. (§ 6. Model Usage)

### Guidance

- GitHub retired Kimi K2.7 Code from Copilot on 2026-10-02; the guidance below serves historical comparison and the lineage of later models.
- Because GitHub retired the model, use this digest for historical comparison and lineage rather than new Copilot selection.
- Do not transfer safety claims from other Kimi reports; this card does not report broad behavioral safety results.
- The forced thinking behavior and 256K context explain its coding-agent positioning, but generated code still needs tests and review.
- Treat MCP and tool-call workflows as prompt-injection exposed because the card provides no robustness result.
- For multimodal history, distinguish image support from experimental video support outside the official API.

## Document coverage

The owner document is the Hugging Face Markdown model card for the retired Kimi K2.7 Code checkpoint. Citations use section headings rather than pages. The digest does not import Kimi K2, K2.5, K2.6, or K3 technical-report facts except where this card itself states lineage, architecture reuse, or benchmark conditions.

- **Card type:** Dedicated. The document is about this model; it may include short sibling sections.
- **Pages specific to this model:** the whole document
- **Names the document uses for this model:** Kimi K2.7 Code, Kimi-K2.7-Code, K2.7-Code
- **Catalog scope:** Moonshot AI's Hugging Face model card for Kimi K2.7 Code. It describes the model as built on Kimi K2.6 with the same architecture as K2.5 and K2.6.
- **Catalog note:** Moonshot AI publishes no PDF system card or technical report for Kimi K2.7 Code. The Hugging Face model card (Markdown) is the owner document; the older Kimi K2 and K2.5 reports are not substituted.
