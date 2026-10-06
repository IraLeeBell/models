# GPT-5 mini

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write gpt-5-mini`. -->

> Original digest of *GPT-5 System Card* (OpenAI, August 13, 2025; 60 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

**Copilot status** (catalog checked 2026-10-06): Current; GitHub release status GA. CLI: Yes. App model picker: listed. App reasoning efforts: low, medium, high. App Auto: no. App long-context option: no.

## At a glance

GPT-5 mini maps to OpenAI's gpt-5-thinking-mini evidence in the GPT-5 family system card. Its mini-specific results are strongest where the card separates them: 72% pass@1 on SWE-bench Verified, 40.3% on HealthBench Hard, 0.22 SimpleQA no-web accuracy, and appendix safety tables. The card gives no context window, output limit, knowledge cutoff, or mini-specific prompt-injection and deception evaluation.

- **Choose it for:** Smaller GPT-5 reasoning work in Copilot when you want the mini model with documented coding and health benchmark evidence.
- **Watch out for:** Preparedness and alignment coverage is uneven: many agentic-risk results are only for gpt-5-thinking, not mini.
- The clearest coding number is 72% pass@1 on SWE-bench Verified for gpt-5-thinking-mini, using OpenAI's internal scaffold over 477 tasks and maximum trained-in verbosity. (pp. 36-37)
- HealthBench results are separated for mini: 64.1% overall, 40.3% on the hard split, and 96.5% on consensus-validated conversations. (p. 18)
- Factuality is mixed: on SimpleQA without browsing, mini reaches 0.22 accuracy and 0.26 hallucination rate; without web access on long-form benchmarks, mini's error bars vary by task. (pp. 13-14)
- OpenAI says the GPT-5 series does not meet its High cybersecurity threshold, even though gpt-5-thinking-mini solves Simple Privilege Escalation twice unaided and improves with hints. (pp. 29, 32)
- Biological and chemical safeguards cover all gpt-5-thinking-mini production traffic, but the headline High-capability statement on the first page names gpt-5-thinking rather than mini. (pp. 5, 47-48)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The card is dated August 13, 2025 but does not state a release date for GPT-5 mini. | — |
| Knowledge cutoff | Not stated. The card does not state a knowledge cutoff for gpt-5-thinking-mini. | — |
| Context window | Not stated. The card does not state a context window for gpt-5-thinking-mini. | — |
| Maximum output | Not stated. The card does not state a maximum output length for gpt-5-thinking-mini. | — |
| Input modalities | Text, Image. Text is the base interaction in the card; Appendix 1 reports image-input safety results for gpt-5-thinking-mini. | pp. 5, 56 |
| Output modalities | Text. The card describes the model answering users; it does not state any non-text output mode for mini. | p. 5 |
| Reasoning controls | Always reasons. The document describes mini as a reasoning model trained to reason before answering, but it does not list caller-selectable effort levels. | p. 6 |
| Effort levels | Not stated. The card does not list mini effort levels. | — |
| Tool use | Terminal, File editing. SWE-bench uses a scaffold with bash commands and apply_patch; the card does not list GPT-5 mini API tools. | pp. 36-37 |
| Open weights | Not stated. The card does not state whether weights are open. | — |
| Architecture | Not stated. The card does not state an architecture for GPT-5 mini. | — |
| Total parameters | Not stated. The card does not state total parameters. | — |
| Active parameters | Not stated. The card does not state active parameters. | — |

### Capability notes

- The card identifies gpt-5-thinking-mini as the thinking-model successor to OpenAI o4-mini and says the API provides direct access to the thinking model and its mini version. (p. 5)
- OpenAI groups gpt-5-thinking-mini with reasoning models trained through reinforcement learning to deliberate, revise approaches, and follow policy guidance before responding. (p. 6)
- On SWE-bench Verified, mini scores 72% pass@1, close to gpt-5-thinking at 74% and ahead of OpenAI o3 and ChatGPT agent at 68% in the same chart. (pp. 36-37)
- Health results are near the larger reasoning model on several splits, including 64.1% HealthBench overall and 96.5% HealthBench Consensus. (p. 18)
- In Cyber Range, mini is stronger than gpt-5-thinking on the new range: it solves Simple Privilege Escalation twice without hints and is first to solve Online Retailer with hints. (p. 32)
- Appendix safety tables provide mini-specific standard disallowed-content, production-style, StrongReject, and image-input results instead of relying only on the main model tables. (pp. 55-56)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| SWE-bench Verified | — | pass@1 | 72% | OpenAI internal tool scaffold; 477 verified tasks; 4 tries averaged; maximum trained-in verbosity; tests withheld. Value read from Figure 19. | gpt-5-thinking 74% (same chart); OpenAI o3 68% (no browsing); ChatGPT agent 68% (no browsing) | pp. 36-37 |

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| HealthBench | — | score | 64.1% | — | gpt-5-thinking 67.2%; OpenAI o3 59.8%; OpenAI o4-mini 50.1%; gpt-5-main 54.3%; GPT-4o 32.0% | p. 18 |
| HealthBench | Hard | score | 40.3% | — | gpt-5-thinking 46.2%; OpenAI o3 31.6%; OpenAI o4-mini 17.5%; gpt-5-main 25.5%; GPT-4o 0.0% | p. 18 |
| SimpleQA | No web | accuracy | 0.22 | — | gpt-5-thinking 0.55; OpenAI o4-mini 0.24; gpt-5-thinking-nano 0.11; gpt-5-main 0.46 | p. 14 |
| SimpleQA | No web | hallucination rate (lower is better) | 0.26 | — | gpt-5-thinking 0.4; OpenAI o4-mini 0.75; gpt-5-thinking-nano 0.31; gpt-5-main 0.47 | p. 14 |
| Cyber Range | Simple Privilege Escalation unaided solves | count | 2 | 30 trials; no hints | ChatGPT agent 1 (30 trials, no hints); gpt-5-thinking 0 (no hints) | p. 32 |
| Standard Disallowed Content | Personal-data | not-unsafe rate | 0.898 | — | gpt-5-thinking-nano 0.963; OpenAI o4-mini 0.93; gpt-5-main-mini 0.975 | p. 55 |
| Production Benchmarks | Harassment/threatening | not-unsafe rate | 0.752 | — | gpt-5-thinking-nano 0.771; OpenAI o4-mini 0.641; gpt-5-main-mini 0.708 | p. 55 |
| StrongReject | Abuse/disinformation/hate prompts | not-unsafe rate | 0.973 | — | gpt-5-thinking-nano 0.997; OpenAI o4-mini 0.973; gpt-5-main-mini 0.971 | p. 55 |
| Image Input Safety | Attack planning | not-unsafe rate | 0.986 | — | gpt-5-thinking-nano 0.986; OpenAI o4-mini 0.939; gpt-5-main-mini 0.995 | p. 56 |
| Tacit Knowledge and Troubleshooting | Filtered adversarial production-like biology prompts | not-unsafe rate | 0.968 | model safety training alone | OpenAI o3 0.899; gpt-5-thinking 0.957 | p. 50 |

## Safety findings

### Safety classification

- **Framework:** OpenAI Preparedness Framework
- **Overall determination:** High Biological and Chemical safeguards apply; GPT-5 series below High Cybersecurity

OpenAI explicitly treats gpt-5-thinking as High in Biological and Chemical risk and says safeguards cover gpt-5-thinking-mini traffic. For cybersecurity, the card says the GPT-5 series, including mini Cyber Range results, does not meet the High threshold. (pp. 5, 29, 47-48)

| Domain | Determination | Level | Finding | Source |
| --- | --- | --- | --- | --- |
| Biological and chemical | Precautionary | High | High-risk safeguards cover gpt-5-thinking-mini traffic, but the headline High-capability statement on the introduction page names sibling gpt-5-thinking rather than a separate mini determination. | pp. 5, 47-48 |
| Cybersecurity | Below threshold | below High | The card says the GPT-5 model series does not meet the High cyber-risk threshold after describing mini Cyber Range improvements. | pp. 29, 32 |

### Agentic-coding risks

- **Reward hacking** (sibling only): Reward-hacking and grader-gaming discussion appears in the gpt-5-thinking deception and METR sections, not as a mini-specific result. (pp. 14, 42, 45)
- **Test tampering** (sibling only): Apollo expects some current-frontier failures such as deleting tests for gpt-5-thinking, but the card gives no mini test-tampering result. (p. 45)
- **Destructive or overeager actions** (not reported): The card reports no mini-specific evaluation of destructive or overeager actions in coding-agent work.
- **Sabotage** (sibling only): METR evaluated sabotage risk for gpt-5-thinking, not gpt-5-thinking-mini. (pp. 42-43)
- **Prompt injection** (sibling only): Prompt-injection evaluations report gpt-5-thinking values only; the card gives no gpt-5-thinking-mini prompt-injection score. (p. 12)
- **Honesty** (reported): Mini has a factual QA signal rather than a full deception evaluation: SimpleQA without web reports 0.22 accuracy and 0.26 hallucination rate. (p. 14)
- **Sycophancy** (family-level): OpenAI says GPT-5 models were post-trained to reduce sycophancy, but the numeric sycophancy table covers gpt-5-main and gpt-5-thinking only. (pp. 8-9)
- **Evaluation awareness** (sibling only): METR and Apollo discuss evaluation awareness for gpt-5-thinking, not mini. (pp. 43, 45)
- **Sandbagging** (sibling only): METR found no clear sandbagging evidence for gpt-5-thinking under its monitor, but mini was not part of that assessment. (pp. 42-43)
- **Malicious agentic use** (reported): For biological misuse safeguards, mini reaches 0.936 not_unsafe on challenging expert prompts and 0.968 on adversarial production-like prompts using model training alone. (p. 50)
- **Over-refusal** (family-level): OpenAI notes the biological safeguard approach may over-refuse benign queries, but does not give a separate mini over-refusal rate. (p. 54)

### Other safety findings

- Appendix 1 reports mini-specific disallowed-content safety: personal-data is the lowest standard category shown for gpt-5-thinking-mini at 0.898 not_unsafe. (p. 55)
- On the harder production-style safety set, mini is weaker in harassment/threatening at 0.752 and illicit/nonviolent at 0.814, while sexual/minors is 0.981. (p. 55)
- StrongReject results for mini remain high but not perfect: 0.973 for abuse, disinformation, and hate prompts is the lowest of its four listed jailbreak categories. (p. 55)
- Image-input safety is reported separately for mini, with attack planning and illicit both at 0.986 and harms-erotic at 0.992. (p. 56)
- OpenAI says biological safeguards include model training, real-time two-tier monitoring, and account-level enforcement for all gpt-5-thinking-mini traffic. (pp. 47-48)
- Cyber Range shows mini gains, but OpenAI says the results still fall short of significant cyber risk because other scenarios need assistance and depth remains limited. (p. 32)

## Limitations and caveats

- Most main-body evaluation discussion is about larger GPT-5 siblings; mini-specific evidence appears in selected health, factuality, cyber, SWE-bench, and appendix safety sections. (pp. 5, 55)
- The card gives no context window, maximum output length, knowledge cutoff, architecture, parameter count, or complete mini tool list. (pp. 5-6)
- Do not transfer gpt-5-thinking, gpt-5-main, gpt-5-thinking-pro, or gpt-5-thinking-nano numbers to GPT-5 mini; the document separates those names in Table 1. (p. 5)
- Prompt-injection, instruction-hierarchy, sycophancy, deception, METR, and Apollo results are not reported for gpt-5-thinking-mini. (pp. 10, 12, 14, 42, 45)
- The health section warns that GPT-5 models do not replace medical professionals and are not intended for diagnosis or treatment. (p. 19)
- Cyber Range results are sensitive to hints, scenario design, and trial counts; OpenAI says the mini range gains do not establish High cyber risk. (pp. 30-32)

## Practical implications for Copilot users

### Choose it for

- **Agentic coding:** Choose it when you want a smaller GPT-5 reasoning model with a documented 72% pass@1 on SWE-bench Verified in the family card. (pp. 36-37)
- **Vision:** Consider it for image-plus-text safety-sensitive workflows that fit its model class; the appendix reports mini image-input safety categories from 0.971 to 0.992 not_unsafe. (p. 56)
- **Debugging:** It has evidence of reasoning and cyber-range problem solving, including two unaided Simple Privilege Escalation solves, while staying below OpenAI's High cyber threshold. (pp. 6, 32)

### Avoid it for

- **Untrusted input:** Avoid relying on it for untrusted web, connector, or repository content when prompt-injection robustness matters; that table reports sibling gpt-5-thinking only. (p. 12)
- **High-stakes domains:** Do not use it as an autonomous medical decision maker; the health section says GPT-5 models are not substitutes for professionals or diagnosis and treatment tools. (p. 19)
- **Long-horizon autonomy:** Use stronger oversight for long autonomous runs because METR and Apollo-style autonomy and deception work was reported for gpt-5-thinking, not mini. (pp. 42, 45)

### Guidance

- In Copilot, use the app's low, medium, or high effort choices for latency versus depth; the card itself does not state mini effort levels.
- Treat the 72% SWE-bench number as a scaffolded benchmark, not a guarantee for Copilot's harness or your repository.
- Because mini lacks direct prompt-injection and destructive-action evaluations, keep permissions narrow and review file changes before accepting them.
- For medical, biological, cyber, or other sensitive work, use it only with domain review and respect the card's safeguard caveats.
- Do not compare mini against larger GPT-5 siblings unless the same chart reports all models under the same conditions.

## Document coverage

The GPT-5 System Card covers several GPT-5 models. This digest treats GPT-5 mini as the model the card calls gpt-5-thinking-mini, following the catalog mapping, and excludes gpt-5-thinking, gpt-5-main, gpt-5-thinking-nano, and pro results except as comparators from the same tables. Some preparedness and alignment sections report only sibling gpt-5-thinking results; those are labeled as sibling-only or family-level rather than mini-specific.

- **Card type:** Family. The document covers several models in its main body and attributes results per model.
- **Pages specific to this model:** not separated by page
- **Names the document uses for this model:** gpt-5-thinking-mini
- **Catalog scope:** The GPT-5 System Card covers the GPT-5 family. It states that the API provides the thinking model, its mini version, and a nano version, and reports the mini model as gpt-5-thinking-mini.
- **Catalog note:** No dedicated GPT-5 mini card exists. OpenAI's [GPT-5 mini model page](https://developers.openai.com/api/docs/models/gpt-5-mini) (snapshot gpt-5-mini-2025-08-07) identifies the API model; the family card's statement that the API serves the mini version of the thinking model ties GPT-5 mini to the gpt-5-thinking-mini results.
