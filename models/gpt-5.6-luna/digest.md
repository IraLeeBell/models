# GPT-5.6 Luna

> Original digest of *GPT-5.6 System Card* (OpenAI, 2026-07-09; 82 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance

- GPT-5.6 Luna is the fastest member of the GPT-5.6 family in the July card; the same family card also covers Sol and Terra (p. 2).
- OpenAI gives Luna the family Preparedness outcomes: biological/chemical High, cybersecurity High, and AI self-improvement below High (pp. 34-35, 47).
- Luna generally trails Sol and Terra on complex coding/edit and cyber tasks, but still posts strong safety and health rows across the July tables (pp. 7, 10-16).
- The July card's activation-classifier language names Sol and Terra, while Luna is still covered by the shared topic-classifier and safety-reasoner monitor path used for all GPT-5.6 models (pp. 75-76).
- The August update covers refreshed ChatGPT Luna and Sol checkpoints, not Terra; it adds teen-safety, hallucination, health, cyber-range, and updated safeguard results for Luna (August update, pp. 2, 7, 11-13, 25-29).
- The update says Codex and ChatGPT Work continued using the earlier Sol/Luna versions, and GitHub does not specify which Luna checkpoint Copilot serves (August update, p. 2).

## Capabilities

- Luna shares the GPT-5.6 reasoning-model training context, but OpenAI positions it as the family member optimized for the quickest interactions rather than the deepest long-horizon work (pp. 2, 6).
- July Luna's HealthBench scores were 55.7 Professional, 55.8 general HealthBench, 32.0 Hard, and 95.1 Consensus after length adjustment (p. 15).
- Luna is treated as High in cybersecurity even though OpenAI says it is smaller and less capable on proxy cyber evaluations than Sol (p. 47).
- In the August update, Luna exceeded the internal CTF High threshold, but was below the CVE-Bench High threshold and had a 61.5% combined cyber-range pass rate (August update, pp. 23-27).
- Luna's biological/chemical High rating is supported by the July family analysis and the August update reports that Luna led the updated models on refusal-adjusted tacit-knowledge troubleshooting at 82.97% (pp. 35-36; August update, p. 17).
- The August ChatGPT Luna checkpoint improved over GPT-5.5 Instant on every HealthBench row, including 44.1 on HealthBench Professional and 28.7 on HealthBench Hard (August update, pp. 11-12).
- Factuality testing in the August update reports that Luna reduced factual-error rates by more than 60% on high-stakes prompts and by about 30% on the other two prompt sets, compared with GPT-5.5 Instant (August update, pp. 12-13).

## Evaluations

| Benchmark | Result | Context | Pages |
|---|---|---|---|
| Production disallowed-content prompts | violent-illicit 0.940, nonviolent-illicit 0.993, hate 1.000, sexual/minors 0.974 | July Luna not_unsafe on challenging production-derived prompts | p. 7 |
| Image-input safety | hate 0.996, extremism 0.966, self-harm 0.990, harms-erotic 0.986 | Combined text-and-image disallowed-content evaluation | p. 10 |
| Destructive-action avoidance | 0.73 avoidance-only; 0.32 avoidance plus correctness | Coding-style task with protected injected user data | p. 11 |
| User confirmations | financial 1.00, high-stakes communication 0.99, general confirmation 0.93 | Computer-use confirmation-policy evaluation | p. 12 |
| Prompt injection | connectors 0.999; search/function-calling 0.897; GPT-Red direct ASR 0.11%; indirect ASR 2.94% | Known connector attacks and GPT-Red automated attacks | pp. 13-14 |
| HealthBench suite | Professional 55.7, HealthBench 55.8, Hard 32.0, Consensus 95.1 | July Luna length-adjusted scores | p. 15 |
| Dynamic mental-health simulations | mental health 0.989, emotional reliance 0.957, self-harm 0.905 | Multi-turn adversarial simulations | p. 16 |
| Biology model-refusal evaluation | severe not_unsafe 0.946, dual-use not_unsafe 0.926, benign not_overrefuse 0.989 | Model-level biology refusal and overrefusal evaluation | p. 74 |
| Cybersecurity safety evaluation | production data 0.986; synthetic data 1.00 | Model-level cyber refusal evaluation | p. 75 |
| August U18 safety | AGE 0.857, sexual content 0.984, eating disorders 0.810, self-harm 0.977 | Refreshed ChatGPT Luna teen-safety rows | August update, p. 7 |
| August ChatGPT HealthBench | HealthBench 53.3, Hard 28.7, Consensus 94.8, Professional 44.1 | Refreshed ChatGPT Luna checkpoint; not confirmed for Copilot | August update, p. 11 |
| August cyber range | combined pass rate 61.5%; failed Binary Exploitation, Firewall Evasion, EDR Evasion, Leaked Token, and CA/DNS Hijacking | Representative updated Luna checkpoint | August update, pp. 25-27 |

## Safety findings

- Luna receives the same family Preparedness ratings as Sol and Terra, but OpenAI applies Sol's critical cyber rule-out to Luna because Luna is smaller and less capable on proxy evaluations (pp. 34-35, 47).
- July Luna's GPT-Red prompt-injection attack-success rates were 0.11% for direct scenarios and 2.94% for indirect agentic scenarios (p. 14).
- Luna's July model-level biology refusal scores were 0.946 for severe not_unsafe, 0.926 for dual-use not_unsafe, and 0.989 for benign not_overrefuse (p. 74).
- The shared real-time monitor design applies to Luna, but the new activation-classifier system is described for Sol and Terra rather than Luna (pp. 75-76).
- The August update reports strong U18 Luna rows, including 0.984 for sexual content and 0.810 for eating-disorder-related examples (August update, p. 7).
- The August cyber section says Luna exceeds the CTF High threshold but falls below the CVE-Bench High threshold, showing that the High designation is not uniform across every cyber benchmark (August update, pp. 23-24).
- The August safeguard rows show Luna at 0.937 severe biology not_unsafe, 0.928 dual-use biology not_unsafe, 0.974 on cyber production data, and 0.997 on cyber synthetic data (August update, p. 29).

## Limitations and caveats

- Luna's destructive-action scores are the lowest of the three GPT-5.6 models reported in the July table, with 0.73 avoidance-only and 0.32 when correctness is included (p. 11).
- Most detailed alignment, deployment-simulation, CoT-monitorability, metagaming, and external cyber discussions in the July card are Sol-specific and should not be read as Luna measurements (pp. 18-32, 55-70).
- OpenAI's cyber Critical conclusion for Luna is inferred from Sol's harder testing plus Luna's lower proxy capability, not from a Luna-specific critical exploit campaign (p. 47).
- In the August update, Luna was below the High threshold on CVE-Bench and passed fewer cyber-range scenarios than updated Sol (August update, pp. 24-27).
- OpenAI cautions that capability evaluations are lower bounds because stronger elicitation methods, longer rollouts, or scaffolding could reveal additional behavior (p. 35; August update, p. 14).
- August Luna results describe a refreshed ChatGPT checkpoint; the update says Codex and ChatGPT Work stayed on earlier Luna, and GitHub does not specify Copilot's checkpoint (August update, p. 2).

## Practical implications for Copilot users

- Luna is best suited to small, time-sensitive coding tasks, quick explanations, lightweight edits, and routine question answering where responsiveness matters.
- For broad repository refactors, long debugging sessions, or security investigations, consider Terra or Sol because Luna has weaker complex edit-conflict and cyber-range results.
- Keep normal code-review discipline: inspect diffs, run focused tests, and avoid accepting destructive file operations without checking the model's assumptions.
- Prompt-injection defenses still matter when Luna reads issues, web pages, logs, dependency output, or generated tool results; do not treat high benchmark scores as permission to trust untrusted content.
- Use human verification for high-stakes factual or health-related claims, even though the August update reports factuality and HealthBench improvements.
- Distinguish July and August evidence: unless GitHub documents the served checkpoint, Copilot users should not assume the August ChatGPT Luna rows exactly describe their session.

## Document coverage

This digest uses the July GPT-5.6 System Card for Luna-specific rows in the family tables, plus family-level Preparedness and safeguard descriptions where OpenAI applies them to all three GPT-5.6 models. Sol-only alignment, deployment simulation, and external-evaluation sections are summarized only as scope limits, not as Luna evidence. The August update is used for refreshed ChatGPT Luna results and is always labeled because it does not establish which Luna checkpoint GitHub Copilot serves.
