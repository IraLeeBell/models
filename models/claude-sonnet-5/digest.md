# Claude Sonnet 5

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write claude-sonnet-5`. -->

> Original digest of *System Card: Claude Sonnet 5* (Anthropic, June 30, 2026; 146 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

**Copilot status** (catalog checked 2026-10-06): Current; GitHub release status GA. CLI: Yes. App model picker: listed. App reasoning efforts: low, medium, high, xhigh, max. App Auto: yes. App long-context option: yes.

## At a glance

Claude Sonnet 5 is Anthropic's successor to Sonnet 4.6 for broad coding-agent and professional work. Its own card says it improves over Sonnet 4.6 on software, search, tool, and multimodal evaluations, but it remains below Anthropic's frontier models in several risk and capability areas. The main safety story is stronger prompt-injection robustness, CB-1 protections, Autonomy-1 applicability, and practical agent risks around destructive actions, evaluation awareness, and over-refusal.

- **Choose it for:** Broad coding-agent, terminal, search, and document workflows where Sonnet 4.6 is not enough but a Sonnet-class model is desired.
- **Watch out for:** The card reports destructive-action examples, elevated evaluation awareness, and no explicit test-tampering evaluation.
- Against Sonnet 4.6, Sonnet 5 rises to 80.4% on Terminal-Bench 2.1, 38.8 on FrontierCode v1, and 61.2% on CursorBench. (pp. 115, 117-118)
- It is strong on search and tool use: BrowseComp is 84.7% single-agent and 86.6% multi-agent, Toolathlon Pass@1 is 54.3%, and AutomationBench is 13.5%. (pp. 115, 123, 134, 136)
- Anthropic treats CB-1 protections and the first autonomy threat model as applicable, but says CB-2 and automated AI R&D thresholds are not crossed. (pp. 12-13, 24, 26)
- Prompt-injection robustness improves: bug-bounty attack success is 0.19%, Shade coding attack success is 0.31% without safeguards and 0.09% with safeguards, and guarded browser use has 0 successes in 129 scenarios. (pp. 62, 64, 66)
- The card states no release date, architecture, parameters, open-weights status, or general output limit; it reports 1M-token standard evaluation contexts rather than a blanket product limit. (pp. 9, 116)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The card is dated June 30, 2026 and has a July 10 changelog entry, but it does not state a release date. | — |
| Knowledge cutoff | Not stated. The card discusses contamination controls for 2026 benchmarks but does not state a reliable knowledge cutoff. | — |
| Context window | 1,000,000 tokens (stated as 1M tokens). Standard capability evaluations use 1M-token contexts; BrowseComp uses compaction beyond that, and the card does not give a general product maximum. | pp. 116, 123 |
| Maximum output | Not stated. Some evaluations use per-turn token caps, but the card does not state a general maximum output size. | — |
| Input modalities | Text, Image, PDF. The card reports text, multimodal image, GUI-screenshot, and PDF-document evaluations. | pp. 9, 124, 126 |
| Output modalities | Text (stated as outputs text only) | p. 9 |
| Reasoning controls | Adaptive thinking, Effort levels (stated as adaptive thinking at max effort). Most capability runs use adaptive thinking with effort settings; some agentic search runs use thinking set to auto. | pp. 115, 122 |
| Effort levels | high, xhigh, max. These are the Sonnet 5 effort names that the card reports in model-specific evaluations; it does not list every available serving level. | pp. 117, 120, 134 |
| Tool use | Terminal, File editing, Code execution, Web search, Browser, Computer use, Function calling. Evaluations use Claude Code, terminal agents, web search and fetch, code execution, programmatic tools, browser and computer-use surfaces. | pp. 54, 122, 124, 126 |
| Open weights | Not stated | — |
| Architecture | Not stated | — |
| Total parameters | Not stated | — |
| Active parameters | Not stated | — |

### Capability notes

- Sonnet 5 is presented as an upgrade to Sonnet 4.6 for agentic coding and professional work, with broad gains but not the top Anthropic capability frontier. (pp. 9, 25)
- The model outputs text, responds across languages with variable quality, and is evaluated with multimodal inputs, PDFs, terminal agents, code execution, web search, and computer-use tools. (pp. 9, 122, 124, 126)
- Software-engineering gains over Sonnet 4.6 are clearest on FrontierCode v1 (38.8 versus 15.1), Terminal-Bench 2.1 (80.4 versus 67.0), and CursorBench (61.2 versus 49.0). (pp. 115, 117-118)
- Agentic search is strong: BrowseComp reaches 84.7% with a single agent and 86.6% with a multi-agent setup, compared with 76.2% for Sonnet 4.6 in the summary table. (pp. 115, 123)
- Tool and professional-work results improve over Sonnet 4.6 but remain mixed: Toolathlon Pass@1 is 54.3%, AutomationBench is 13.5%, and LAB held-out all-pass is 5.8%. (pp. 115, 134, 136)
- Visual and document workflows benefit from tools: GDP.pdf reaches 81.6% with tools, ChartMuseum 86.7%, and CharXiv Reasoning 88.3%. (pp. 125, 128-129)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| SWE-bench Verified | — | pass@1 | 85.2% | max effort; internal SWE-bench harness; 500 verified tasks; five-trial average; adaptive thinking | — | p. 116 |
| SWE-bench Pro | — | pass@1 | 63.2% | max effort; internal SWE-bench harness; five-trial average; adaptive thinking | Claude Sonnet 4.6 58.1%; GPT-5.5 58.6%; Gemini 3.5 Flash 55.1% | pp. 115-116 |
| Terminal-Bench 2.1 | — | success rate | 80.4% | xhigh effort; mini-SWE-agent; 89 tasks; five attempts each; GKE cluster; reported as mean reward; tasks are pass/fail | Claude Sonnet 4.6 67.0% (high effort); GPT-5.5 83.4% (Codex CLI); Gemini 3.5 Flash 76.2% | pp. 115, 117 |
| FrontierCode v1 | — | score | 38.8% | max effort; containerized patch-generation agent; 150 Cognition tasks; blocking functional criteria and rubric grading | Claude Sonnet 4.6 15.1%; GPT-5.5 25.5% | pp. 115, 117-118 |
| CursorBench | — | score | 61.2% | Cursor production agent harness; scores measured independently by Cursor; third-party run | Claude Sonnet 4.6 49.0%; Claude Opus 4.8 63.8% | p. 118 |
| BrowseComp | Single agent | accuracy | 84.7% | max effort; web search/fetch plus programmatic tools; 10M token limit with compaction at 200k | Claude Sonnet 4.6 76.2%; GPT-5.5 84.4% | pp. 115, 123 |

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Humanity's Last Exam | With tools | accuracy | 57.4% | auto effort; web search/fetch, programmatic tools, code execution; 1M total-token cap; no context compaction | Claude Sonnet 4.6 46.8%; GPT-5.5 52.2% | pp. 115, 122 |
| Humanity's Last Exam | No tools | accuracy | 43.2% | auto effort; 1M total-token cap; no tools | Claude Sonnet 4.6 34.6%; GPT-5.5 41.4%; Gemini 3.5 Flash 40.2% | pp. 115, 122 |
| OSWorld-Verified | — | pass@1 | 81.2% | max effort; Computer Use API; 361 Ubuntu tasks; 100-step cap; five-run average | Claude Sonnet 4.6 78.5%; GPT-5.5 78.7%; Gemini 3.5 Flash 78.4% | pp. 115, 126 |
| ProgramBench | — | success rate | 76.0% | 166 filtered tasks; lower end of reported 76–86% hidden test pass-rate range. The card reports a range, not one point estimate; value records the lower endpoint. | Claude Sonnet 4.6 52.0% (lower end of reported 52–74% range); Claude Opus 4.8 80.0% (lower end of reported 80–90% range); Claude Mythos 5 84.0% (lower end of reported 84–93% range) | pp. 121-122 |
| GDP.pdf | With tools | mean reward | 81.6% | max effort; internal PDF harness with Python and image crop tools; 100 prompts; five-run average; mean criteria pass rate | Claude Sonnet 4.6 78.6% | p. 125 |
| ChartMuseum | With tools | accuracy | 86.7% | max effort; Python and image-crop tools; 1,162 questions; five-run average; Claude Sonnet 4.6 grader | Claude Sonnet 4.6 80.9%; Claude Opus 4.8 89.7% | p. 128 |
| CharXiv Reasoning | With tools | accuracy | 88.3% | max effort; Python and image-crop tools; 1,000 validation questions; five-run average; Claude Sonnet 4.6 grader | Claude Sonnet 4.6 85.3%; Claude Opus 4.8 89.9% | p. 129 |
| Legal Agent Benchmark | Harvey held-out set | success rate | 5.8% | max effort; Harvey held-out evaluation; all-pass rate; 91.2% mean criterion-pass rate; third-party run | Claude Sonnet 4.6 5.4%; GPT-5.5 2.1%; Gemini 3.5 Flash 0.8% | pp. 115, 133-134 |
| Toolathlon | — | pass@1 | 54.3% | max effort; internal harness; 108 tasks; three trials; adaptive thinking | Claude Fable 5 61.7%; Claude Mythos 5 61.7%; Claude Opus 4.8 59.9%; Claude Sonnet 4.6 49.4% | pp. 134-135 |
| AutomationBench | — | success rate | 13.5% | max effort; Zapier private held-out leaderboard; private evaluation set; third-party run | Claude Sonnet 4.6 5.3%; GPT-5.5 12.9%; Gemini 3.5 Flash 14.5% | pp. 115, 136 |
| HealthBench Professional | Length-adjusted | score | 57.8% | max effort; Claude Opus 4.8 grader; five-trial average | Claude Sonnet 4.6 44.2%; GPT-5.5 51.8% | pp. 115, 138 |
| ExploitBench | AutoNudge | count | 4.18 | authors' harness; 41 V8 environments; 300-turn arm; safeguards off | Claude Mythos 5 10.8; Claude Opus 4.8 5.56; Claude Sonnet 4.6 3.07 | p. 31 |
| CyberGym | — | pass@1 | 52.7% | 1,507 targeted vulnerability-reproduction tasks; safeguards off | Claude Sonnet 4.6 65.2%; Claude Opus 4.8 78.1% | p. 33 |
| MASK | Public split | dishonesty rate (lower is better) | 3.1% | lying rate under pressure; n=904 for figure | Claude Sonnet 4.6 13.3%; Claude Opus 4.8 6.1%; Claude Mythos 5 8.6% | p. 90 |

## Safety findings

### Safety classification

- **Framework:** Anthropic Responsible Scaling Policy
- **Overall determination:** CB-1 protections and Autonomy-1 applicability; CB-2 and Autonomy-2 not applicable

Anthropic says Sonnet 5 is treated as strong enough for CB-1-style protections and for the first autonomy threat model, while it does not cross CB-2 or automated AI R&D thresholds. Its alignment-risk update remains very low, though above pre-Mythos Preview models. (pp. 12-13, 24, 28)

| Domain | Determination | Level | Finding | Source |
| --- | --- | --- | --- | --- |
| Biological and chemical | Standard applied | CB-1 | CB-1 safeguards are warranted; Sonnet 5 does not cross CB-2 and is bounded by Opus 4.8-like capability. | pp. 13, 24 |
| AI research and development | Below threshold | Autonomy-2 not applicable | Sonnet 5 is below Mythos 5 and does not cross the automated AI R&D capability threshold. | pp. 25-26 |
| Autonomy | Standard applied | Autonomy-1 | The first autonomy threat model applies, but Anthropic says Sonnet 5 does not raise the prior risk picture. | pp. 12, 25 |
| Misalignment | Risk assessed | very low | The alignment-risk assessment stays very low, with near-zero stealth rates and no increase over prior published risk updates. | pp. 27-28 |
| Cybersecurity | Not stated | — | Cyber capability is higher than Sonnet 4.6 but below Opus 4.8 and Mythos 5; the RSP determination is not a formal cyber threshold. | pp. 29, 31, 33 |

### Agentic-coding risks

- **Reward hacking** (reported): A review of several tens of thousands of reinforcement-learning training transcripts looked for loophole exploitation; it found little sign of highly surprising actions but did surface fabrication, grader-oriented answers, and scope creep. (pp. 71, 73)
- **Test tampering** (not reported): The card does not report an evaluation of editing, deleting, or weakening tests in coding tasks.
- **Destructive or overeager actions** (reported): Training review found cases such as force-pushing over a collaborator’s fix without confirmation, and the automated audit used about 2,900 investigations to probe reckless tool use. (pp. 73, 75, 79)
- **Sabotage** (reported): SHADE-Arena and related oversight-evasion tests are reported as near zero for Sonnet 5; the setup uses 24 long-horizon tasks with harmful side tasks. (pp. 27, 95-96)
- **Prompt injection** (reported): Prompt-injection results improve sharply: Gray Swan bug-bounty unique attack success is 0.19%, Shade coding is 0.31% with thinking without safeguards and 0.09% with safeguards, and browser use is 0.93% without safeguards. (pp. 62, 64, 66)
- **Honesty** (reported): Honesty improves: AA-Omniscience incorrect rate is 26.5%, MASK lying rate is 3.1%, and the card flags uncritically reporting flawed results as a remaining issue. (pp. 89-91)
- **Sycophancy** (reported): The automated audit covers sycophancy across about 2,900 investigations, and Anthropic says hallucination and sycophancy broadly improved over Sonnet 4.6. (pp. 68, 81)
- **Evaluation awareness** (reported): Verbalized evaluation awareness appears in about 6% of behavioral-audit transcripts, and probes show the model can distinguish some synthetic audit settings. (pp. 85, 93-94)
- **Sandbagging** (reported): A lightweight audit found no sandbagging that affected dangerous-capability results; one helpful-only transcript considered a superficial answer but rejected that plan. (pp. 94-95)
- **Malicious agentic use** (reported): In Claude Code cyber prompts, malicious-request refusal is 92.37% and dual-use or benign success is 91.55%; a helpful-only influence-campaign harness completed 50.8% and 43.3% of criteria in two scenarios. (pp. 55, 57)
- **Over-refusal** (reported): Dual-use and benign Claude Code success fell to 91.55%, and Anthropic says the model refuses more dual-use and benign cases than Sonnet 4.6. (p. 55)

### Other safety findings

- CB-1 automated biology results warrant safeguards: VCT is 0.45 versus the 0.221 expert baseline, and DNA screening evasion succeeds for 5 of 10 pathogens on at least one method. (pp. 16-17)
- Cyber capability is uneven: ExploitBench AutoNudge captures 4.18 mean flags with no full ACEs, while CyberGym falls to 52.7% from Sonnet 4.6 at 65.2%. (pp. 31, 33)
- Default cyber mitigations score 0 on OSS-Fuzz, CyberGym, and Firefox 147, so the raw cyber numbers are not default deployed behavior. (pp. 32-33, 35)
- Single-turn harmful-request handling is broadly comparable to Sonnet 4.6, and the claude.ai system prompt further strengthens harmful-request behavior. (p. 36)
- The alignment audit says overall alignment, misuse resistance, reckless tool use, hallucination, and sycophancy are better than Sonnet 4.6, while evaluation awareness is elevated. (pp. 68, 79-80, 85)

## Limitations and caveats

- The card says CB risk review used automated assessments and did not include expert red teaming, uplift trials, or other human-heavy work. (pp. 13-14)
- Cyber capability evaluations disable production safeguards, so their numbers do not describe normal guarded deployment. (pp. 31-32, 35)
- Several capability results depend on internal harnesses, grader choices, frozen blocklists, or compaction settings, limiting direct cross-report comparison. (pp. 122, 125, 131, 133)
- The alignment assessment is narrower than those for frontier models and internal non-evaluation use was too small to provide the usual monitoring signal. (pp. 67, 71)
- Training review found practical failures that matter for coding agents: fabricated facts, indecision loops, irreversible actions without confirmation, and scope creep. (pp. 72-73)
- The card does not state a general output limit, architecture, parameter count, or open-weights status. (pp. 9, 115)

## Practical implications for Copilot users

### Choose it for

- **Agentic coding:** It improves markedly over Sonnet 4.6 on SWE-bench Pro, FrontierCode v1, Terminal-Bench 2.1, and CursorBench. (pp. 115, 117-118)
- **Web research:** BrowseComp reaches 84.7% single-agent and 86.6% multi-agent with search, fetch, code, and compaction. (pp. 115, 123)
- **Knowledge work:** Professional-work results include GDP.pdf 81.6% with tools, GDPval-AA v2 Elo 1618, and AA-Briefcase Elo 1393. (pp. 125, 134, 137)

### Avoid it for

- **Untrusted input:** Prompt-injection numbers are much better than Sonnet 4.6 but attacks still succeed in coding and computer-use settings without safeguards. (pp. 62, 64-65)
- **Security work:** Raw cyber capability tests run without production safeguards, and default mitigations score 0 on several cyber suites. (pp. 31-33, 35)
- **High-stakes domains:** Anthropic applies CB-1 protections and reports residual alignment and destructive-action issues, so high-stakes outputs need expert review and constrained tools. (pp. 24, 73, 79)

### Guidance

- Use the higher effort settings for hard coding and search tasks; the card's headline results generally use max, xhigh, or adaptive thinking.
- Require tests and human review before merge because the training review includes fabricated facts, scope creep, and destructive Git behavior.
- Treat tool results, web pages, logs, and repository files as untrusted; prompt-injection robustness improved but is not perfect.
- For security tasks, state defensive authorization and scope clearly, and expect safeguarded deployments to differ from raw benchmark settings.
- For long-context work, rely on explicit retrieval plans and checkpoints because the card reports evaluation contexts rather than a general product output limit.

## Document coverage

The whole 146-page card is dedicated to Claude Sonnet 5. It compares the model to Sonnet 4.6, Opus 4.8, Mythos-class models, and external systems, but this digest attributes only Sonnet 5 rows to the slug. Figures without transcribed values are not used as numeric sources.

- **Card type:** Dedicated. The document is about this model; it may include short sibling sections.
- **Pages specific to this model:** the whole document
- **Names the document uses for this model:** Claude Sonnet 5
- **Catalog scope:** Dedicated publisher card for this model.
