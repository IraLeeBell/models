# Kimi K3

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write kimi-k3`. -->

> Original digest of *Kimi K3: Open Frontier Intelligence — Technical Report of Kimi K3* (Moonshot AI, July 23, 2026; 47 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and [system-card.md](system-card.md) for the full text.

**Copilot status** (catalog checked 2026-10-06): Current; GitHub release status GA. CLI: Yes. App model picker: not listed on the check date. App Auto: no. It was not offered in the app model picker on the check date.

## At a glance

Kimi K3 is Moonshot AI's open-weight, native multimodal 2.8T-parameter MoE model with 104B active parameters and a one-million-token context window. The report emphasizes agentic coding, tool use, long-context RL, and open weights, with strong coding and agentic benchmark results. Safety coverage is narrow and mainly cyber capability; no named safety framework is stated.

- **Choose it for:** Large-context, agentic coding and multimodal workflows where open weights and tool-heavy evaluation results matter.
- **Watch out for:** No formal safety framework is named, and prompt-injection, harmful-content, jailbreak, honesty, and sycophancy evaluations are absent.
- The report states 2.8T total parameters, 104B active parameters, native vision, full weight release, and up to a one-million-token context window. (pp. 1-2)
- Coding and agentic scores are the decision hook: 67.5 on DeepSWE, 88.3 on Terminal-Bench 2.1, 81.2 on FrontierSWE, 42.0 on SWE-Marathon, 91.2 on BrowseComp, and 94.5 on MCPMark-Verified. (pp. 27-28)
- Post-training spans general, agentic, and coding domains across multiple effort levels, then distills domain- and effort-specialized policies into one model. (pp. 2, 12-13)
- Cyber evaluation shows meaningful dual-use capability: about 70% of reviewed vulnerability findings were confirmed, and the model solved 14 of 36 exploit-development tasks. (pp. 30-31)
- The report gives no named safety framework and does not report harmful-content, jailbreak, prompt-injection, honesty, or sycophancy evaluations. (pp. 25, 30)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The report is dated 2026-07-23 in catalog metadata and says weights are released, but the body does not state a model release date. | — |
| Knowledge cutoff | Not stated. The report does not state a knowledge cutoff. | — |
| Context window | 1,000,000 tokens (stated as 1-million-token context window) | pp. 1-2 |
| Maximum output | Not stated. The report discusses output and tool-call tokens during training but does not state a serving output limit. | — |
| Input modalities | Text, Image, Video (stated as text, images, and videos) | p. 9 |
| Output modalities | Text. The report describes text, code, and tool-call generation; visual artifacts are produced through code and screenshots rather than a named image-output mode. | pp. 9, 16 |
| Reasoning controls | Effort levels. The report describes multiple reasoning-effort levels and a chat-template option for thinking effort. | pp. 2, 13, 46 |
| Effort levels | low, high, max (stated as low, high, and max expert models). The report's evaluations use max for Kimi K3; low and high are named during effort-level RL. | pp. 13, 26 |
| Tool use | Function calling, Web search, Code execution, MCP. Training and evaluation include tool calls, agent web searches, Python execution, and MCP benchmarks. | pp. 2, 15, 26, 28 |
| Open weights | Yes (stated as release the full Kimi K3 model weights) | pp. 1-2 |
| Architecture | Mixture of experts (stated as Mixture-of-Experts) | pp. 1-2 |
| Total parameters | 2.8 trillion (stated as 2.8T total parameters) | pp. 1-2 |
| Active parameters | 104 billion (stated as 104 billion activated parameters) | pp. 1-2 |

### Capability notes

- The architecture combines Kimi Delta Attention, periodic Gated MLA, Attention Residuals, and Stable LatentMoE to scale long-context and depth information flow. (pp. 2-6)
- Stable LatentMoE uses 896 routed experts with 16 selected per token, two shared experts, normalized routing output, SiTU-GLU, and Quantile Balancing. (pp. 6-8)
- MoonViT-V2 processes images and videos into the shared backbone, enabling iterative workflows where code, screenshots, and rendered results stay in one context. (p. 9)
- Pretraining covers text, code, mathematics, knowledge, and vision data, then extends the context length with long-context cleaning and synthetic long-range tasks. (pp. 10-12)
- Post-training starts with SFT, then trains specialized RL experts across domains and effort levels, and finally consolidates them through multi-teacher on-policy distillation. (pp. 12-13)
- Agentic RL environments include search and professional work, software engineering, kernel optimization, vision-in-the-loop reasoning, persistent assistants, web development, and autonomous execution. (pp. 14-16)
- Infrastructure supports long trajectories with resumable microVM sandboxes, external KV-cache retention, and KDA-aware prefix caching for million-token workloads. (pp. 21-23)
- Quantization-aware post-training uses MXFP4 expert weights and MXFP8 expert activations while keeping non-expert modules at higher precision. (p. 14)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| DeepSWE v1.1 | — | pass@1 | 67.5% | max effort; Kimi Code CLI; v1.1 tasks; mini-SWE-agent reference score 67.3 | GPT-5.6 Sol 73.0% (max); Claude Fable 5 70.0% (max, with fallback); GPT-5.5 67.0% (xhigh); Claude Opus 4.8 59.0% (max); GLM-5.2 46.2% (max) | pp. 26-27 |
| Terminal-Bench 2.1 | — | success rate | 88.3% | max effort; best score across harnesses; all non-GPT-5.5 baselines at max | GPT-5.6 Sol 88.8% (max); Claude Fable 5 88.0% (max, with fallback); Claude Opus 4.8 84.6% (max); GPT-5.5 83.4% (xhigh); GLM-5.2 82.7% (max) | pp. 26-28 |
| FrontierSWE | — | score | 81.2% | max effort; Kimi Code CLI; dominance scores recomputed from official script as of July 16, 2026 | Claude Fable 5 86.6% (max, with fallback); GPT-5.6 Sol 71.3% (max); GLM-5.2 67.3% (max); Claude Opus 4.8 66.7% (max); GPT-5.5 64.9% (xhigh) | pp. 26-28 |
| SWE-Marathon | — | success rate | 42.0% | max effort; Kimi Code CLI; H20-calibrated branch of official tasks as of July 9, 2026 | Claude Opus 4.8 40.0% (max); GPT-5.6 Sol 39.0% (max); Claude Fable 5 35.0% (max, with fallback); GPT-5.5 14.0% (xhigh); GLM-5.2 13.0% (max) | pp. 26-28 |
| BrowseComp | — | accuracy | 91.2% | max effort; context compaction at 300K tokens; 90.4% without context management | GPT-5.6 Sol 90.4% (max); Claude Fable 5 88.0% (max, with fallback); GPT-5.5 84.4% (xhigh); Claude Opus 4.8 84.3% (max) | pp. 26-28 |
| MCPMark Verified | — | score | 94.5% | max effort; verified MCP tasks | GPT-5.6 Sol 92.9% (max); Claude Fable 5 87.4% (max, with fallback); GPT-5.5 92.9% (xhigh); Claude Opus 4.8 76.4% (max) | pp. 26-28 |

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| ProgramBench | — | success rate | 77.8% | max effort; Kimi Code CLI | GPT-5.6 Sol 77.6% (max); Claude Fable 5 76.8% (max, with fallback); Claude Opus 4.8 71.9% (max); GPT-5.5 70.8% (xhigh); GLM-5.2 63.7% (max) | pp. 27-28 |
| Kimi Code Bench v2 | 2.0 internal | score | 72.9% | max effort; Kimi Code CLI; realistic end-to-end coding-agent tasks | Claude Fable 5 76.9% (max, with fallback); Claude Opus 4.8 71.7% (max); GPT-5.5 69.0% (xhigh); GPT-5.6 Sol 64.8% (max); GLM-5.2 64.2% (max) | pp. 27, 29 |
| MCP Atlas | — | success rate | 84.2% | max effort; 500-task public subset; 100-turn limit; Gemini 3.1 Pro judge | Claude Fable 5 84.7% (max, with fallback); GPT-5.6 Sol 83.6% (max); Claude Opus 4.8 83.6% (max); GPT-5.5 82.8% (xhigh); GLM-5.2 82.6% (max) | pp. 26-27 |
| AutomationBench | — | success rate | 30.8% | max effort; 600-task public subset | GPT-5.6 Sol 29.7% (max); Claude Fable 5 29.1% (max, with fallback); Claude Opus 4.8 27.2% (max); GPT-5.5 22.7% (xhigh); GLM-5.2 12.9% (max) | pp. 26-28 |
| GDPval-AA v2 | — | Elo | 1,686 Elo | max effort; Artificial Analysis score as of July 23, 2026; third-party run | Claude Fable 5 1,747 Elo (max, with fallback); GPT-5.6 Sol 1,736 Elo (max); Claude Opus 4.8 1,593 Elo (max); GLM-5.2 1,510 Elo (max); GPT-5.5 1,491 Elo (xhigh) | pp. 26-28 |
| GPQA Diamond | — | accuracy | 93.5% | max effort; single-step reasoning; top-p 0.95 | Claude Fable 5 92.6% (max, with fallback); GPT-5.6 Sol 94.1% (max); Claude Opus 4.8 91.0% (max); GPT-5.5 93.5% (xhigh); GLM-5.2 91.2% (max) | pp. 26-27 |
| Humanity's Last Exam | With tools | accuracy | 56.0% | max effort; HLE-Full; general tools | Claude Fable 5 63.0% (max, with fallback); GPT-5.6 Sol 58.0% (max); Claude Opus 4.8 57.9% (max); GPT-5.5 52.2% (xhigh) | pp. 26-27 |
| Math-Vision | With Python | accuracy | 97.8% | max effort; vision benchmark with Python tool augmentation | Claude Fable 5 98.6% (max, with fallback); GPT-5.6 Sol 97.8% (max); Claude Opus 4.8 97.1% (max); GPT-5.5 96.8% (xhigh) | pp. 27-28 |
| Kimi Webdev Bench | Overall win-minus-lose | score | 31.0% | max effort; Claude Code; blind expert comparison against Claude Opus 4.8 | — | pp. 29-30 |

## Safety findings

### Safety classification

- **Framework:** No safety framework stated
- **Overall determination:** Not stated

The Kimi K3 report does not state a named safety framework or formal safety-level determination. It includes a cyber capability evaluation with operational-risk framing, but no overarching framework, threshold level, or broad deployment classification is stated.

The document states no per-domain determinations.

### Agentic-coding risks

- **Reward hacking** (reported): Training environments include safeguards against reward hacking in kernel optimization, autonomous execution, and web-development rewards, but the report does not publish a behavioral eval rate for Kimi K3. (p. 16)
- **Test tampering** (not reported): The report mentions correctness and anti-cheat validators for SWE-Marathon but does not report a test-tampering evaluation.
- **Destructive or overeager actions** (not reported): The report trains and evaluates long-horizon agents but does not report destructive-action or over-eager action measurements.
- **Sabotage** (not reported): The report does not include sabotage or oversight-evasion evaluations.
- **Prompt injection** (not reported): The report lists agentic and MCP benchmarks but does not test injected instructions from tools, files, web pages, or messages.
- **Honesty** (reported): The in-house Faithfulness benchmark reports 1 minus hallucination rate; Kimi K3 scores 85.5, but the report gives no detailed honesty or false-success analysis. (pp. 29-30)
- **Sycophancy** (not reported): The report does not mention or evaluate sycophancy.
- **Malicious agentic use** (reported): Cyber testing shows dual-use capability: 14 of 36 in-house exploit-development tasks solved and 0 of 41 arbitrary-code-execution tasks in the joint UK AISI/NIST CAISI assessment. (p. 31)

### Other safety findings

- Cyber evaluation is organized by operational risk into vulnerability discovery and exploit development, and excludes Anthropic and OpenAI frontier models because they refuse cyber-related tasks. (p. 30)
- In vulnerability discovery, about 70% of human-reviewed candidate findings were confirmed as real, including 16 previously unknown vulnerabilities across six projects. (p. 30)
- In exploit development, Kimi K3 solves 14 of 36 tasks, compared with 8 of 36 for GLM-5.2; 10 of Kimi K3's successes are user-space tasks. (p. 31)
- Failure analysis attributes unsolved exploit tasks to incomplete exploit-chain finishing, poor mitigation-aware strategy selection, debugging loops, and weak final verification. (p. 31)
- A joint UK AISI and NIST CAISI assessment finds Kimi K3 ahead of GLM-5.2 on ExploitBench and an enterprise-network task, but at 0 of 41 arbitrary-code-execution tasks. (p. 31)
- Outside cyber capability, the report does not provide CBRN, harmful-content, jailbreak, prompt-injection, or formal safety-threshold findings. (pp. 25, 30)

## Limitations and caveats

- Moonshot says Kimi K3 still trails Claude Fable 5 and GPT-5.6 Sol overall, with remaining gaps on research-level reasoning such as HLE-Full and CritPt. (pp. 2, 26)
- Capability comparisons mix harnesses, fallbacks, leaderboard sources, dates, and max-versus-xhigh effort settings, so exact rank should be read with those conditions. (pp. 26-27)
- Internal benchmarks show weaker spots in 24/7 ClawBench, MIRA Bench, Agentic Vision Bench, Knowledge Work Vision Bench, and Agent Behavior Bench. (p. 30)
- Cyber results show a gap to human security experts on hard kernel targets and end-to-end exploit chains, despite strong Tier 1 results. (p. 31)
- The report is a technical report rather than a safety card, and it omits many behavioral-safety categories that model administrators may expect. (pp. 25, 30)
- Case studies are illustrative and should not be treated as standardized benchmark guarantees. (pp. 33-34)

## Practical implications for Copilot users

### Choose it for

- **Agentic coding:** Kimi K3 reports strong coding-agent scores, including 67.5 on DeepSWE, 88.3 on Terminal-Bench 2.1, 81.2 on FrontierSWE, and 42.0 on SWE-Marathon. (pp. 27-28)
- **Long context:** The report states a one-million-token context window and describes million-token agentic RL infrastructure for long trajectories. (pp. 1-2, 21)
- **Vision:** Native image and video input shares the backbone with text, supporting code-and-screenshot feedback loops and tool-augmented visual reasoning. (pp. 9, 28)
- **Web development:** Kimi Webdev Bench shows a +31.0 win-minus-lose margin over Claude Opus 4.8 under blind expert judging. (pp. 29-30)

### Avoid it for

- **Untrusted input:** The report does not test prompt injection from tools, web pages, files, or MCP results, despite heavy tool-use positioning. (pp. 25, 28)
- **High-stakes domains:** No broad behavioral-safety framework or harmful-content evaluation is stated, and cyber results show meaningful dual-use capability. (pp. 30-31)
- **Security work:** For unsupervised offensive or production-adjacent security work, the cyber section shows exploit capability and explicit gaps in final verification. (pp. 30-31)

### Guidance

- Use Kimi K3 for repository-scale context and agentic coding when local policy permits open-weight models; keep tests and code review in the loop.
- Because the report lacks prompt-injection evidence, sandbox tool calls and treat repository files, MCP outputs, and web content as untrusted.
- Limit permissions for security-sensitive work; the report demonstrates real vulnerability discovery and exploit-development capability.
- Copilot CLI lists the model, but the app picker did not show it on the catalog check date, so do not plan app workflows around it.
- The report's max-effort benchmark setup may not match every Copilot run; compare outcomes with project-specific tests rather than table rank alone.

## Document coverage

The 47-page Moonshot AI technical report is about Kimi K3 only. It is not a system card: architecture, training, infrastructure, capability evaluations, third-party results, and cyber capability are covered, but standard behavioral-safety categories are mostly absent. Comparator rows name other models only as baselines.

- **Card type:** Dedicated. The document is about this model; it may include short sibling sections.
- **Pages specific to this model:** the whole document
- **Names the document uses for this model:** Kimi K3
- **Catalog scope:** Moonshot AI technical report for Kimi K3; no separate system card is published.
- **Catalog note:** The technical report is the most specific publisher document for Kimi K3.
