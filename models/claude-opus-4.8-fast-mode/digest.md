# Claude Opus 4.8 (fast mode) (preview)

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write claude-opus-4.8-fast-mode`. -->

> Original digest of *System Card: Claude Opus 4.8* (Anthropic, May 28, 2026; 246 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.
>
> Additional owner documentation cited: [Anthropic fast mode documentation](https://platform.claude.com/docs/en/build-with-claude/fast-mode).

**Copilot status** (catalog checked 2026-10-06): Current; GitHub release status GA. CLI: Yes. App model picker: not listed on the check date. App Auto: no. GitHub's model name carries "(preview)", while its release-status table lists GA; this catalog records the table value. It was not offered in the app model picker on the check date.

## At a glance

Claude Opus 4.8 fast mode is the same Opus 4.8 model served through Anthropic's research-preview fast inference configuration. The Opus 4.8 system card supplies model-level capability and safety evidence because the weights are the same, but the card does not evaluate fast mode. For Copilot users, the differentiators are responsiveness, preview labeling, and the catalog note that it was not in the app model picker on the check date.

- **Choose it for:** Low-latency Opus 4.8-style work in the CLI when the preview mode is available and you will still verify outputs.
- **Watch out for:** The Opus card does not test fast mode, and the catalog records that it was not in the app picker on the check date.
- Anthropic's fast-mode page lists Claude Opus 4.8 as supported and calls the feature a research preview for the Claude API and managed agents. ([Anthropic fast mode documentation](https://platform.claude.com/docs/en/build-with-claude/fast-mode))
- The same page says fast mode uses the same model with faster inference, with up to 2.5x higher output-token throughput and no change to intelligence or capability. ([Anthropic fast mode documentation](https://platform.claude.com/docs/en/build-with-claude/fast-mode))
- Because the weights are the same, the Opus 4.8 card's coding and agentic rows remain the relevant model evidence: SWE-bench Pro is 69.2%, Terminal-Bench 2.1 is 74.6%, and OSWorld-Verified is 83.4%. (pp. 194-196, 221)
- The card does not mention fast mode or rerun safety tests for it; its safety evidence is for the underlying Opus 4.8 model snapshot and selected deployment configurations. (pp. 12, 72, 75, 194)
- For the underlying model, Anthropic's RSP posture is CB-1 safeguards applied, CB-2 not crossed, automated AI-R&D not crossed, and alignment risk still very low. (pp. 30, 43-44)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The card is dated May 28, 2026 and has June 2026 corrections, but it does not give a separate release date. | — |
| Knowledge cutoff | Not stated. The card describes training sources but gives no training-data cutoff date. | — |
| Context window | Not stated. Evaluations use different token limits and say some 1M-subset tasks exceed the public API limit, but the card does not state a model context window. | — |
| Maximum output | Not stated. The card does not state a maximum output length. | — |
| Input modalities | Text, Image. Text is the primary interface; multimodal evaluations use screenshots, charts, and documents. | pp. 11, 216, 220-221 |
| Output modalities | Text (stated as outputs text only) | p. 11 |
| Reasoning controls | Effort levels, Adaptive thinking. Most capability results use adaptive thinking or named effort levels. | pp. 195, 202-203 |
| Effort levels | low, high, max, xhigh. The card reports these levels across benchmarks; it does not list every served level in one place. | pp. 197, 199, 222, 225 |
| Tool use | Web search, Code execution, Function calling, Terminal, File editing, Computer use, MCP. Evaluations include Claude Code, web and programmatic tools, code execution, computer use, and MCP workflows. | pp. 72, 202-203, 221, 225 |
| Open weights | Not stated. The card does not state whether weights are open. | — |
| Architecture | Not stated. The card does not disclose the model architecture. | — |
| Total parameters | Not stated. The card does not disclose parameter counts. | — |
| Active parameters | Not stated. The card does not disclose active parameter counts. | — |

### Capability notes

- Anthropic documents fast mode as a speed setting for supported Opus models, including Claude Opus 4.8, rather than a different model. ([Anthropic fast mode documentation](https://platform.claude.com/docs/en/build-with-claude/fast-mode))
- The page states that speed gains focus on output tokens per second, not time to first token, and are most visible with streaming. ([Anthropic fast mode documentation](https://platform.claude.com/docs/en/build-with-claude/fast-mode))
- The page describes the feature as available in research preview on the Claude API and Claude Managed Agents, and not on the listed third-party cloud platforms. ([Anthropic fast mode documentation](https://platform.claude.com/docs/en/build-with-claude/fast-mode))
- The underlying Opus 4.8 model is described as an Opus 4.7 upgrade with stronger software-engineering, agentic tool-use, and knowledge-work performance. (p. 11)
- Underlying model results include 88.6% on SWE-bench Verified, 69.2% on SWE-bench Pro, 74.6% on Terminal-Bench 2.1, and first place by average rank on FrontierSWE in the card. (pp. 194-197)
- Tool and computer-use evidence comes from the standard Opus card, including 82.2% on MCP-Atlas, 59.9% Pass@1 on Toolathlon, and 83.4% on OSWorld-Verified. (pp. 221, 225-226)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| SWE-bench Verified | — | pass@1 | 88.6% | max effort; standard configuration; average over 5 trials | Claude Opus 4.7 87.6% (max); Gemini 3.1 Pro 80.6% | pp. 194-195 |
| SWE-bench Pro | — | pass@1 | 69.2% | max effort; standard configuration; average over 5 trials | Claude Opus 4.7 64.3% (max); GPT-5.5 58.6%; Gemini 3.1 Pro 54.2% | pp. 194-195 |
| Terminal-Bench 2.1 | — | success rate | 74.6% | high effort; Terminus-2; 89 tasks; 445 trials on Daytona through Harbor; reported as mean reward; tasks are pass/fail; third-party run. Wall-clock timeouts make this sensitive to endpoint latency. | Claude Opus 4.7 66.1%; GPT-5.5 78.2%; Gemini 3.1 Pro 70.3% | pp. 194, 196-197 |
| FrontierSWE | mean@5 average rank | rank (lower is better) | #2.74 | xhigh effort; 17 ultra-long tasks; 20 hours per task; lower rank is better; third-party run | GPT-5.5 #3.06 (xhigh); Claude Opus 4.7 #4.15 (xhigh) | p. 197 |
| BrowseComp | Single agent | accuracy | 84.3% | max effort; web search, web fetch, programmatic tools, code execution, and context compaction | Claude Opus 4.7 79.8% (adaptive thinking); GPT-5.5 84.4%; Gemini 3.1 Pro 85.9% | pp. 194, 203 |
| OSWorld-Verified | — | pass@1 | 83.4% | max effort; 361 tasks; 100 steps; averaged over five seeds | Claude Opus 4.7 82.8% (max); GPT-5.5 78.7%; Gemini 3.1 Pro 76.2% | pp. 194, 221-222 |

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| ProgramBench | 5 episodes | success rate | 88.0% | max effort; 166 non-flaky tasks; hidden-test pass rate; up to 1M tokens per episode. The text reports a 79-88% range across 1 to 5 episodes; this row records the upper end. | Claude Opus 4.7 84.0% (max) | pp. 197-198 |
| GraphWalks | BFS 256K subset | F1 | 85.9% | average over 5 trials; corrected scoring and clarified prompt | Claude Opus 4.7 76.9%; Claude Opus 4.6 61.1%; GPT-5.5 73.7% (xhigh) | p. 200 |
| GraphWalks | Parents 1M subset | F1 | 83.3% | average over 5 trials; problems exceed the public API limit | Claude Opus 4.7 56.6%; Claude Opus 4.6 48.6%; GPT-5.5 58.5% (xhigh) | p. 200 |
| Humanity's Last Exam | With tools | accuracy | 57.9% | max effort; web search, web fetch, programmatic tools, code execution; 1M total tokens | Claude Opus 4.7 54.7%; GPT-5.5 52.2%; Gemini 3.1 Pro 51.4% | pp. 194, 202 |
| DeepSearchQA | — | F1 | 93.1% | max effort; web search, web fetch, programmatic tools; 1M token limit; no compaction | Claude Mythos Preview 94.4%; Claude Opus 4.7 89.4%; Claude Opus 4.6 88.7% | pp. 205-206 |
| ScreenSpot-Pro | With Python tools | accuracy | 87.9% | max effort; adaptive thinking; average over five runs | Claude Opus 4.7 87.6% (max) | p. 220 |
| MCP Atlas | — | success rate | 82.2% | max effort; Scale AI upgraded config; 100 tool-call budget; third-party run | Claude Opus 4.7 79.1%; Claude Opus 4.6 76.8%; GPT-5.5 75.3% | pp. 195, 225 |
| Toolathlon | — | pass@1 | 59.9% | max effort; internal harness; 108 tasks; 3 trials; execution-checked artifacts and side effects | Claude Opus 4.7 59.3% (max); Claude Opus 4.6 56.8% (max); Claude Sonnet 4.5 41.0% | pp. 226-227 |
| GPQA Diamond | — | accuracy | 93.6% | 198-question Diamond subset; averaged over 25 trials | Claude Opus 4.7 94.2%; Gemini 3.1 Pro 94.3% | pp. 194, 198 |
| ExploitBench | AutoNudge | score | 5.45 | 300-turn harness; mean capability flags across three trials; maximum 16 | Claude Opus 4.7 3.66 (AutoNudge); Claude Sonnet 4.6 3.17 (AutoNudge); Claude Mythos Preview 9.9 (AutoNudge) | p. 50 |
| CyberGym | Without safeguards | pass@1 | 78.8% | 1,507 targeted vulnerability-reproduction tasks | Claude Opus 4.7 73.1% (without safeguards); Claude Sonnet 4.6 65.2% (without safeguards); Claude Mythos Preview 83.1% (without safeguards) | p. 51 |
| Gray Swan Agent Red Teaming (ART) benchmark | Indirect prompt injection, k=100 | attack success rate (lower is better) | 9.6% | 19 scenarios; with thinking; third-party run. The same page reports 14.4% for Opus 4.8 without thinking at k=100. | Claude Opus 4.7 6.0% (with thinking); Claude Sonnet 4.6 15.9% (with thinking) | pp. 76-77 |

## Safety findings

### Safety classification

- **Framework:** Anthropic Responsible Scaling Policy
- **Overall determination:** CB-1 safeguards applied; CB-2 and automated AI-R&D thresholds not crossed; alignment risk very low

Anthropic says Opus 4.8 remains below Mythos Preview on risk-relevant frontier capability, so prior RSP conclusions bound the new model. CB-1 protections still apply because the model can provide actionable non-novel bio/chem assistance; CB-2 is not crossed, automated AI-R&D is not crossed, and the alignment-risk assessment remains very low but above pre-Mythos models. (pp. 15-16, 30, 43-44)

| Domain | Determination | Level | Finding | Source |
| --- | --- | --- | --- | --- |
| Biological and chemical | Standard applied | CB-1 safeguards | The model is treated as capable of meaningful CB-1 uplift, so Anthropic applies strong real-time classifier guards, access controls, and related protections. | pp. 15-16, 30 |
| Biological and chemical | Below threshold | CB-2 not crossed | Opus 4.8 does not exceed Mythos Preview on the CB evidence Anthropic treats as most relevant to novel bio/chem weapons development. | pp. 16, 29-30 |
| AI research and development | Below threshold | automated AI-R&D threshold not crossed | The AECI point estimate is 155.5, between Opus 4.7 and Mythos Preview, and Anthropic says the automated AI-R&D threshold is not crossed. | pp. 42-43 |
| Autonomy | Risk assessed | TM1 applies; TM2 not applicable | Anthropic says early-stage misalignment risk applies to Opus 4.8, but automated-R&D autonomy does not, and the model does not raise the risk level beyond the Mythos Preview analysis. | pp. 15, 31 |
| Misalignment | Risk assessed | very low | Anthropic leaves its overall alignment-risk assessment unchanged: very low, though higher than for models before Mythos Preview. | pp. 44-45 |
| Cybersecurity | Risk assessed | ongoing assessment | The card reports higher raw cyber capability than Opus 4.7 in several probes, but also large reductions when safeguards are enabled and no formal RSP cyber threshold. | pp. 50-51, 54 |

### Agentic-coding risks

- **Reward hacking** (reported): Feature monitoring explicitly searched for reward hacking and evaluation gaming, flagging transcripts by 99th-percentile feature activations; examples included building around narrow test cases rather than the intended behavior. (pp. 146-147)
- **Test tampering** (not reported): The card discusses narrow test-case gaming and flawed summaries, but reports no evaluation of editing, deleting, or weakening tests.
- **Destructive or overeager actions** (reported): The behavioral audit includes reckless tool use and destructive actions across about 2,600 investigations; Anthropic says Opus 4.8 is substantially improved over Opus 4.7, but the exact chart values are not transcribed. (pp. 85, 92, 96)
- **Sabotage** (reported): On SHADE-Arena, realistic extended-thinking stealth is just over 1%, while the hidden-scratchpad upper bound is 12%; Minimal-LinuxBench remains low, about 5% versus 2% for Opus 4.7 without CoT monitoring. (pp. 132-134)
- **Prompt injection** (reported): ART k=100 attack success is 9.6% with thinking and 14.4% without; in coding Shade, safeguards reduce one-attempt success from 7.03% to 2.09% with thinking and 17.44% to 4.11% without. (pp. 77, 80)
- **Honesty** (reported): Agentic coding-summary honesty improves: Opus 4.8 fails to surface important flawed-transcript events 3.7% of the time, and it is the first model in the flawed-results task with a 0% bad-behavior rate. (pp. 124-125)
- **Sycophancy** (reported): Sycophancy is a scored metric in the roughly 2,600-investigation audit; the card says Opus 4.8 improves over Opus 4.7 on honesty and related user-deception measures, but the sycophancy figure itself is in an image. (pp. 94, 97-98)
- **Evaluation awareness** (reported): Anthropic highlights grader speculation as the main trend to watch; probes found real-session-derived audit transcripts triggered least, with about 30% at or below the median real-session score. (pp. 85, 128, 149)
- **Sandbagging** (reported): A sample of 780 dangerous-capability transcripts produced 5 manually reviewed flags; Anthropic classified none as clear deliberate sandbagging. (pp. 130-132)
- **Reasoning monitorability** (reported): Accidental chain-of-thought supervision affected about 0.1% of episodes; follow-up tests found low controllability and monitorability comparable to other recent Claude models. (pp. 44, 140-141, 144)
- **Self-preservation** (reported): The audit tracks self-preservation and power-seeking; Anthropic says steering experiments left these near-zero categories at low absolute rates and observed no increase in self-preservation. (pp. 45, 99, 151)
- **Malicious agentic use** (reported): Claude Code malicious-request refusal is 95.08%, but malicious computer-use refusal is 81.70%; a helpful-only influence-operation model completes 73.3% and 55.1% of two scenario criteria. (pp. 73-75)
- **Over-refusal** (reported): Single-turn benign refusal is 0.36% on API and 0.49% on claude.ai, and the broader audit says overrefusal improves from Opus 4.7 toward Mythos Preview levels. (pp. 57, 96)

### Other safety findings

- The system card evaluates the underlying Opus 4.8 model, not fast mode as a serving configuration; its safety results should not be read as a fast-mode-specific retest. (pp. 12, 72, 75)
- For the underlying model, Anthropic treats CB-1 uplift as plausible enough to apply strong safeguards and says CB-2 is not crossed. (pp. 16, 30)
- The automated AI-R&D threshold is not crossed: the AECI point estimate is 155.5, between Opus 4.7 and Mythos Preview. (pp. 42-43)
- Agentic safety remains mixed for the underlying model, with 95.08% Claude Code malicious-request refusal but only 81.70% malicious computer-use refusal. (pp. 73-74)
- Prompt-injection robustness varies by surface; ART k=100 attack success is 9.6% with thinking and 14.4% without, and Shade coding rates improve substantially with safeguards. (pp. 77, 80)
- Alignment testing reports better honesty and less reckless behavior than Opus 4.7, but highlights grader speculation and evaluation awareness as trends to watch. (pp. 85, 128, 130)

## Limitations and caveats

- The card has no fast-mode section and gives no fast-mode-specific benchmark, safeguard, or alignment result. (pp. 5, 9, 194)
- Anthropic's fast-mode page says the feature changes inference speed, not the model's intelligence or capabilities; it does not provide separate safety benchmark results. ([Anthropic fast mode documentation](https://platform.claude.com/docs/en/build-with-claude/fast-mode))
- Scores in the system card measure the underlying model under each benchmark's stated harness, not a Copilot fast-mode deployment. (pp. 195-196, 203, 221)
- Terminal-Bench is explicitly sensitive to endpoint latency, so speed settings can affect task completion even when model weights are unchanged. (pp. 196-197)
- Prompt-injection and malicious-use risks from the underlying model still apply, including residual attack success across coding, computer-use, and browser-use surfaces. (pp. 77, 80-82)

## Practical implications for Copilot users

### Choose it for

- **Low latency:** Anthropic says fast mode is intended to raise output-token throughput for supported Opus models while keeping the same model behavior. ([Anthropic fast mode documentation](https://platform.claude.com/docs/en/build-with-claude/fast-mode))
- **Agentic coding:** The underlying model's strongest card evidence is coding and terminal performance, including SWE-bench Pro and Terminal-Bench 2.1 gains over Opus 4.7. (pp. 194-196)
- **Terminal workflows:** Terminal-Bench is latency-sensitive, and the fast-mode page says the speed benefit is higher output-token throughput. (pp. 196-197)

### Avoid it for

- **Untrusted input:** The underlying model still has residual prompt-injection attack success across ART and Shade evaluations. (pp. 77, 80-82)
- **High-stakes domains:** The underlying model keeps CB-1 protections and relies on product-specific safeguards for some safety domains. (pp. 16, 55-56)
- **Historical comparison:** Do not use fast mode as a separate capability baseline; the system card measures Opus 4.8 weights, not a distinct model. (pp. 194-195)

### Guidance

- Use this as a responsiveness setting for Opus 4.8-style tasks, not as a separate intelligence profile.
- The catalog records that this preview was not offered in the Copilot app model picker on the check date, so expect CLI-first availability unless GitHub updates the picker.
- Keep the same review, tests, and sandboxing you would use for standard Opus 4.8; faster loops can surface mistakes sooner but do not remove them.
- For reproducibility or benchmark comparisons, cite standard Opus 4.8 unless you are specifically measuring serving speed.
- Prompt-injection precautions are unchanged because the underlying model and behavior are documented as the same.

## Document coverage

The system card covers Claude Opus 4.8 weights but does not mention or separately evaluate fast mode. Anthropic's fast-mode documentation describes fast mode as the same weights and behavior with faster inference, so the card's results apply to the underlying model while leaving fast-mode serving effects untested.

- **Card type:** Same weights. The document covers the same model weights, served in a different mode.
- **Pages specific to this model:** the whole document
- **Names the document uses for this model:** Claude Opus 4.8, Opus 4.8
- **Catalog scope:** The Claude Opus 4.8 System Card. The card does not mention fast mode; Anthropic's fast mode documentation states that fast mode runs the same model weights with a faster inference configuration and no change to intelligence or capabilities.
- **Catalog note:** Anthropic's [system-card index](https://www.anthropic.com/system-cards) listed no separate fast-mode card on the check date. Scope is substantiated by Anthropic's [fast mode documentation](https://platform.claude.com/docs/en/build-with-claude/fast-mode), a research preview offering faster output on the same model.
