# Gemini 3.8 Flash

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write gemini-3.8-flash`. -->

> Original digest of *Gemini 3.8 Flash — Model Card* (Google DeepMind, September 2026; 8 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

**Copilot status** (catalog checked 2026-10-06): Current; GitHub release status GA. CLI: Yes. App model picker: listed. App reasoning efforts: low, medium, high. App Auto: yes. App long-context option: yes.

## At a glance

Gemini 3.8 Flash is a current Google Flash model built on 3.7 Flash for fast multimodal, long-context, and agentic coding work. Its short card adds a new benchmark image with stronger DeepSWE and Terminal-Bench 2.1 results, while most architecture and safety detail is inherited from 3.7 Flash. Safety evidence is thin for agentic coding risks and relies on Google’s assessment that no new Frontier Safety threshold is likely reached.

- **Choose it for:** Fast agentic coding, terminal, multimodal, and knowledge-work tasks when you can verify outputs and want the latest Flash results.
- **Watch out for:** The card omits most agentic-risk tests and inherits Frontier Safety conclusions rather than giving a new domain table.
- The benchmark image shows the main gains over its predecessor in agentic software work: DeepSWE rises from 65.3% to 73.7%, and Terminal-Bench 2.1 from 85.8% to 89.4%. (p. 5)
- It keeps the Flash interface shape: text, image, audio, and video inputs, a 1M-token context window, text output, and a 64K-token output limit. (p. 2)
- The strongest chart rows are not uniform: Gemini 3.8 Flash leads the shown models on Finance Agent v2 and LABBench2, but trails Claude Opus 5 on DeepSWE and the OSWorld computer-use row. (p. 5)
- Google did not run a new per-domain Frontier Safety table here; it relies on 3.7 Flash and says 3.8 Flash is unlikely to reach any tracked or critical capability level. (p. 8)
- Automated safety is mostly similar to 3.7 Flash, but multilingual safety moves 5.4 percentage points in the worse direction and unjustified refusals rise 1.1 points. (p. 7)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The card is dated 2026-09, but it does not state a separate model release date. | — |
| Knowledge cutoff | March 2026 (stated as knowledge cutoff date for Gemini 3.8 Flash is March 2026) | p. 6 |
| Context window | 1,000,000 tokens (stated as up to 1M tokens) | p. 2 |
| Maximum output | 64,000 tokens (stated as 64K token output) | p. 2 |
| Input modalities | Text, Image, Audio, Video | p. 2 |
| Output modalities | Text | p. 2 |
| Reasoning controls | Effort levels. The card says effort settings tune quality, latency, and token usage, but it does not name the levels. | p. 2 |
| Effort levels | Not stated. The card does not name the individual effort or thinking levels. | — |
| Tool use | Terminal, Computer use. Evaluation coverage includes terminal and computer-use benchmarks; the card does not describe an API tool surface. | pp. 4-5 |
| Open weights | Not stated. The card does not say the weights are open. | — |
| Architecture | Not stated. Architecture details are deferred to a predecessor or sibling card. | — |
| Total parameters | Not stated. The card does not state a parameter count. | — |
| Active parameters | Not stated. The card does not state active parameters. | — |

### Capability notes

- Google describes 3.8 Flash as the next Flash iteration, built on 3.7 Flash, with advances in software engineering and agentic knowledge workflows. (p. 2)
- The model keeps multimodal input, long context, and long text output from recent Flash cards. (p. 2)
- Google says effort settings can be customized to balance answer quality, latency, and token usage. (p. 2)
- Distribution channels named by the publisher include Gemini app, Gemini API, Google AI Studio, AI Mode, Antigravity, and an enterprise agent platform. (pp. 3-4)
- The chart reports 73.7% on DeepSWE, 89.4% on Terminal-Bench 2.1, 59.0 on the OSWorld computer-use row, and 61.4% on Vals Finance Agent v2. (p. 5)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| DeepSWE v1.1 | — | pass@1 | 73.7% | — | Gemini 3.7 Flash 65.3%; Claude Opus 5 74.0%; Claude Sonnet 5 53.8%; GPT-5.6 Sol 72.7%; GPT-5.6 Terra 69.6% | p. 5 |
| Terminal-Bench 2.1 | — | success rate | 89.4% | — | Gemini 3.7 Flash 85.8%; Claude Opus 5 89.1%; Claude Sonnet 5 80.4%; GPT-5.6 Sol 88.8%; GPT-5.6 Terra 87.4% | p. 5 |
| Terminal-Bench 4.0 | — | success rate | 19.1% | — | Gemini 3.7 Flash 11.2%; Claude Opus 5 51.8%; Claude Sonnet 5 12.4%; GPT-5.6 Sol 37.3%; GPT-5.6 Terra 23.6% | p. 5 |
| OSWorld 2.0 | — | score | 59.0% | partial score; batch tool enabled | Gemini 3.7 Flash 50.6%; Claude Opus 5 75.4%; Claude Sonnet 5 42.6%; GPT-5.6 Sol 62.6%; GPT-5.6 Terra 50.2% | p. 5 |

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| GDPval-AA v2 | — | Elo | 1,545 Elo | — | Gemini 3.7 Flash 1,482 Elo; Claude Opus 5 1,824 Elo; Claude Sonnet 5 1,584 Elo; GPT-5.6 Sol 1,710 Elo; GPT-5.6 Terra 1,528 Elo | p. 5 |
| Finance Agent v2 | — | accuracy | 61.4% | — | Gemini 3.7 Flash 59.0%; Claude Opus 5 58.6%; Claude Sonnet 5 53.9%; GPT-5.6 Sol 53.8%; GPT-5.6 Terra 54.4% | p. 5 |
| Legal Agent Benchmark | Harvey all-pass rate | success rate | 10.0% | — | Gemini 3.7 Flash 8.8%; Claude Opus 5 6.7%; Claude Sonnet 5 5.0%; GPT-5.6 Sol 2.5%; GPT-5.6 Terra 0.8% | p. 5 |
| GDP.pdf | — | success rate | 35.0% | all-pass rate | Gemini 3.7 Flash 34.0%; Claude Opus 5 37.0%; Claude Sonnet 5 28.0%; GPT-5.6 Sol 40.0%; GPT-5.6 Terra 29.0% | p. 5 |
| CharXiv Reasoning | No tools | accuracy | 86.2% | — | Gemini 3.7 Flash 84.5%; Claude Opus 5 83.7%; Claude Sonnet 5 70.1%; GPT-5.6 Sol 85.8%; GPT-5.6 Terra 85.9% | p. 5 |
| LVBench | Agentic | accuracy | 87.8% | — | Gemini 3.7 Flash 85.4%; Claude Opus 5 75.4%; Claude Sonnet 5 68.5%; GPT-5.6 Sol 82.1%; GPT-5.6 Terra 78.9% | p. 5 |
| HLE-Verified | — | accuracy | 54.9% | — | Gemini 3.7 Flash 53.6%; Claude Opus 5 54.4%; Claude Sonnet 5 31.0%; GPT-5.6 Sol 54.5%; GPT-5.6 Terra 51.1% | p. 5 |
| BioMysteryBench | Human difficult | accuracy | 56.5% | — | Gemini 3.7 Flash 43.5%; Claude Opus 5 49.4%; Claude Sonnet 5 34.1%; GPT-5.6 Sol 44.7%; GPT-5.6 Terra 49.4% | p. 5 |
| LABBench2 | — | accuracy | 86.2% | — | Gemini 3.7 Flash 82.1%; Claude Opus 5 84.2%; Claude Sonnet 5 80.1%; GPT-5.6 Sol 82.1%; GPT-5.6 Terra 81.2% | p. 5 |

## Safety findings

### Safety classification

- **Framework:** Google DeepMind Frontier Safety Framework
- **Overall determination:** Unlikely to reach any T/CCL based on Gemini 3.7 Flash

Google says Gemini 3.8 Flash has no meaningful new capability increase over 3.7 Flash in Frontier Safety domains and therefore is unlikely to reach tracked or critical capability levels. The card does not repeat the 3.7 per-domain table. (p. 8)

| Domain | Determination | Level | Finding | Source |
| --- | --- | --- | --- | --- |
| Overall deployment standard | Below threshold | T/CCLs not reached | Based on 3.7 Flash testing, Google assesses 3.8 Flash as unlikely to reach any tracked or critical capability level. | p. 8 |

### Agentic-coding risks

- **Reward hacking** (not reported): The card reports no evaluation of grader gaming or reward exploitation.
- **Test tampering** (not reported): The card reports no test editing, deletion, or weakening evaluation.
- **Destructive or overeager actions** (not reported): The card reports no evaluation of irreversible or unrequested tool actions.
- **Sabotage** (not reported): The card does not report a sabotage or task-undermining evaluation for this model.
- **Prompt injection** (not reported): The card reports jailbreak and content-safety work, but not injected instructions from files, tools, or web content.
- **Honesty** (not reported): The card reports no honesty, deception, or false-task-success evaluation.
- **Sycophancy** (not reported): The card reports no sycophancy evaluation.
- **Over-refusal** (reported): Automated unjustified-refusal performance worsens by 1.1 percentage points versus 3.7 Flash, with lower values preferred. (p. 7)

### Other safety findings

- Automated safety comparisons show text-to-text safety down 0.4 points, image-to-text unchanged, tone up 0.2 points, and unjustified refusals up 1.1 points versus 3.7 Flash. (p. 7)
- The multilingual safety row worsens by 5.4 points, even though Google summarizes overall safety and tone as similar. (p. 7)
- Specialist red teams found child-safety launch thresholds satisfied, content safety similar or improved against 3.7 Flash, and no egregious issues in broader probing. (p. 8)
- Google says manual review of automated losses found false positives or non-egregious material rather than severe content problems. (p. 7)
- The Frontier Safety section is inherited: based on 3.7 Flash, Google says 3.8 Flash is unlikely to reach any tracked or critical capability level. (p. 8)

## Limitations and caveats

- The card defers architecture, training data, training processing, hardware, and software details to the 3.7 Flash card. (pp. 2-3)
- Known limitations include hallucinations, continuing jailbreak-resistance work, occasional slowness or timeouts, and heavier token usage at higher effort settings. (p. 6)
- Knowledge is dated March 2026 overall, with some domains potentially limited to January 2025. (p. 6)
- Capability methodology is mostly external; the card provides a benchmark image rather than detailed harness descriptions. (pp. 4-5)
- Frontier Safety is not newly tested in a per-domain table for this card. (p. 8)

## Practical implications for Copilot users

### Choose it for

- **Agentic coding:** DeepSWE v1.1 reaches 73.7%, and Google positions the release around software engineering and agentic knowledge workflows. (pp. 2, 5)
- **Terminal workflows:** Terminal-Bench 2.1 is 89.4% and Terminal-Bench 4.0 improves over 3.7 Flash, giving the strongest direct CLI-style signal in the card. (p. 5)
- **Long context:** The document states a 1M-token input window and reports strong long-video, bio-research, and PDF-style results in the same chart. (pp. 2, 5)

### Avoid it for

- **Untrusted input:** No prompt-injection evaluation is reported, despite the model being positioned for agents and workflows that may read external content. (pp. 6, 8)
- **High-stakes domains:** The card names hallucinations and relies on inherited safety detail, so medical, legal, security, or safety-critical outputs need expert review. (pp. 6, 8)

### Guidance

- Prefer the lowest effort setting that solves the task; the card links higher effort with more token usage and possible slower responses.
- For repository edits, keep tests protected and review diffs because reward hacking, test tampering, and destructive actions are not evaluated.
- Treat benchmark gains as directional: Copilot uses its own harness, not the publisher benchmark setup.
- Use long context for large files and logs, but ask for grounded references because hallucination remains listed.
- For non-English sensitive content, add extra review because the multilingual safety row regresses versus 3.7 Flash.

## Document coverage

The whole 8-page document is dedicated to Gemini 3.8 Flash. It contains one benchmark image read from the PDF and a short safety section that compares against 3.7 Flash. Architecture, data, acceptable-use, risk, and Frontier Safety details are mostly delegated to earlier cards, so this digest does not import details from those external documents.

- **Card type:** Dedicated. The document is about this model; it may include short sibling sections.
- **Pages specific to this model:** the whole document
- **Names the document uses for this model:** Gemini 3.8 Flash
- **Catalog scope:** Dedicated publisher card for this model.
