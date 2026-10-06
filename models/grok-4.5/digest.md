# Grok 4.5

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write grok-4.5`. -->

> Original digest of *Model Card: Grok 4.5* (xAI, July 14, 2026; 29 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

**Copilot status** (catalog checked 2026-10-06): Current; GitHub release status GA. CLI: Yes. App model picker: listed. App reasoning efforts: low, medium, high. App Auto: no. App long-context option: yes.

## At a glance

Grok 4.5 is xAI's first model in this new Grok line, with a dedicated card focused on agentic software work, terminal tasks, engineering design, knowledge work, search, and AI R&D. Its strongest model-choice signal is breadth: it pairs strong coding-agent results with low jailbreak, self-harm, dishonesty, and sycophancy rates. The card predates Grok 4.6 and 4.7, so use it mainly as the baseline for that lineage.

- **Choose it for:** Broad agentic coding, terminal, and engineering tasks where high-effort runs can be checked with tests and review.
- **Watch out for:** No context-window, output-limit, prompt-injection, destructive-action, or test-tampering evidence is reported.
- Coding-agent results are the lead signal: DeepSWE v1.0 is 62.0% pass@1, DeepSWE v1.1 is 53.0%, SWE-Marathon is 29.0%, and Terminal-Bench 2.1 is 83.3% task success. (pp. 6-7, 9-10)
- The card presents Grok 4.5 as a step beyond earlier xAI models, saying it handles larger tasks with fewer steps than previous models while keeping text output and text/image input. (p. 4)
- xAI treats dual-use biology and chemistry tests as safety-threshold evaluations and says Grok 4.5 remains sub-threshold, while reporting unrestricted VCT at 65.5% and WMDP-Bio at 90.9%. (p. 22)
- Safeguard results include 0.73% jailbreak compliance, 1.1% broad harmful-request compliance, 0.5% self-harm compliance, 0.67% MASK-Rectified dishonesty, and 0.01% sycophancy. (pp. 24-27)
- The card gives a January 2026 pretraining cutoff but does not state a release date, context window, output limit, architecture, or parameter count. (p. 5)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The card is dated July 14, 2026 and notes a July 20 revision, but it gives no release date. | — |
| Knowledge cutoff | January 2026 (stated as pretraining cutoff of January 2026) | p. 5 |
| Context window | Not stated | — |
| Maximum output | Not stated | — |
| Input modalities | Text, Image | p. 4 |
| Output modalities | Text | p. 4 |
| Reasoning controls | Effort levels. The card reports results at high effort but does not describe every available control. | p. 6 |
| Effort levels | high. High is the only Grok 4.5 effort level used in the reported benchmark rows. | p. 6 |
| Tool use | Terminal, File editing, Web search. The card evaluates repository editing, command execution, Grok Build, and grounded answering with search tools. | pp. 5-6, 19 |
| Open weights | Not stated | — |
| Architecture | Not stated | — |
| Total parameters | Not stated | — |
| Active parameters | Not stated | — |

### Capability notes

- Grok 4.5 is described as the initial release of a new SpaceXAI/Cursor model family, optimized for agentic coding, engineering, design, professional workflows, and efficient reasoning. (p. 4)
- The model was pretrained on public, internally generated, and rights-cleared data, then midtrained and post-trained with supervised fine-tuning plus reinforcement learning from human and synthetic reward signals. (p. 5)
- Coding coverage spans repository issue resolution, multilingual repair, program reconstruction, terminal work, codebase question answering, and a false-claim check for agent reports. (pp. 6-12)
- Engineering and professional-work coverage includes electrical design, 3D and CAD generation, GDPval-AA v2, and banking-style tool-use workflows. (pp. 13-16)
- The card also measures AI R&D assistance and relational-data reasoning through SpaceXAI MTS Eval and RelBench, although only the chart supplies the MTS numeric point. (pp. 17-18)
- Search and factuality are represented by a single-turn hallucination suite and DeepSearchQA; the hallucination result is lower than the comparison rows in that chart. (p. 19)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| DeepSWE v1.0 | — | pass@1 | 62.0% | high effort; each provider's harness; run by Artificial Analysis on the Datacurve eval; third-party run | Claude Fable 5 66.1% (max, with fallback); GPT-5.5 64.3% (xhigh); Claude Opus 4.8 55.8% (max); Claude Opus 4.7 40.1% (max) | p. 6 |
| DeepSWE v1.1 | — | pass@1 | 53.0% | high effort; mini-SWE-agent; updated contamination-resistant tasks; third-party run | Claude Fable 5 70.0% (max, with fallback); GPT-5.5 67.0% (xhigh); Claude Opus 4.8 59.0% (max); GLM-5.2 44.0% (max) | p. 7 |
| APEX-SWE | — | pass@1 | 51.2% | high effort; integration and observability tasks; third-party run | Claude Fable 5 54.8% (max, with fallback); Claude Opus 4.8 47.3% (high); Claude Sonnet 5 43.6% (high); GPT-5.5 40.8% (xhigh); GPT-5.6 Sol 39.7% (xhigh) | p. 7 |
| SWE-Marathon | — | success rate | 29.0% | high effort; full task set; multi-layer verification intended to resist shortcuts | Claude Opus 4.8 26.0% (max); Claude Fable 5 24.0% (max, with fallback); Claude Opus 4.7 16.0% (max); GLM-5.2 13.0% (max); GPT-5.5 12.0% (xhigh) | p. 9 |
| FrontierSWE | — | win rate | 78% | high effort; Grok CLI; Dominance versus a random baseline; up to 20 hours per task; third-party run | Claude Fable 5 89% (max, with fallback); Claude Opus 4.8 73% (max); GLM-5.2 72% (max); GPT-5.5 70% (xhigh) | p. 9 |
| Terminal-Bench 2.1 | — | success rate | 83.3% | high effort; Grok Build; containerized terminal workflows | Claude Fable 5 84.3% (max, with fallback); GPT-5.5 83.4% (xhigh); Claude Opus 4.8 78.9% (max); Claude Opus 4.7 78.9% (max) | p. 10 |

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| SWE-bench Pro | — | pass@1 | 64.7% | high effort; controls for reward-hacking attempts are noted | Claude Fable 5 80.4% (max, with fallback); Claude Opus 4.8 69.2% (max); Claude Opus 4.7 64.3% (max); GLM-5.2 62.1% (max); GPT-5.5 58.6% (xhigh) | p. 8 |
| FalseClaimBench | — | accuracy | 84.0% | high effort; agent claims checked against actual workspace state | Claude Opus 4.8 59.0% (max); GLM-5.2 38.0% (max) | p. 12 |
| CAD-Bench | — | mean reward | 88.1% | high effort; parametric CAD and 3D modeling tasks; third-party run | Claude Fable 5 88.5% (max); Claude Opus 4.8 88.2% (max); Claude Sonnet 5 86.9% (max); GPT-5.6 Sol 84.9% (xhigh) | p. 14 |
| GDPval-AA v2 | — | Elo | 1,535 Elo | high effort; Artificial Analysis GDPval-AA v2 harness; third-party run | Claude Fable 5 1,760 Elo (max, with fallback); GPT-5.6 Sol 1,743 Elo (max); Claude Sonnet 5 1,607 Elo (max); Claude Opus 4.8 1,600 Elo (max); GLM-5.2 1,514 Elo (max); GPT-5.5 1,493 Elo (xhigh) | p. 15 |
| FACTS Benchmark Suite | Single-turn hallucination | hallucination rate (lower is better) | 0.98% | high effort; single-turn unsupported-claim rate | GPT-5.5 1.14% (xhigh); Claude Opus 4.8 3.35% (max) | p. 19 |
| DeepSearchQA | — | accuracy | 38.4% | high effort; internal implementation of DeepSearchQA | Claude Opus 4.8 40.7% (max) | p. 19 |
| CyberGym | Mean reproduced | pass@1 | 80.4% | high effort; unrestricted cyber capability probe | Claude Mythos 5 83.8%; GPT-5.6 Sol 83.6% (max); Claude Opus 4.8 78.1% (max); GPT-5.5 73.7% (xhigh); Claude Opus 4.7 73.1% (max) | p. 20 |
| Virology Capabilities Test | — | accuracy | 65.5% | high effort; without safeguards; dual-use capability signal | — | p. 22 |
| WMDP | WMDP-Bio | accuracy | 90.9% | high effort; without safeguards; dual-use knowledge | — | p. 22 |
| xAI jailbreak suites | Standard jailbreaks | harmful compliance rate (lower is better) | 0.73% | high effort; should-refuse prompts under adversarial pressure | — | p. 24 |
| MASK | MASK-Rectified | dishonesty rate (lower is better) | 0.67% | high effort | — | p. 27 |
| xAI sycophancy evaluation | — | sycophancy rate (lower is better) | 0.01% | high effort | — | p. 27 |

## Safety findings

### Safety classification

- **Framework:** xAI Frontier Artificial Intelligence Framework
- **Overall determination:** Sub-threshold dual-use biology and chemistry knowledge

The card treats its dual-use biology and chemistry suites as xAI safety-threshold evaluations and says Grok 4.5 remains below threshold, with limited actionable uplift for a trained actor. Cyber capability is measured separately, but the card does not state a cyber threshold determination. (p. 22)

| Domain | Determination | Level | Finding | Source |
| --- | --- | --- | --- | --- |
| Biological and chemical | Below threshold | — | Sub-threshold dual-use knowledge on biology and chemistry threshold evaluations. | p. 22 |
| Cybersecurity | Not stated | — | Cyber capability and cyber safeguards are evaluated, but no safety-threshold conclusion is stated for cyber. | pp. 20-21 |

### Agentic-coding risks

- **Reward hacking** (not reported): The card says some benchmarks use controls or verification to resist reward hacking, but it reports no observed reward-hacking rate for Grok 4.5.
- **Test tampering** (not reported): The card does not evaluate whether the model weakens, deletes, or edits tests.
- **Destructive or overeager actions** (not reported): The card gives no evaluation of irreversible or unrequested agent actions.
- **Sabotage** (not reported): No sabotage, oversight-evasion, or deliberate-undermining evaluation is reported.
- **Prompt injection** (not reported): The card tests jailbreaks from the user or system side but not instructions injected through files, tools, search results, or web content.
- **Honesty** (reported): FalseClaimBench reports 84.0% fully true agent claims, and MASK-Rectified dishonesty is 0.67% under pressure to lie. (pp. 12, 27)
- **Sycophancy** (reported): The internal sycophancy test reports a 0.01% rate, measured as accuracy loss when a user supplies misleading context. (p. 27)
- **Malicious agentic use** (reported): HackerBench v0.2 reports 7.8% harmful or dual-use compliance with release safeguards enabled. (p. 21)
- **Over-refusal** (reported): HackerBench v0.2 reports 1.1% benign refusal. (p. 21)

### Other safety findings

- CyberGym is 80.4% mean reproduced in an unrestricted capability probe; xAI separates that ability measurement from safeguarded behavior on harmful cyber requests. (pp. 20-21)
- HackerBench v0.2 reports 7.8% harmful or dual-use compliance and 1.1% benign refusal with standard safeguards. (p. 21)
- For biology and chemistry, the card reports sub-threshold dual-use knowledge, with VCT at 65.5%, WMDP-Bio at 90.9%, WMDP-Chem at 87.3%, ProtocolQA at 87.0%, and BixBench at 93.8%. (pp. 22-23)
- Jailbreak compliance is 0.73% across a broad, updated set of attacks against should-refuse prompts. (p. 24)
- General output safety reports 1.1% broad harmful-request compliance, 0.0% child-safety compliance, and CBRN refusal accuracy from 96.7% to 97.9%. (p. 25)
- Mental-health and behavior measurements report 0.5% self-harm compliance, 20.4% epistemic-bias rate, 0.67% MASK-Rectified dishonesty, and 0.01% sycophancy. (pp. 26-27)

## Limitations and caveats

- xAI says the model is not intended to make high-stakes medical, legal, financial, or safety-critical decisions without human oversight and domain-expert validation. (p. 5)
- The card gives text and image input with text output, but no audio, video, context-window, output-limit, architecture, or parameter details. (pp. 4-5)
- The January 2026 pretraining cutoff means newer facts depend on retrieval, provided context, or later tools rather than pretraining alone. (p. 5)
- Several important measurements are internal, harness-specific, or chart-only, limiting independent reproducibility from the card alone. (pp. 4, 17, 21)
- Unrestricted cyber and biology capability probes should not be interpreted as normal deployed behavior under safeguards. (pp. 20, 22)
- The card reports user- and system-message jailbreaks, but no prompt-injection tests involving external tool outputs or repository files. (p. 24)

## Practical implications for Copilot users

### Choose it for

- **Agentic coding:** It has strong same-card coding results across DeepSWE, APEX-SWE, SWE-Bench Pro, and SWE-Marathon. (pp. 6-9)
- **Terminal workflows:** Terminal-Bench 2.1 is 83.3% task success in the Grok Build harness. (p. 10)
- **Knowledge work:** The card includes office and professional-work tasks such as GDPval-AA v2 and banking-style tool use. (pp. 15-16)
- **Security work:** CyberGym and HackerBench separate capability from safeguard behavior, supporting defensive, authorized use with controls. (pp. 20-21)

### Avoid it for

- **Untrusted input:** No prompt-injection evaluation is reported for content read through tools, files, search, or web pages. (p. 24)
- **High-stakes domains:** The card explicitly requires human and domain-expert oversight for high-stakes domains. (p. 5)
- **Long-horizon autonomy:** Although long-task results are strong, the card does not test destructive actions, test tampering, or reward-hacking behavior by this model. (pp. 8-9)

### Guidance

- Use high effort for benchmark-like coding work; all reported Grok 4.5 results in the card use high effort.
- Require tests, diffs, and explicit evidence of completed work because the card measures false claims but does not eliminate them.
- Keep security tasks defensive, authorized, and sandboxed, with narrow access to credentials and production systems.
- For search-heavy answers, require sources and independent checks; strong search scores do not guarantee every claim is grounded.
- The Copilot app offers a long-context option, but the card does not state the model's context window, so confirm limits outside the card.

## Document coverage

The complete 29-page card is specific to Grok 4.5. Other Grok, Claude, GPT, Gemini, GLM, and Mythos models appear only as comparison rows in xAI's charts or tables. This digest treats those numbers as comparators, not as evidence about Grok 4.5, and omits most reference-list detail.

- **Card type:** Dedicated. The document is about this model; it may include short sibling sections.
- **Pages specific to this model:** the whole document
- **Names the document uses for this model:** Grok 4.5
- **Catalog scope:** Dedicated publisher card for this model.
- **Catalog note:** The PDF linked from GitHub's comparison served a blank one-page file on the check date; xAI's nonblank Grok 4.5 card is recorded here.
