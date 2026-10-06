# GPT-5.6 Terra

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write gpt-5.6-terra`. -->

> Original digest of *GPT-5.6 System Card* (OpenAI, July 9, 2026; 82 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

**Copilot status** (catalog checked 2026-10-06): Current; GitHub release status GA. CLI: Yes. App model picker: listed. App reasoning efforts: none, low, medium, high, xhigh, max. App Auto: yes. App long-context option: yes.

## At a glance

GPT-5.6 Terra is OpenAI's middle GPT-5.6 family member in the July system card. It receives the same family Preparedness designations as Sol and Luna—High for biological/chemical risk and cybersecurity, below High for AI self-improvement—while many deep alignment, external cyber, and deployment-simulation results are Sol-only. Terra's own rows emphasize safety, prompt injection, HealthBench, destructive-action avoidance, and selected bio/cyber capability signals.

- **Choose it for:** Reviewed coding, debugging, and defensive triage where Terra's stronger-than-Luna rows are useful but Sol-only evidence is not required.
- **Watch out for:** Do not import Sol's external evaluations or August Sol/Luna checkpoint results; Terra has less long-horizon evidence.
- OpenAI gives Terra the same family-level Preparedness designations: High for biological/chemical risk and cybersecurity, below the High threshold for AI self-improvement, and below Critical by family assessment. (pp. 35-36, 47)
- Terra's own July rows include 0.37 on destructive-action avoidance plus correctness, 0.946 on prompt-injection search/function-calling accuracy, and 57.7 on HealthBench Professional. (pp. 11, 13, 15)
- For biology, Terra is the highest new July model on refusal-adjusted tacit-knowledge troubleshooting at 84.1%, above the 80% expert-consensus threshold used in the card. (p. 40)
- Cybersecurity High applies to Terra, but the Critical rule-out relies on Sol's harder testing plus Terra being smaller and less capable on proxy cyber evaluations. (p. 47)
- The July safeguard stack names Terra with Sol for activation classifiers and applies the shared topical-classifier and safety-reasoner monitor to all three GPT-5.6 models. (pp. 75-76)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The system card is dated 2026-07-09 but does not give a model release date. | — |
| Knowledge cutoff | Not stated. The card does not state a knowledge cutoff. | — |
| Context window | Not stated. The card does not state a context window. | — |
| Maximum output | Not stated. The card does not state a maximum output length. | — |
| Input modalities | Text, Image. The card evaluates text prompts and combined text-image inputs; it does not list every supported input type. | pp. 7, 10 |
| Output modalities | Text. The evaluated safety and robustness tasks score assistant text responses. | pp. 7, 10 |
| Reasoning controls | Effort levels (stated as reasoning effort). The card says results vary with the amount of thinking used, but does not enumerate served effort levels. | p. 3 |
| Effort levels | Not stated. The card names lowest deployment settings and maximum reasoning effort in places, but does not list product effort levels. | p. 3 |
| Tool use | Computer use, Function calling, Web search, Browser, Code execution, Terminal, File editing. These tools appear in evaluations: computer-use confirmations, function-calling/search prompt injection, file edits, browser/computer access, and terminal-like cyber harnesses. | pp. 11, 13, 23, 44, 49 |
| Open weights | Not stated. The card does not state whether weights are open. | — |
| Architecture | Not stated. The card identifies GPT-5.6 as a reasoning model family but does not state an architecture identifier. | — |
| Total parameters | Not stated. The card does not state a parameter count. | — |
| Active parameters | Not stated. The card does not state an active-parameter count. | — |

### Capability notes

- Terra is one of the three GPT-5.6 reasoning models and shares the family training and safety framework described in the system card. (pp. 2, 6)
- Terra retains much of Sol's health performance in July tables: 57.7 on HealthBench Professional, 57.0 on HealthBench, 32.7 on HealthBench Hard, and 95.1 on Consensus after length adjustment. (p. 15)
- OpenAI extends the High cybersecurity designation to Terra, while saying Terra is less capable overall than Sol in that domain. (p. 47)
- Terra exceeds GPT-5.5 on the internal CTF proxy but remains below Sol; the card gives no Terra numeric CTF score in the transcription. (p. 49)
- Terra has low CoT controllability similar to prior models, unlike Sol's higher controllability result, which OpenAI treats as a favorable safety signal. (p. 28)
- AI self-improvement sections group Terra with Sol on improved research debugging, NanoGPT, and PostTrainBench Lite performance, while the family stays below the High threshold. (pp. 58, 62, 65)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

The document reports no coding or agentic benchmark results for this model.

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Production Benchmarks | Self-harm | not-unsafe rate | 0.962 | July model; no system-level safeguards | GPT-5.5 0.917 (thinking; same table) | p. 7 |
| Image Input Safety | Self-harm | not-unsafe rate | 0.986 | Combined text-and-image disallowed-content cases | GPT-5.5 0.983 (same table) | p. 10 |
| Destructive Action Avoidance | Avoidance + correctness | safe response rate | 0.37 | Coding-style task with protected user data injected into the environment | GPT-5.5 0.44 (same table) | p. 11 |
| User Confirmations | General confirmation | accuracy | 0.94 | Computer-use confirmation-policy evaluation | GPT-5.5 0.94 (same table) | p. 12 |
| Prompt Injection | Connector attacks | accuracy | 1.0 | Known connector attacks | GPT-5.5 1.0 (same table) | p. 13 |
| Prompt Injection | Indirect prompt injection | attack success rate (lower is better) | 3.32% | GPT-Red agentic attacks | — | p. 14 |
| HealthBench Professional | — | score | 57.7% | Length-adjusted July score | GPT-5.5 51.8% (length-adjusted) | p. 15 |
| HealthBench | Hard | score | 32.7% | Length-adjusted July score | GPT-5.5 31.5% (length-adjusted) | p. 15 |
| Dynamic Mental Health Simulations | Self-harm | not-unsafe rate | 0.947 | Dynamic adversarial multi-turn simulations | GPT-5.5 0.868 (same table) | p. 16 |
| Tacit Knowledge and Troubleshooting | Refusal-adjusted | accuracy | 84.1% | Refusals and safe completions counted as successes | — | p. 40 |
| BioSecBench | Severe biology refusal | not-unsafe rate | 0.95 | Model-level biology refusal evaluation | GPT-5.5 0.958 (thinking; same table) | p. 74 |
| BioSecBench | Benign biology over-refusal | not-overrefuse rate | 0.978 | Benign advanced-biology prompts | GPT-5.5 0.917 (thinking; same table) | p. 74 |
| OpenAI cybersecurity safety evaluation | Production data | safe response rate | 0.987 | Model-level cybersecurity refusal evaluation | GPT-5.5 0.928 (same table) | p. 75 |

## Safety findings

### Safety classification

- **Framework:** OpenAI Preparedness Framework
- **Overall determination:** High for biological/chemical and cybersecurity; below High for AI self-improvement

OpenAI applies the same Preparedness designations to the GPT-5.6 family: High capability for biological/chemical risk and cybersecurity, below the High threshold for AI self-improvement, and not Critical for the tested biological and cyber pathways. (pp. 35-36, 47)

| Domain | Determination | Level | Finding | Source |
| --- | --- | --- | --- | --- |
| Biological and chemical | Threshold reached | High | All three GPT-5.6 models are treated as High capability for biological and chemical risk after three of four novice-uplift evaluations exceeded indicative thresholds; none of the critical biological evaluations exceeded threshold. | pp. 35-36 |
| Cybersecurity | Threshold reached | High | Sol is treated as High but below Critical in cybersecurity, and OpenAI extends that designation to Terra and Luna because they reach the High bar while remaining less capable than Sol on proxy cyber tests. | p. 47 |
| AI self-improvement | Below threshold | Below High | OpenAI says none of the GPT-5.6 models reach its High threshold for AI self-improvement. | p. 35 |

### Agentic-coding risks

- **Reward hacking** (sibling only): Sol has reported metagaming and cheating signals; the card does not report a Terra-specific reward-hacking or grader-gaming result. (pp. 30, 68-69)
- **Test tampering** (not reported): The card does not report Terra-specific test editing, deletion, or weakening behavior.
- **Destructive or overeager actions** (reported): Terra scores 0.81 on avoidance-only and 0.37 when correctness is also required in the destructive-action evaluation. (p. 11)
- **Sabotage** (sibling only): UK AISI sabotage testing is reported for Sol, not Terra. (pp. 68-69)
- **Prompt injection** (reported): Terra scores 1.000 on connector prompt-injection accuracy and 0.946 on search/function-calling accuracy; GPT-Red attack success is 0.061% direct and 3.32% indirect. (pp. 13-14)
- **Honesty** (not reported): The card does not report Terra-specific false-completion, deception, or honesty benchmark results.
- **Sycophancy** (not reported): The card reports no Terra sycophancy evaluation.
- **Malicious agentic use** (reported): Terra is covered by the cyber and biological model-level safety training tables, with cyber production refusal 0.987 and synthetic refusal 0.998. (p. 75)
- **Over-refusal** (reported): The biology table reports Terra benign not_overrefuse at 0.978 on low-risk advanced-biology workflows. (p. 74)

### Other safety findings

- Terra shares the family Preparedness result: High for biological/chemical and cybersecurity risk, below High for AI self-improvement. (pp. 35-36, 47)
- OpenAI says Terra and Luna are smaller and less capable than Sol on proxy cyber evaluations, so Sol's Critical cyber rule-out applies to them. (p. 47)
- Terra's GPT-Red prompt-injection attack-success rates are 0.061% for direct attacks and 3.32% for indirect attacks. (p. 14)
- Terra's biology refusal rows are 0.950 severe not_unsafe, 0.911 dual-use not_unsafe, and 0.978 benign not_overrefuse. (p. 74)
- Terra's cyber model-level refusal rows are 0.987 on production-derived data and 0.998 on synthetic data. (p. 75)
- The monitor stack uses activation classifiers for Terra and Sol, plus topical classifiers and a safety-reasoner monitor across the full GPT-5.6 family. (pp. 75-76)

## Limitations and caveats

- The family card reports many deeper sections only for Sol, including deployment simulations, external cyber and alignment evaluations, and detailed Critical cyber testing. (pp. 18-19, 55-56, 68-69)
- Disallowed-content and ChatGPT misalignment deployment-simulation forecasts were scoped to Sol only. (pp. 8, 17-18)
- Terra's Critical cyber conclusion relies partly on lower proxy capability relative to Sol, not a separate Terra VulnLMP campaign. (p. 47)
- Terra trails Sol on destructive-action avoidance plus correctness, 0.37 versus 0.44, which matters for edit-conflict workflows. (p. 11)
- OpenAI says capability evaluations are lower bounds because other scaffolds, longer rollouts, fine-tuning, or prompting could elicit more capability. (p. 35)

## Practical implications for Copilot users

### Choose it for

- **Debugging:** Terra is grouped with Sol as improving on internal research debugging and related AI self-improvement proxy tasks while staying below High for that domain. (pp. 58, 65)
- **Computer use:** Terra scores 0.98 on both financial and high-stakes communication confirmations and 0.94 on general confirmations. (p. 12)
- **Security work:** Terra reaches OpenAI's High cybersecurity designation, with human-led defensive use discussed in the safeguards section. (pp. 47, 75)

### Avoid it for

- **Long-horizon autonomy:** Sol-only deployment simulations carry the most detailed long-horizon agentic-risk evidence; Terra lacks those direct external results. (pp. 18-19, 68)
- **Untrusted input:** Indirect GPT-Red prompt-injection attack success is still 3.32%, so untrusted tool output or web content needs containment. (p. 14)
- **High-stakes domains:** The card gives benchmark and safeguard evidence, not validation for autonomous high-stakes decisions without human review. (pp. 15, 35)

### Guidance

- Use Terra when you want a balance between speed and reasoning depth, but do not need Sol's broader external-evaluation record.
- Review generated patches and run tests, especially when Terra edits existing workspaces; its combined destructive-action score is below Sol's.
- Keep retrieved content and tool output isolated from instructions, because prompt-injection attacks still succeed in a small share of tests.
- For advanced security work, keep tasks authorized and defensive and escalate chained exploit research to stricter human review.
- Do not cite August Sol or Luna rows as Terra behavior; the catalog lists no Terra supplement.

## Document coverage

The July GPT-5.6 system card covers Sol, Terra, and Luna. This digest uses Terra rows from family tables and family-level Preparedness findings that explicitly cover all three. Sol-only deployment simulations, external evaluations, and Critical cyber rule-out work are treated as scope limits rather than Terra evidence. The August update covers Sol and Luna only and is not cited for Terra.

- **Card type:** Family. The document covers several models in its main body and attributes results per model.
- **Pages specific to this model:** not separated by page
- **Names the document uses for this model:** GPT-5.6 Terra, Terra, gpt-5.6-terra
- **Catalog scope:** The GPT-5.6 System Card covers the Sol, Terra, and Luna family members. The August update does not cover Terra.
