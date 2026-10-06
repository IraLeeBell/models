# Grok 4.6

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write grok-4.6`. -->

> Original digest of *Model Card: Grok 4.6* (xAI, August 12, 2026; 42 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

**Copilot status** (catalog checked 2026-10-06): Current; GitHub release status GA. CLI: Yes. App model picker: listed. App reasoning efforts: low, medium, high, xhigh. App Auto: no. App long-context option: yes.

## At a glance

Grok 4.6 is xAI's Grok 4.5 successor, with longer supplemental training and broader agentic RL for coding, knowledge work, engineering, CAD, and AI R&D. It improves over Grok 4.5 on most long-running coding, terminal, and engineering suites, but the card also reports worse hallucination, self-harm, MASK-Rectified, and sycophancy rates. xAI keeps it below FAIF biology and chemistry thresholds and reports small cyber gains.

- **Choose it for:** Longer coding-agent, terminal, engineering, and AI-R&D tasks where xhigh or high effort can be reviewed carefully.
- **Watch out for:** Factuality and several behavior scores regress versus Grok 4.5, and prompt-injection or destructive-action testing is absent.
- Against Grok 4.5, the biggest model-lineage gains are agentic work: DeepSWE v1.1 rises to 67.0% at xhigh, SWE-Marathon v1.1 to 31.9%, Terminal-Bench 3.0 to 26.0%, and APEX-Agents to 57.5%. (pp. 12-14, 17)
- The card says supplemental training ran longer than Grok 4.5 and added curated reasoning data, engineering corpora, an improved optimizer, Grok 4.5-generated SFT traces, and agentic RL for knowledge work, coding, kernels, web development, and CAD. (p. 7)
- AI R&D and engineering coverage broadens: MTS Eval is 61.1%, InferenceEval 46.9%, KernelBenchInternal v1.1 37.2%, EEBench 60.0% at xhigh, and CADGenBench 40.9%. (pp. 20, 22, 24-26)
- xAI places Grok 4.6 below FAIF biology and chemistry thresholds, while noting a limited biological capability lift over Grok 4.5 and improved CBRN refusal recall. (pp. 32, 37)
- Safety is mixed: jailbreak compliance improves to 0.04% on standard attacks, but StrongReject rises to 3.9%, self-harm compliance to 0.84%, MASK-Rectified dishonesty to 1.90%, and sycophancy to 0.04%. (pp. 35, 38-39)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The card is dated August 12, 2026 with an August 17 revision, but it gives no release date. | — |
| Knowledge cutoff | January 2026 (stated as pretraining data cutoff of January 2026). Supplemental training used data generated as late as June 2026. | p. 7 |
| Context window | Not stated | — |
| Maximum output | Not stated | — |
| Input modalities | Text, Image | p. 7 |
| Output modalities | Text | p. 7 |
| Reasoning controls | Effort levels. Benchmark rows use high and xhigh thinking efforts; the card does not describe every available control. | pp. 8, 12 |
| Effort levels | high, xhigh. Levels used in the card's Grok 4.6 results. | pp. 8, 12 |
| Tool use | Terminal, File editing, Web search. The card evaluates Grok Build, file and terminal tools in legal-agent work, repository editing, and search-based answering. | pp. 7, 19, 28 |
| Open weights | Not stated | — |
| Architecture | Not stated. The card calls Grok 4.6 part of a 1.5T-scale family, but does not give a precise architecture identifier. | — |
| Total parameters | Not stated. The card says 1.5T-scale, not an exact parameter count. | — |
| Active parameters | Not stated | — |

### Capability notes

- Grok 4.6 extends Grok 4.5 and is described as better at autonomous, challenging tasks with fewer steps and fewer output tokens than other frontier models. (p. 6)
- Training adds a longer supplemental phase than Grok 4.5, including curated model-generated data, engineering corpora, an improved optimizer, Grok 4.5-generated SFT traces, and agentic RL across knowledge work, coding, kernels, web development, and CAD. (p. 7)
- Coding evaluations cover Cursor IDE workflows, observability/integration tasks, maintainer-style PR quality, repository repair, multi-hour tasks, and terminal work. (pp. 8, 10-14)
- Knowledge-work evaluations span GDPval-AA v2, AA-Briefcase, APEX-Agents, OfficeQA Pro, and legal-agent tasks with file, shell, and document skills. (pp. 15-19)
- Engineering and CAD results include EEBench, 3DCodeBench, PartBench, CADGenBench, and CADBench, with several gains over Grok 4.5. (pp. 20-23)
- AI R&D capability is tested through a production inference-optimization exercise, SpaceXAI MTS Eval, InferenceEval, and KernelBenchInternal v1.1. (pp. 24-26)
- Search and factuality are explicitly measured, but hallucination rises to 1.7% while DeepSearchQA falls behind the Grok 4.5 comparison row. (pp. 27-28)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| CursorBench 3.2 | — | score | 70.8% | xhigh effort; Cursor agent; fixed Cursor tasks; 41,136 output tokens per task; third-party run | — | p. 8 |
| APEX-SWE | — | pass@1 | 56.4% | high effort; Terminus 2; integration and observability tasks; third-party run | Claude Opus 5 63.7% (max); Claude Fable 5 58.8% (max, with fallback); Grok 4.5 53.6% (high); Kimi K3 48.0% (max); Claude Sonnet 5 46.4% (max); GPT-5.6 Sol 45.8% (xhigh) | p. 10 |
| FrontierCode v1.1 | — | score | 61.3% | high effort; Grok Build; extended set of 150 samples; third-party run | Claude Fable 5 64.9% (max, with fallback); Claude Opus 5 63.6% (max); GPT-5.6 Sol 60.6% (max); Claude Opus 4.8 59.6% (max); GPT-5.5 56.7% (xhigh); Grok 4.5 56.6% (high) | p. 11 |
| DeepSWE v1.1 | — | pass@1 | 67.0% | xhigh effort; mini-SWE-agent; Datacurve evaluation; third-party run | Claude Opus 5 74.0% (max); GPT-5.6 Sol 73.0% (max); Claude Fable 5 70.0% (max, with fallback); Kimi K3 69.0% (max); GPT-5.5 67.0% (xhigh); Grok 4.5 54.0% (high) | p. 12 |
| SWE-Marathon v1.1 | — | success rate | 31.9% | high effort; Grok Build; provider harnesses; Abundant AI run; third-party run | Claude Opus 5 50.0% (max); Claude Opus 4.8 48.8% (max); Kimi K3 48.1% (max); Claude Fable 5 45.0% (max, with fallback); GPT-5.6 Sol 42.5% (max); Grok 4.5 29.4% (high) | p. 13 |
| Terminal-Bench 3.0 | — | success rate | 26.0% | high effort; Grok Build; Harbor run; successor to Terminal-Bench 2.1; third-party run | Claude Opus 5 43.5% (max); GPT-5.6 Sol 34.6% (max); Claude Fable 5 34.1% (max, with fallback); Claude Opus 4.8 21.1% (max); Grok 4.5 15.7% (high); Claude Sonnet 5 14.6% (max) | p. 14 |

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| CursorBench 3.2 | — | score | 69.9% | high effort; Cursor agent; Grok 4.5 high comparison is 66.7%; third-party run | Grok 4.5 66.7% (high) | p. 8 |
| DeepSWE v1.1 | — | pass@1 | 65.9% | high effort; mini-SWE-agent; Datacurve evaluation; third-party run | Grok 4.5 54.0% (high); Claude Sonnet 5 54.0% (max) | p. 12 |
| GDPval-AA v2 | — | Elo | 1,753 Elo | high effort; Artificial Analysis GDPval-AA v2 harness; third-party run | Claude Opus 5 1,849 Elo (max); Claude Fable 5 1,741 Elo (max, with fallback); GPT-5.6 Sol 1,728 Elo (max); Kimi K3 1,682 Elo (max); Claude Sonnet 5 1,601 Elo (max); Grok 4.5 1,526 Elo (high) | p. 15 |
| AA-Briefcase | — | Elo | 1,577 Elo | high effort; Artificial Analysis; offline multi-week professional projects; third-party run | Claude Opus 5 1,715 Elo (max); Claude Fable 5 1,574 Elo (max, with fallback); Kimi K3 1,541 Elo (max); GPT-5.6 Sol 1,502 Elo (max); Claude Sonnet 5 1,383 Elo (max); Grok 4.5 1,313 Elo (high) | p. 16 |
| APEX-Agents | — | pass@1 | 57.5% | high effort; Mercor harness; professional multi-application tasks; third-party run | Claude Opus 5 60.6% (max); Claude Fable 5 59.2% (max, with fallback); GPT-5.6 Sol 56.7% (max); Claude Opus 4.8 56.2% (max); GPT-5.5 55.5% (xhigh); Grok 4.5 47.1% (high) | p. 17 |
| Legal Agent Benchmark | Harvey final score | score | 15.8% | high effort; Valkyrie; internet disabled; fixed legal tools and skills; third-party run | Grok 4.5 12.9% (high); Claude Opus 5 11.7% (max); Claude Fable 5 11.3% (max, with fallback); GPT-5.6 Sol 2.5% (max) | p. 19 |
| EEBench | V1 core corpus | mean reward | 60.0% | xhigh effort; Grok Build; peers use their providers' harnesses; third-party run | Claude Opus 5 61.6% (max); Claude Fable 5 54.2% (max, with fallback); Grok 4.5 50.9% (high); GPT-5.6 Sol 39.4% (max) | p. 20 |
| CADGenBench | Generation split | mean reward | 40.9% | high effort; Grok Build; peers use their providers' harnesses; third-party run | GPT-5.6 Sol 37.1% (xhigh); Claude Opus 5 36.6% (max); Grok 4.5 33.2% (high) | p. 22 |
| CAD-Bench | — | mean reward | 88.4% | xhigh effort; Grok Build; gNucleus run; third-party run | Claude Opus 5 90.6% (max); GPT-5.6 Sol 86.5% (max); Grok 4.5 83.7% (high) | p. 23 |
| SpaceXAI MTS Eval | — | score | 61.1% | high effort; Grok Build; standard non-GPU suite; fixed rollout resources | Grok 4.5 57.1% (high); Claude Opus 4.8 55.8% (max); Claude Opus 5 52.6% (max); GPT-5.6 Sol 52.1% (xhigh); GPT-5.5 46.4% (xhigh) | p. 24 |
| InferenceEval | — | accuracy | 46.9% | high effort; Grok Build; hidden GPU unit and integration probes | GPT-5.6 Sol 44.1% (max); Claude Opus 5 43.0% (max); Grok 4.5 41.3% (high); Claude Opus 4.8 40.7% (max); Kimi K3 39.8% (max); GPT-5.5 38.9% (xhigh) | p. 25 |
| KernelBenchInternal v1.1 | — | accuracy | 37.2% | high effort; Grok Build; sandboxed GPU kernel-writing tasks | Claude Opus 5 48.1% (max); Kimi K3 41.0% (max); Claude Opus 4.8 37.5% (max); GPT-5.6 Sol 34.4% (max); GPT-5.5 34.0% (xhigh); Grok 4.5 29.7% (high) | p. 26 |
| FACTS Benchmark Suite | Single-turn hallucination | hallucination rate (lower is better) | 1.7% | high effort; Grok Build; unsupported-claim rate | Claude Opus 4.8 3.4% (max); GPT-5.5 1.1% (xhigh); Grok 4.5 0.98% (high) | p. 27 |
| DeepSearchQA | — | accuracy | 81.6% | high effort; Grok Build; internal implementation | GPT-5.5 87.8% (xhigh); Grok 4.5 85.3% (high); Claude Opus 4.8 84.8% (max); GPT-5.6 Sol 75.0% (high) | p. 28 |
| CyberGym | Mean reproduced | pass@1 | 79.7% | high effort; Grok Build; without safeguards | GPT-5.6 Sol 83.6% (max); GPT-5.5 81.8% (xhigh); Grok 4.5 79.0% (high); Claude Opus 4.8 78.1% (max) | p. 29 |
| CVE-Bench | — | mean reward | 39.8% | high effort; Grok Build; without safeguards | Grok 4.5 35.2% (high) | p. 30 |
| SecureCodeReview | — | mean reward | 58.7% | high effort; Grok Build; security fixes without new security regressions | GPT-5.5 64.1% (xhigh); GPT-5.6 Sol 57.5% (max); Grok 4.5 49.4% (high) | p. 30 |
| Virology Capabilities Test | — | accuracy | 67.4% | high effort; without production safeguards; dual-use signal | Grok 4.5 65.5% (high) | p. 32 |
| WMDP | WMDP-Bio | accuracy | 90.0% | high effort; without production safeguards | Grok 4.5 90.9% (high) | p. 33 |
| xAI jailbreak suites | Standard jailbreaks | harmful compliance rate (lower is better) | 0.04% | high effort | Grok 4.5 0.73% (high) | p. 35 |
| StrongReject | — | harmful compliance rate (lower is better) | 3.9% | high effort | Grok 4.5 1.5% (high) | p. 35 |
| xAI jailbreak suites | Long-horizon jailbreaks | harmful compliance rate (lower is better) | 1.0% | high effort | — | p. 35 |
| MASK | MASK-Rectified | dishonesty rate (lower is better) | 1.9% | high effort | Grok 4.5 0.67% (high) | p. 38 |
| xAI sycophancy evaluation | — | sycophancy rate (lower is better) | 0.04% | high effort | Grok 4.5 0.01% (high) | p. 39 |

## Safety findings

### Safety classification

- **Framework:** xAI Frontier Artificial Intelligence Framework
- **Overall determination:** Below FAIF dual-use biology and chemistry thresholds

xAI treats its biology and chemistry suites as FAIF threshold evaluations and says Grok 4.6 remains below threshold, despite a limited biological lift over Grok 4.5. Cyber capability rises modestly and is corroborated by outside evaluators, but the card states no cyber threshold result. (pp. 29, 32)

| Domain | Determination | Level | Finding | Source |
| --- | --- | --- | --- | --- |
| Biological and chemical | Below threshold | — | Below FAIF dual-use thresholds, with limited biological uplift over Grok 4.5 and improved weapons-path refusals reported elsewhere. | p. 32 |
| Cybersecurity | Not stated | — | Cyber capability gains over Grok 4.5 are concentrated in defense and vulnerability mitigation, but no FAIF threshold determination is given. | p. 29 |

### Agentic-coding risks

- **Reward hacking** (not reported): The card mentions verification designed to resist reward hacking, but reports no Grok 4.6 reward-hacking rate or observation.
- **Test tampering** (not reported): The card reports no evaluation of modifying or weakening tests.
- **Destructive or overeager actions** (not reported): The card does not evaluate destructive or unrequested agent actions.
- **Sabotage** (not reported): No sabotage or oversight-evasion evaluation is reported.
- **Prompt injection** (not reported): Jailbreaks are tested, but the card reports no prompt-injection evaluation through files, tool outputs, search, or web content.
- **Honesty** (reported): MASK-Rectified dishonesty is 1.90%, worse than the 0.67% Grok 4.5 comparison row; false claims of task completion are not separately measured. (p. 38)
- **Sycophancy** (reported): Sycophancy is 0.04%, compared with 0.01% for Grok 4.5. (p. 39)
- **Malicious agentic use** (reported): HackerBench v0.2 reports 6.9% harmful or dual-use compliance under the release safeguard stack. (p. 31)
- **Over-refusal** (reported): HackerBench v0.2 reports 0.0% benign refusal. (p. 31)

### Other safety findings

- The revision log says the final card corrected HackerBench v0.2, self-harm, MASK, and Legal Agent Benchmark figures, so the corrected revision is the source for those numbers. (p. 2)
- Cyber results show small gains over Grok 4.5: CyberGym is 79.7% versus 79.0%, CVE-Bench is 39.8% versus 35.2%, and SecureCodeReview is 58.7% versus 49.4%, with capability probes run without production safeguards. (pp. 29-30)
- HackerBench v0.2 with release safeguards reports 6.9% harmful or dual-use compliance and 0.0% benign refusal. (p. 31)
- Biology and chemistry remain below FAIF thresholds; VCT rises to 67.4%, Biosecurity VCT to 47.8%, BioUseBench severity-5 refusal to 90.7%, and LAB-Bench to 80.7%, while WMDP-Bio and ProtocolQA decline versus Grok 4.5. (pp. 32-34)
- Jailbreak results are mixed: standard jailbreak compliance improves to 0.04%, StrongReject worsens to 3.9%, and long-horizon jailbreak compliance is 1.0%. (p. 35)
- General and CBRN refusals improve versus Grok 4.5, with broad harmful-request compliance at 0.93%, child-safety compliance at 0.00%, and bio and chem refusal recall at 100.0%. (pp. 36-37)
- Behavioral and self-harm metrics regress versus Grok 4.5: self-harm compliance is 0.84%, MASK-Rectified dishonesty 1.90%, and sycophancy 0.04%. (pp. 38-39)

## Limitations and caveats

- The card requires human and domain-expert oversight for high-stakes medical, legal, financial, and safety-critical decisions. (p. 6)
- It states text and image input with text output, but gives no context window, maximum output, exact parameter count, or architecture details beyond a broad family scale. (pp. 6-7)
- The revision log records corrected results, making earlier copies of the card unreliable for several benchmark and safety figures. (p. 2)
- Factuality worsens versus the Grok 4.5 comparison row, and DeepSearchQA is lower than the Grok 4.5 row in the same chart. (pp. 27-28)
- Cyber and biology capability probes often run without production safeguards, so they are not normal deployed-behavior measurements. (pp. 29, 32)
- The card reports no prompt-injection, reward-hacking, test-tampering, destructive-action, or sabotage evaluation for agentic coding workflows. (pp. 35, 38)

## Practical implications for Copilot users

### Choose it for

- **Agentic coding:** It improves over Grok 4.5 on APEX-SWE, FrontierCode v1.1, DeepSWE v1.1, and SWE-Marathon v1.1. (pp. 10-13)
- **Terminal workflows:** Terminal-Bench 3.0 rises to 26.0% in Grok Build, ahead of the Grok 4.5 high comparison row. (p. 14)
- **Knowledge work:** Grok 4.6 is near the top of several professional-work charts, including GDPval-AA v2, AA-Briefcase, APEX-Agents, and OfficeQA Pro. (pp. 15-18)
- **Security work:** The card shows improved defensive cyber and vulnerability-mitigation results while separately measuring harmful-request compliance. (pp. 29-31)

### Avoid it for

- **Untrusted input:** The card reports no prompt-injection tests for external content read by tools, files, search, or repositories. (p. 35)
- **High-stakes domains:** xAI says high-stakes domains require human oversight and domain-expert validation. (p. 6)
- **Web research:** The hallucination rate rises versus the Grok 4.5 comparison, and DeepSearchQA trails the Grok 4.5 row in the same chart. (pp. 27-28)

### Guidance

- Use high or xhigh for difficult agent work; the card's main Grok 4.6 coding rows use those efforts.
- Treat factual answers cautiously and ask for source grounding, because the card's factuality and search rows do not improve uniformly over Grok 4.5.
- Keep repository permissions narrow and review tests, because the card does not assess test tampering or destructive actions.
- Sandbox security tasks and keep them defensive and authorized; cyber capability probes intentionally remove production safeguards.
- Copilot Auto does not select this model, so choose it explicitly when the extra reasoning is worth the additional latency and token usage.
- The Copilot app offers a long-context option, but the card does not state a context window or output limit.

## Document coverage

The whole 42-page card is about Grok 4.6. It includes a revision log, capability sections, safety evaluations, and comparison rows for Grok 4.5 plus non-xAI models. This digest uses sibling and peer values only as comparators and incorporates the final corrected numbers from the card.

- **Card type:** Dedicated. The document is about this model; it may include short sibling sections.
- **Pages specific to this model:** the whole document
- **Names the document uses for this model:** Grok 4.6
- **Catalog scope:** Dedicated publisher card for this model.
