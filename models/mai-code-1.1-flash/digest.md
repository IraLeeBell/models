# MAI-Code-1.1-Flash

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write mai-code-1.1-flash`. -->

> Original digest of *MAI-Code-1.1-Flash model card* (Microsoft, August 11, 2026; 6 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

**Copilot status** (catalog checked 2026-10-06): Current; GitHub release status GA. CLI: Yes. App model picker: listed. App reasoning efforts: low, medium, high. App Auto: yes. App long-context option: no. GitHub notes that MAI models are continuously improved, so served checkpoints may change.

## At a glance

MAI-Code-1.1-Flash is Microsoft's current sparse-MoE coding model for Copilot, adding image input to the MAI-Code Flash line while keeping a 256K-token context and 5B active parameters. Its card shows the clearest gains over MAI-Code-1-Flash on Terminal Bench 2.1 and image-to-code tasks. Safety coverage is process-oriented and names cyber and secure-coding checks, but it gives no numeric safety outcomes or agentic-misalignment tests.

- **Choose it for:** Responsive coding-agent work, repository questions, refactors, and UI tasks where image input may help.
- **Watch out for:** Safety evidence is qualitative, max output is not stated, and prompt-injection or test-tampering behavior is not measured.
- Compared with MAI-Code-1-Flash in the same card, pass rate rises from 51.7% to 62.9% on Terminal Bench 2.1 and from 71.6% to 72.6% on SWE-Bench Verified. (p. 5)
- The update adds image input: Microsoft reports 42.1% on ScreenShot2WebApp and 11.5% on Vision2Web Level3, with GPT 5.4 mini at 39.3% and 10.1% in the same table. (pp. 1, 5)
- The model is a sparse mixture-of-experts transformer with 138B total parameters, 5B active parameters, text and image inputs, text output, and a 256K-token context. (p. 1)
- Microsoft says the production Copilot harness includes repository context, tool calls, and verification, so the pass rates measure end-to-end developer workflows rather than stripped-down tasks. (p. 5)
- The safety section names data filtering, alignment training, cyber and secure-coding evaluations, safety classifiers, and filters, but gives no benchmark scores for those safety checks. (p. 4)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | August 11, 2026 (stated as August 11, 2026) | p. 1 |
| Knowledge cutoff | December 2025 (stated as Pretraining cut-off date: December 2025) | p. 3 |
| Context window | 256,000 tokens (stated as 256K tokens) | p. 1 |
| Maximum output | Not stated. The card does not state a maximum generated-output length. | — |
| Input modalities | Text, Image (stated as Text, Image) | p. 1 |
| Output modalities | Text (stated as Text) | p. 1 |
| Reasoning controls | Adaptive thinking. The card describes adaptive solution length rather than a user-set control. | pp. 2-3 |
| Effort levels | Not stated. The card names no user-selectable effort levels. | — |
| Tool use | Function calling. The benchmark method includes tool calls in the production Copilot harness but does not enumerate tool types. | p. 5 |
| Open weights | Not stated. The card does not state whether weights are open. | — |
| Architecture | Mixture of experts (stated as sparse Mixture-of-Experts layers) | p. 1 |
| Total parameters | 138 billion (stated as 138B total) | p. 1 |
| Active parameters | 5 billion (stated as 5B active) | p. 1 |

### Capability notes

- The model is built for coding assistance with text and image inputs, text output, a 256K-token context, and sparse mixture-of-experts layers. (p. 1)
- Microsoft positions it for Copilot developer work: agentic coding in repositories, repository question answering, refactoring, code generation and completion, telemetry-grounded tasks, and tool-using scenarios. (p. 2)
- Training starts from a compressed MAI-Thinking-1 mid-training checkpoint, then adds supervised tuning, about 2 million synthetic agentic tasks, and reinforcement learning across more than 150,000 environments. (p. 3)
- Using only the 1.1 card, the main differences from MAI-Code-1-Flash are image input, MAI-Code-1-Flash as a dependency, higher SWE-Bench Verified and Terminal Bench 2.1 pass rates, and new image-to-code tables. (pp. 1-2, 5)
- All compared models in the SWE-Bench Verified and Terminal Bench 2.1 table were evaluated in the same VS Code-based production Copilot harness with repository context, tool calls, and verification. (p. 5)
- The card reports strong web-app generation relative to the listed peers: Text2WebApp is 74.1%, while Claude Haiku 4.5 is 11.5% and GPT 5.4 mini is 58.3% in the same table. (p. 5)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| SWE-bench Verified | — | pass@1 | 72.6% | VS Code-based Copilot production harness; repository context, tool calls, and verification included; 8.6K average token usage | MAI-Code-1-Flash 71.6% (10.8K average token usage); Claude Haiku 4.5 69.8% (20.9K average token usage); GPT-5.4 mini 69.2% (9.4K average token usage) | p. 5 |
| Terminal-Bench 2.1 | — | success rate | 62.9% | VS Code-based Copilot production harness; repository context, tool calls, and verification included; 17.0K average token usage | MAI-Code-1-Flash 51.7% (14.2K average token usage); Claude Haiku 4.5 49.4% (25.5K average token usage); GPT-5.4 mini 60.7% (21.9K average token usage) | p. 5 |
| Text2WebApp | — | pass@1 | 74.1% | VS Code-based Copilot production harness; internal web-app development evaluation; 17.1K average token usage | Claude Haiku 4.5 11.5% (60.0K average token usage); GPT-5.4 mini 58.3% (36.4K average token usage) | p. 5 |
| ScreenShot2WebApp | — | pass@1 | 42.1% | VS Code-based Copilot production harness; screenshot-to-web-app evaluation; 10.5K average token usage | Claude Haiku 4.5 10.0% (33.9K average token usage); GPT-5.4 mini 39.3% (26.6K average token usage) | p. 5 |
| Vision2Web | Vision2Web Level3 | pass@1 | 11.5% | VS Code-based Copilot production harness; 15.1K average token usage | Claude Haiku 4.5 13.7% (36.5K average token usage); GPT-5.4 mini 10.1% (3.7K average token usage) | p. 5 |

### Other reported results

None beyond the headline results.

## Safety findings

### Safety classification

- **Framework:** No safety framework stated
- **Overall determination:** Not stated

The card does not name a Microsoft safety framework or assign an overall safety level. It instead describes training-time filtering and alignment, cyber and secure-coding evaluations, and release checks using safety classifiers and filters.

The document states no per-domain determinations.

### Agentic-coding risks

- **Reward hacking** (not reported): The card reports no evaluation of reward hacking, grader gaming, or exploiting benchmark rubrics.
- **Test tampering** (not reported): The card reports no evaluation of modifying, deleting, or weakening tests during coding tasks.
- **Destructive or overeager actions** (not reported): The card reports no evaluation of irreversible or unrequested tool actions by the model.
- **Sabotage** (not reported): The card reports no sabotage, oversight-evasion, or deliberate underperformance evaluation.
- **Prompt injection** (not reported): The card describes tool-using workflows and safety filters but reports no prompt-injection or instruction-hierarchy test.
- **Honesty** (not reported): The card reports no honesty, deception, or false-claim-of-completion evaluation.
- **Sycophancy** (not reported): The card reports no sycophancy or user-pressure evaluation.

### Other safety findings

- Pretraining reduces exposure to harmful material by filtering it out or lowering its weight in the data mixture. (p. 4)
- Later supervised and reinforcement-learning stages are described as alignment steps intended to favor helpful and safer responses and discourage undesirable outputs. (p. 4)
- Safety evaluation coverage is named qualitatively: CyberBench, CyberSecEval, and SecRepo for security threats, vulnerability avoidance, and secure-coding alignment. (p. 4)
- The release process used production model APIs with safety classifiers and filters applied, but the card does not publish numeric outcomes for those checks. (p. 4)

## Limitations and caveats

- Microsoft warns that generated code or prose can be inaccurate, incomplete, or otherwise wrong, and says developers should review, test, and validate outputs before consequential use. (p. 4)
- The safety section names methods and benchmark families but gives no safety scores, thresholds, or per-risk outcomes. (p. 4)
- The 1.1 card defers more general benchmarks to the MAI-Code-1-Flash card, so this document mainly supports coding, web-app, and image-to-code comparison. (p. 5)
- The distribution text is mixed: one passage says VS Code with CLI planned later, while another says all GitHub Copilot clients. (pp. 2, 4)
- No maximum output length, open-weight status, prompt-injection result, or honesty result is stated. (pp. 1, 4)

## Practical implications for Copilot users

### Choose it for

- **Agentic coding:** The card's direct comparison reports 72.6% on SWE-Bench Verified and 62.9% on Terminal Bench 2.1 in a production Copilot harness with repository context, tools, and verification. (p. 5)
- **Web development:** The web-app table reports 74.1% on Text2WebApp and 42.1% on ScreenShot2WebApp, both above the GPT 5.4 mini comparator in the same chart. (p. 5)
- **Vision:** Unlike MAI-Code-1-Flash, the model accepts image input and is evaluated on screenshot and vision-to-web coding tasks. (pp. 1, 5)
- **Quick edits:** Microsoft describes adaptive solution length, with shorter answers for simpler requests and more reasoning on harder tasks. (pp. 2-3)

### Avoid it for

- **Untrusted input:** The card lists safety filters and security evaluations but no prompt-injection test for instructions embedded in files, tool outputs, or web content. (p. 4)
- **High-stakes domains:** Microsoft says generated outputs can be wrong and should be reviewed, tested, and validated before consequential use. (p. 4)

### Guidance

- Use the model's low, medium, or high Copilot app efforts based on task difficulty; the card does not map benchmark rows to those effort settings.
- Treat the MAI-Code-1.1 gains over MAI-Code-1-Flash as strongest evidence for terminal-agent and image-to-code work, not for every reasoning benchmark.
- Keep tests and code review in the loop because the card does not evaluate test tampering, reward hacking, or false claims of completion.
- Use image input for UI context, but verify carefully: Vision2Web Level3 trails Claude Haiku 4.5 in the card's own table.
- GitHub notes that MAI models are continuously improved, so a served checkpoint may differ from the card's August 2026 results.

## Document coverage

The six-page Microsoft card is dedicated to MAI-Code-1.1-Flash. MAI-Code-1-Flash, Claude Haiku 4.5, and GPT 5.4 mini appear only as comparison rows in the evaluation tables; this digest uses them only as comparators. The card defers broader general benchmarks to the earlier MAI-Code-1-Flash card, so they are not repeated here.

- **Card type:** Dedicated. The document is about this model; it may include short sibling sections.
- **Pages specific to this model:** the whole document
- **Names the document uses for this model:** MAI-Code-1.1-Flash
- **Catalog scope:** Dedicated publisher card for this model.
