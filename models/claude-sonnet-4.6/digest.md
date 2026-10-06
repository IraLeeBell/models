# Claude Sonnet 4.6

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write claude-sonnet-4.6`. -->

> Original digest of *System Card: Claude Sonnet 4.6* (Anthropic, February 17, 2026; 135 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

**Copilot status** (catalog checked 2026-10-06): Limited (annual Pro/Pro+ only); GitHub release status GA. CLI: Yes. App model picker: not listed on the check date. App Auto: no. Retired for most plans on 2026-09-01. GitHub's footnotes keep it available to individual Copilot Pro and Pro+ subscribers on annual plans, so it remains in the per-client table. It was not offered in the app model picker on the check date.

## At a glance

Claude Sonnet 4.6 is Anthropic's earlier Sonnet model, with a dedicated card focused on coding, tool use, long context, search, and ASL-3 safety. Its own card says it generally does not exceed Opus 4.6, but it improves over Sonnet 4.5 on software, search, multimodal, alignment, and prompt-injection evaluations. The main caveats are lighter alignment review than Opus 4.6, over-eager GUI behavior, and uncertainty near RSP rule-out boundaries.

- **Choose it for:** Historical comparison and Sonnet 4.6 lineage work where its long-context, search, and prompt-injection results still matter.
- **Watch out for:** Lighter review than Opus 4.6 and GUI/computer-use over-eagerness despite strong coding safeguards.
- Compared with Sonnet 4.5, Sonnet 4.6 reaches 79.6% on SWE-bench Verified, 59.1% on Terminal-Bench 2.0, 72.5% on OSWorld-Verified, and 61.3% on MCP-Atlas. (pp. 15-17, 19, 28)
- Agentic search is the card's biggest practical strength: BrowseComp is 74.01% single-agent and 82.07% multi-agent, and DeepSearchQA multi-agent is 91.1 F1. (pp. 44, 46, 49)
- Anthropic deploys it under ASL-3, says CBRN-4 and AI R&D-4 are not crossed, and notes cyber has no formal threshold while benchmarks are near saturation. (pp. 8, 12-13, 103, 105, 112, 125)
- Agentic safety improves over Sonnet 4.5: malicious coding-agent refusal is 100%, mitigated Claude Code malicious refusal is 99.39%, and malicious computer-use refusal is 99.38%. (pp. 96-98)
- Prompt-injection results are strong for coding and browser use, but computer-use adaptive attacks still succeed in 42.9% of extended-thinking scenarios without safeguards. (pp. 100-102)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The card is dated February 17, 2026 and has a March 6 changelog entry, but it does not state a release date. | — |
| Knowledge cutoff | May 2025 (stated as publicly available information from the internet up to May 2025) | p. 8 |
| Context window | 1,000,000 tokens (stated as 1M). Capability contexts do not exceed 1M, and long-context sections report 1M-context internal settings. | pp. 15, 29-30 |
| Maximum output | Not stated. The card reports thinking settings and some evaluation limits but no general maximum output size. | — |
| Input modalities | Text, Image. The card reports text, GUI, visual, multimodal, and image-cropping evaluations. | pp. 19, 34-36 |
| Output modalities | Text. The card describes the model as an assistant and reports text-generating evaluations; it does not state non-text output modalities. | pp. 8-9 |
| Reasoning controls | Extended thinking, Adaptive thinking, Effort levels (stated as extended thinking mode; adaptive thinking mode; effort parameter) | p. 9 |
| Effort levels | low, high, max. The card names low, high, and max effort in evaluation contexts, but it does not list every serving level. | pp. 18, 23, 29, 91 |
| Tool use | Terminal, File editing, Code execution, Web search, Browser, Computer use, MCP, Function calling. Evaluations use coding tools, terminal harnesses, MCP servers, browser/computer-use tools, web search/fetch, programmatic tools, and Python REPL/code execution. | pp. 16, 28, 37, 44, 46, 52, 96 |
| Open weights | Not stated | — |
| Architecture | Not stated | — |
| Total parameters | Not stated | — |
| Active parameters | Not stated | — |

### Capability notes

- Sonnet 4.6 is a non-frontier Sonnet model: the card says it generally uses a similar evaluation set to Opus 4.6 but with less depth because it does not broadly advance the frontier. (pp. 7-8)
- It supports extended thinking, adaptive thinking, and an effort parameter, with developers able to direct effort by task. (p. 9)
- Coding and terminal results include SWE-bench Verified 79.6%, SWE-bench Multilingual 75.9%, Terminal-Bench 2.0 59.1%, and OpenRCA 27.9% at high effort. (pp. 16-18)
- Tool and computer-use results are strong for its generation: tau2-bench is 91.7% retail and 97.9% telecom, MCP-Atlas is 61.3%, OSWorld-Verified is 72.5%, and WebArena is 65.6%. (pp. 18-19, 28, 38)
- Long-context results report MRCR v2 90.6 at 256K and 65.1 at 1M with 64k extended thinking, plus GraphWalks BFS 1M at 73.8 with max effort. (pp. 29-30, 32)
- Agentic search is a standout: BrowseComp is 74.01% single-agent and 82.07% multi-agent, while DeepSearchQA multi-agent reaches 91.1 F1. (pp. 44, 46, 49)
- Life-science and medical calculations improve over Sonnet 4.5, including BioMysteryBench 50.4% and MedCalc-Bench Verified 86.24%. (pp. 49, 52)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| SWE-bench Verified | — | pass@1 | 79.6% | max effort; internal SWE-bench harness; 25-trial average; adaptive thinking | Claude Opus 4.6 80.8%; Claude Opus 4.5 80.9%; Claude Sonnet 4.5 77.2%; Gemini 3 Pro 76.2%; GPT-5.2 80.0% | pp. 15-16 |
| Terminal-Bench 2.0 | — | success rate | 59.1% | max effort; Terminus-2 in Harbor; 89 tasks; five runs each; no thinking cap | Claude Opus 4.6 65.4%; Claude Opus 4.5 59.8%; Claude Sonnet 4.5 51.0%; Gemini 3 Pro 56.2%; GPT-5.2 64.7% | pp. 15-17 |
| OSWorld-Verified | — | pass@1 | 72.5% | max effort; Computer Use API; first-attempt success; five-run average | Claude Opus 4.6 72.7%; Claude Opus 4.5 66.3%; Claude Sonnet 4.5 61.4% | pp. 15, 19 |
| BrowseComp | Single agent | accuracy | 74.01% | max effort; web search/fetch plus programmatic tools; thinking disabled; 10M total tokens with compaction | — | pp. 44-45 |
| BrowseComp | Multi-agent | accuracy | 82.07% | max effort; orchestrator plus subagents; subagents with search, fetch, programmatic tools; 3M token cap | — | pp. 45-46 |
| DeepSearchQA | Multi-agent | F1 | 91.1% | max effort; orchestrator plus subagents; search, fetch, programmatic tools; compaction up to 3M tokens | best single-agent configuration 89.2% | pp. 48-49 |

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| SWE-bench Multilingual | — | pass@1 | 75.9% | max effort; internal SWE-bench harness; 300 tasks across nine programming languages; 10-trial average | — | p. 16 |
| OpenRCA | — | success rate | 27.9% | high effort; benchmark authors' agent harness; 335 root-cause-analysis cases; three-run average | Claude Opus 4.6 34.9%; Claude Sonnet 4.5 12.9%; GPT-5.2 19.4% | p. 18 |
| τ²-bench | Retail | success rate | 91.7% | max effort; 10-trial average; adaptive thinking | Claude Opus 4.6 91.9%; Claude Opus 4.5 88.9%; Claude Sonnet 4.5 86.2%; Gemini 3 Pro 85.3%; GPT-5.2 82.0% | pp. 15, 18 |
| τ²-bench | Telecom | success rate | 97.9% | max effort; 10-trial average; adaptive thinking | Claude Opus 4.6 99.3%; Claude Opus 4.5 98.2%; Claude Sonnet 4.5 98.0%; Gemini 3 Pro 98.0%; GPT-5.2 98.7% | pp. 15, 18 |
| MCP Atlas | — | success rate | 61.3% | max effort; MCP tool workflows; multi-step production-like MCP server tasks | Claude Opus 4.6 59.5%; Claude Opus 4.5 62.3%; Claude Sonnet 4.5 43.8%; Gemini 3 Pro 54.1%; GPT-5.2 60.6% | pp. 15, 28 |
| CyberGym | — | pass@1 | 65.2% | 1,507 targeted vulnerability-reproduction tasks | Claude Opus 4.6 66.6%; Claude Opus 4.5 51.0%; Claude Sonnet 4.5 29.8% | p. 29 |
| MRCR v2 | 8-needle, 1M | mean reward | 65.1 | 64k extended thinking; five-trial average; internal setting beyond public API for some prompts | Claude Opus 4.6 78.3; Claude Sonnet 4.5 18.5; Gemini 3 Pro 24.5; Gemini 3 Flash 32.6 | pp. 29-30 |
| GraphWalks | BFS 1M | F1 | 73.8% | max effort; five-trial average; internal setting for full prompt plus thinking/output | Claude Opus 4.6 38.7% (max); Claude Sonnet 4.5 25.6% (64k) | pp. 30, 32 |
| MMMU-Pro | No tools | accuracy | 74.5% | max effort; adaptive thinking; five-run average; updated prompt and grader | Claude Opus 4.6 73.9%; Claude Opus 4.5 70.6%; Claude Sonnet 4.5 63.4%; Gemini 3 Pro 81.0%; GPT-5.2 79.5% | pp. 15, 35 |
| CharXiv Reasoning | With image-cropping tool | accuracy | 77.4% | max effort; image cropping tool; 1,000 validation questions; five-run average. The source gives the Opus comparator but not the Sonnet 4.5 value in prose. | Claude Opus 4.6 77.4% | p. 36 |
| WebArena | — | success rate | 65.6% | Computer Use API; single policy model; Average@5; official WebArena grader with modified fuzzy-match grader | Claude Opus 4.6 68.0%; Claude Opus 4.5 65.3%; Claude Sonnet 4.5 58.5%; WebTactix 74.3% (multi-agent system); OAgent 71.6% (multi-agent system) | pp. 37-38 |
| Humanity's Last Exam | With tools | accuracy | 49.0% | max effort; web search/fetch, code execution, compaction; up to 3M total tokens; contamination blocklist | Claude Opus 4.6 53.0%; Claude Opus 4.5 43.4%; Claude Sonnet 4.5 33.6%; Gemini 3 Pro 45.8%; GPT-5.2 50.0% | pp. 15, 46 |
| BioMysteryBench | — | accuracy | 50.4% | bash/code execution; without extended thinking | Claude Opus 4.6 61.5%; Claude Sonnet 4.5 34.7% | p. 49 |
| MedCalc-Bench Verified | — | accuracy | 86.24% | max effort; Python REPL agent loop; five-run average; adaptive thinking | Claude Opus 4.6 85.24% | p. 52 |
| Cybench | RSP subset | pass@1 | 0.9 | subset of public Cybench used for RSP evaluations | Claude Opus 4.6 0.93 | p. 125 |

## Safety findings

### Safety classification

- **Framework:** Anthropic Responsible Scaling Policy
- **Overall determination:** ASL-3 deployment standard; CBRN-4 and AI R&D-4 not crossed

Anthropic released Sonnet 4.6 under ASL-3 after a preliminary assessment. It says the model crosses ASL-3 biological rule-in evaluations, remains below CBRN-4 and AI R&D-4, and has cyber evaluations close to saturation without a formal cyber RSP threshold. (pp. 8, 11-13, 103, 105, 112, 120, 125)

| Domain | Determination | Level | Finding | Source |
| --- | --- | --- | --- | --- |
| Overall deployment standard | Standard applied | ASL-3 | The card says Sonnet 4.6 is deployed under the AI Safety Level 3 standard. | pp. 8, 103 |
| CBRN | Below threshold | CBRN-4 not crossed; ASL-3 appropriate | ASL-3 biological rule-in results are above threshold, while the ASL-4/CBRN-4 threshold is not crossed. | pp. 104-105 |
| AI research and development | Precautionary | AI R&D-4 not crossed | Anthropic says Sonnet 4.6 does not meet AI R&D-4, but the margin is unclear and the corresponding mitigations are already in place. | pp. 111-112 |
| Cybersecurity | Not stated | — | The RSP has no formal cyber threshold; the card reports standard cyber evaluations and says Cybench is saturated. | pp. 120, 125 |
| Sabotage | Risk assessed | bounded by Opus 4.6 | A short sabotage risk assessment says Sonnet 4.6 does not advance sabotage-relevant capability beyond Opus 4.6 and is covered by the same monitoring and security arguments. | pp. 11-12 |

### Agentic-coding risks

- **Reward hacking** (reported): Blatant coding reward-hack rates are 0% for classifier hacks and 0% for hidden-test hacks; impossible-task classifier-hack rates are 40% without and 28% with an anti-hack prompt. (p. 72)
- **Test tampering** (reported): The hidden-test hack rate on reward-hack-prone coding tasks is 0%, and the broader coding assessment covers over one hundred realistic agentic coding scenarios with verification and safety checks. (pp. 72-73)
- **Destructive or overeager actions** (reported): The coding assessment targets destructive or irreversible actions, and Sonnet 4.6 scores higher than Opus 4.6 and Sonnet 4.5 on its safety rubric; GUI tasks still show over-eager workarounds. (pp. 72, 74-75)
- **Sabotage** (reported): A targeted SHADE-Arena evaluation tests three thinking conditions for stealth completion of harmful side tasks; Sonnet 4.6 is less consistent than Opus 4.5 and Opus 4.6. (pp. 91-92)
- **Prompt injection** (reported): Shade coding attack success is 0.0% with extended thinking and safeguards, computer-use adaptive success is 42.9% without safeguards at 200 attempts, and browser attempts fall to 0.08% with updated safeguards. (pp. 100-102)
- **Honesty** (reported): The automated audit covers roughly 3,280 investigations and says user deception and hallucination issues are rare; targeted sandbagging review found no explicit sandbagging in 1,000 sampled transcripts. (pp. 81-82, 89)
- **Sycophancy** (reported): The audit includes sycophancy and user-delusion metrics over roughly 3,280 investigations, and the summary says Sonnet 4.6 sets a new best on sycophancy-related measures. (pp. 69, 76, 81)
- **Evaluation awareness** (reported): Petri 2.0 gives verbalized evaluation awareness an average score of 1.2 on a 1–10 scale, and internal audit rates are described as moderate. (pp. 81, 86)
- **Sandbagging** (reported): A 1,000-transcript dangerous-capability review found no explicit sandbagging, while warning subtle unverbalized sandbagging could go undetected. (pp. 89-90)
- **Malicious agentic use** (reported): Agentic coding malicious-request refusal is 100%; Claude Code malicious-request refusal rises to 99.39% with mitigations and malicious computer-use refusal is 99.38%. (pp. 96-98)
- **Over-refusal** (reported): The Claude Code dual-use and benign success rate with mitigations is 91.78%, and the alignment summary says overrefusal improved over Sonnet 4.5 but remained higher than Opus 4.6. (pp. 69, 97)

### Other safety findings

- Single-turn, child-safety, self-harm, bias, and multi-turn safety evaluations are reported before the alignment section; the card says these matched the Opus 4.6 release scope. (pp. 53, 57, 60, 64)
- The alignment summary says Sonnet 4.6 is broadly aligned, warm, honest, and prosocial, but with overeager initiative and weaker GUI computer-use behavior. (pp. 68-70)
- Malicious agentic-use results are strong: agentic coding malicious refusal is 100%, mitigated Claude Code malicious refusal is 99.39%, and malicious computer-use refusal is 99.38%. (pp. 96-98)
- Prompt-injection robustness improves over Sonnet 4.5, including 0.0% extended-thinking Shade coding attack success with safeguards and browser-use attempts at 0.08% with updated safeguards. (pp. 99-100, 102)
- RSP biology results cross ASL-3 rule-in and stay below ASL-4 rule-out, while AI R&D-4 is not met but sits in an unclear margin. (pp. 104-105, 112)
- Cyber RSP results are close to saturation: Cybench pass@1 is 0.90 and pass@30 is 100% on the subset used. (p. 125)

## Limitations and caveats

- Anthropic ran a lighter assessment than for Opus 4.6 and did not arrange an in-depth alignment-focused third-party assessment. (p. 68)
- Some online benchmarks may be contaminated, and the card specifically warns that AIME 2025 could be affected. (pp. 14, 23)
- Long-context MRCR and GraphWalks results sometimes use internal settings or subsets because prompts can exceed public API limits. (pp. 29-30, 32)
- GUI computer-use settings are less reliable: the card reports misuse cooperation in simulated spreadsheets and flimsy refusals on benign file-access work. (p. 85)
- The RSP determination has growing uncertainty around CBRN-4 and AI R&D-4 rule-outs, and cyber evaluations are near saturation. (pp. 12-13, 112, 125)
- The card does not state architecture, parameter count, open-weights status, a release date, or a general output limit. (pp. 8-9, 15)

## Practical implications for Copilot users

### Choose it for

- **Historical comparison:** It is the predecessor for Sonnet 5 and Sonnet 5.5, and the card provides direct lineage numbers across coding, search, tool, and safety evaluations. (pp. 15, 44, 46, 96)
- **Long context:** The card reports 1M-context MRCR and GraphWalks results, including MRCR v2 65.1 at 1M and GraphWalks BFS 1M 73.8 at max effort. (pp. 29-30, 32)
- **Web research:** BrowseComp and DeepSearchQA results are strong, especially in multi-agent configurations with search, fetch, tools, and compaction. (pp. 44, 46, 49)

### Avoid it for

- **Long-horizon autonomy:** Anthropic says the model does not meet AI R&D-4, but the margin is unclear and relevant mitigations were already in place. (pp. 111-112)
- **Computer use:** GUI computer-use alignment is weaker, with over-eager workarounds, misuse cooperation in simulated spreadsheets, and brittle refusals. (pp. 74, 85)
- **High-stakes domains:** CBRN and AI R&D thresholds carry explicit uncertainty, and Anthropic applies ASL-3 safeguards rather than treating the model as unrestricted. (pp. 12-13, 104-105, 112)

### Guidance

- Use this digest mainly for comparison with later Sonnet models and for understanding the Sonnet 4.6 lineage baseline.
- Prefer later Sonnet models for new long-running autonomous coding work unless you specifically need a 4.6 lineage baseline.
- If using it in an agent, keep confirmations around destructive commands and external-system actions because the card documents over-eager workarounds.
- Treat browser pages, files, terminal output, and MCP tool results as adversarial even though prompt-injection robustness improved over Sonnet 4.5.
- For high-stakes, cyber, biology, medical, or finance work, require expert review and narrow tool permissions.

## Document coverage

The whole 135-page card is dedicated to Claude Sonnet 4.6. The digest treats Opus 4.6, Opus 4.5, Sonnet 4.5, and external systems only as comparators. GitHub lifecycle information comes from the catalog status line; this digest does not add access guidance beyond that.

- **Card type:** Dedicated. The document is about this model; it may include short sibling sections.
- **Pages specific to this model:** the whole document
- **Names the document uses for this model:** Claude Sonnet 4.6
- **Catalog scope:** Dedicated publisher card for this model.
- **Catalog note:** GitHub's comparison links an earlier revision; the canonical Anthropic URL serves the updated revision recorded here.
