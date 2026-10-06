# GPT-6 Luna

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write gpt-6-luna`. -->

> Original digest of *GPT-6 Astra System Card* (OpenAI, September 3, 2026; 175 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

**Copilot status** (catalog checked 2026-10-06): Current; GitHub release status GA. CLI: Yes. App model picker: listed. App reasoning efforts: none, low, medium, high, xhigh, max. App Auto: yes. App long-context option: yes.

## At a glance

GPT-6 Luna has appendix coverage beside GPT-6 Sol. Appendix A reports no public coding benchmarks such as SWE-bench or Terminal-Bench; its coding-relevant evidence is OpenAI-run AI self-improvement work, where Luna scores 46.62% on research debugging and 21.83% on KernelGen 1P. OpenAI treats Luna as High in cybersecurity and biological/chemical capability, below Critical in cyber, and below High in self-improvement, while omitting several Luna-specific monitorability and deployment-simulation measurements it gives for Sol.

- **Choose it for:** Well-scoped agentic coding, security-adjacent, or AI R&D-style help where a smaller GPT-6 model is enough and visible verification stays in place.
- **Watch out for:** Luna lacks Sol's CoT-controllability and Codex deployment-simulation details, public coding benchmarks are absent, and some robustness may reflect broader refusals.
- OpenAI treats Luna as High capability for cybersecurity and biological/chemical domains, below High for AI self-improvement, and below Critical for cybersecurity. (pp. 120, 144, 146, 151)
- Appendix A reports no public coding benchmark rows such as SWE-bench or Terminal-Bench for Luna; its coding-relevant AI self-improvement values are 46.62% research debugging and 21.83% KernelGen 1P. (pp. 151-153)
- Appendix A links both smaller GPT-6 models back to Astra for their training-data and training-method description, while most methods remain in the main body. (p. 120)
- Prompt-injection instruction-hierarchy robustness is 99.97%, but the appendix provides only the instruction-hierarchy table as text; indirect-prompt chart values are not transcribed. (pp. 124-125)
- Luna is safer in the external-message test than Sol: board discovery is 76%, with no observed communication attempts and no unauthorized actions. (pp. 132-133)
- Luna trails Sol on automated cyber capability results: 43.4% ExploitBench, 34.2% SEC-Bench Pro, 11.6% ExploitGym, and one of 22 Sandbox Bench targets. (pp. 147-149, 151)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. Appendix A was added in the card change log after the original card date, but it does not state a separate release date for this model. | — |
| Knowledge cutoff | Not stated. Appendix A links Sol and Luna back to Astra for training-data and training-method description, but no knowledge cutoff is stated. | p. 120 |
| Context window | Not stated. Appendix A does not state a context window. | — |
| Maximum output | Not stated. Appendix A does not state a maximum output length. | — |
| Input modalities | Not stated. Appendix A reports text, agentic, and image-input safety evaluations but does not list supported modalities. | pp. 120, 123 |
| Output modalities | Not stated. Appendix A does not list output modalities. | — |
| Reasoning controls | Effort levels. Appendix evaluations repeatedly use maximum reasoning effort, but the appendix does not list the full control surface. | pp. 129-130 |
| Effort levels | max. Maximum reasoning effort is named in Appendix A evaluations; this is not a complete list of product effort options. | pp. 129-130 |
| Tool use | Browser, Computer use, File editing. Appendix A reports Codex, Chat Plugins, simulated browsing, and agentic cyber evaluations; tool support is described through evaluation harnesses, not as a product feature list. | pp. 122, 132-133, 147 |
| Open weights | Not stated. The appendix does not say the weights are open. | — |
| Architecture | Not stated. The appendix does not state an architecture. | — |
| Total parameters | Not stated. The appendix does not state a parameter count. | — |
| Active parameters | Not stated. The appendix does not state active parameters. | — |

### Capability notes

- Appendix A ties Luna to Astra for training inputs and training method, but it does not publish Luna-specific architecture, size, context, or output-limit details. (p. 120)
- OpenAI treats Luna as High in cybersecurity and biological/chemical capability, below Critical in cyber, and below High in AI self-improvement. (pp. 120, 144, 146, 151)
- Luna is below Sol on the automated cyber capability results reported in text, including ExploitBench, SEC-Bench Pro, and ExploitGym. (pp. 147-149)
- On HealthBench Professional, Luna reaches 60.8 length-adjusted, up 5.1 from GPT-5.6 Luna, while HealthBench and HealthBench Hard regress with shorter answers. (p. 126)
- In the external-agent-message test, Luna found the board less often than other models and had no observed communication attempts or specified unauthorized actions. (pp. 132-133)
- The appendix omits Luna from CoT-controllability testing, leaving no Luna-specific number for that monitorability concern. (p. 137)
- Appendix A gives Luna chart values for research debugging and KernelGen 1P, but it does not give Luna-specific MLE-Bench Revised, NanoGPT, or PostTrainBench Lite values. (pp. 151-153)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| OpenAI research debugging evaluation | — | mean reward | 46.62% | research-debugging agent evaluation; 41 real research bugs plus 6 alignment-auditing tasks; chart reports mean rubric reward. Appendix A says Sol and Luna stay below the High threshold for AI self-improvement. | GPT-6 Astra 78.05% (same figure); GPT-6 Sol 64.2% (same figure); GPT-5.6 Sol 68.32% (same figure); GPT-5.6 Luna 50.8% (same figure) | pp. 151-152 |
| KernelGen 1P | — | mean reward | 21.83% | kernel-development environment with correctness and performance tests; OpenAI first-party hardware kernels; chart reports mean rubric reward | GPT-6 Astra 66.72% (same figure); GPT-6 Sol 38.12% (same figure); GPT-5.6 Sol 61.08% (same figure); GPT-5.6 Luna 22.4% (same figure) | pp. 152-153 |

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Production Benchmarks | Non-violent illicit behavior | safe response rate | 0.997 | challenging production-derived prompts | GPT-5.6 Luna 0.993 (same category); GPT-6 Astra 0.997 (same category); GPT-6 Sol 0.993 (same category) | p. 120 |
| Under-18 Safety | Eating disorders | safe response rate | 0.871 | teen-specific safety protections | GPT-5.6 Luna 0.702 (same category); GPT-6 Astra 0.921 (same category); GPT-6 Sol 0.853 (same category) | p. 122 |
| Agentic Safe Completions | Codex prod - Non-violent Wrongdoing | safe response rate | 1.0 | Codex prod; action-level safety in agentic requests | GPT-5.6 Sol 0.906 (same row); GPT-6 Astra 0.954 (same row); GPT-6 Sol 0.99 (same row) | p. 122 |
| OpenAI static jailbreak evaluations | Cyber | safe response rate | 87.5% | defender success rate; 95% interval 83.8-90.5 | GPT-5.6 Sol 59.0% (same prompts); GPT-6 Astra 91.5% (same prompts); GPT-6 Sol 79.8% (same prompts) | p. 123 |
| Instruction Hierarchy | — | success rate | 99.97% | defender success rate averaged per defender query | GPT-6 Astra 99.99% (same table); GPT-6 Sol 99.97% (same table) | p. 125 |
| HealthBench Professional | Length-adjusted | score | 60.8 | unadjusted 61.2; mean response length 2,119 characters | GPT-5.6 Luna 55.7 (length-adjusted); GPT-6 Astra 64.7 (length-adjusted); GPT-6 Sol 60.8 (length-adjusted) | p. 126 |
| OpenAI external agent messages | Specified unauthorized action | misbehavior rate (lower is better) | 0.0% | simulated local message board; 0 communication attempts and 0 specified unauthorized actions; board discovery 76%; Figure 66 label | GPT-5.6 Sol 51.9% (specified unauthorized action; Figure 66 label); GPT-6 Astra 0.0% (specified unauthorized action; Figure 66 label); GPT-6 Sol 11.25% (specified unauthorized action; Figure 66 label) | pp. 132-133 |
| Multimodal Troubleshooting Virology | — | pass@1 | 49.1% | High threshold 31% | GPT-6 Sol 50.6% (same table) | p. 145 |
| ExploitBench | — | score | 43.4% | max effort; automated cyber evaluation; known vulnerabilities; possible historical-exposure caveat | GPT-6 Sol 81.7% (max) | p. 147 |
| SEC-Bench Pro | — | score | 34.2% | automated cyber evaluation; large JavaScript engines | GPT-6 Astra 85.4% (same text); GPT-6 Sol 66.3% (same text) | p. 148 |
| ExploitGym | — | success rate | 11.6% | automated cyber evaluation; working exploits on challenges | GPT-6 Sol 22.1% (same text); GPT-5.6 Sol 30.3% (higher maximum using more tokens) | p. 149 |
| Sandbox Bench | — | count | 1 | CTF-style sandbox challenges; 1 of 22 targets; one runtime target and no parser or proxy target | GPT-6 Astra 10 (10 of 22 targets); GPT-6 Sol 1 (1 of 22 targets); GPT-5.6 Sol 1 (1 of 22 targets) | p. 151 |
| OpenAI biology model refusal evaluation | Severe | safe response rate | 0.985 | model response only; full safeguards not included | GPT-5.6 Luna 0.946 (same row); GPT-6 Astra 0.998 (same row); GPT-6 Sol 0.998 (same row) | p. 154 |
| OpenAI cybersecurity safety evaluation | Production Chat | safe response rate | 0.951 | model response only; full safeguards not included | GPT-5.6 Luna 0.986 (same row); GPT-6 Astra 0.97 (same row); GPT-6 Sol 0.957 (same row) | p. 154 |

## Safety findings

### Safety classification

- **Framework:** OpenAI Preparedness Framework
- **Overall determination:** High in Cybersecurity and Biological and Chemical; below High in AI Self-Improvement; below Critical in Cybersecurity

Appendix A states that OpenAI treats Luna as High capability in cybersecurity and biological/chemical domains, below High for AI self-improvement, and below Critical in cybersecurity. Critical biology testing was not required because Luna scored below GPT-5.6 Sol on all High evaluations. (pp. 120, 144)

| Domain | Determination | Level | Finding | Source |
| --- | --- | --- | --- | --- |
| Cybersecurity | Standard applied | High; below Critical | Luna is treated as High in cybersecurity but remains below Critical after automated evaluations where it underperforms Sol. | pp. 144, 146 |
| Biological and chemical | Standard applied | High; Critical not required | Luna is treated as High in biological and chemical capability; separate Critical testing was not required because it trailed the GPT-5.6 Sol baseline across the High evaluations. | pp. 144-145 |
| AI self-improvement | Below threshold | Below High | OpenAI states that Sol and Luna do not reach the High threshold for AI self-improvement. | pp. 144, 151 |

### Agentic-coding risks

- **Reward hacking** (not reported): Appendix A does not report Luna-specific reward-hacking or grader-gaming measurements.
- **Test tampering** (not reported): Appendix A does not report Luna editing, deleting, or weakening tests.
- **Destructive or overeager actions** (reported): Luna has no observed communication attempts and no specified unauthorized actions in the external-agent-message test, and it makes no honeypot exploit attempts. (pp. 130, 132-133)
- **Sabotage** (sibling only): Appendix A reports OAI-repo Sabotage v2 for Sol, but does not give a Luna sabotage or monitor-evasion result. (p. 140)
- **Prompt injection** (reported): Luna reaches 99.97% instruction-hierarchy defender success, and Appendix A says prompt-injection and hierarchy robustness improved over predecessors. (pp. 124-125)
- **Honesty** (reported): Luna improves over GPT-5.6 Luna on coding deception by more than 3x and on the broken-search-tool failure rate by nearly 3x, though exact Luna rates are figure-only. (pp. 131-132)
- **Sycophancy** (not reported): Appendix A does not report a Luna sycophancy evaluation.
- **Evaluation awareness** (sibling only): Appendix A reports evaluation-awareness rates for Sol's Codex simulation, but not for Luna. (p. 136)
- **Reasoning monitorability** (sibling only): Appendix A explicitly omits Luna from CoT-controllability evaluations, so Sol's 23.2% value does not apply to Luna. (p. 137)
- **Malicious agentic use** (reported): Luna scores 1.000 on Codex non-violent wrongdoing, 0.960 on Codex self-harm, and 0.957 on human red-teaming for Codex in the agentic safe-completion table. (p. 122)
- **Over-refusal** (reported): Appendix A cautions that some Luna jailbreak robustness may come from a broader tendency to refuse requests, and its benign biology not-overrefuse score is 0.958. (pp. 124, 154)

### Other safety findings

- Static jailbreak robustness improves over earlier models: Luna reaches 73.8% on bio high-risk, 73.0% on bio severe, 89.3% on severe violence, and 87.5% on cyber. (p. 123)
- Luna's biology refusal safety is 0.985 on severe prompts and 0.962 on dual-use prompts, with a benign not-overrefuse score of 0.958. (p. 154)
- Cybersecurity safety scores are 0.951 for production chat, 0.997 for synthetic agentic environments, and 0.987 for semi-synthetic agentic environments. (p. 154)
- OpenAI says Luna's stronger jailbreak scores may partly reflect a wider refusal tendency, so robustness and helpfulness need to be read together. (p. 124)
- Luna is not separately Critical-tested for biological capability because it is below GPT-5.6 Sol on all High biological evaluations. (p. 145)

## Limitations and caveats

- Luna's public coverage is an appendix, and method details are mostly inherited from the Astra main body rather than restated for Luna. (pp. 120, 153-154)
- The appendix does not state Luna's context window, maximum output, architecture, parameters, exact modalities, or full reasoning-effort list. (p. 120)
- No Luna-specific Codex deployment-simulation rate is reported, unlike Sol's 42 severe flags among 50,319 tasks. (pp. 133-134)
- Luna is omitted from CoT-controllability evaluations, leaving no Luna-specific monitorability number for that concern. (p. 137)
- HealthBench regressions are difficult to interpret because Luna's answers are shorter than the length ranges used to calibrate the penalties. (p. 126)
- Automated cyber capability is lower than Sol's across ExploitBench, SEC-Bench Pro, and ExploitGym, and Sandbox Bench records only one target. (pp. 147-149, 151)

## Practical implications for Copilot users

### Choose it for

- **Agentic coding:** Luna has strong agentic safe-completion rows and no observed unauthorized action in the external-agent-message test, making it plausible for bounded agent tasks with visible review. (pp. 122, 132-133)
- **Untrusted input:** Luna reaches 99.97% instruction-hierarchy defender success and has no specified unauthorized actions in the external-message evaluation, though this is not a full prompt-injection guarantee. (pp. 125, 132-133)
- **Code review:** The appendix reports improvements on coding deception and broken-search behavior against the GPT-5.6 Luna baseline, supporting review-style tasks where claims are checked. (pp. 131-132)

### Avoid it for

- **Long-horizon autonomy:** The appendix omits Luna-specific Codex deployment-simulation and CoT-controllability results, so long autonomous runs have less evidence than Sol or Astra. (pp. 133, 137)
- **Security work:** For advanced exploit-heavy work, Luna trails Sol on ExploitBench, SEC-Bench Pro, ExploitGym, and Sandbox Bench while still being a High cyber-capability model. (pp. 146-149, 151)
- **High-stakes domains:** Luna is High in cyber and biological/chemical capability, has HealthBench regressions on two variants, and lacks the detailed main-body evidence Astra receives. (pp. 126, 144)

### Guidance

- Use Luna for smaller, bounded Copilot tasks with tests and review; do not infer long-run safety from missing Luna-specific monitorability data.
- Keep approvals around external messages, privileged operations, and deployments even though the appendix reports no observed external-message unauthorized actions for Luna.
- For security tasks, prefer tightly scoped defensive requests and review outputs carefully; the appendix treats Luna as High cyber capability but lower than Sol on exploit benchmarks.
- Copilot offers Luna in Auto, the CLI, the app picker, low through max reasoning efforts plus none, and a long-context option; pin the effort when comparing runs.
- If refusals or terse answers reduce usefulness, ask for explicit assumptions, tests, and edge cases rather than broadening permissions.

## Document coverage

GPT-6 Luna is covered in Appendix A, page-marker pages 120-154, of the GPT-6 Astra System Card. This digest uses Luna-specific rows and Appendix A family statements for Sol and Luna; it does not borrow Sol-only monitorability or deployment-simulation numbers, and it uses main-body pages only for shared methods the appendix points back to.

- **Card type:** Appendix. This model is covered in an appendix or section of a sibling model's document.
- **Pages specific to this model:** pp. 120-154
- **Names the document uses for this model:** GPT-6 Luna
- **Catalog scope:** Appendix A, "GPT-6 Sol, GPT-6 Luna", of the GPT-6 Astra System Card (begins on PDF page 119).
- **Catalog note:** No standalone GPT-6 Luna card exists; the GPT-6 Astra card covers it in Appendix A.
