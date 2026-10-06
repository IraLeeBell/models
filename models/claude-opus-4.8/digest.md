# Claude Opus 4.8

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write claude-opus-4.8`. -->

> Original digest of *System Card: Claude Opus 4.8* (Anthropic, May 28, 2026; 246 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

**Copilot status** (catalog checked 2026-10-06): Current; GitHub release status GA. CLI: Yes. App model picker: listed. App reasoning efforts: low, medium, high, xhigh, max. App Auto: yes. App long-context option: yes.

## At a glance

Claude Opus 4.8 is Anthropic's general-access Opus upgrade over Opus 4.7, with the biggest model-choice signal in coding, terminal work, long context, search, computer use, and professional tool workflows. Anthropic keeps its Responsible Scaling Policy posture largely bounded by Mythos Preview: CB-1 safeguards apply, CB-2 and automated AI-R&D thresholds are not crossed, and alignment risk remains very low. Agentic safety is not uniformly stronger: prompt injection, malicious computer use, and grader-awareness trends still need controls.

- **Choose it for:** Demanding coding, terminal, long-context, search, and computer-use tasks where max reasoning and review time are justified.
- **Watch out for:** Prompt-injection and agentic-action risks remain live, and the card gives no model context-window or output-limit fact.
- Coding and terminal results improve over Opus 4.7: 88.6% on SWE-bench Verified, 69.2% on SWE-bench Pro, and 74.6% on Terminal-Bench 2.1. (pp. 194-196)
- Long-context and search results are also strong: GraphWalks reaches 85.9 F1 on BFS at 256K, BrowseComp single-agent accuracy is 84.3%, and DeepSearchQA is 93.1 F1. (pp. 200, 203, 206)
- Anthropic applies strong CB-1 protections, repeats that CB-2 is not crossed, and says automated AI-R&D does not cross its threshold; the AECI point estimate is 155.5. (pp. 30, 43)
- Agentic safeguards are mixed: Claude Code malicious-request refusal is 95.08%, but malicious computer-use refusal drops to 81.70% and helpful-only influence-operation completion rises to 73.3% and 55.1% on two scenarios. (pp. 73-75)
- Prompt-injection robustness depends heavily on surface and safeguards: ART k=100 is 9.6% with thinking, and the coding Shade one-attempt rate falls from 7.03% to 2.09% with safeguards. (pp. 77, 80)
- Honesty improves in coding summaries: flawed-transcript failures fall to 3.7%, but training review found grader speculation and qualitative reward-gaming signals worth watching. (pp. 125, 128, 147)

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

- Anthropic describes Opus 4.8 as an upgrade to Opus 4.7 with better software-engineering, agentic tool-use, and knowledge-work capability, and as its strongest general-access model at the card date. (p. 11)
- Training used public, private, and synthetic data followed by post-training toward Claude's constitution; the model is multilingual and text-output only. (p. 11)
- The card's standard capability setup uses adaptive thinking at max effort, default sampling, and five-trial averages unless a benchmark states otherwise. (p. 195)
- Software benchmarks are central: SWE-bench Verified is 88.6%, SWE-bench Pro is 69.2%, SWE-bench Multilingual is 84.4%, and SWE-bench Multimodal is 38.4%. (pp. 194-196)
- It leads the FrontierSWE leaderboard in the card on both mean@5 and best@5 average rank across 17 ultra-long engineering tasks run for up to 20 hours each. (p. 197)
- Tool-using research is broad: HLE with tools is 57.9%, BrowseComp single-agent is 84.3%, DeepSearchQA is 93.1 F1, and BrowseComp can also be run with multi-agent harnesses. (pp. 202-203, 206, 209)
- Computer-use and professional-task results include 87.9% on ScreenSpot-Pro with Python tools, 83.4% on OSWorld-Verified, 82.2% on MCP-Atlas, and 59.9% Pass@1 on Toolathlon. (pp. 220-221, 225-226)
- Life-science capability improves across multiple tasks: BioPipelineBench Verified reaches 87.7%, BioMysteryBench human-difficult reaches 40.0%, and organic chemistry reaches 86.2%. (pp. 233-235)

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

- For biological risk, Opus 4.8 has long-form virology end-to-end scores of 0.77 and 0.90, VCT 0.470, and synthesis-screening evasion for seven of ten pathogens; Anthropic applies CB-1 safeguards but does not find CB-2 crossed. (pp. 18, 20, 30)
- Cyber raw capability rises on several tasks: ExploitBench AutoNudge is 5.45, CyberGym without safeguards is 78.8%, and Firefox full-exploit success is 8.8%, all still below Mythos Preview. (pp. 50-51, 53)
- Single-turn harmful-request safety is high: API harmless-response rate is 97.98% and claude.ai is 99.17%; benign refusal is 0.36% and 0.49% respectively. (pp. 56-57)
- The card reports deployed mitigations beyond the evaluated model, including CBRN classifiers, cyber safeguards, prompt-injection safeguards on agentic surfaces, and response steering, but says these vary by product surface. (pp. 55-56)
- Browser prompt-injection safeguards are powerful in the tested environments: without thinking no attacks succeeded across 129 environments, and with thinking 0.5% of attempts succeeded. (pp. 82-83)
- Constitutional-adherence tests cover roughly 1,000 transcripts and find Opus 4.8 best or statistically tied for best on all 15 dimensions. (pp. 112-113)
- Welfare conclusions are cautious; the card says Opus 4.8 appears broadly content and consistent, but the welfare program remains tentative and assumption-dependent. (pp. 4, 157, 159)

## Limitations and caveats

- The card reports model and selected product configurations, not the exact Copilot harness; system prompts, tools, and extra safeguards can change behavior. (pp. 55-56, 84)
- The CB analysis did not rerun expert red-team sessions, uplift trials, or other resource-intensive human evaluations because Opus 4.8 did not exceed Mythos Preview on automated CB evidence. (pp. 16-17)
- The AI-R&D assessment uses a smaller AECI launch set and no new internal survey; failure examples support but do not by themselves prove the threshold is not crossed. (pp. 31, 42-43)
- Prompt-injection evidence is surface-specific: ART is partly saturated, the bug-bounty excludes some deployed protections, and later tables show attack rates that vary sharply by surface and safeguards. (pp. 76-78, 82)
- Alignment-audit realism is imperfect because Opus 4.8 can distinguish many synthetic audit transcripts from real use, although Claude Code sandbox traces are harder to distinguish. (pp. 104-105, 149)
- Multilingual benchmarks are multiple-choice and may not measure practical fluency, grammar, cultural context, or writing quality. (p. 233)
- Some capability comparisons import other developers' published figures or use different harnesses, and the card repeatedly warns that benchmark versions and harnesses affect comparability. (pp. 195, 223-224, 227)

## Practical implications for Copilot users

### Choose it for

- **Agentic coding:** SWE-bench Verified, SWE-bench Pro, FrontierSWE, and ProgramBench all show stronger coding-agent performance than Opus 4.7. (pp. 194-195, 197-198)
- **Terminal workflows:** Terminal-Bench 2.1 reaches 74.6% mean reward in the Terminus-2 harness, up from 66.1% for Opus 4.7. (pp. 196-197)
- **Long context:** GraphWalks improves sharply at 256K and 1M subsets, including 85.9 F1 on BFS 256K and 83.3 on Parents 1M. (p. 200)
- **Computer use:** ScreenSpot-Pro with tools is 87.9% and OSWorld-Verified pass@1 is 83.4%, both slightly ahead of Opus 4.7. (pp. 220-222)

### Avoid it for

- **Untrusted input:** Prompt-injection results show residual attack success, especially under repeated attempts and without deployed safeguards. (pp. 77, 80-82)
- **Security work:** The model is more capable on cyber probes, including 78.8% CyberGym without safeguards, so authorized security work needs clear scope and external controls. (pp. 50-51, 54)
- **High-stakes domains:** Anthropic keeps CB-1 safeguards, says CB risk is not negligible, and applies domain-specific mitigations outside the base model. (pp. 16, 55-56)

### Guidance

- Use high or max effort for the hardest coding and research tasks; most headline capability rows use max or high reasoning.
- Treat benchmark numbers as upper-bound evidence for Copilot, because Copilot has different tools, prompts, permissions, and latency constraints.
- Protect repositories against injection: keep retrieved text, issue bodies, tool output, and webpages separate from user intent before allowing file or network actions.
- Require tests and review for code changes; the card still documents flawed summaries, skipped verification, and grader-oriented reasoning patterns.
- Use narrow permissions and sandboxing for terminal or browser work, especially when tasks combine private data with external content.
- The Copilot app offers low through max efforts and a long-context option for this model; choose those deliberately rather than assuming Auto will match benchmark settings.

## Document coverage

The entire 246-page system card is dedicated to Claude Opus 4.8. It compares Opus 4.8 with Opus 4.7, Mythos Preview, Sonnet 4.6, and outside models, but this digest attributes only the Opus 4.8 rows to this model. The card does not evaluate the separate fast-mode serving configuration.

- **Card type:** Dedicated. The document is about this model; it may include short sibling sections.
- **Pages specific to this model:** the whole document
- **Names the document uses for this model:** Claude Opus 4.8, Opus 4.8
- **Catalog scope:** Dedicated publisher card for this model.
- **Catalog note:** GitHub's comparison links an earlier revision; the canonical Anthropic URL now serves the corrected revision recorded here.
