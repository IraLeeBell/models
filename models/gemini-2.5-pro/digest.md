# Gemini 2.5 Pro

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write gemini-2.5-pro`. -->

> Original digest of *Gemini 2.5 Pro Model Card* (Google DeepMind, June 27, 2025; 21 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

**Copilot status:** Retired from GitHub Copilot on 2026-07-31. This digest is kept for historical comparison and model lineage. GitHub listed it for VS Code and other IDEs but not for the CLI.

## At a glance

Gemini 2.5 Pro is a retired Google multimodal reasoning model and the oldest Gemini model in this batch. The 21-page card is much fuller than the later Flash cards: it covers sparse MoE architecture, broad GA benchmark tables, automated and assurance safety work, and detailed FSF sections. It remains useful for lineage, especially because later Gemini 3 cards compare against or inherit parts of its evaluation approach.

- **Choose it for:** Historical comparison for Gemini’s Pro lineage across coding, multimodal, long-context, factuality, and FSF baselines.
- **Watch out for:** Retired and not a current CLI option; cyber uplift hit an alert threshold, and GA deceptive-alignment testing was incomplete.
- The GA benchmark tables report 69.0% on LiveCodeBench, 82.2% on Aider Polyglot, 59.6% single-attempt and 67.2% multiple-attempt SWE-bench Verified, plus 58.0% on MRCR v2 at 128K. (pp. 5-6)
- The model is a sparse mixture-of-experts multimodal reasoning model with text, image, audio, and video input, 1M-token context, and 64K-token text output. (p. 2)
- Google’s FSF summary says no CCL is reached for GA, but cyber uplift reached an alert threshold and triggered more frequent testing and faster mitigations. (pp. 11, 21)
- GA deceptive-alignment evaluations were not completed; Google relies on Experimental 03-25 results to judge GA unlikely to reach either instrumental-reasoning CCL. (pp. 20-21)
- Safety improvements over Gemini 1.5 Pro include lower text and multilingual violation rates and much better tone and instruction following, but image-to-text violations rise 1.8 points and over-refusals remain a known limitation. (pp. 9-10)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The card is dated 2025-06-27, but it does not state a separate model release date. | — |
| Knowledge cutoff | January 2025 (stated as knowledge cutoff date for Gemini 2.5 Pro was January 2025) | p. 7 |
| Context window | 1,000,000 tokens (stated as 1M token context window) | p. 2 |
| Maximum output | 64,000 tokens (stated as 64K token output) | p. 2 |
| Input modalities | Text, Image, Audio, Video | p. 2 |
| Output modalities | Text | p. 2 |
| Reasoning controls | Always reasons. The card calls Gemini 2.5 Pro a thinking model, but does not state user-selectable effort levels. | p. 2 |
| Effort levels | Not stated. The card does not name the individual effort or thinking levels. | — |
| Tool use | Web search, Code execution, File editing. The evaluation section describes search/code settings, tool-use data in post-training, and SWE-bench scaffolding; it does not define a product tool interface. | p. 4 |
| Open weights | Not stated. The card does not say the weights are open. | — |
| Architecture | Mixture of experts. The card describes the Gemini 2.5 models as sparse mixture-of-experts transformers. | p. 2 |
| Total parameters | Not stated. The card does not state a parameter count. | — |
| Active parameters | Not stated. The card does not state active parameters. | — |

### Capability notes

- The card describes Gemini 2.5 Pro as Google’s most advanced complex-task model at the time, able to handle text, audio, image, video, and whole-code-repository inputs. (p. 2)
- Gemini 2.5 models are sparse mixture-of-experts transformers with native multimodal support. (p. 2)
- Training data included public web documents, code, images, audio, video, instruction-tuning data, preferences, and tool-use data, with deduplication, safety filtering, and quality filtering. (p. 3)
- The evaluation setup distinguishes single-attempt and multiple-attempt settings, provider-sourced comparison numbers, thinking versus non-thinking comparators, and MRCR v2 methodology changes. (p. 4)
- Intended uses are enhanced reasoning, advanced coding, multimodal understanding, and long context. (p. 7)
- GA benchmark rows include 86.4% on GPQA Diamond, 82.2% on Aider Polyglot, 87.8% on FACTS Grounding, 86.9% on VideoMME, and 89.2% on Global MMLU Lite. (pp. 5-6)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| LiveCodeBench | UI 1/1/2025-5/1/2025; single attempt | pass@1 | 69.0% | — | OpenAI o3 72.0% (high); OpenAI o4-mini 75.8% (high); Claude Sonnet 4 48.9%; Claude Opus 4 51.1% (32K thinking); DeepSeek R1 70.5% | p. 5 |
| Aider Polyglot | Diff-fenced | pass@1 | 82.2% | — | Gemini 2.5 Pro Preview 05-06 72.7% (diff); Gemini 2.5 Pro Experimental 03-25 68.6% (diff); OpenAI o3 79.6% (diff; high); OpenAI o4-mini 72.0% (diff; high); Claude Sonnet 4 61.3% (diff); Claude Opus 4 72.0% (diff; 32K thinking) | p. 5 |
| SWE-bench Verified | Single attempt | pass@1 | 59.6% | — | Gemini 2.5 Pro Preview 05-06 63.2%; Gemini 2.5 Pro Experimental 03-25 63.8%; OpenAI o3 69.1% (high); OpenAI o4-mini 68.1% (high); Claude Sonnet 4 72.7%; Claude Opus 4 72.5% (32K thinking) | p. 5 |
| SWE-bench Verified | Multiple attempts | pass@1 | 67.2% | — | Claude Sonnet 4 80.2%; Claude Opus 4 79.4% (32K thinking); DeepSeek R1 57.6% | p. 5 |

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Humanity's Last Exam | — | accuracy | 21.6% | — | Gemini 2.5 Pro Preview 05-06 17.8%; Gemini 2.5 Pro Experimental 03-25 18.8%; OpenAI o3 20.3% (high); OpenAI o4-mini 18.1% (high); Claude Sonnet 4 7.8%; Claude Opus 4 10.7% (32K thinking) | p. 5 |
| GPQA Diamond | Single attempt | accuracy | 86.4% | — | Gemini 2.5 Pro Preview 05-06 83.0%; Gemini 2.5 Pro Experimental 03-25 84.0%; OpenAI o3 83.3% (high); OpenAI o4-mini 81.4% (high); Claude Sonnet 4 75.4%; Claude Opus 4 79.6% (32K thinking) | p. 5 |
| AIME 2025 | Single attempt | accuracy | 88.0% | — | Gemini 2.5 Pro Preview 05-06 83.0%; Gemini 2.5 Pro Experimental 03-25 86.7%; OpenAI o3 88.9% (high); OpenAI o4-mini 92.7% (high); Claude Sonnet 4 70.5%; Claude Opus 4 75.5% (32K thinking) | p. 5 |
| SimpleQA | — | accuracy | 54.0% | — | Gemini 2.5 Pro Preview 05-06 50.8%; Gemini 2.5 Pro Experimental 03-25 52.9%; OpenAI o3 48.6% (high); OpenAI o4-mini 19.3% (high); Grok 3 Beta 43.6% (extended thinking); DeepSeek R1 27.8% | p. 5 |
| FACTS Grounding | — | score | 87.8% | — | OpenAI o3 69.6% (high); OpenAI o4-mini 62.1% (high); Claude Sonnet 4 79.1%; Claude Opus 4 77.7% (32K thinking); Grok 3 Beta 74.8% (extended thinking); DeepSeek R1 82.4% | p. 5 |
| MMMU | Single attempt | accuracy | 82.0% | — | Gemini 2.5 Pro Preview 05-06 79.6%; Gemini 2.5 Pro Experimental 03-25 81.7%; OpenAI o3 82.9% (high); OpenAI o4-mini 81.6% (high); Claude Sonnet 4 74.4%; Claude Opus 4 76.5% (32K thinking) | p. 5 |
| VideoMME | Audio, visual, subtitles | accuracy | 86.9% | — | Gemini 2.5 Pro Preview 05-06 84.8% | p. 6 |
| Video-MMMU | — | accuracy | 83.6% | — | — | p. 6 |
| MRCR v2 | 8-needle; 128K average | accuracy | 58.0% | — | OpenAI o3 57.1% (high); OpenAI o4-mini 36.3% (high); Claude Sonnet 4 39.1%; Claude Opus 4 16.1% (no thinking and API refusals); Grok 3 Beta 34.0% (extended thinking) | p. 6 |
| MRCR v2 | 8-needle; 1M pointwise | accuracy | 16.4% | — | — | p. 6 |
| Global MMLU (Lite) | — | accuracy | 89.2% | — | Gemini 2.5 Pro Preview 05-06 88.6%; Gemini 2.5 Pro Experimental 03-25 89.8% | p. 6 |

## Safety findings

### Safety classification

- **Framework:** Google DeepMind Frontier Safety Framework
- **Overall determination:** No CCL reached for GA; cyber uplift alert threshold reached; deceptive alignment GA incomplete

For Gemini 2.5 Pro GA, Google says no new alert thresholds or CCLs were reached, while cyber uplift had already reached an alert threshold and prompted a response plan. Deceptive-alignment evaluations for GA were not complete; Google relies on earlier 2.5 Pro results to judge CCLs unlikely. (pp. 11-12, 21)

| Domain | Determination | Level | Finding | Source |
| --- | --- | --- | --- | --- |
| CBRN | Below threshold | Uplift Level 1 | GA shows minor increases over Experimental 03-25 but does not reach the CBRN alert threshold or CCL. | pp. 12-13 |
| Cybersecurity | Below threshold | Autonomy Level 1; CCL not reached | GA key-skills results are 7/8 easy, 10/28 medium, and 1/12 hard, below the cyber autonomy CCL. | pp. 11, 15-16 |
| Cybersecurity | Alert threshold reached | Uplift Level 1; CCL not reached | Google says cyber uplift reached the early-warning alert threshold, although GA remains below the CCL. | pp. 11, 14, 21 |
| Machine-learning R&D | Below threshold | Autonomy/uplift Level 1 | GA best RE-Bench runs are 50% to 125% of expert-written solutions, but the alert threshold is not reached. | pp. 17, 19 |
| Deceptive alignment | Not evaluated | Instrumental reasoning L1/L2 | GA deceptive-alignment evaluations were not completed; Experimental 03-25 results make Google judge GA unlikely to reach either CCL. | pp. 20-21 |

### Agentic-coding risks

- **Reward hacking** (reported): Frontier Safety correctness checks reviewed RE-Bench trajectories and did not find benchmark-invalidating errors or an obvious reward-hack exploitation path. (p. 21)
- **Test tampering** (not reported): The card reports no evaluation of editing, deleting, or weakening tests in coding tasks.
- **Destructive or overeager actions** (not reported): The card reports no evaluation of destructive or unrequested tool actions.
- **Sabotage** (not reported): GA deceptive-alignment evaluations were incomplete; the card mentions earlier Decision Sabotage results only for Preview/Experimental lineage, not GA.
- **Prompt injection** (not reported): The card reports no prompt-injection evaluation involving tool, file, browser, or repository content.
- **Honesty** (not reported): The card reports no honesty, deception, or false-task-success evaluation for GA.
- **Sycophancy** (not reported): The card reports no sycophancy evaluation.
- **Evaluation awareness** (family-level): Earlier 2.5 Pro deceptive-alignment work tested situational awareness; GA testing was not complete, and Google uses earlier results only to judge GA unlikely to reach CCLs. (pp. 20-21)
- **Over-refusal** (reported): Google names over-refusals and tone as the main safety limitations for Gemini 2.5 Pro. (p. 10)

### Other safety findings

- Development safety results versus Gemini 1.5 Pro 002 show text-to-text violations down 0.9%, multilingual violations down 3.5%, image-to-text violations up 1.8% with a non-egregious note, tone up 18.4%, and instruction following up 14.8%. (p. 9)
- Assurance evaluations found low safety-policy violation rates across modalities for the experimental, preview, and GA versions. (pp. 9-10)
- For CBRN, Google says the model gives detailed technical knowledge but does not consistently enable progress through key bottleneck stages. (pp. 12-13)
- Cyber key-skills results for GA are 7/8 easy, 10/28 medium, and 1/12 hard, and Google says both cyber CCLs are not reached. (pp. 11, 15-16)
- Cyber uplift nonetheless reaches an early-warning alert threshold, prompting a response plan, more frequent testing, and accelerated mitigations. (pp. 11, 14, 21)
- For ML R&D, GA best RE-Bench runs are between 50% and 125% of expert-written solutions, but the model remains below the alert threshold. (pp. 17, 19)
- GA deceptive-alignment testing was incomplete; earlier 2.5 Pro results are used to judge GA unlikely to reach instrumental-reasoning CCLs. (pp. 20-21)

## Limitations and caveats

- General limitations include hallucinations, causal-understanding weaknesses, complex logical-deduction limits, and counterfactual-reasoning limits. (p. 7)
- The knowledge cutoff is January 2025. (p. 7)
- The main safety limitations are over-refusals and tone, including refusals that can sound preachy. (p. 10)
- Capability comparisons mix provider-reported numbers, different scaffolds, thinking settings, single versus multiple attempts, and leaderboard sources. (p. 4)
- MRCR v2 uses a harder eight-needle methodology than prior reports. (p. 4)
- GA deceptive-alignment evaluations were not complete at update time. (pp. 20-21)
- RE-Bench covers only a subset of the skills needed for the full AI R&D pipeline. (pp. 17-18)

## Practical implications for Copilot users

### Choose it for

- **Historical comparison:** The card is a detailed predecessor record for later Gemini Pro and Flash claims, with GA benchmark, safety, and FSF results. (pp. 2, 5, 11)
- **Long context:** The model has a 1M-token context window and reports MRCR v2 at both 128K average and 1M pointwise settings. (pp. 2, 6)
- **Vision:** The card reports multimodal input plus MMMU, Vibe-Eval, VideoMME, and Video-MMMU results for GA. (pp. 2, 5-6)

### Avoid it for

- **Security work:** Cyber uplift reaches an alert threshold even though the CCL is not reached. (pp. 11, 14, 21)
- **Untrusted input:** Prompt-injection robustness is not reported, despite evaluations involving search, code, and agent scaffolds. (pp. 4, 20)
- **High-stakes domains:** The card lists hallucination and reasoning limitations, plus incomplete GA deceptive-alignment evaluation. (pp. 7, 20)

### Guidance

- GitHub retired Gemini 2.5 Pro from Copilot on 2026-07-31; the guidance below serves historical comparison and the lineage of later models.
- Use this digest as historical context; GitHub retired the model and did not list it for the Copilot CLI.
- For historical code outputs, rerun modern tests because the card predates later Gemini safety and coding improvements.
- Treat cyber or security automation cautiously in successors because this card already triggered an FSF alert threshold.
- Do not use this card alone to conclude situational-awareness or stealth risks are covered for GA.
- When comparing benchmarks, account for the card’s caveat that scaffolds, thinking settings, and attempt counts differ by model.

## Document coverage

The 21-page document is dedicated to Gemini 2.5 Pro GA while retaining Preview 05-06 and Experimental 03-25 rows. Capability tables on pages 5-6 and several FSF figures were rendered to verify image-only values. Evaluation rows identify when values are GA-specific; earlier-version details are used only where the card itself uses them for lineage or GA risk judgments.

- **Card type:** Dedicated. The document is about this model; it may include short sibling sections.
- **Pages specific to this model:** the whole document
- **Names the document uses for this model:** Gemini 2.5 Pro
- **Catalog scope:** Dedicated publisher card for this model.
