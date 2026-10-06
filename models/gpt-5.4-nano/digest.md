# GPT-5.4 nano

> No publisher system card or model card exists for GPT-5.4 nano. The closest owner documentation is OpenAI's
> [GPT-5.4 nano model page](https://developers.openai.com/api/docs/models/gpt-5.4-nano); this digest summarizes that page and notes that the GPT-5.4 Thinking card does not mention nano.

## At a glance

- No OpenAI system card or model card covers GPT-5.4 nano, and the GPT-5.4 Thinking System Card does not discuss a nano model.
- OpenAI's model page identifies the current snapshot as `gpt-5.4-nano-2026-03-17` and describes GPT-5.4 nano as a small GPT-5.4-class model for simple high-volume tasks such as classification, extraction, ranking, and sub-agent work.
- The owner page lists a 400,000-token context window, 128,000 maximum output tokens, an August 31, 2025 knowledge cutoff, and reasoning-token support with `reasoning_effort` values from `none` through `xhigh`.
- Modalities are text input/output and image input only; the page marks audio and video as unsupported.
- The page lists support for streaming, function calling, structured outputs, and several Responses API tools, while marking fine-tuning, computer use, and tool search as unsupported.
- GitHub's per-client availability table marks GPT-5.4 nano unavailable in all Copilot clients except the Codex extension for VS Code, so it is a utility model rather than a selectable model in the Copilot CLI or app.

## What the publisher documents

- **Identity and snapshot:** OpenAI documents `gpt-5.4-nano` with the `gpt-5.4-nano-2026-03-17` snapshot.
- **Intended use:** The page positions it for simple high-volume work including classification, data extraction, ranking, and sub-agent tasks.
- **Context and outputs:** The owner page states a 400,000-token context window and 128,000 maximum output tokens.
- **Inputs and outputs:** It supports text input/output and image input; audio and video are not supported.
- **Reasoning controls:** The page says reasoning tokens are supported and `reasoning_effort` can be `none`, `low`, `medium`, `high`, or `xhigh`.
- **Tooling:** The page lists function calling, structured outputs, streaming, web search, file search, image generation, code interpreter, hosted shell, apply-patch, skills, and MCP support, but not fine-tuning, computer use, or tool search.
- **What is absent:** The owner page does not provide safety evaluations, benchmark tables, Preparedness classifications, red-team results, or deployment safeguards comparable to a system card.

## Practical implications for Copilot users

- In Copilot, treat GPT-5.4 nano as background utility infrastructure unless you are specifically using a surface that exposes it; it is not a normal CLI or app picker choice.
- Its published owner documentation supports expectations of low-latency, structured, high-volume helper work, not deep repository reasoning or complex architecture review.
- Because there is no system card, do not infer GPT-5.4 Thinking's safety findings, High-capability determinations, or benchmark scores for GPT-5.4 nano.
- The large context and output limits on the owner page are API facts, not a promise that any Copilot client will expose those limits or expose the model directly.
- For any visible output produced through a workflow using this model, continue to validate factual, security, and code changes with normal review and tests.

## Document coverage

This digest uses OpenAI's GPT-5.4 nano model page saved for this catalog entry. It does not cite PDF pages because no publisher system card or model card exists for this model. The digest also notes the catalog scope caveat that the GPT-5.4 Thinking card does not mention nano and that GitHub exposes it only as a utility model in the Codex extension for VS Code.
