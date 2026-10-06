# Gemini 3.7 Flash

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write gemini-3.7-flash`. -->

> Original digest of *Gemini 3.7 Flash — Model Card* (Google DeepMind, August 2026; 9 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

**Copilot status** (catalog checked 2026-10-06): Current; GitHub release status GA. CLI: Yes. App model picker: listed. App reasoning efforts: low, medium, high. App Auto: no. App long-context option: yes.

## At a glance

Gemini 3.7 Flash is a current Google Flash model built on 3.6 Flash with improved core reasoning and agentic video support. Its chart shows strong terminal, coding, computer-use, long-context, and specialist-task results for a fast model. Unlike 3.8 Flash, this card includes a per-domain Frontier Safety table: no tracked or critical capability level is reached, although CBRN and cyber hit alert thresholds for critical levels.

- **Choose it for:** Fast multimodal coding, terminal, video, and workflow tasks where the 3.7 card’s fuller safety table matters.
- **Watch out for:** CBRN and cyber alert thresholds are reached even though CCLs are not, and most agentic-coding misbehavior tests are absent.
- The benchmark image reports 65.3% on DeepSWE, 85.8% on Terminal-Bench 2.1, 47.9% on the OSWorld computer-use row, and 26.3% on Agent’s Last Exam. (p. 5)
- It is a multimodal Flash successor to 3.6 Flash with algorithmic improvements, agentic video support, 1M-token input context, and 64K-token text output. (p. 2)
- Google’s FSF table says CBRN tracked capability is not reached, CBRN and cyber reach alert thresholds for CCLs but not CCLs, and harmful manipulation, ML R&D, and misalignment remain below relevant thresholds. (pp. 8-9)
- Automated safety is mixed relative to 3.6 Flash: text safety worsens 1.17 points, multilingual improves 0.48, tone worsens 0.47, and unjustified refusals worsen 0.84. (p. 7)
- The card reports situational-awareness strength in the misalignment row, but says the model cannot bypass test restrictions and cannot chain coding tasks into an end-to-end research workflow. (p. 9)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The card is dated 2026-08, but it does not state a separate model release date. | — |
| Knowledge cutoff | March 2026 (stated as knowledge cutoff date for Gemini 3.7 Flash is March 2026) | p. 6 |
| Context window | 1,000,000 tokens (stated as up to 1M tokens) | p. 2 |
| Maximum output | 64,000 tokens (stated as 64K token output) | p. 2 |
| Input modalities | Text, Image, Audio, Video | p. 2 |
| Output modalities | Text | p. 2 |
| Reasoning controls | Effort levels. The card says thinking configurations are customizable but does not name the available levels. | p. 2 |
| Effort levels | Not stated. The card does not name the individual effort or thinking levels. | — |
| Tool use | Terminal, Computer use. The benchmark chart includes terminal and computer-use rows; no product tool interface is specified. | pp. 4-5 |
| Open weights | Not stated. The card does not say the weights are open. | — |
| Architecture | Not stated. Architecture details are deferred to a predecessor or sibling card. | — |
| Total parameters | Not stated. The card does not state a parameter count. | — |
| Active parameters | Not stated. The card does not state active parameters. | — |

### Capability notes

- Google says 3.7 Flash adds algorithmic reasoning improvements over 3.6 Flash and supports agentic video understanding. (p. 2)
- The interface includes text, image, audio, and video inputs with a 1M-token context window and text output up to 64K tokens. (p. 2)
- The card says thinking configurations are customizable for task demands, but it does not enumerate the levels. (p. 2)
- Intended uses include agentic workflows, complex video reasoning, coding tasks, and enterprise workflows. (p. 5)
- The chart reports broad gains over its predecessor, including FrontierCode Main at 43.6%, DeepSWE at 65.3%, and the OSWorld computer-use row at 47.9%. (p. 5)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| FrontierCode v1.1 | Main | score | 43.6% | — | Gemini 3.6 Flash 34.4%; Claude Sonnet 5 42.7%; GPT-5.6 Terra 41.3% | p. 5 |
| DeepSWE v1.1 | — | pass@1 | 65.3% | — | Gemini 3.6 Flash 48.6%; Claude Sonnet 5 53.8%; GPT-5.6 Terra 69.6%; Muse Spark 1.2 54.9% | p. 5 |
| Code Arena | — | Elo | 1,588 Elo | — | Gemini 3.6 Flash 1,538 Elo; Claude Sonnet 5 1,541 Elo; GPT-5.6 Terra 1,523 Elo; Muse Spark 1.2 1,535 Elo | p. 5 |
| Terminal-Bench 2.1 | — | success rate | 85.8% | — | Gemini 3.6 Flash 78.0%; Claude Sonnet 5 80.4%; GPT-5.6 Terra 87.4%; Muse Spark 1.2 82.9% | p. 5 |
| Terminal-Bench 3.0 | — | success rate | 14.9% | — | Gemini 3.6 Flash 5.4%; Claude Sonnet 5 14.6%; GPT-5.6 Terra 20.8% | p. 5 |
| AutomationBench | — | success rate | 30.4% | private enterprise workflow automation set | Gemini 3.6 Flash 17.0%; Claude Sonnet 5 10.7%; GPT-5.6 Terra 23.6% | p. 5 |

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Artificial Analysis Intelligence Index | — | score | 56 | — | Gemini 3.6 Flash 52; Claude Sonnet 5 55; GPT-5.6 Terra 57; Muse Spark 1.2 57 | p. 5 |
| GDPval-AA v2 | — | Elo | 1,525 Elo | — | Gemini 3.6 Flash 1,422 Elo; Claude Sonnet 5 1,598 Elo; GPT-5.6 Terra 1,578 Elo; Muse Spark 1.2 1,628 Elo | p. 5 |
| Harvey LAB-AA | — | accuracy | 90.7% | — | Gemini 3.6 Flash 85.1%; Claude Sonnet 5 90.1%; GPT-5.6 Terra 85.2% | p. 5 |
| GDP.pdf | — | success rate | 34.0% | — | Gemini 3.6 Flash 22.0%; Claude Sonnet 5 28.0%; GPT-5.6 Terra 24.7%; Muse Spark 1.2 16.0% | p. 5 |
| CharXiv Reasoning | No tools | accuracy | 84.5% | — | Gemini 3.6 Flash 85.2%; Claude Sonnet 5 77.0%; GPT-5.6 Terra 85.9% | p. 5 |
| CharXiv Reasoning | With tools | accuracy | 88.7% | — | Gemini 3.6 Flash 89.4%; Claude Sonnet 5 88.3% | p. 5 |
| LVBench | — | accuracy | 85.4% | — | Gemini 3.6 Flash 84.2%; Claude Sonnet 5 68.5%; GPT-5.6 Terra 78.9% | p. 5 |
| MRCR v2 | 8-needle; 128K average | accuracy | 97.0% | — | Gemini 3.6 Flash 91.8%; Claude Sonnet 5 81.5%; GPT-5.6 Terra 93.5% | p. 5 |
| OSWorld 2.0 | — | success rate | 47.9% | — | Gemini 3.6 Flash 33.8%; GPT-5.6 Terra 50.2% | p. 5 |
| Agent's Last Exam | — | success rate | 26.3% | — | Gemini 3.6 Flash 24.2%; Claude Sonnet 5 33.3%; GPT-5.6 Terra 28.0% | p. 5 |
| HLE-Verified | — | accuracy | 53.6% | — | Gemini 3.6 Flash 51.2%; Claude Sonnet 5 31.0%; GPT-5.6 Terra 51.1% | p. 5 |
| BioMysteryBench | Human difficult | accuracy | 43.5% | — | Gemini 3.6 Flash 41.2%; Claude Sonnet 5 34.1%; GPT-5.6 Terra 49.4% | p. 5 |
| LABBench2 | — | accuracy | 82.1% | — | Gemini 3.6 Flash 76.1%; Claude Sonnet 5 80.1%; GPT-5.6 Terra 81.2% | p. 5 |

## Safety findings

### Safety classification

- **Framework:** Google DeepMind Frontier Safety Framework
- **Overall determination:** No tracked or critical capability levels reached; CBRN and cyber alert thresholds noted

Google reports a per-domain FSF table for 3.7 Flash. CBRN tracked capability is not reached; CBRN and cybersecurity reach alert thresholds for critical levels but remain below CCLs; harmful manipulation, ML R&D, and misalignment remain below alert or tracked thresholds. (pp. 8-9)

| Domain | Determination | Level | Finding | Source |
| --- | --- | --- | --- | --- |
| CBRN | Below threshold | Uplift TCL; TCL not reached | Google says it can rule out the CBRN tracked capability level with reasonable confidence. | p. 8 |
| CBRN | Alert threshold reached | Uplift Level 1 CCL; CCL not reached | CBRN expert red teaming elicited some full-journey actionable information, so Google treats the CCL alert threshold as reached while the CCL itself is below threshold. | p. 8 |
| Cybersecurity | Alert threshold reached | Uplift Level 1 CCL; CCL not reached | The cyber row says the alert threshold is reached, but the CCL is not. | p. 8 |
| Harmful manipulation | Below threshold | Level 1 CCL; CCL not reached | Human behavior studies show some influence ability, but overall efficacy is below the CCL alert threshold. | pp. 8-9 |
| Misalignment | Below threshold | Stealth/situational TCL | The model recognizes some test settings but cannot bypass restrictions, so the tracked level is not reached. | p. 9 |
| Machine-learning R&D | Below threshold | Acceleration/automation CCLs | The model completes individual coding tasks but lacks independence for an end-to-end research workflow, and the alert threshold is not reached. | p. 9 |

### Agentic-coding risks

- **Reward hacking** (not reported): The card reports no evaluation of grader gaming or reward exploitation.
- **Test tampering** (not reported): The card reports no test editing, deletion, or weakening evaluation.
- **Destructive or overeager actions** (not reported): The card reports no evaluation of irreversible or unrequested tool actions.
- **Sabotage** (not reported): The card does not report a sabotage or task-undermining evaluation for this model.
- **Prompt injection** (not reported): The card reports jailbreak and content-safety work, but not injected instructions from files, tools, or web content.
- **Honesty** (not reported): The card reports no honesty, deception, or false-task-success evaluation.
- **Sycophancy** (not reported): The card reports no sycophancy evaluation.
- **Evaluation awareness** (reported): The misalignment row says the model can correctly assess when it is in a testing environment, though it cannot bypass the restrictions. (p. 9)
- **Over-refusal** (reported): Automated unjustified refusals worsen by 0.84 percentage points versus 3.6 Flash, with lower values preferred. (p. 7)

### Other safety findings

- Automated development results versus 3.6 Flash are mixed: text-to-text safety worsens 1.17 points, multilingual safety improves 0.48, tone worsens 0.47, and unjustified refusals worsen 0.84. (p. 7)
- Specialist red teaming found required child-safety thresholds met, content safety similar or improved versus 3.6 Flash, and no egregious concerns outside strict policies. (pp. 7-8)
- The CBRN table says both the tracked level and the critical level are not reached, but the CCL alert threshold is reached because experts could elicit some accurate full-harm-journey information. (p. 8)
- The cybersecurity row reaches an alert threshold for Uplift Level 1 but remains below the CCL. (p. 8)
- Google says the model recognizes some testing environments but cannot bypass testing restrictions and cannot chain individual coding tasks into independent ML R&D. (p. 9)

## Limitations and caveats

- Known limitations include hallucinations, ongoing jailbreak-resistance work, occasional slowness or timeouts, and uneven knowledge recency. (p. 6)
- Architecture, training data, training processing, hardware, software, acceptable use, and safety policy detail are deferred to the 3.6 Flash card. (pp. 2-3, 6)
- Capability methods are mostly external to the card, and the benchmark results appear in a chart image. (pp. 4-5)
- The automated safety table is a development evaluation rather than human evaluation or red teaming. (pp. 6-7)
- Google cautions that improved safety evaluations are not directly comparable with earlier Gemini card results. (p. 7)

## Practical implications for Copilot users

### Choose it for

- **Agentic coding:** DeepSWE v1.1 is 65.3%, FrontierCode 1.1 Main is 43.6%, and the intended-use section names coding and agentic workflows. (p. 5)
- **Terminal workflows:** Terminal-Bench 2.1 is 85.8% and Terminal-Bench 3.0 is 14.9% in the same chart. (p. 5)
- **Vision:** The model supports video input and is positioned for complex video reasoning, with LVBench at 85.4%. (pp. 2, 5)

### Avoid it for

- **Security work:** Cyber reaches an FSF alert threshold for Uplift Level 1, so offensive or dual-use security work needs strict boundaries. (p. 8)
- **Untrusted input:** The card does not report prompt-injection testing for content retrieved through tools, files, web pages, or repositories. (pp. 6, 8)

### Guidance

- Use 3.7 Flash when you want a fast Gemini model with a more explicit FSF table than 3.8 Flash provides.
- Keep command execution sandboxed and reviewed because the card records a cyber alert threshold.
- Do not treat the chart as Copilot performance; Copilot uses a different agent harness.
- For video and long-context prompts, require citations to files or frames because hallucination remains listed.
- Use extra caution on workflows with untrusted files or tool outputs because prompt injection is not tested.

## Document coverage

The whole 9-page document is dedicated to Gemini 3.7 Flash. One benchmark image supplies most capability numbers, while pages 8-9 contain a model-specific Frontier Safety table. The card still delegates many architecture, data, acceptable-use, and policy details to 3.6 Flash; this digest covers only facts in the 3.7 Flash card.

- **Card type:** Dedicated. The document is about this model; it may include short sibling sections.
- **Pages specific to this model:** the whole document
- **Names the document uses for this model:** Gemini 3.7 Flash
- **Catalog scope:** Dedicated publisher card for this model.
