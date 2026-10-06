# Raptor mini

> No publisher system card or model card exists for Raptor mini. The closest owner documentation is GitHub's [Raptor mini public preview changelog](https://github.blog/changelog/2025-11-10-raptor-mini-is-rolling-out-in-public-preview-for-github-copilot/); GitHub's supported-models documentation also identified the model as a fine-tuned GPT-5 mini.

## At a glance

- GitHub announced Raptor mini for Copilot public preview on November 10, 2025, describing it as an experimental model for Visual Studio Code.
- The changelog said users could select it in the VS Code Copilot Chat model picker for chat, ask, edit, and agent modes.
- The supported-models documentation listed the provider lineage as a fine-tuned GPT-5 mini, but no card evaluates the Raptor-specific fine-tune.
- GitHub did not list Raptor mini for the Copilot CLI in the catalog context for this digest.
- For base-model safety and capability context, readers should consult the [gpt-5-mini](../gpt-5-mini/) folder, with the caveat that fine-tuning can change behavior.
- GitHub later retired Raptor mini on 2026-09-01, so this entry is historical.

## What the publisher documents

- The changelog documents public-preview availability in VS Code and describes Raptor mini as experimental owner documentation, not a model card or system card.
- GitHub's supported-models docs supplied the lineage note that Raptor mini was a fine-tuned GPT-5 mini; they did not provide Raptor-specific evaluations.
- No owner document reports benchmark scores, training data, safety mitigations, refusal behavior, jailbreak robustness, or secure-coding evaluations for Raptor mini itself.
- The base GPT-5 mini material may help explain the underlying family, but it cannot establish how the Raptor fine-tune behaved after additional training or product integration.

## Practical implications for Copilot users

- GitHub retired the model on 2026-09-01; the remaining bullets are for historical comparison and for understanding the successor model's lineage.
- Treat Raptor mini as a VS Code-era experimental fine-tune, not as a model with a public standalone safety or benchmark record.
- If comparing old Copilot behavior, separate base GPT-5 mini evidence from Raptor mini's undocumented fine-tuning effects.
- Do not assume CLI availability, because the owner documentation described Visual Studio Code selection rather than Copilot CLI use.
- For security-sensitive or production code generated during the preview, rely on tests, code review, and the base-model card only as incomplete background.

## Document coverage

This digest uses GitHub's changelog entry and the catalog-provided note from GitHub's supported-models documentation. It intentionally does not create model-card claims where no publisher card exists. The gpt-5-mini folder is the nearest base-model reference, but it is not evidence for Raptor mini's fine-tuned behavior.
