# GPT-5.6 Terra

> Original digest of *GPT-5.6 System Card* (OpenAI, 2026-07-09; 82 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance

- GPT-5.6 Terra is the middle member of the GPT-5.6 family; the July system card covers Sol, Terra, and Luna together, but many deep-dive analyses are Sol-only (pp. 2, 18-22).
- OpenAI assigns Terra the same Preparedness outcomes as its siblings: biological/chemical High, cybersecurity High, and AI self-improvement below High (pp. 34-35, 47).
- Terra's reported strengths are broad safety, strong prompt-injection results, HealthBench scores close to Sol, and enough biological/cyber capability to receive the family High designations (pp. 13-16, 35, 47).
- On coding-style safety, Terra scored 0.81 for avoiding data overwrites and 0.37 when correctness was also required, between Sol and Luna on both rows (p. 11).
- The safeguards section explicitly names Terra, along with Sol, as using activation classifiers in addition to the monitor stack that applies to all GPT-5.6 models (pp. 75-76).

## Capabilities

- Terra uses the same GPT-5.6 family training context and reasoning-model framing as Sol and Luna, with evaluations reported across safety, robustness, health, Preparedness, and safeguards (pp. 2-6).
- In HealthBench, Terra retained much of Sol's health performance: Professional 57.7, HealthBench 57.0, Hard 32.7, and Consensus 95.1 after length adjustment (p. 15).
- Terra is classified as High in cybersecurity; OpenAI says it is less capable overall than Sol in that domain, but still above the High bar (p. 47).
- On the internal CTF set, Terra exceeded GPT-5.5 and trailed Sol, giving OpenAI another signal for the cybersecurity High designation (p. 49).
- For biological tacit-knowledge questions, Terra had the highest new-model score when refusals and safe completions were counted as successes: 84.1%, above the 80% expert-consensus threshold (p. 40).
- Terra was included in CoT-Control testing and showed low controllability similar to earlier models, unlike Sol's higher controllability result (p. 28).
- In AI self-improvement proxy tasks, OpenAI groups Terra with Sol as improving over GPT-5.5 on internal research debugging, NanoGPT, and PostTrainBench Lite, yet still keeps the category below High (pp. 58-66).

## Evaluations

| Benchmark | Result | Context | Pages |
|---|---|---|---|
| Production disallowed-content prompts | violent-illicit 0.952, nonviolent-illicit 0.990, hate 1.000, sexual/minors 0.974 | Terra not_unsafe on challenging production-derived prompts | p. 7 |
| Image-input safety | hate 0.999, extremism 0.978, self-harm 0.986, harms-erotic 0.991 | Combined text-and-image disallowed-content evaluation | p. 10 |
| Destructive-action avoidance | 0.81 avoidance-only; 0.37 avoidance plus correctness | Measures completing a task without overwriting adversarially injected user data | p. 11 |
| User confirmations | financial 0.98, high-stakes communication 0.98, general confirmation 0.94 | Computer-use confirmation-policy evaluation | p. 12 |
| Prompt injection | connectors 1.000; search/function-calling 0.946; GPT-Red direct ASR 0.061%; indirect ASR 3.32% | Connector attacks and GPT-Red direct/agentic attacks | pp. 13-14 |
| HealthBench suite | Professional 57.7, HealthBench 57.0, Hard 32.7, Consensus 95.1 | Length-adjusted scores | p. 15 |
| Dynamic mental-health simulations | mental health 0.985, emotional reliance 0.976, self-harm 0.947 | Multi-turn adversarial user simulations | p. 16 |
| CoT-Control | low controllability similar to previous models | Run only on Sol and Terra; low is the desired direction | p. 28 |
| Tacit knowledge and troubleshooting | 84.1% with refusal adjustment | Highest new-model score; above the 80% expert-consensus threshold | p. 40 |
| Internal CTF | above GPT-5.5 and below Sol | OpenAI's curated CTF evaluation for the High cyber threshold | p. 49 |
| Biology model-refusal evaluation | severe not_unsafe 0.950, dual-use not_unsafe 0.911, benign not_overrefuse 0.978 | Model-response safety before monitor performance | p. 74 |
| Cybersecurity safety evaluation | production data 0.987; synthetic data 0.998 | Model-response refusal evaluation | p. 75 |

## Safety findings

- Terra shares the family Preparedness outcome: High in biological/chemical and cybersecurity capability, below High in AI self-improvement (pp. 34-35, 47).
- OpenAI's cyber Critical rule-out was tested directly on Sol and then applied to Terra and Luna because they are smaller and less capable on proxy cyber evaluations (p. 47).
- Terra's GPT-Red attack-success rates were 0.061% for direct prompt injections and 3.32% for indirect prompt injections, both measured against automated red-team attacks (p. 14).
- Biology model-level refusal results show Terra at 0.950 on severe not_unsafe prompts and 0.978 on benign not_overrefuse prompts, reflecting both refusal behavior and reduced overrefusal pressure (p. 74).
- Cybersecurity refusal results show Terra at 0.987 on production-derived data and 0.998 on synthetic data (p. 75).
- Activation classifiers are part of Terra's higher-risk safeguard path, while the two-tier topical-classifier and safety-reasoner monitor design is shared across all GPT-5.6 models (pp. 75-76).
- Terra's low CoT controllability result is a favorable contrast to Sol in the card's reasoning-trace controllability discussion (p. 28).

## Limitations and caveats

- The July family card introduces Terra alongside Sol and Luna, but many deeper deployment-simulation and external-evaluation sections are Sol-specific rather than Terra measurements (pp. 2, 18-22, 55-70).
- Deployment-simulation forecasts for disallowed content and ChatGPT misalignment were evaluated for Sol only, so they should not be projected to Terra (pp. 8, 17-18).
- Several external evaluations, including SecureBio, Irregular, UK AISI, METR, and Apollo summaries, are Sol-focused and do not establish Terra-specific outcomes (pp. 46, 55-70).
- Terra's cyber Critical conclusion partly relies on Sol's harder test plus Terra's lower proxy capability, not on a separate Terra VulnLMP demonstration (p. 47).
- Terra trailed Sol on complex edit-conflict performance, with 0.37 on avoidance plus correctness versus Sol's 0.44 (p. 11).
- OpenAI warns that capability testing is a lower bound because stronger scaffolds, longer rollouts, fine-tuning, or new elicitation methods could change observed behavior (p. 35).

## Practical implications for Copilot users

- Terra is a sensible default when a task needs more reasoning than a fast model but does not obviously require the most intensive Sol-style investigation.
- For everyday coding, still inspect generated patches and run tests; Terra's conflict-avoidance score is strong but below Sol on the combined task-completion metric.
- Use Terra for authorized defensive security triage with normal review controls, but escalate long-horizon exploit research, broad vulnerability campaigns, or ambiguous dual-use work to stricter human oversight.
- Its prompt-injection results are strong, yet developers should still treat retrieved documents, web pages, terminal output, and issue comments as untrusted instructions.
- Prefer Sol when the work depends on the Sol-only external cyber, agentic-coding, or AI R&D evidence; prefer Luna when latency matters more than complex autonomy.
- Do not import August Sol/Luna checkpoint claims into Terra evaluations; the public supplement gives no Terra measurements.

## Document coverage

This digest uses the GPT-5.6 System Card sections on family scope, safety, robustness, health, alignment, Preparedness, and safeguards, focusing on rows where Terra appears explicitly. Sol-only deployment simulations, external evaluations, and chain-of-thought discussions are included only as caveats when they affect how Terra should be interpreted. The August update does not cover Terra, and the catalog lists no Terra supplement, so no Terra claim here cites that document.
