# GPT-5.4 nano

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write gpt-5.4-nano`. -->

> No publisher system card or model card exists for GPT-5.4 nano. This digest summarizes the closest owner documentation: [OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano). See [source.md](source.md) for provenance.

**Copilot status** (catalog checked 2026-10-06): Utility only (not selectable); GitHub release status GA. CLI: No. GitHub's per-client table marks it unavailable in every client except the Codex extension for VS Code (Copilot Pro+), so it is not a manually selectable CLI or app model.

## At a glance

GPT-5.4 nano has no publisher system card or model card; the closest owner source is OpenAI's API model page. That page states a 400,000-token context window, 128,000-token maximum output, text and image input, text output, an August 31, 2025 knowledge cutoff, reasoning effort levels from none through xhigh, and supported tools. The catalog marks it as a GitHub utility model rather than a manually selectable Copilot CLI or app model.

- **Choose it for:** Utility helper tasks only where the owner page's limits and tool list are enough and no safety-card evidence is needed.
- **Watch out for:** No publisher card, no benchmark results, no Preparedness classification, and no Copilot CLI or app picker availability.
- The owner page states a 400,000-token context window, a 272,000-token maximum input, and a 128,000-token maximum output. ([OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano))
- It lists text and image input, text output, an August 31, 2025 knowledge cutoff, and reasoning token support. ([OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano))
- Reasoning effort supports none by default plus low, medium, high, and xhigh; the page reports no benchmark or safety evaluation table. ([OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano))
- Responses API tools listed include function calling, web search, file search, image generation, code interpreter, hosted shell, patch application, skills, and MCP. ([OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano))

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The owner page names a default snapshot dated 2026-03-17 but does not state a model release date. | — |
| Knowledge cutoff | August 31, 2025 (stated as Aug 31, 2025 knowledge cutoff) | [OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano) |
| Context window | 400,000 tokens (stated as 400,000 context window) | [OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano) |
| Maximum output | 128,000 tokens (stated as 128,000 max output tokens) | [OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano) |
| Input modalities | Text, Image (stated as Input modalities: text, image) | [OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano) |
| Output modalities | Text (stated as Output modalities: text) | [OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano) |
| Reasoning controls | Effort levels (stated as Reasoning.effort supports). The page also states reasoning token support. | [OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano) |
| Effort levels | none, low, medium, high, xhigh (stated as none (default), low, medium, high and xhigh) | [OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano) |
| Tool use | Function calling, Web search, File search, Code execution, Terminal, File editing, MCP, Image generation, Skills (stated as Responses API supported tools). The page names code_interpreter, hosted_shell, and apply_patch; these are mapped to code-execution, terminal, and file-editing. | [OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano) |
| Open weights | Not stated. The owner page does not state open weights. | — |
| Architecture | Not stated. The owner page does not state an architecture. | — |
| Total parameters | Not stated. The owner page does not state total parameters. | — |
| Active parameters | Not stated. The owner page does not state active parameters. | — |

### Capability notes

- OpenAI's page positions GPT-5.4 nano for simple high-volume helper work such as classification, extraction, ranking, and sub-agent tasks. ([OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano))
- The page gives serving limits: 400,000 tokens of context, 272,000 maximum input tokens, and 128,000 maximum output tokens. ([OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano))
- It supports text and image input with text output and has an August 31, 2025 knowledge cutoff. ([OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano))
- Reasoning effort can be none, low, medium, high, or xhigh, with none as the default. ([OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano))
- The Responses API tool list includes function calling, web search, file search, image generation, code interpreter, hosted shell, patch application, skills, and MCP. ([OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano))

## Evaluations

The owner documentation reports no benchmark results for this model.

## Safety findings

### Safety classification

- **Framework:** No safety framework stated
- **Overall determination:** Not stated

No publisher system card or model card exists for GPT-5.4 nano, and the owner API page does not state a safety framework, Preparedness classification, or per-domain determination.

The document states no per-domain determinations.

### Agentic-coding risks

- **Reward hacking** (not reported): No card exists, and the owner page reports no reward-hacking or grader-gaming evaluation.
- **Test tampering** (not reported): No card exists, and the owner page reports no test-tampering evaluation.
- **Destructive or overeager actions** (not reported): No card exists, and the owner page reports no destructive-action or overeager-agent evaluation.
- **Sabotage** (not reported): No card exists, and the owner page reports no sabotage or oversight-evasion evaluation.
- **Prompt injection** (not reported): No card exists, and the owner page reports no prompt-injection robustness result.
- **Honesty** (not reported): No card exists, and the owner page reports no honesty, deception, or hallucination evaluation.
- **Sycophancy** (not reported): No card exists, and the owner page reports no sycophancy evaluation.

### Other safety findings

The owner documentation reports no other safety findings.

## Limitations and caveats

- No publisher system card or model card exists for GPT-5.4 nano, so there are no card-based benchmark, red-team, Preparedness, or safeguard results. ([OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano))
- The owner page gives serving facts but no evaluation methodology, model training description, architecture, parameter count, or safety classification. ([OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano))
- Do not attribute GPT-5.4 or GPT-5.4 mini card results to nano; the catalog says the GPT-5.4 Thinking card does not mention it. ([OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano))

## Practical implications for Copilot users

### Choose it for

- **Quick edits:** Use it only for simple helper work such as classification, extraction, ranking, or sub-agent tasks where the owner page's serving facts are sufficient. ([OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano))
- **Vision:** Consider it for lightweight text-plus-image inputs because the owner page lists image input and text output. ([OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano))

### Avoid it for

- **Agentic coding:** Avoid treating it as a validated coding agent; the owner page reports no coding benchmarks or system-card safety evidence. ([OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano))
- **High-stakes domains:** Avoid high-stakes or sensitive autonomous decisions because there is no card, safety framework, or evaluation evidence for those uses. ([OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano))
- **Long-horizon autonomy:** Avoid long autonomous runs because the owner page gives no agentic-risk results, despite listing tools such as hosted shell and patch application. ([OpenAI GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano))

### Guidance

- In GitHub Copilot, treat this as a utility model: the catalog says it is not manually selectable in the CLI or app picker.
- Use only the documented serving facts above; do not borrow GPT-5.4 or GPT-5.4 mini system-card results.
- Because no card exists, require stronger human review before using tool outputs that can affect files, shells, or external data.
- For model comparisons, record it as no-card coverage rather than as a member of the GPT-5.4 Thinking card.

## Document coverage

No publisher system card or model card covers GPT-5.4 nano, and the GPT-5.4 Thinking card does not mention it. This digest therefore uses only the owner model page named in the catalog for serving facts. It does not import GPT-5.4 or GPT-5.4 mini safety, benchmark, or Preparedness results, and all agentic-risk topics are marked not reported.

- **Card type:** None. No publisher system card or model card exists.
- **Pages specific to this model:** not applicable
- **Catalog scope:** No publisher system card covers GPT-5.4 nano. The GPT-5.4 Thinking System Card does not mention it.
- **Catalog note:** No dedicated card. Closest owner documentation: OpenAI's [GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano) (snapshot gpt-5.4-nano-2026-03-17).
