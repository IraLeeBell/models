# MAI-Code-1-Flash

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write mai-code-1-flash`. -->

> Original digest of *MAI-Code-1-Flash model card* (Microsoft, June 2, 2026; 6 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

**Copilot status:** Retired from GitHub Copilot on 2026-09-10. This digest is kept for historical comparison and model lineage.

## At a glance

MAI-Code-1-Flash is Microsoft's retired first MAI-Code Flash coding model for GitHub Copilot, using a sparse-MoE transformer with 137B total parameters, 5B active parameters, and a 256K-token context. Its card reports strong production-harness coding, math, science, instruction-following, and tool-use results against Claude Haiku 4.5, but it documents text input only. Safety coverage is qualitative and does not measure the required agentic-coding risks.

- **Choose it for:** Historical comparison with MAI-Code-1.1-Flash and old Copilot routing decisions, not as a current model choice.
- **Watch out for:** Text-only card, retired catalog status, no numeric safety outcomes, and no prompt-injection or test-tampering evaluation.
- In the coding table, MAI-Code-1-Flash reports 71.6% on SWE-Bench Verified, 51.2% on SWE-Bench Pro, 65.5% on SWE-Bench Multilingual, and 54.8% on Terminal Bench 2. (p. 5)
- The same card reports 92.5% on AIME 2026, 84.6% on GPQA Diamond, 75.0 average on IF Bench, and 71.7 on the telecom split of tau2-Bench. (pp. 5-6)
- It is a text-to-text sparse mixture-of-experts coding model with 137B total parameters, 5B active parameters, text input, text output, and a 256K-token context. (p. 1)
- The production-harness coding methodology includes repository context, tool calls, and verification, and compares models under the same settings. (p. 6)
- Safety reporting names cyber and secure-coding assessments plus classifiers and filters, but publishes no safety benchmark numbers or agentic-risk tests. (p. 4)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | June 2, 2026 (stated as June 2, 2026) | p. 1 |
| Knowledge cutoff | December 2025 (stated as December 2025) | p. 3 |
| Context window | 256,000 tokens (stated as 256K tokens) | p. 1 |
| Maximum output | Not stated. The card does not state a maximum generated-output length. | — |
| Input modalities | Text (stated as Text) | p. 1 |
| Output modalities | Text (stated as Text) | p. 1 |
| Reasoning controls | Adaptive thinking. The card describes adaptive solution length rather than a user-set control. | pp. 2-3 |
| Effort levels | Not stated. The card names no user-selectable effort levels. | — |
| Tool use | Function calling. The benchmark method includes tool calls in the production Copilot harness but does not enumerate tool types. | p. 6 |
| Open weights | Not stated. The card does not state whether weights are open. | — |
| Architecture | Mixture of experts (stated as sparse Mixture-of-Experts layers) | p. 1 |
| Total parameters | 137 billion (stated as 137B total) | p. 1 |
| Active parameters | 5 billion (stated as 5B active) | p. 1 |

### Capability notes

- The model is a text-only coding assistant with a 256K-token context and sparse mixture-of-experts layers. (p. 1)
- Microsoft positions it for agentic coding in repositories, repository question answering, refactoring, code generation and completion, telemetry-grounded tasks, and tool use inside Copilot. (p. 2)
- Training starts from MAI-Thinking-1's mid-training checkpoint, then adds supervised tuning, about 2 million synthetic agentic tasks, and reinforcement learning over more than 150,000 environments. (p. 3)
- The card says all evaluation runs used the production GitHub Copilot harness for software engineering, repository question answering, refactoring, and telemetry-grounded tasks. (p. 3)
- Against Claude Haiku 4.5 in the card's coding table, MAI-Code-1-Flash leads on each listed pass rate, including SWE-Bench Pro at 51.2% versus 35.2%. (p. 5)
- The card also reports noncoding strengths, including 92.5% AIME 2026, 84.6% GPQA Diamond, and a 75.0 average on IF Bench. (p. 5)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| SWE-bench Verified | — | pass@1 | 71.6% | VS Code-based Copilot production harness; repository context, tool calls, and verification included; 10.8K average token usage | Claude Haiku 4.5 66.6% (27.3K average token usage) | p. 5 |
| SWE-bench Pro | — | pass@1 | 51.2% | VS Code-based Copilot production harness; 28.0K average token usage | Claude Haiku 4.5 35.2% (29.8K average token usage) | p. 5 |
| SWE-bench Multilingual | — | pass@1 | 65.5% | VS Code-based Copilot production harness; 15.3K average token usage | Claude Haiku 4.5 62.7% (17.2K average token usage) | p. 5 |
| Terminal-Bench 2.0 | — | success rate | 54.8% | VS Code-based Copilot production harness; Terminal Bench 2; 21.6K average token usage | Claude Haiku 4.5 41.6% (25K average token usage) | p. 5 |
| τ²-bench | Telecom | success rate | 71.7% | agentic tool use | Claude Haiku 4.5 54.7% | p. 6 |

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| AIME 2026 | — | accuracy | 92.5% | 23.6K average token usage | Claude Haiku 4.5 83.3% (30.3K average token usage) | p. 5 |
| Humanity's Last Exam | — | accuracy | 18% | academic reasoning, text; 26.3K average token usage | Claude Haiku 4.5 9.5% (22.2K average token usage) | p. 5 |
| GPQA Diamond | — | accuracy | 84.6% | biology, chemistry, and physics; 9.6K average token usage | Claude Haiku 4.5 73.2% (14.6K average token usage) | p. 5 |
| IFBench | — | score | 75.0 | average; precise instruction following | Claude Haiku 4.5 46.1 (average) | p. 5 |

## Safety findings

### Safety classification

- **Framework:** No safety framework stated
- **Overall determination:** Not stated

The card does not name a Microsoft safety framework or assign an overall safety level. It describes filtering, alignment training, cyber and secure-coding evaluations, and release checks with safety classifiers and filters.

The document states no per-domain determinations.

### Agentic-coding risks

- **Reward hacking** (not reported): The card reports no evaluation of reward hacking, grader gaming, or exploiting benchmark rubrics.
- **Test tampering** (not reported): The card reports no evaluation of modifying, deleting, or weakening tests during coding tasks.
- **Destructive or overeager actions** (not reported): The card reports no evaluation of irreversible or unrequested tool actions by the model.
- **Sabotage** (not reported): The card reports no sabotage, oversight-evasion, or deliberate underperformance evaluation.
- **Prompt injection** (not reported): The card describes tool-using workflows and safety filters but reports no prompt-injection or instruction-hierarchy test.
- **Honesty** (not reported): The card reports no honesty, deception, or false-claim-of-completion evaluation.
- **Sycophancy** (not reported): The card reports no sycophancy or user-pressure evaluation.

### Other safety findings

- Pretraining filters out or down-ranks harmful material to limit exposure during base-model learning. (p. 4)
- Later supervised and reinforcement-learning stages are described as alignment steps for safer and more helpful behavior. (p. 4)
- Microsoft names CyberBench, CyberSecEval, and SecRepo as security and secure-coding checks for threats, vulnerabilities, and secure-coding alignment. (p. 4)
- Release review used production model APIs with safety classifiers and filters, but the card does not publish numeric outcomes for those checks. (p. 4)

## Limitations and caveats

- The card documents text input only, so it provides no image-grounded behavior like the later MAI-Code-1.1-Flash card. (p. 1)
- Microsoft warns that generated text and code may be inaccurate, incomplete, or otherwise wrong, and calls for review, testing, and validation before consequential use. (p. 4)
- Safety reporting is qualitative: it names evaluation families and release controls but does not provide pass rates or thresholds. (p. 4)
- The launch distribution was VS Code only with CLI planned later, so the card's availability statements are historical rather than current-selection guidance. (pp. 2, 4)
- No maximum output length, open-weight status, prompt-injection result, honesty result, or sycophancy result is stated. (pp. 1, 4)

## Practical implications for Copilot users

### Choose it for

- **Historical comparison:** Use the card as the baseline for the MAI-Code Flash line: MAI-Code-1.1-Flash directly compares itself against these SWE-Bench Verified and Terminal Bench 2.1 rows. (p. 5)
- **Agentic coding:** For historical analysis of old outputs, the card reports 71.6% on SWE-Bench Verified, 51.2% on SWE-Bench Pro, and 54.8% on Terminal Bench 2 in a production Copilot harness. (pp. 5-6)
- **Terminal workflows:** Terminal Bench 2 is the terminal-specific result in the card, with 54.8% for MAI-Code-1-Flash versus 41.6% for Claude Haiku 4.5. (p. 5)

### Avoid it for

- **Vision:** The model summary lists text input only and gives no image benchmark results. (p. 1)
- **Untrusted input:** The card reports no prompt-injection test despite describing tool-using workflows and safety filters. (pp. 2, 4)
- **High-stakes domains:** Microsoft says outputs can be wrong and should be reviewed, tested, and validated before consequential use. (p. 4)

### Guidance

- GitHub retired MAI-Code-1-Flash from Copilot on 2026-09-10; the guidance below serves historical comparison and the lineage of later models.
- Do not carry MAI-Code-1.1-Flash image results backward to this model; the older card documents text input only.
- When comparing with MAI-Code-1.1-Flash, focus on shared rows such as SWE-Bench Verified and Terminal Bench 2.1 rather than unrelated benchmarks.
- Keep old generated changes under test and review because the card reports no reward-hacking, test-tampering, or prompt-injection checks.
- Treat launch availability statements as historical; the renderer's catalog status is the current source for retirement and Copilot availability.

## Document coverage

The six-page Microsoft card is dedicated to MAI-Code-1-Flash. Claude Haiku 4.5 is included only as the comparison model in the evaluation tables. The digest treats this model as a retired historical baseline for the MAI-Code Flash line and does not apply later MAI-Code-1.1-Flash image-input results to it.

- **Card type:** Dedicated. The document is about this model; it may include short sibling sections.
- **Pages specific to this model:** the whole document
- **Names the document uses for this model:** MAI-Code-1-Flash
- **Catalog scope:** Dedicated publisher card for this model.
