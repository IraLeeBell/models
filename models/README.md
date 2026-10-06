# GitHub Copilot model catalog

Checked **2026-10-06** against [GitHub's supported-model tables](https://docs.github.com/en/copilot/reference/ai-models/supported-models)
([frozen docs revision](https://github.com/github/docs/tree/45a0f053ac67e8d1f56fc8f7ee38f0b2a58925c3/data/tables/copilot)).
**29 folders**: 28 listed for CLI in the per-client table;
GPT-6.1 Sol is additionally listed for CLI Auto but not yet in that table.
The app manual picker was observed to list 24 of these publicly
documented models; 15 appear in GitHub's separate app Auto table.
One model, Claude Sonnet 4.6, has a documented annual-plan exception
despite an earlier retirement date. GPT-5.4 nano is a non-selectable
utility model and has no folder.

The **app picker** observation is local to the checked date and account;
a blank observation does not mean a model is unavailable to every user.
The **app Auto** column means eligible for *automatic selection*, not
necessarily selectable manually. Neither is the GitHub.com browser column.
CLI evidence is from the per-client table except where explicitly noted.
Plan, policies, region, and rollout can alter actual availability.

| Model | Publisher | CLI evidence | App picker observed | App Auto | Owner document |
| --- | --- | --- | --- | --- | --- |
| [GPT-5 mini](./gpt-5-mini/digest.md) | OpenAI | per-client | yes | not listed | [none confirmed](./gpt-5-mini/source.md) |
| [GPT-5.3-Codex](./gpt-5.3-codex/digest.md) | OpenAI | per-client | yes | not listed | [HTML](./gpt-5.3-codex/source.md) |
| [GPT-5.4](./gpt-5.4/digest.md) | OpenAI | per-client | yes | not listed | [PDF](./gpt-5.4/source.md) |
| [GPT-5.4 mini](./gpt-5.4-mini/digest.md) | OpenAI | per-client | yes | not listed | [PDF](./gpt-5.4-mini/source.md) |
| [GPT-5.5](./gpt-5.5/digest.md) | OpenAI | per-client | yes | not listed | [PDF](./gpt-5.5/source.md) |
| [GPT-5.6 Luna](./gpt-5.6-luna/digest.md) | OpenAI | per-client | yes | yes | [PDF](./gpt-5.6-luna/source.md) |
| [GPT-5.6 Sol](./gpt-5.6-sol/digest.md) | OpenAI | per-client | yes | yes | [PDF](./gpt-5.6-sol/source.md) |
| [GPT-5.6 Terra](./gpt-5.6-terra/digest.md) | OpenAI | per-client | yes | yes | [PDF](./gpt-5.6-terra/source.md) |
| [GPT-6 Astra](./gpt-6-astra/digest.md) | OpenAI | per-client | yes | yes | [PDF](./gpt-6-astra/source.md) |
| [GPT-6 Luna](./gpt-6-luna/digest.md) | OpenAI | per-client | yes | yes | [PDF](./gpt-6-luna/source.md) |
| [GPT-6 Sol](./gpt-6-sol/digest.md) | OpenAI | per-client | yes | yes | [PDF](./gpt-6-sol/source.md) |
| [GPT-6.1 Sol](./gpt-6.1-sol/digest.md) | OpenAI | Auto only | yes | yes | [none confirmed](./gpt-6.1-sol/source.md) |
| [Claude Fable 5](./claude-fable-5/digest.md) | Anthropic | per-client | not observed | not listed | [PDF](./claude-fable-5/source.md) |
| [Claude Fable 5.1](./claude-fable-5.1/digest.md) | Anthropic | per-client | not observed | not listed | [PDF](./claude-fable-5.1/source.md) |
| [Claude Haiku 4.5](./claude-haiku-4.5/digest.md) | Anthropic | per-client | yes | yes | [PDF](./claude-haiku-4.5/source.md) |
| [Claude Opus 4.8](./claude-opus-4.8/digest.md) | Anthropic | per-client | yes | yes | [PDF](./claude-opus-4.8/source.md) |
| [Claude Opus 4.8 (fast mode) (preview)](./claude-opus-4.8-fast-mode/digest.md) | Anthropic | per-client | not observed | not listed | [PDF](./claude-opus-4.8-fast-mode/source.md) |
| [Claude Opus 5](./claude-opus-5/digest.md) | Anthropic | per-client | yes | yes | [PDF](./claude-opus-5/source.md) |
| [Claude Opus 5.5](./claude-opus-5.5/digest.md) | Anthropic | per-client | yes | yes | [PDF](./claude-opus-5.5/source.md) |
| [Claude Sonnet 4.6](./claude-sonnet-4.6/digest.md) (limited) | Anthropic | per-client | not observed | not listed | [PDF](./claude-sonnet-4.6/source.md) |
| [Claude Sonnet 5](./claude-sonnet-5/digest.md) | Anthropic | per-client | yes | yes | [PDF](./claude-sonnet-5/source.md) |
| [Claude Sonnet 5.5](./claude-sonnet-5.5/digest.md) | Anthropic | per-client | yes | yes | [none confirmed](./claude-sonnet-5.5/source.md) |
| [Gemini 3.7 Flash](./gemini-3.7-flash/digest.md) | Google | per-client | yes | not listed | [PDF](./gemini-3.7-flash/source.md) |
| [Gemini 3.8 Flash](./gemini-3.8-flash/digest.md) | Google | per-client | yes | yes | [PDF](./gemini-3.8-flash/source.md) |
| [MAI-Code-1.1-Flash](./mai-code-1.1-flash/digest.md) | Microsoft | per-client | yes | yes | [PDF](./mai-code-1.1-flash/source.md) |
| [Kimi K3](./kimi-k3/digest.md) | Moonshot AI | per-client | not observed | not listed | [PDF](./kimi-k3/source.md) |
| [Grok 4.5](./grok-4.5/digest.md) | xAI | per-client | yes | not listed | [PDF](./grok-4.5/source.md) |
| [Grok 4.6](./grok-4.6/digest.md) | xAI | per-client | yes | not listed | [PDF](./grok-4.6/source.md) |
| [Grok 4.7](./grok-4.7/digest.md) | xAI | per-client | yes | not listed | [PDF](./grok-4.7/source.md) |

**Documentation:** [Supported models](https://docs.github.com/en/copilot/reference/ai-models/supported-models) (release status, CLI, app Auto,
retirement history); [model comparison](https://docs.github.com/en/copilot/reference/ai-models/model-comparison) (use cases and
publisher links). The per-client GitHub.com column is **not** app evidence.
The release-status and retirement tables disagree for Claude Sonnet 4.6;
the retirement footnote preserves access for annual individual subscribers.
The catalog labels this restricted exception rather than calling it
universally available.

**Licensing:** Publisher PDFs and full-text extractions are *not* committed.
An official public download URL is not a redistribution license. The
repository's MIT license covers only its own code and original summaries.
26 entries link to a matching owner document; the other
3 explicitly explain the missing dedicated card.
A PDF hash in `source.md` identifies the publisher file downloaded for
verification on the checked date; it does not imply a local PDF is shipped.

**Updating:** Edit `catalog.json` with public evidence, update the checked
date and docs revision, verify owner URL, title and scope, then run
`python3 models/generate.py --write` and
`python3 models/generate.py --check`. Do not assign a family card to a
new variant unless the publisher document explicitly covers it.
