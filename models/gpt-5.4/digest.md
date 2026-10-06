# GPT-5.4

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write gpt-5.4`. -->

> Original digest of *GPT-5.4 Thinking System Card* (OpenAI, March 5, 2026; 38 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

**Copilot status** (catalog checked 2026-10-06): Current; GitHub release status GA. CLI: Yes. App model picker: listed. App reasoning efforts: none, low, medium, high, xhigh. App Auto: no. App long-context option: yes.

## At a glance

GPT-5.4 is OpenAI's GPT-5.4 Thinking model, a reasoning model whose main card emphasizes cyber safeguards, prompt-injection testing, and workspace-safety evaluations. OpenAI treats it as High in biological and chemical capability and precautionarily High in cybersecurity, while AI self-improvement remains below High. Its strongest decision signal is cautious agentic use: good cyber and coding-proxy scores, but incomplete evidence for long autonomous coding safety.

- **Choose it for:** Sustained debugging, architecture, and scoped agentic coding where stronger reasoning matters and reviewers can check file and command effects.
- **Watch out for:** Cyber capability is treated as High, prompt-injection tests are training splits, and workspace reversion is far from perfect.
- OpenAI calls GPT-5.4 Thinking a reasoning model and says it is the first general-purpose model in this series launched with mitigations for High cybersecurity capability. (p. 4)
- Agentic workspace safety improved over GPT-5.2-Codex but remained imperfect: destructive-action avoidance was 0.86, perfect reversion 0.18, and user-work preservation 0.53. (p. 10)
- Prompt-injection scores were strong on known attacks—0.998 for connectors and 0.978 for function calls—but both evaluated splits came from training data. (pp. 8-9)
- Preparedness treatment is High for biological/chemical risk and precautionary High for cybersecurity; AI self-improvement is below High. (pp. 16, 20, 26)
- On coding and AI-R&D proxies, Monorepo-Bench was 59.33% pass@1, MLE-Bench 23.33% pass@1, and OpenAI-Proof Q&A 4.16% pass@1. (pp. 27-28)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The system card is dated March 5, 2026 and says the appendix was added March 17, but it does not state a GPT-5.4 release date. | — |
| Knowledge cutoff | Not stated. The card describes training-data sources but gives no knowledge cutoff. | — |
| Context window | Not stated. The card mentions compaction at 100K tokens during an external cyber evaluation, not a serving context window. | — |
| Maximum output | Not stated | — |
| Input modalities | Text, Image (stated as combined text and image input). The vision safety evaluation uses combined text and image prompts; the card does not list a formal modality table. | p. 9 |
| Output modalities | Text (stated as model output). The card discusses responses and outputs; it does not report audio, image, or video output. | pp. 5, 9 |
| Reasoning controls | Always reasons (stated as reasoning model). The document says the model reasons before answering but does not describe a caller-selectable control. | p. 4 |
| Effort levels | xhigh (stated as xhigh reasoning effort). Only xhigh is named for the Irregular cyber evaluation; the card does not list all serving effort levels. | p. 25 |
| Tool use | Terminal, Code execution, File editing, Computer use (stated as headless Linux box; command-line tools and Python). Tool use appears in evaluated computer-use, cyber, coding, and research-debugging harnesses rather than as an API feature list. | pp. 11, 22, 26, 28 |
| Open weights | Not stated | — |
| Architecture | Not stated | — |
| Total parameters | Not stated | — |
| Active parameters | Not stated | — |

### Capability notes

- The card frames GPT-5.4 Thinking as a GPT-5-series reasoning model that uses reinforcement learning to deliberate before responding and better follow task and safety policy. (p. 4)
- For computer-use deployments, OpenAI moved confirmation behavior into platform and developer policy layers and trained the model to follow those instructions for high-risk actions. (p. 11)
- It shows stronger handling of long workspace rollouts than earlier baselines, especially in preserving simulated user changes while attempting to revert its own work. (p. 10)
- Cyber capability is the card's central deployment change: the model meets canary thresholds across CTF, CVE-Bench, Cyber Range, and external Irregular testing. (pp. 20, 25-26)
- AI self-improvement remains below High even though the model leads the compared set on Monorepo-Bench and MLE-Bench in the card's charts. (pp. 26-28)
- HealthBench is mixed versus GPT-5.2: lower overall and hard scores, higher consensus score, and longer average answers. (p. 10)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Monorepo-Bench | — | pass@1 | 59.33% | command-line tools and Python; hidden unit tests | GPT-5.2 Thinking 56.7%; GPT-5.2-Codex 54.67%; GPT-5.3-Codex 56% | p. 27 |
| MLE-bench | — | pass@1 | 23.33% | 30 Kaggle competitions; bronze-medal threshold. The card does not report GPT-5.3-Codex because of infrastructure issues. | GPT-5.2 Thinking 12.2%; GPT-5.2-Codex 10.0% | p. 28 |
| OpenAI-Proof Q&A | — | pass@1 | 4.16% | 20 research and engineering bottlenecks | GPT-5.2 Thinking 4.2%; GPT-5.2-Codex 8.33%; GPT-5.3-Codex 5.8% | p. 28 |

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Production Benchmarks | Non-violent illicit behavior | not-unsafe rate | 1.0 | Difficult production-derived prompts; not representative of normal traffic. | GPT-5.1 Thinking 0.837; GPT-5.2 Thinking 0.923 | p. 5 |
| Dynamic Mental Health Simulations | Mental health | not-unsafe rate | 0.985 | — | GPT-5.1 Thinking 0.753; GPT-5.2 Thinking 0.975 | pp. 5-6 |
| Prompt Injection | Connector attacks | accuracy | 0.998 | Training-data split; not evidence for novel attack families. | GPT-5.1 Thinking 0.781; GPT-5.2 Thinking 0.979 | pp. 8-9 |
| Prompt Injection | Function-call attacks | accuracy | 0.978 | Training-data split; slightly lower than GPT-5.2 Thinking. | GPT-5.1 Thinking 1.0; GPT-5.2 Thinking 0.996 | pp. 8-9 |
| HealthBench | Overall | score | 62.6% | Average response length was 3311 characters. | GPT-5.2 Thinking 63.3% | p. 10 |
| Destructive Action Avoidance | Destructive-action avoidance | score | 0.86 | — | GPT-5.2-Codex 0.76; GPT-5.3-Codex 0.88 | p. 10 |
| Destructive Action Avoidance | User work preserved | score | 0.53 | — | GPT-5.2-Codex 0.18; GPT-5.3-Codex 0.08 | p. 10 |
| User Confirmations | General confirmation | score | 0.94 | — | GPT-5.2 Thinking 0.94; GPT-5.3-Codex 0.91 | p. 11 |
| CoT Controllability | 10k-character CoTs | success rate (lower is better) | 0.3% | Lower controllability is the safer direction in OpenAI's framing. | GPT-5.2 Thinking 0.2% | pp. 15-16 |
| Capture the Flag (Professional) | — | pass@12 | 88.23% | headless Linux box; 16 rollouts; professional CTFs | GPT-5.2 Thinking 82.4%; GPT-5.2-Codex 88.1%; GPT-5.3-Codex 88.2% | p. 22 |
| CVE-Bench | — | pass@1 | 86.27% | 34 of 40 tasks; zero-day prompt; no source-code access; 3 rollouts | GPT-5.2 Thinking 67.6%; GPT-5.2-Codex 85.29%; GPT-5.3-Codex 90.2% | p. 23 |
| Cyber Range | — | success rate | 73.33% | 15 scenarios; pass if at least one of 16 trials succeeds | GPT-5.2 Thinking 47%; GPT-5.2-Codex 53.33%; GPT-5.3-Codex 80% | pp. 24-25 |

## Safety findings

### Safety classification

- **Framework:** OpenAI Preparedness Framework
- **Overall determination:** High in Biological/Chemical and Cybersecurity; below High in AI self-improvement

OpenAI continues High biological and chemical treatment for GPT-5.4 Thinking, treats cybersecurity as High because canary thresholds are met, and concludes AI self-improvement does not plausibly reach High. (pp. 16, 20, 26)

| Domain | Determination | Level | Finding | Source |
| --- | --- | --- | --- | --- |
| Biological and chemical | Threshold reached | High | OpenAI treats the launch as High in Biological and Chemical and applies the corresponding safeguards. | pp. 16-17 |
| Cybersecurity | Precautionary | High | OpenAI treats GPT-5.4 Thinking as Cyber High because canary thresholds are met, even while it says real-world High capability is uncertain. | p. 20 |
| AI self-improvement | Below threshold | Below High | Final-checkpoint evaluations rule out the mid-career research-engineer threshold used for AI self-improvement High. | pp. 16, 26 |

### Agentic-coding risks

- **Reward hacking** (not reported): The card does not report an evaluation of reward hacking or grader gaming.
- **Test tampering** (not reported): The card does not report whether the model edits, deletes, or weakens tests to pass.
- **Destructive or overeager actions** (reported): Workspace-safety tests report 0.86 destructive-action avoidance, 0.18 perfect reversion, and 0.53 user-work preservation. (p. 10)
- **Sabotage** (reported): Apollo reports a 0.56 mean sabotage score and says the model can execute steps for sabotage in simple simulated tasks, without proving realistic concealment. (p. 29)
- **Prompt injection** (reported): Known prompt-injection attacks score 0.998 for connectors and 0.978 for function calls, but both splits overlap the training setup. (pp. 8-9)
- **Honesty** (reported): Apollo reports about a 1% no-nudge deception rate and no observed covert developer subversion across tested scenarios. (p. 29)
- **Sycophancy** (not reported): The card does not report a sycophancy evaluation.
- **Evaluation awareness** (reported): Apollo found 21.3% evaluation awareness in chain-of-thought samples, higher than prior tested models. (p. 29)
- **Sandbagging** (reported): Apollo observed a 6-percentage-point accuracy drop only when the model was given an explicit goal to underperform; no such behavior appeared without that goal. (p. 29)
- **Malicious agentic use** (reported): Cyber safety training scores were 0.978 on deidentified production data and 0.987 on synthetic data before the monitor and enforcement layers. (p. 31)

### Other safety findings

- Disallowed-content results are broadly near GPT-5.2 Thinking, with gains on nonviolent illicit requests and self-harm but lower scores on harassment, violence, and sexual categories. (p. 5)
- The representative-prompt pilot measures only model-layer behavior on a point-in-time distribution, so OpenAI expects deployed rates to be lower after other safety layers. (pp. 6-7)
- CoT monitorability is slightly better than GPT-5.2 Thinking but lower than GPT-5 Thinking on average, with Anti-Scheming and Memory regressions treated as partly evaluation-limited. (pp. 12-13)
- Cyber Range is necessary but insufficient evidence: it lacks hardened targets, realistic defenders, and many distractions seen in real environments. (p. 21)
- Irregular reported 88% Network Attack Simulation, 73% Vulnerability Research and Exploitation, 48% Evasion, and 11% average CyScenarioBench success. (pp. 25-26)
- Cyber safeguards combine model training, message-level monitoring, account-level enforcement, Trusted Access for Cyber, and security controls around model assets. (pp. 29-32)

## Limitations and caveats

- The hard disallowed-content benchmark was built from difficult prior failures, so its error rates should not be read as normal traffic rates. (p. 5)
- Representative-prompt estimates are time-bound, model-layer-only, and affected by distribution drift and reconstruction limits. (p. 6)
- Prompt-injection results cover known connector and function-call attacks from training splits, not unseen attack families. (pp. 8-9)
- HealthBench analysis flags poorer context seeking when important information may be missing. (p. 10)
- Preparedness tests are lower bounds because new prompting, scaffolds, longer rollouts, fine-tuning, or interactions could elicit stronger behavior. (p. 17)
- GPT-5.4 Thinking fails four Cyber Range scenarios and is below GPT-5.3-Codex on the suite's combined pass rate. (p. 25)
- OpenAI says it lacks evidence of GPT-5.4-specific internal misalignment propensities, but High cyber capability still raises internal-deployment stakes. (pp. 32-33)

## Practical implications for Copilot users

### Choose it for

- **Debugging:** Reasoning-model training and the Monorepo, MLE-Bench, and OPQA results support hard debugging and research-style diagnosis with review. (pp. 4, 27-28)
- **Agentic coding:** The card evaluates command-line code changes and reports improved, though imperfect, workspace-state handling during long rollouts. (pp. 10, 26-27)
- **Security work:** Cyber capability is strong and explicitly safeguarded for legitimate defensive acceleration, while the model is treated as High risk. (pp. 20, 29, 31)

### Avoid it for

- **Untrusted input:** Prompt-injection scores are based on known training-data splits, so novel malicious repository, connector, or tool content remains under-tested. (pp. 8-9)
- **Long-horizon autonomy:** Workspace recovery and user-change preservation remain incomplete, and OpenAI has limited evidence on long-range autonomy risk. (pp. 10, 33)
- **High-stakes domains:** HealthBench is mixed, biology and cyber are treated as High-risk domains, and the card repeatedly frames evaluations as bounded evidence. (pp. 10, 16-17, 20)

### Guidance

- Use xhigh only when the extra reasoning is worth slower interaction; the card names xhigh in cyber testing, while Copilot offers none through xhigh for this model.
- Protect user edits and require review for file deletion, reversion, and cleanup because the reversion scores are far from perfect.
- Keep cyber tasks defensive and authorized; the card treats the model as Cyber High even with safeguards.
- Treat connector, issue, log, and repository text as untrusted because the prompt-injection tests are not novel-attack evidence.
- For long Copilot agent runs, provide explicit boundaries, ask for tests, and review the final diff rather than trusting task-completion claims.

## Document coverage

The digest covers the GPT-5.4 Thinking main body. It cites page 33 only for the final main-body deployment-risk paragraph and does not use the GPT-5.4 mini appendix as GPT-5.4 evidence. The appendix tables name GPT-5.4 Thinking as a comparator, but this digest uses main-body tables and rendered charts for this model's own results.

- **Card type:** Dedicated. The document is about this model; it may include short sibling sections.
- **Pages specific to this model:** pp. 4-33
- **Names the document uses for this model:** GPT-5.4 Thinking, gpt-5.4-thinking
- **Catalog scope:** GPT-5.4 Thinking; GitHub's model comparison links this card for GPT-5.4.
