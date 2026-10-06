# Gemini 3.1 Pro

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write gemini-3.1-pro`. -->

> Original digest of *Gemini 3.1 Pro Model Card* (Google DeepMind, February 2026; 9 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

**Copilot status:** Retired from GitHub Copilot on 2026-09-01. This digest is kept for historical comparison and model lineage.

## At a glance

Gemini 3.1 Pro is a retired Google Pro reasoning model for complex multimodal, coding, search, tool-use, and long-context work. Its short card reports a broad benchmark image with strong coding and tool rows, then a detailed Frontier Safety table. No CCL is reached, but cyber reaches an alert threshold and misalignment testing shows notable situational-awareness results.

- **Choose it for:** Historical comparison for Pro-level coding, terminal, MCP, search, and long-context baselines before later Gemini releases.
- **Watch out for:** Retired; cyber reaches an alert threshold, and many operational limitations are delegated to Gemini 3 Pro.
- The benchmark image reports 80.6% on SWE-bench Verified, 54.2% on SWE-bench Pro, 68.5% on Terminal-Bench 2.0, 69.2% on MCP Atlas, and 85.9% on BrowseComp. (p. 4)
- It is a retired Pro reasoning model for complex multimodal tasks, large sources, and whole code repositories, with 1M-token context and 64K-token text output. (p. 2)
- Google says CBRN, harmful manipulation, ML R&D, and misalignment remain below alert thresholds; cyber reaches an alert threshold but stays below the CCL. (pp. 7-9)
- Misalignment testing reports near-perfect success on three situational-awareness challenges, but inconsistent performance elsewhere, so the alert threshold is not reached. (p. 9)
- Most limitations, architecture, data, acceptable-use, and mitigation details are referred to the Gemini 3 Pro card. (pp. 2, 5, 7)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The card is dated 2026-02, but it does not state a separate model release date. | — |
| Knowledge cutoff | Not stated. The card does not state a knowledge cutoff for this model. | — |
| Context window | 1,000,000 tokens (stated as up to 1M tokens) | p. 2 |
| Maximum output | 64,000 tokens (stated as 64K token output) | p. 2 |
| Input modalities | Text, Image, Audio, Video | p. 2 |
| Output modalities | Text | p. 2 |
| Reasoning controls | Extended thinking. Deep Think mode is used in Frontier Safety evaluations; the card does not describe a general picker setting. | p. 2 |
| Effort levels | Not stated. The card does not name the individual effort or thinking levels. | — |
| Tool use | Terminal, MCP, Web search, Browser, Code execution. The benchmark chart includes terminal, MCP, browsing/search, and search plus code settings; no product tool surface is specified. | p. 4 |
| Open weights | Not stated. The card does not say the weights are open. | — |
| Architecture | Not stated. Architecture details are deferred to a predecessor or sibling card. | — |
| Total parameters | Not stated. The card does not state a parameter count. | — |
| Active parameters | Not stated. The card does not state active parameters. | — |

### Capability notes

- Google describes 3.1 Pro as the most advanced Gemini model for complex tasks at publication, able to work over multimodal inputs and entire code repositories. (p. 2)
- Inputs include text, image, audio, and video with up to 1M tokens of context; output is text up to 64K tokens. (p. 2)
- The model is based on Gemini 3 Pro, with architecture and training data details deferred to that card. (p. 2)
- Intended uses include agentic performance, advanced coding, long context, multimodal understanding, and algorithmic development. (p. 5)
- The chart reports 80.6% on SWE-bench Verified, 2887 Elo on LiveCodeBench Pro, and 85.9% on BrowseComp. (p. 4)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Terminal-Bench 2.0 | — | success rate | 68.5% | Terminus-2 | Gemini 3 Pro 56.9%; Claude Sonnet 4.6 59.1%; Claude Opus 4.6 65.4%; GPT-5.2 54.0%; GPT-5.3-Codex 77.3% | p. 4 |
| SWE-bench Verified | Single attempt | pass@1 | 80.6% | — | Gemini 3 Pro 76.2%; Claude Sonnet 4.6 79.6%; Claude Opus 4.6 80.8%; GPT-5.2 80.0% | p. 4 |
| SWE-bench Pro | Public; single attempt | pass@1 | 54.2% | — | Gemini 3 Pro 43.3%; GPT-5.2 55.6%; GPT-5.3-Codex 56.8% | p. 4 |
| APEX-Agents | — | pass@1 | 33.5% | — | Gemini 3 Pro 18.4%; Claude Opus 4.6 29.8%; GPT-5.2 23.0% | p. 4 |
| τ²-bench | Retail | success rate | 90.8% | — | Gemini 3 Pro 85.3%; Claude Sonnet 4.6 91.7%; Claude Opus 4.6 91.9%; GPT-5.2 82.0% | p. 4 |
| MCP Atlas | — | success rate | 69.2% | — | Gemini 3 Pro 54.1%; Claude Sonnet 4.6 61.3%; Claude Opus 4.6 59.5%; GPT-5.2 60.6% | p. 4 |

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Humanity's Last Exam | No tools | accuracy | 44.4% | — | Gemini 3 Pro 37.5%; Claude Sonnet 4.6 33.2%; Claude Opus 4.6 40.0%; GPT-5.2 34.5% | p. 4 |
| Humanity's Last Exam | Search and code execution | accuracy | 51.4% | — | Gemini 3 Pro 45.8%; Claude Sonnet 4.6 49.0%; Claude Opus 4.6 53.1%; GPT-5.2 45.5% | p. 4 |
| ARC-AGI-2 | — | accuracy | 77.1% | — | Gemini 3 Pro 31.1%; Claude Sonnet 4.6 58.3%; Claude Opus 4.6 68.8%; GPT-5.2 52.9% | p. 4 |
| GPQA Diamond | No tools | accuracy | 94.3% | — | Gemini 3 Pro 91.9%; Claude Sonnet 4.6 89.9%; Claude Opus 4.6 91.3%; GPT-5.2 92.4% | p. 4 |
| LiveCodeBench Pro | — | Elo | 2,887 Elo | — | Gemini 3 Pro 2,439 Elo; GPT-5.2 2,393 Elo | p. 4 |
| SciCode | — | accuracy | 59.0% | — | Gemini 3 Pro 56.0%; Claude Sonnet 4.6 47.0%; Claude Opus 4.6 52.0%; GPT-5.2 52.0% | p. 4 |
| GDPval-AA | — | Elo | 1,317 Elo | — | Gemini 3 Pro 1,195 Elo; Claude Sonnet 4.6 1,633 Elo; Claude Opus 4.6 1,606 Elo; GPT-5.2 1,462 Elo | p. 4 |
| τ²-bench | Telecom | success rate | 99.3% | — | Gemini 3 Pro 98.0%; Claude Sonnet 4.6 97.9%; Claude Opus 4.6 99.3%; GPT-5.2 98.7% | p. 4 |
| BrowseComp | — | accuracy | 85.9% | — | Gemini 3 Pro 59.2%; Claude Sonnet 4.6 74.7%; Claude Opus 4.6 84.0%; GPT-5.2 65.8% | p. 4 |
| MMMU-Pro | No tools | accuracy | 80.5% | — | Gemini 3 Pro 81.0%; Claude Sonnet 4.6 74.5%; Claude Opus 4.6 73.9%; GPT-5.2 79.5% | p. 4 |
| MMMLU | — | accuracy | 92.6% | — | Gemini 3 Pro 91.8%; Claude Sonnet 4.6 89.3%; Claude Opus 4.6 91.1%; GPT-5.2 89.6% | p. 4 |
| MRCR v2 | 8-needle; 128K average | accuracy | 84.9% | — | Gemini 3 Pro 77.0%; Claude Sonnet 4.6 84.9%; Claude Opus 4.6 84.0%; GPT-5.2 83.8% | p. 4 |
| MRCR v2 | 8-needle; 1M pointwise | accuracy | 26.3% | — | Gemini 3 Pro 26.3% | p. 4 |

## Safety findings

### Safety classification

- **Framework:** Google DeepMind Frontier Safety Framework
- **Overall determination:** Below alert thresholds except cyber alert threshold; no CCL reached

Google evaluated Gemini 3.1 Pro, focusing on Deep Think mode for several domains. It remains below alert thresholds for CBRN, harmful manipulation, ML R&D, and misalignment; cyber reaches an alert threshold inherited from the series but remains below the CCL. (pp. 7-9)

| Domain | Determination | Level | Finding | Source |
| --- | --- | --- | --- | --- |
| CBRN | Below threshold | Uplift Level 1; CCL not reached | Deep Think can provide accurate, actionable information but not novel or complete instructions for critical stages required for the CCL. | p. 8 |
| Cybersecurity | Alert threshold reached | Uplift Level 1; CCL not reached | The model has increased cyber capabilities and reaches the alert threshold, but not the uplift required for the CCL; Deep Think does not improve cyber results. | p. 8 |
| Harmful manipulation | Below threshold | Level 1 exploratory; CCL not reached | The maximum belief-change odds ratio is 3.6x, matching Gemini 3 Pro, and does not reach the alert threshold. | p. 8 |
| Machine-learning R&D | Below threshold | Acceleration/automation CCLs | RE-Bench improves to a 1.27 human-normalized average but remains below the alert threshold. | p. 9 |
| Misalignment | Below threshold | Instrumental reasoning L1/L2 | Situational-awareness performance is stronger on three challenges but inconsistent overall, so the alert threshold is not reached. | p. 9 |

### Agentic-coding risks

- **Reward hacking** (not reported): The card reports no evaluation of grader gaming or reward exploitation.
- **Test tampering** (not reported): The card reports no test editing, deletion, or weakening evaluation.
- **Destructive or overeager actions** (not reported): The card reports no evaluation of irreversible or unrequested tool actions.
- **Sabotage** (not reported): The card does not report a sabotage or task-undermining evaluation for this model.
- **Prompt injection** (not reported): The card reports jailbreak and content-safety work, but not injected instructions from files, tools, or web content.
- **Honesty** (not reported): The card reports no honesty, deception, or false-task-success evaluation.
- **Sycophancy** (not reported): The card reports no sycophancy evaluation.
- **Evaluation awareness** (reported): The misalignment row says the model solves three situational-awareness challenges almost 100% of the time, but other results are inconsistent. (p. 9)
- **Sandbagging** (not reported): The card reports situational awareness and stealth probes, but no sandbagging evaluation.

### Other safety findings

- Automated safety results versus Gemini 3.0 Pro show text-to-text safety up 0.10%, multilingual safety up 0.11%, image-to-text safety down 0.33%, tone up 0.02%, and unjustified refusals down 0.08%. (p. 6)
- Specialist red teams found child-safety thresholds satisfied and content safety broadly similar to Gemini 3.0 Pro. (p. 7)
- The CBRN row says Deep Think can provide accurate information but does not provide enough novel or complete critical-stage instructions to reach the CCL. (p. 8)
- Cyber testing reaches an alert threshold but stays below the CCL, and Deep Think performs worse than the standard model in that domain. (p. 8)
- ML R&D RE-Bench improves over Gemini 3 Pro, but the average remains below the alert threshold; misalignment results are strong on three situational-awareness challenges but inconsistent overall. (p. 9)

## Limitations and caveats

- Known limitations, acceptable use, architecture, training data, hardware, software, and risk mitigations are mostly delegated to Gemini 3 Pro. (pp. 2-3, 5, 7)
- Capability benchmark methodology is external to the card, and the main results are in a rendered image. (p. 4)
- The development safety table is automated testing rather than human evaluation or red teaming. (p. 6)
- Google says safety results are consistent with the original Gemini 3.0 Pro safety assessment. (p. 6)
- Deep Think does not improve cyber capability in the reported tests. (p. 8)

## Practical implications for Copilot users

### Choose it for

- **Historical comparison:** The model is a key predecessor that later Gemini Flash cards use for safety and capability comparisons. (pp. 4, 7)
- **Agentic coding:** SWE-bench Verified is 80.6%, SWE-bench Pro is 54.2%, Terminal-Bench 2.0 is 68.5%, and MCP Atlas is 69.2%. (p. 4)
- **Web research:** BrowseComp is 85.9% with search, Python, and browsing, one of the strongest chart rows. (p. 4)

### Avoid it for

- **Security work:** Cyber reaches an FSF alert threshold even though the CCL is not reached. (p. 8)
- **Untrusted input:** Prompt-injection robustness is not reported, and the card delegates most risk mitigations. (p. 7)

### Guidance

- GitHub retired Gemini 3.1 Pro from Copilot on 2026-09-01; the guidance below serves historical comparison and the lineage of later models.
- Use this digest to understand retired Pro behavior and why later Gemini cards cite 3.1 Pro for Frontier Safety.
- For historical coding outputs, rerun tests because reward hacking, test tampering, and prompt injection are not evaluated.
- Treat Deep Think results as domain-specific; the card says it does not improve cyber performance.
- Retirement means current Copilot choices should use newer available models, not this historical entry.

## Document coverage

The whole 9-page document is dedicated to Gemini 3.1 Pro. It includes a benchmark image on page 4, a safety image on page 6, and a text Frontier Safety table on pages 8-9. Many architecture, data, acceptable-use, limitation, and mitigation details are delegated to Gemini 3 Pro, so this digest does not import them.

- **Card type:** Dedicated. The document is about this model; it may include short sibling sections.
- **Pages specific to this model:** the whole document
- **Names the document uses for this model:** Gemini 3.1 Pro
- **Catalog scope:** Dedicated publisher card for this model.
