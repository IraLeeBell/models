# Kimi K3

> Original digest of *Kimi K3: Open Frontier Intelligence — Technical Report of Kimi K3* (Moonshot AI, 2026-07-23; 47 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and [system-card.md](system-card.md) for the full text.

## At a glance

- Kimi K3 is presented in a technical report, not a system card; the report describes architecture, training, infrastructure, evaluations, and case studies for a single open-weight model (pp. 1-2).
- The model is a 2.8T-parameter native multimodal MoE with 104B activated parameters and a context window up to 1 million tokens (pp. 1-2).
- Core architecture choices include hybrid Kimi Delta Attention and Gated MLA, Attention Residuals across depth, Stable LatentMoE with 896 routed experts and 16 active experts per token, and MoonViT-V2 for image/video inputs (pp. 3-10).
- Pretraining uses curated text domains plus large-scale vision data; the report claims about a 2.5× scaling-efficiency gain over Kimi K2 (pp. 10-12).
- Post-training combines supervised tuning, reinforcement learning across general, agentic, and coding domains at multiple reasoning-effort levels, and multi-teacher on-policy distillation into one model (pp. 12-14).
- Evaluation coverage is broad across coding, agentic, reasoning, knowledge, and vision benchmarks; Kimi K3 often leads open-weight comparisons while still trailing the strongest proprietary baselines overall (pp. 25-28).
- Safety coverage is narrow: the substantive safety-style section is a cyber capability evaluation, with no dedicated harmful-content, CBRN, jailbreak, or preparedness-threshold analysis (pp. 30-31).

## Capabilities

- Kimi K3 uses a 2.8T total-parameter MoE backbone with 104B activated parameters, native vision, and a 1M-token context window (pp. 1-2).
- Hybrid attention repeats three KDA layers followed by one Gated MLA layer, with a final global-attention layer at the end of the backbone (pp. 3-5).
- Attention Residuals let layers attend over earlier block representations, reducing the depth bottleneck of ordinary residual accumulation (p. 6).
- Stable LatentMoE scales channel mixing through 896 routed experts, 16 selected routed experts, two shared experts, RMS-normalized routing output, SiTU-GLU activation, and Quantile Balancing (pp. 6-9).
- The native vision path encodes images and videos with MoonViT-V2 and brings visual tokens into the same backbone, supporting iterative code-and-screenshot workflows (pp. 9-10).
- The training corpus spans web text, code, mathematics, knowledge, and vision data, with long-context cleaning and synthetic long-range tasks used for 1M-token adaptation (pp. 10-12).
- Post-training covers general tasks, general agents, and coding agents, then consolidates nine domain/effort expert policies with multi-teacher on-policy distillation (pp. 12-14).
- Quantization-aware post-training uses MXFP4 expert weights and MXFP8 activations for expert components, while non-expert modules remain at higher precision (p. 14).

## Evaluations

| Benchmark | Result | Context | Pages |
| --- | --- | --- | --- |
| GPQA Diamond | 93.5% | Graduate-level reasoning and knowledge; compared with proprietary and open-weight baselines | pp. 26-27 |
| HLE-Full | 43.5% without tools / 56.0% with tools | Research-level reasoning; the report notes gaps to Claude Fable 5 and GPT-5.6 Sol | pp. 26-27 |
| DeepSWE | 67.5% | Agentic coding; Kimi K3 ranks behind Claude Fable 5 and GPT-5.6 Sol in the report's comparison | pp. 27-28 |
| ProgramBench | 77.8% | Code-generation agent benchmark; best score in the table | pp. 27-28 |
| Terminal-Bench 2.1 | 88.3% | Agentic terminal coding; near GPT-5.6 Sol's 88.8% in the report | pp. 27-28 |
| FrontierSWE | 81.2% | Long-horizon software engineering; second in the table behind Claude Fable 5 | pp. 27-28 |
| SWE-Marathon | 42.0% | GPU-kernel-oriented suite; best score in the table | pp. 27-28 |
| BrowseComp | 91.2% | Agentic browsing/search benchmark; best listed result | pp. 27-28 |
| MCPMark-Verified | 94.5% | MCP tool-use evaluation across verified tasks | pp. 27-28 |
| AutomationBench | 30.8% | Public agent automation subset; best listed result | pp. 27-28 |
| Math-Vision | 94.3% without Python / 97.8% with Python | Vision reasoning; Python tools improve the reported score | pp. 27-28 |
| ZeroBench-main | 23.0% pass@5 without Python / 41.0% with Python | Challenging vision benchmark; tied for the no-tool top score in the table | pp. 27-28 |
| Kimi Webdev Bench | 58.6% win, 13.8% tie, 27.6% lose; +31.0 win-minus-lose | Blind expert judging versus Claude Opus 4.8 in a Claude Code harness | pp. 29-30 |
| Cyber exploit suite | 14 of 36 tasks solved; GLM-5.2 solved 8 of 36 | In-house Tier 2 exploit-development suite spanning user-space and kernel tracks | pp. 30-31 |

## Safety findings

- The cyber section separates vulnerability discovery from exploit development and evaluates recent deployed software plus internal systems, making it the report's main dual-use safety evidence (p. 30).
- In the vulnerability-discovery tier, human review confirmed about 70% of reviewed findings as genuine and found 16 previously unknown vulnerabilities across six projects (p. 30).
- In the exploit-development tier, Kimi K3 solved 14 of 36 tasks, with most successes on user-space targets and persistent gaps on hardened kernel tasks (pp. 30-31).
- The report identifies recurring exploit-task failure modes: incomplete final chaining, poor strategy under mitigations, unproductive debugging loops, and insufficient final verification (p. 31).
- A joint UK AI Security Institute and NIST CAISI assessment is summarized as consistent with Moonshot's results: Kimi K3 exceeded GLM-5.2 on ExploitBench and a simulated enterprise-network task, but achieved arbitrary code execution on 0 of 41 tasks (p. 31).
- Beyond cyber capability, safety evaluation coverage is thin: the report does not provide CBRN, harmful-content, jailbreak, prompt-injection, or formal preparedness-threshold findings (pp. 25-31).

## Limitations and caveats

- Kimi K3 still trails the strongest proprietary systems overall, especially on research-level reasoning such as HLE-Full and CritPt (p. 26).
- The public comparison depends on heterogeneous harnesses, fallbacks, third-party leaderboards, and maximum-effort settings, so exact rank should be read with those evaluation details (p. 26).
- Internal evaluation shows weaker areas in enterprise routing, always-on assistant work, agent-behavior scoring, visual agent tasks, and Knowledge Work Vision Bench (p. 30).
- Cyber results show meaningful dual-use capability but also a clear gap to expert exploit developers on hard kernel and end-to-end exploit tasks (p. 31).
- The report is a technical report rather than a safety card, and it omits many standard safety categories that Copilot administrators might expect from a system card (pp. 25-31).
- Case studies are illustrative, not standardized evaluations, so they should not be treated as reproducible benchmark guarantees (pp. 33-34).

## Practical implications for Copilot users

- Kimi K3 is best read as a large-context, agentic coding option with strong reported results on software engineering, terminal, and tool-use tasks.
- The 1M-token context and native vision path can help with large repositories and UI feedback loops, but developers should still isolate untrusted files and watch for prompt-injection attempts.
- Because cyber capability is nontrivial, restrict tool permissions, avoid handing it production secrets, and review any security-sensitive code it generates.
- Use project tests, linters, and human review to catch the exploit-task failure modes the report itself identifies: incomplete chains, poor strategy choices, and weak final verification.
- Do not infer broad safety guarantees from the technical report; its safety evidence is mostly cyber capability analysis, not a full harmful-content or misuse evaluation.
- For tasks involving images, videos, or generated interfaces, pair the model's multimodal strengths with visual inspection and automated checks where possible.

## Document coverage

This digest draws from the abstract and introduction, architecture sections, pretraining/post-training sections, evaluation tables, cyber evaluation, and case studies. It omits most infrastructure derivations, mathematical appendices, references, and contribution lists. The report is specific to Kimi K3 and should not be read as a system card for Kimi K2.x models or future Moonshot releases.
