# GPT-5.6 Luna

<!-- Generated from digest.json by models/digest_check.py. Edit digest.json, then run `python3 digest_check.py --write gpt-5.6-luna`. -->

> Original digest of *GPT-5.6 System Card* (OpenAI, July 9, 2026; 82 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.
>
> Also cited: *GPT-5.6 – August Updates* (OpenAI, August 6, 2026; 30 pages), cited as "August update".

**Copilot status** (catalog checked 2026-10-06): Current; GitHub release status GA. CLI: Yes. App model picker: listed. App reasoning efforts: none, low, medium, high, xhigh, max. App Auto: yes. App long-context option: yes.

## At a glance

GPT-5.6 Luna is OpenAI's fastest GPT-5.6 family member in the July card. It shares the family High designations for biological/chemical and cybersecurity capability, but its own rows generally trail Sol and Terra on complex edit-conflict and cyber-range evidence. The August supplement adds refreshed ChatGPT Luna measurements, but GitHub does not identify which Luna checkpoint Copilot serves.

- **Choose it for:** Fast, reviewed coding help and lightweight troubleshooting where Luna's latency profile matters more than Sol-only long-horizon evidence.
- **Watch out for:** Luna has weaker complex edit-conflict and cyber-range rows, and the August ChatGPT checkpoint is not confirmed as Copilot's checkpoint.
- The July card names Luna as the fastest GPT-5.6 member while applying the same family Preparedness result: High for biological/chemical risk and cybersecurity, below High for AI self-improvement. (pp. 2, 35, 47)
- Luna's own July rows include 0.32 on destructive-action avoidance plus correctness, 0.897 on prompt-injection search/function-calling accuracy, and 55.7 on HealthBench Professional. (pp. 11, 13, 15)
- Cybersecurity High applies to Luna, but the Critical rule-out relies on Sol's harder evaluation and Luna being less capable on proxy cyber tests. (p. 47)
- The August ChatGPT Luna checkpoint is below the CVE-Bench High threshold and passes 61.5% of cyber-range scenarios, failing five named scenarios. (August update, pp. 24, 27)
- The August update reports Luna at 53.3 on HealthBench and 44.1 on HealthBench Professional, with improved factuality versus GPT-5.5 Instant but no GitHub checkpoint mapping. (August update, pp. 11-12)

## Capabilities

### Key facts

| Fact | Value | Source |
| --- | --- | --- |
| Release date | Not stated. The system card is dated 2026-07-09 but does not give a model release date. | — |
| Knowledge cutoff | Not stated. The card does not state a knowledge cutoff. | — |
| Context window | Not stated. The card does not state a context window. | — |
| Maximum output | Not stated. The card does not state a maximum output length. | — |
| Input modalities | Text, Image. The card evaluates text prompts and combined text-image inputs; it does not list every supported input type. | pp. 7, 10 |
| Output modalities | Text. The evaluated safety and robustness tasks score assistant text responses. | pp. 7, 10 |
| Reasoning controls | Effort levels (stated as reasoning effort). The card says results vary with the amount of thinking used, but does not enumerate served effort levels. | p. 3 |
| Effort levels | Not stated. The card names lowest deployment settings and maximum reasoning effort in places, but does not list product effort levels. | p. 3 |
| Tool use | Computer use, Function calling, Web search, Browser, Code execution, Terminal, File editing. These tools appear in evaluations: computer-use confirmations, function-calling/search prompt injection, file edits, browser/computer access, and terminal-like cyber harnesses. | pp. 11, 13, 23, 44, 49 |
| Open weights | Not stated. The card does not state whether weights are open. | — |
| Architecture | Not stated. The card identifies GPT-5.6 as a reasoning model family but does not state an architecture identifier. | — |
| Total parameters | Not stated. The card does not state a parameter count. | — |
| Active parameters | Not stated. The card does not state an active-parameter count. | — |

### Capability notes

- Luna is the fastest member named in the three-model GPT-5.6 family and shares the family reasoning-model framing and safety framework. (pp. 2, 6)
- Luna's July HealthBench rows are 55.7 on Professional, 55.8 on HealthBench, 32.0 on Hard, and 95.1 on Consensus after length adjustment. (p. 15)
- OpenAI extends the High cybersecurity designation to Luna while saying Luna is less capable than Sol on proxy cyber evaluations. (p. 47)
- The July internal CTF text says Luna exceeds the Preparedness High threshold and exceeds GPT-5.4, but not GPT-5.5 or Terra; the transcription gives no numeric Luna CTF score. (p. 49)
- The August ChatGPT Luna checkpoint improves over GPT-5.5 Instant on every HealthBench row and reports 82.97% on refusal-adjusted tacit-knowledge troubleshooting. (August update, pp. 11, 17)
- For the August cyber-range scenarios, Luna passes 61.5% overall and fails Binary Exploitation, Firewall Evasion, EDR Evasion, Leaked Token, and CA/DNS Hijacking. (August update, pp. 25-27)

## Evaluations

Results are as the document reports them. Scores from different publishers, harnesses, effort levels, or tool settings are often not directly comparable; the Setting column records those conditions.

### Headline coding and agentic results

The document reports no coding or agentic benchmark results for this model.

### Other reported results

| Benchmark | Variant | Metric | Result | Setting | Comparators | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Production Benchmarks | Self-harm | not-unsafe rate | 0.954 | July model; no system-level safeguards | GPT-5.5 0.917 (thinking; same table) | p. 7 |
| Image Input Safety | Self-harm | not-unsafe rate | 0.99 | Combined text-and-image disallowed-content cases | GPT-5.5 0.983 (same table) | p. 10 |
| Destructive Action Avoidance | Avoidance + correctness | safe response rate | 0.32 | Coding-style task with protected user data injected into the environment | GPT-5.5 0.44 (same table) | p. 11 |
| User Confirmations | General confirmation | accuracy | 0.93 | Computer-use confirmation-policy evaluation | GPT-5.5 0.94 (same table) | p. 12 |
| Prompt Injection | Connector attacks | accuracy | 0.999 | Known connector attacks | GPT-5.5 1.0 (same table) | p. 13 |
| Prompt Injection | Indirect prompt injection | attack success rate (lower is better) | 2.94% | GPT-Red agentic attacks | — | p. 14 |
| HealthBench Professional | — | score | 55.7% | Length-adjusted July score | GPT-5.5 51.8% (length-adjusted) | p. 15 |
| HealthBench | Hard | score | 32.0% | Length-adjusted July score | GPT-5.5 31.5% (length-adjusted) | p. 15 |
| Dynamic Mental Health Simulations | Self-harm | not-unsafe rate | 0.905 | Dynamic adversarial multi-turn simulations | GPT-5.5 0.868 (same table) | p. 16 |
| Tacit Knowledge and Troubleshooting | August refusal-adjusted | accuracy | 82.97% | max effort; Refusals and safe completions counted as successes | — | August update, p. 17 |
| BioSecBench | Severe biology refusal | not-unsafe rate | 0.946 | Model-level biology refusal evaluation | GPT-5.5 0.958 (thinking; same table) | p. 74 |
| BioSecBench | Benign biology over-refusal | not-overrefuse rate | 0.989 | Benign advanced-biology prompts | GPT-5.5 0.917 (thinking; same table) | p. 74 |
| OpenAI cybersecurity safety evaluation | Production data | safe response rate | 0.986 | Model-level cybersecurity refusal evaluation | GPT-5.5 0.928 (same table) | p. 75 |
| Under-18 Safety | Eating disorders | not-unsafe rate | 0.81 | lowest deployment setting effort; Updated ChatGPT checkpoint; teen-specific safety standard | GPT-5.5 Instant (June Update) 0.635 (same table) | August update, p. 7 |
| HealthBench Professional | August update | score | 44.1% | lowest deployment setting effort; Length-adjusted August ChatGPT checkpoint | GPT-5.5 Instant 38.4% (same table) | August update, p. 11 |
| Dynamic Mental Health Simulations | August self-harm | not-unsafe rate | 0.911 | lowest deployment setting effort; Dynamic adversarial multi-turn simulations | GPT-5.5 Instant (June Update) 0.967 (same table) | August update, p. 9 |
| Cyber Range | — | success rate | 61.5% | max effort; Representative updated checkpoint; pass/fail over 16 trials per scenario | GPT-5.5 92.3% (thinking; same table) | August update, pp. 25, 27 |
| OpenAI cybersecurity safety evaluation | Production data | safe response rate | 0.974 | August update checkpoint; model-level cyber refusal evaluation | GPT-5.6 Sol 0.981 (July checkpoint) | August update, p. 29 |

## Safety findings

### Safety classification

- **Framework:** OpenAI Preparedness Framework
- **Overall determination:** High for biological/chemical and cybersecurity; below High for AI self-improvement

OpenAI applies the same Preparedness designations to the GPT-5.6 family: High capability for biological/chemical risk and cybersecurity, below the High threshold for AI self-improvement, and not Critical for the tested biological and cyber pathways. (pp. 35-36, 47)

| Domain | Determination | Level | Finding | Source |
| --- | --- | --- | --- | --- |
| Biological and chemical | Threshold reached | High | All three GPT-5.6 models are treated as High capability for biological and chemical risk after three of four novice-uplift evaluations exceeded indicative thresholds; none of the critical biological evaluations exceeded threshold. | pp. 35-36 |
| Cybersecurity | Threshold reached | High | Sol is treated as High but below Critical in cybersecurity, and OpenAI extends that designation to Terra and Luna because they reach the High bar while remaining less capable than Sol on proxy cyber tests. | p. 47 |
| AI self-improvement | Below threshold | Below High | OpenAI says none of the GPT-5.6 models reach its High threshold for AI self-improvement. | p. 35 |

### Agentic-coding risks

- **Reward hacking** (sibling only): Sol has reported metagaming and cheating signals; the card does not report a Luna-specific reward-hacking or grader-gaming result. (pp. 30, 68-69)
- **Test tampering** (not reported): The card does not report Luna-specific test editing, deletion, or weakening behavior.
- **Destructive or overeager actions** (reported): Luna scores 0.73 on avoidance-only and 0.32 when correctness is also required, the lowest of the three July GPT-5.6 rows. (p. 11)
- **Sabotage** (sibling only): UK AISI sabotage testing is reported for Sol, not Luna. (pp. 68-69)
- **Prompt injection** (reported): Luna scores 0.999 on connector prompt-injection accuracy and 0.897 on search/function-calling accuracy; GPT-Red attack success is 0.11% direct and 2.94% indirect. (pp. 13-14)
- **Honesty** (not reported): The supplement reports factuality gains for Luna, but the card does not report a Luna-specific agentic honesty or false-completion evaluation.
- **Sycophancy** (not reported): The card reports no Luna sycophancy evaluation.
- **Malicious agentic use** (reported): Luna is covered by the cyber and biology safety training tables; July cyber refusal is 0.986 on production data and 1.00 on synthetic data. (p. 75)
- **Over-refusal** (reported): The biology table reports Luna benign not_overrefuse at 0.989 on low-risk advanced-biology workflows. (p. 74)

### Other safety findings

- Luna shares the family Preparedness result: High for biological/chemical and cybersecurity risk, below High for AI self-improvement. (pp. 35-36, 47)
- OpenAI applies Sol's Critical cyber rule-out to Luna because Luna is smaller and less capable on proxy cyber evaluations. (p. 47)
- Luna's GPT-Red prompt-injection attack-success rates are 0.11% for direct attacks and 2.94% for indirect attacks. (p. 14)
- Luna's biology refusal rows are 0.946 severe not_unsafe, 0.926 dual-use not_unsafe, and 0.989 benign not_overrefuse. (p. 74)
- Luna's July cyber refusal rows are 0.986 on production-derived data and 1.00 on synthetic data. (p. 75)
- The shared two-tier monitor design applies to Luna, while the new activation-classifier system is described for Sol and Terra rather than Luna. (pp. 75-76)
- The August update reports Luna U18 rows including 0.984 for sexual content, 0.810 for eating disorders, and 0.977 for self-harm. (August update, p. 7)
- The August safeguard rows report Luna at 0.937 severe biology not_unsafe, 0.928 dual-use biology not_unsafe, 0.974 on cyber production data, and 0.997 on cyber synthetic data. (August update, p. 29)

## Limitations and caveats

- Luna has the lowest July destructive-action scores among the three GPT-5.6 models, at 0.73 avoidance-only and 0.32 with correctness. (p. 11)
- Detailed deployment-simulation, internal coding misalignment, CoT monitorability, metagaming, and external cyber/alignment sections are Sol-specific rather than Luna measurements. (pp. 18-19, 22, 30, 55, 68-69)
- Luna's Critical cyber conclusion relies on Sol's harder testing plus Luna's lower proxy capability, not a separate Luna critical-exploit campaign. (p. 47)
- OpenAI says capability evaluations are lower bounds because other scaffolds, longer rollouts, fine-tuning, or prompting could elicit more capability. (p. 35)
- The August Luna representative checkpoint is below the CVE-Bench High threshold and passes fewer cyber-range scenarios than August Sol. (August update, pp. 24, 27)
- The August update applies to refreshed ChatGPT Luna; it says Codex and ChatGPT Work stayed on July versions and does not map GitHub Copilot to a checkpoint. (August update, p. 2)

## Practical implications for Copilot users

### Choose it for

- **Low latency:** The July card names Luna as the fastest GPT-5.6 member, making it the family choice for fast reviewed interactions. (p. 2)
- **Quick edits:** Use Luna for short, supervised coding and explanation tasks rather than broad autonomous edits; its destructive-action row is weaker than Sol and Terra. (p. 11)
- **Vision:** The card reports Luna image-input safety rows for combined text-and-image inputs, including 0.990 on self-harm and 0.986 on harms-erotic. (p. 10)

### Avoid it for

- **Long-horizon autonomy:** Sol-only long-horizon and external evaluations should not be treated as Luna evidence, and Luna has weaker destructive-action rows. (pp. 11, 18-19)
- **Security work:** For advanced cyber investigations, Luna is High by framework but below August Sol on cyber range and below the CVE-Bench High threshold in the update. (August update, pp. 24, 27)
- **High-stakes domains:** The supplement reports HealthBench and factuality improvements, but those are benchmark signals for a ChatGPT checkpoint and not unsupervised high-stakes validation. (August update, pp. 11-12)

### Guidance

- Use Luna when responsiveness matters and the task is small enough for easy human review.
- Prefer Terra or Sol for broad refactors, long debugging sessions, or security investigations that need stronger long-horizon evidence.
- Inspect patches before applying them; Luna's combined destructive-action score is the weakest of the three GPT-5.6 rows.
- Keep prompt-injection defenses in place for issues, logs, terminal output, and web content; Luna still has indirect GPT-Red successes.
- Keep July and August evidence separate unless GitHub documents that Copilot serves the August ChatGPT Luna checkpoint.

## Document coverage

The July system card covers Sol, Terra, and Luna together. This digest uses Luna-specific table rows and family-level determinations that explicitly apply to all three models; Sol-only alignment, deployment-simulation, and external-evaluation sections are scope limits. The August supplement covers refreshed ChatGPT Luna and Sol checkpoints and is cited only where it names Luna.

- **Card type:** Family. The document covers several models in its main body and attributes results per model.
- **Pages specific to this model:** not separated by page
- **Names the document uses for this model:** GPT-5.6 Luna, Luna, gpt-5.6-luna
- **Catalog scope:** The GPT-5.6 System Card covers the Sol, Terra, and Luna family members. The August update covers refreshed ChatGPT versions of Sol and Luna.
- **Catalog note:** The August update states that Codex and ChatGPT Work continue to use the previously released GPT-5.6 versions; GitHub does not state which GPT-5.6 Luna checkpoint Copilot serves.
