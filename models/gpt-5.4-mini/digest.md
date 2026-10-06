# GPT-5.4 mini

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write gpt-5.4-mini`. -->

> Original digest of *GPT-5.4 Thinking System Card* (OpenAI, March 5, 2026; 38 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

**Copilot status** (catalog checked 2026-10-06): Current; GitHub release status GA. CLI: Yes. App model picker: listed. App reasoning efforts: none, low, medium, high, xhigh. App Auto: no. App long-context option: no.

## At a glance

GPT-5.4 mini is documented only in an appendix to the GPT-5.4 Thinking card, so the evidence is narrower than a full system card. The appendix reports disallowed-content, mental-health, CoT-controllability, Preparedness, biology, cyber, and AI self-improvement measurements. OpenAI concludes the mini model is below High across biological/chemical, cybersecurity, and AI self-improvement domains.

- **Choose it for:** Scoped coding or defensive-security tasks where the appendix's Monorepo, CTF, and CVE-Bench scores are enough evidence and stronger models are unnecessary.
- **Watch out for:** Do not import GPT-5.4 Thinking main-body results; the mini appendix omits destructive-action, prompt-injection, and broader capability tests.
- Section 6 is the GPT-5.4 mini appendix and says it was added for the mini launch; it is not a standalone card. (p. 33)
- OpenAI determines GPT-5.4 mini is below High capability in biochemical, cybersecurity, and AI self-improvement domains. (p. 34)
- Appendix coding and cyber proxies are nontrivial: 54.00% on Monorepo-Bench, 81.32% pass@12 on CTF, and 83.33% pass@1 on CVE-Bench. (p. 36)
- Biology comparisons do not justify Bio High: raw scores are 46.5% on multimodal virology, 33.64% on ProtocolQA, 71.67% on tacit knowledge, and 31.91% on TroubleshootingBench. (pp. 35-36)
- CoT controllability is described as lower than any previously reported OpenAI model in the suite, but the appendix gives no numeric mini value in text. (pp. 33-34)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The appendix says it was added March 17, 2026 for the launch, but it does not state a release date as a fact field. | — |
| Knowledge cutoff | Not stated. The appendix does not state a knowledge cutoff for GPT-5.4 mini. | — |
| Context window | Not stated | — |
| Maximum output | Not stated | — |
| Input modalities | Not stated. The appendix reports selected evaluations but does not list GPT-5.4 mini input modalities. | — |
| Output modalities | Not stated. The appendix does not list GPT-5.4 mini output modalities. | — |
| Reasoning controls | Not stated. The appendix discusses CoT controllability but not any serving control for reasoning. | — |
| Effort levels | Not stated. No effort levels are stated for GPT-5.4 mini in the appendix. | — |
| Tool use | Not stated. The appendix reports CTF, CVE-Bench, Monorepo-Bench, and OPQA scores but does not describe the mini model's tool harnesses. | — |
| Open weights | Not stated | — |
| Architecture | Not stated | — |
| Total parameters | Not stated | — |
| Active parameters | Not stated | — |

### Capability notes

- OpenAI documents GPT-5.4 mini in Section 6 of the GPT-5.4 Thinking card, with selected safety and Preparedness measurements instead of a full model description. (p. 33)
- Disallowed-content results are reported alongside GPT-5.4 Thinking, including 0.992 for violent illicit behavior and 1.000 for nonviolent illicit behavior. (p. 33)
- Dynamic adversarial simulations show high not-unsafe rates for mini: 0.985 mental health, 0.977 emotional reliance, and 0.980 self-harm. (p. 33)
- The appendix says the model received the full biological-risk safety training even though OpenAI does not classify it as Bio High. (p. 35)
- For AI self-improvement proxies, GPT-5.4 mini scores 54.00% on Monorepo-Bench and 7.5% on OpenAI-Proof Q&A. (p. 36)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Monorepo-Bench | — | pass@1 | 54.0% | — | GPT-5.4 59.33% (as GPT-5.4 Thinking) | p. 36 |
| OpenAI-Proof Q&A | — | pass@1 | 7.5% | — | GPT-5.4 4.16% (as GPT-5.4 Thinking) | p. 36 |

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Production Benchmarks | Violent illicit behavior | not-unsafe rate | 0.992 | — | GPT-5.1 Thinking 0.959; GPT-5.2 Thinking 0.979; GPT-5.4 0.971 (as GPT-5.4 Thinking) | p. 33 |
| Production Benchmarks | Non-violent illicit behavior | not-unsafe rate | 1.0 | — | GPT-5.1 Thinking 0.837; GPT-5.2 Thinking 0.923; GPT-5.4 1.0 (as GPT-5.4 Thinking) | p. 33 |
| Dynamic Mental Health Simulations | Mental health | not-unsafe rate | 0.985 | — | GPT-5.1 Thinking 0.753; GPT-5.2 Thinking 0.975; GPT-5.4 0.985 (as GPT-5.4 Thinking) | p. 33 |
| Dynamic Mental Health Simulations | Self-harm | not-unsafe rate | 0.98 | — | GPT-5.1 Thinking 0.904; GPT-5.2 Thinking 0.955; GPT-5.4 0.977 (as GPT-5.4 Thinking) | p. 33 |
| Multimodal Troubleshooting Virology | — | pass@1 | 46.5% | Raw score; appendix also reports 47.0% with refusals, safe completions, and cheating counted as successes. | GPT-5 41.91%; GPT-5.4 50.37% (as GPT-5.4 Thinking) | pp. 35-36 |
| ProtocolQA Open-Ended | — | pass@1 | 33.64% | Raw score; refusal-inclusive value is 34.24%. | GPT-5 36.73%; GPT-5.4 42.48% (as GPT-5.4 Thinking) | pp. 35-36 |
| Tacit Knowledge and Troubleshooting | — | cons@32 | 71.67% | Raw score; refusal-inclusive value is 77.77%. | GPT-5 74.33%; GPT-5.4 65.0% (as GPT-5.4 Thinking; 83.8% refusal-inclusive) | pp. 35-36 |
| TroubleshootingBench | — | pass@1 | 31.91% | Raw score; refusal-inclusive value is 33.11%. | GPT-5 32.75%; GPT-5.4 35.75% (as GPT-5.4 Thinking; 38.85% refusal-inclusive) | pp. 35-36 |
| Capture the Flag (Professional) | — | pass@12 | 81.32% | — | GPT-5.4 88.23% (as GPT-5.4 Thinking) | p. 36 |
| CVE-Bench | — | pass@1 | 83.33% | — | GPT-5.4 86.27% (as GPT-5.4 Thinking) | p. 36 |

## Safety findings

### Safety classification

- **Framework:** OpenAI Preparedness Framework
- **Overall determination:** Below High in biochemical, cybersecurity, and AI self-improvement domains

OpenAI's appendix determines GPT-5.4 mini is below High across all three Preparedness domains it discusses. The biological conclusion relies on GPT-5 physical-world evidence plus automated comparisons showing mini is not enough above GPT-5 to warrant a different classification. (pp. 34-36)

| Domain | Determination | Level | Finding | Source |
| --- | --- | --- | --- | --- |
| Biological and chemical | Below threshold | Below High | OpenAI concludes GPT-5.4 mini is not Bio High under the current novice-uplift criterion while still applying full biological-risk safety training. | pp. 35-36 |
| Cybersecurity | Below threshold | Below High | The appendix says Preparedness determinations place GPT-5.4 mini below High in cybersecurity and reports only CTF and CVE-Bench proxy scores. | pp. 34, 36 |
| AI self-improvement | Below threshold | Below High | The appendix places AI self-improvement below High and reports Monorepo-Bench and OPQA scores as supporting evidence. | pp. 34, 36 |

### Agentic-coding risks

- **Reward hacking** (not reported): The mini appendix reports no reward-hacking or grader-gaming evaluation.
- **Test tampering** (not reported): The mini appendix reports no test-tampering evaluation.
- **Destructive or overeager actions** (sibling only): The main card reports destructive-action and reversion tests for GPT-5.4 Thinking, but the mini appendix does not repeat them for GPT-5.4 mini.
- **Sabotage** (sibling only): Apollo sabotage results in the main body are for GPT-5.4 reasoning; the mini appendix does not report sabotage results for GPT-5.4 mini.
- **Prompt injection** (sibling only): Prompt-injection connector and function-call scores are reported for GPT-5.4 Thinking in the main body, not for GPT-5.4 mini.
- **Honesty** (sibling only): The main-body Apollo deception discussion does not apply to the appendix model, and the mini section has no honesty evaluation.
- **Sycophancy** (not reported): Neither the mini appendix nor the relevant main-body scope reports a sycophancy evaluation for GPT-5.4 mini.

### Other safety findings

- Disallowed-content not-unsafe scores are high in some categories but lower than GPT-5.4 Thinking on harassment, extremism, self-harm, violence, sexual, and sexual/minors. (p. 33)
- OpenAI treats lower CoT controllability as favorable for monitorability risk and says GPT-5.4 mini is lower than any previously reported model in that suite. (pp. 33-34)
- The biology determination depends partly on a physical-world novice study for GPT-5, then asks whether mini is enough more concerning than GPT-5 to change the threshold call. (pp. 34-36)
- Even refusal-inclusive biology scoring leaves GPT-5.4 mini below a Bio High conclusion in OpenAI's judgment. (p. 36)
- The appendix reports cyber proxy scores but still keeps the mini model below High cybersecurity capability. (pp. 34, 36)

## Limitations and caveats

- There is no standalone GPT-5.4 mini card; the appendix gives a selected safety snapshot rather than full model data, training, tools, or deployment architecture. (p. 33)
- Main-body GPT-5.4 Thinking evaluations should not be attributed to the mini model unless the appendix itself provides a mini column. (pp. 33, 36)
- The biology conclusion uses a GPT-5 physical-world novice study and automated comparisons rather than a separate physical-world mini study. (pp. 34-35)
- Refusal-inclusive biology values are conservative capability estimates, not observed helpful task-completion behavior. (pp. 35-36)
- The appendix omits mini-specific HealthBench, prompt-injection, destructive-action, jailbreak, broader coding, and long-rollout evaluations. (pp. 33-36)

## Practical implications for Copilot users

### Choose it for

- **Agentic coding:** The appendix reports 54.00% pass@1 on Monorepo-Bench, a pull-request-style code benchmark, for GPT-5.4 mini. (p. 36)
- **Security work:** CTF and CVE-Bench scores are substantial while OpenAI still classifies the mini model below High for cybersecurity. (pp. 34, 36)
- **Quick edits:** The appendix supports using mini as a smaller model only where selected safety and code-proxy evidence is sufficient, not for broad high-risk autonomy. (pp. 33, 36)

### Avoid it for

- **Large refactors:** The appendix does not report broad refactoring, workspace-state, or destructive-action results for the mini model. (pp. 33, 36)
- **Untrusted input:** Prompt-injection robustness is not repeated for GPT-5.4 mini, so untrusted connector, repository, or issue content lacks mini-specific evidence. (pp. 33-34)
- **High-stakes domains:** The appendix's below-High determinations are risk-threshold calls, not correctness guarantees for biology, cyber, or AI-R&D tasks. (pp. 34-36)

### Guidance

- Do not use GPT-5.4 Thinking's main-body scores as mini scores; the appendix is the model-specific evidence.
- For Copilot, treat mini as a scoped option when quick iteration matters, but escalate ambiguous multi-file or high-risk work to a model with a fuller card.
- Require normal code review and tests because the appendix omits destructive-action, prompt-injection, and long-rollout agent results.
- Keep security prompts authorized and defensive despite the below-High cyber classification.
- The Copilot app does not list a long-context option for this model, so avoid assuming the same context behavior as GPT-5.4.

## Document coverage

The PDF page marker for the appendix starts on page 33, not page 32. This digest uses only Section 6, pages 33-36, for GPT-5.4 mini facts and results. Main-body GPT-5.4 Thinking evaluations are treated only as sibling comparators when they appear in appendix tables, and omitted evaluations are marked sibling-only or not reported.

- **Card type:** Appendix. This model is covered in an appendix or section of a sibling model's document.
- **Pages specific to this model:** pp. 33-36
- **Names the document uses for this model:** GPT-5.4 mini, gpt-5.4-mini
- **Catalog scope:** Section 6, "Appendix: GPT-5.4 mini" (PDF pages 32-36) of the GPT-5.4 Thinking System Card.
- **Catalog note:** No standalone GPT-5.4 mini card exists; the GPT-5.4 Thinking card devotes an appendix to it.
