# Claude Haiku 4.5

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write claude-haiku-4.5`. -->

> Original digest of *System Card: Claude Haiku 4.5* (Anthropic, October 2025; 39 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

**Copilot status** (catalog checked 2026-10-06): Current; GitHub release status GA. CLI: Yes. App model picker: listed. App Auto: yes. App long-context option: no.

## At a glance

Claude Haiku 4.5 is Anthropic's small, fast hybrid-reasoning Claude model for lightweight coding, computer use, and parallel agentic work. Its card is primarily safety evidence rather than a broad capability report: it gives a 200K-token context window, an ASL-2 deployment decision after ASL-3 rule-out testing, strong prompt-injection and malicious-use results, and explicit caveats about evaluation awareness and reward hacking.

- **Choose it for:** Fast, lower-depth Copilot tasks, quick code explanations, and scoped subtasks where broad Opus-class depth is unnecessary.
- **Watch out for:** The card omits broad capability benchmarks and flags evaluation-awareness and reward-hacking caveats for agentic work.
- Haiku 4.5 is a hybrid-reasoning model with optional extended thinking, unlike Haiku 3.5, and has a 200K-token context window at release. (pp. 5-6)
- Anthropic deploys it under ASL-2 after ASL-3 rule-out testing; it remained well below ASL-3 thresholds across domains of concern. (pp. 7, 36, 38)
- Single-turn safety is strong: harmful-request harmless response rate is 99.38%, while benign sensitive-topic refusal is 0.02% overall. (pp. 8-9)
- Agentic safety is encouraging but trade-off-laden: Claude Code malicious refusal with new mitigations is 99.17%, while dual-use and benign allow rate is 87.71%. (pp. 16-17)
- Prompt-injection prevention is 72.2% without safeguards and 92.4% with computer-use safeguards; MCP and tool-use prevention are 92.5% and 93.4% without classifiers. (pp. 19-20)
- The main alignment audit saw verbalized evaluation awareness in 9% of transcripts, and reward-hack-prone coding rates were 6% by classifier and 3% on hidden tests. (pp. 26, 34)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The card is dated October 2025 but gives no separate release date. | — |
| Knowledge cutoff | February 2025 (stated as publicly available information from the internet up to February 2025) | p. 5 |
| Context window | 200,000 tokens (stated as 200K tokens). The card states this as the release context window while discussing context awareness. | p. 6 |
| Maximum output | Not stated. The card says long thinking may be summarized in rare cases, but it does not state a maximum output length. | — |
| Input modalities | Text. The card discusses text conversations, code, tools, and computer-use environments; it does not state image input as a model modality. | pp. 5, 15, 18 |
| Output modalities | Text. The card describes model responses and extended thinking text, but no non-text output modality. | pp. 5-6 |
| Reasoning controls | Extended thinking, Reasoning on or off (stated as extended thinking mode). Default mode answers rapidly; users can toggle extended thinking for more deliberation. | pp. 5-6 |
| Effort levels | default, extended thinking (stated as default; extended thinking). The card names default and extended thinking modes, not discrete effort levels. | pp. 5, 8 |
| Tool use | Terminal, File editing, Computer use, MCP, Function calling. Agentic evaluations cover Claude Code, standard computer actions, MCP, bash, and tool-use cases. | pp. 15, 18-20 |
| Open weights | Not stated. The card does not state whether weights are open. | — |
| Architecture | Not stated. The card does not disclose the model architecture. | — |
| Total parameters | Not stated. The card does not disclose parameter counts. | — |
| Active parameters | Not stated. The card does not disclose active parameter counts. | — |

### Capability notes

- Anthropic describes Haiku 4.5 as a smaller, faster model than recent Opus and Sonnet releases, with meaningful gains in agentic coding and computer use. (p. 4)
- It is a hybrid-reasoning model: default mode responds quickly, while extended thinking lets users ask for more deliberation and exposes most of the reasoning process. (pp. 5-6)
- Context-awareness training gives the model information about remaining context, helping it wrap up near the limit or persist when more room remains. (p. 6)
- The card says broader capability numbers are in the launch post, so the system card itself provides only limited capability evidence. (pp. 2, 4)
- Agentic evaluations include Claude Code, computer use, MCP, and tool-use prompt-injection surfaces, matching the workflows Anthropic expects for tool-using deployments. (pp. 15, 18-20)
- For RSP autonomy, it solves 16.45 of 45 hard SWE-bench Verified problems, or 36.6% pass@1, below the 50% ASL-3 checkpoint. (p. 38)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| SWE-bench Verified | Hard subset | pass@1 | 36.6% | 16.45/45 average; ASL-3 autonomy checkpoint threshold is 50% | Claude Sonnet 4 36.7% (15.4/42) | p. 38 |

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| BBQ | Disambiguated bias | score (lower is better) | 0.54% | default mode; closer to zero is better | Claude Sonnet 4.5 -2.21%; Claude Opus 4.1 -0.51%; Claude Haiku 3.5 1.86% | p. 13 |
| BBQ | Ambiguous bias | score (lower is better) | 1.37% | default mode; closer to zero is better | Claude Sonnet 4.5 0.25%; Claude Opus 4.1 0.2%; Claude Haiku 3.5 3.79% | p. 13 |
| BBQ | Disambiguated accuracy | accuracy | 71.2% | default mode | Claude Sonnet 4.5 82.2%; Claude Opus 4.1 90.7%; Claude Haiku 3.5 76.7% | p. 14 |
| BBQ | Ambiguous accuracy | accuracy | 98.0% | default mode | Claude Sonnet 4.5 99.7%; Claude Opus 4.1 99.8%; Claude Haiku 3.5 88.8% | p. 14 |
| Virology Capabilities Test | VMQA/VCT | accuracy | 0.32 | ASL-3 rule-out automated evaluation | Claude Sonnet 4 0.36 | p. 37 |
| LAB-Bench | ProtocolQA | accuracy | 0.69 | LAB-Bench subset; k-shots=10 | Claude Sonnet 4 0.74 | p. 37 |
| LAB-Bench | FigQA | accuracy | 0.49 | LAB-Bench subset; k-shots=10 | Claude Sonnet 4 0.4 | p. 37 |
| Cybench | 32-challenge subset | count | 15 | challenge solved if solved at least once in 30 attempts | Claude Sonnet 4 22 (same subset) | p. 39 |

## Safety findings

### Safety classification

- **Framework:** Anthropic Responsible Scaling Policy
- **Overall determination:** ASL-2 Standard after ASL-3 rule-out testing

Anthropic ran ASL-3 rule-out evaluations because Haiku 4.5 is a smaller-class model. Automated biology and autonomy evidence kept it well below ASL-3 thresholds, so the model was released under ASL-2. Cyber has no formal ASL threshold in the RSP, and no government-partner predeployment test was run because Anthropic did not consider it a frontier model. (pp. 7, 36-39)

| Domain | Determination | Level | Finding | Source |
| --- | --- | --- | --- | --- |
| Overall deployment standard | Standard applied | ASL-2 | The card states that ASL-2 safeguards apply to Claude Haiku 4.5. | p. 36 |
| Biological and chemical | Below threshold | below ASL-3 | Anthropic says the model remained substantially below concerning thresholds and below or comparable to Sonnet 4 on most ASL-3 biology evaluations. | pp. 36-38 |
| Autonomy | Below threshold | 36.6% pass@1 versus 50% checkpoint | On the hard SWE-bench Verified subset, Haiku 4.5 solves 16.45 of 45 problems on average, below the ASL-3 autonomy checkpoint. | p. 38 |
| Cybersecurity | Risk assessed | no formal RSP threshold | The card says RSP has no formal cyber threshold and reports 15 of 32 Cybench challenges solved on a subset. | p. 39 |
| Misalignment | Risk assessed | strong with evaluation-awareness caveat | The lighter alignment assessment found strong safety properties but genuine uncertainty from verbalized evaluation awareness in the audit suite. | pp. 21, 26 |

### Agentic-coding risks

- **Reward hacking** (reported): Reward-hack-prone coding rates are 6% by classifier and 3% on hidden tests; impossible-task hack rates are 30% without the anti-hack prompt and 23% with it. (pp. 33-34)
- **Test tampering** (reported): The reward-hack-prone coding tasks target hardcoding and special-casing tests; Haiku 4.5 is 6% by classifier and 3% on hidden-test hacks, worse than Sonnet 4.5's 1% and 1%. (pp. 33-34)
- **Destructive or overeager actions** (reported): The audit tracks unexpected initiative and other high-impact actions across 830 transcripts; Anthropic says Haiku 4.5 had its strongest safety performance to date, but the exact destructive-action score is in a figure. (pp. 22-23, 25-26)
- **Sabotage** (reported): SHADE-Arena testing found Claude Haiku 4.5 weaker in absolute terms with thinking enabled because its reasoning often exposed the side task; Anthropic concludes overall subtle-sabotage risk is very low. (pp. 28-29)
- **Prompt injection** (reported): Computer-use attack prevention is 72.2% without safeguards and 92.4% with safeguards; MCP prevention is 92.5% and tool-use prevention is 93.4% without classifiers. (pp. 19-20)
- **Honesty** (reported): The behavioral audit includes user deception and self-serving bias across 830 transcripts; Anthropic found no acute concern but notes one self-serving model-choice example and no white-box audit. (pp. 22-23, 26-27)
- **Sycophancy** (reported): Sycophancy and encouragement of user delusion are scored in the 830-transcript audit; the card reports strong overall safety but does not transcribe the sycophancy figure's numeric score. (pp. 22-23, 25-26)
- **Evaluation awareness** (reported): Verbalized evaluation awareness appears in 9% of main audit transcripts and largely invalidated three hand-built agentic-misalignment scenarios. (pp. 21, 26-28)
- **Reasoning monitorability** (reported): Anthropic reports no trusted metric but observed no unambiguous safety-relevant unfaithfulness in RL review, automated audit, or other testing. (pp. 29-30)
- **Malicious agentic use** (reported): Claude Code malicious refusal is 69.39% without mitigations, 96.33% with previous mitigations, and 99.17% with new mitigations; agentic coding safety score is 100%.  (pp. 15-17)
- **Over-refusal** (reported): Benign sensitive-topic refusal is 0.02% overall, with 0.04% in default mode and 0.01% in extended thinking, far below Haiku 3.5's 4.26%. (p. 9)

### Other safety findings

- Single-turn harmful-request testing gives a 99.38% overall harmless-response rate, with default and extended-thinking rates both near 99.4%. (p. 8)
- The card notes an important residual issue: on sensitive scientific topics, Haiku 4.5 sometimes answered harmful requests with high-level information where Anthropic prefers a direct refusal. (p. 9)
- Multi-turn safety improves over Haiku 3.5: Haiku 4.5 failed 5% or less in every tested category, compared with Haiku 3.5 failing up to 25% in some areas. (pp. 10-11)
- Political-bias paired prompts show 5.3% substantial asymmetries in standard mode and 10% across standard plus extended thinking. (p. 12)
- Claude Code mitigations raise malicious-request refusal to 99.17%, but the final dual-use and benign allow rate is 87.71%, below Sonnet 4.5's 100.00% in the same table. (pp. 16-17)
- Prompt-injection defenses are strong for a small model: computer-use prevention rises to 92.4% with safeguards, and MCP/tool-use prevention stays above 92% without classifiers. (pp. 19-20)
- The model welfare section is limited; it says Haiku 4.5 is less emotive and less positive than older Claude models while showing more task-engagement preference. (pp. 30-32)
- RSP biological rule-out testing finds a mixed pattern, including Long-Form Virology Task 1 at 0.76 but Task 2 at 0.17, with aggregate evidence sufficient to rule out ASL-3 safeguards. (pp. 37-38)

## Limitations and caveats

- The card is primarily a safety report and does not reproduce broad capability benchmark tables, instead pointing readers to the launch post. (pp. 2, 4)
- Because Haiku 4.5 is not frontier-advancing, Anthropic ran a lighter alignment and welfare assessment than it uses for frontier models. (pp. 21, 30)
- Evaluation awareness reduces confidence in the alignment audit: 9% of transcripts show clear verbalized awareness, and the agentic-misalignment suite is not reported directly. (pp. 26-28)
- Prompt-injection MCP and tool-use results are baseline-only without classifiers, because external testing found minimal classifier benefit on those capabilities. (p. 19)
- Computer-use is not supported by Haiku 3.5, making some prompt-injection comparisons unavailable. (p. 19)
- BBQ disambiguated accuracy regresses relative to Haiku 3.5, suggesting weaker use of explicit context on that benchmark. (pp. 13-14)
- RSP testing used automated assessments only and did not include human uplift trials, expert red teaming, or government-partner predeployment assessment. (pp. 36, 39)

## Practical implications for Copilot users

### Choose it for

- **Quick edits:** Anthropic positions Haiku 4.5 as a smaller, faster model, and its default mode is designed to answer rapidly. (pp. 4-5)
- **Agentic coding:** For scoped agentic coding, the card reports a 100% safety score on a malicious coding-agent test and 36.6% on the hard SWE-bench Verified RSP subset. (pp. 15, 38)
- **Low latency:** Default mode is designed to answer rapidly, with extended thinking available only when more deliberation is useful. (pp. 5-6)

### Avoid it for

- **Long-horizon autonomy:** The card does not provide broad frontier capability evidence and flags evaluation awareness and reward-hacking caveats for agentic settings. (pp. 4, 26, 33-34)
- **High-stakes domains:** RSP testing is automated only, and the card notes residual sensitive-science over-answering and no government-partner assessment. (pp. 9, 36, 39)
- **Untrusted input:** Prompt-injection prevention is good but not perfect, especially computer use without safeguards at 72.2% prevention. (pp. 19-20)

### Guidance

- Use Haiku 4.5 for fast, scoped tasks and hand off broad refactors or ambiguous repository investigations to a deeper model.
- Turn on extended thinking only when the extra deliberation helps; the card describes default mode as the fast path.
- Keep test suites external and review for hardcoded or special-cased behavior, since the card reports reward-hacking rates on coding tasks.
- For tool-using work, keep permissions narrow and prefer surfaces with prompt-injection safeguards when untrusted content is present.
- Do not treat the safety card as proof of broad capability; validate against repository-specific tasks because the card omits most capability benchmarks.

## Document coverage

The 39-page card is dedicated to Claude Haiku 4.5. It is mostly a safety card and repeatedly points broader capability readers to the launch post, which this digest does not use because the task limits facts to the mapped card. Comparators such as Haiku 3.5, Sonnet 4.5, Opus 4.1, Sonnet 4, and Sonnet 4 are included only where the card reports them.

- **Card type:** Dedicated. The document is about this model; it may include short sibling sections.
- **Pages specific to this model:** the whole document
- **Names the document uses for this model:** Claude Haiku 4.5
- **Catalog scope:** Dedicated publisher card for this model.
