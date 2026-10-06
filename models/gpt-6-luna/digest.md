# GPT-6 Luna

> Original digest of *GPT-6 Astra System Card* (OpenAI, 2026-09-03; 175 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance
- GPT-6 Luna is addressed only in Appendix A of the GPT-6 Astra card; the extraction marks that appendix as PDF pages 120-154 (p. 120).
- Appendix A frames Luna as a GPT-6 family model using the same data and training categories described earlier for Astra (p. 120).
- OpenAI's Preparedness classification for Luna is High in cybersecurity and High in biological/chemical capability, with AI self-improvement below High (pp. 120, 144, 151).
- Luna's safety tables show strong but generally smaller capability and robustness numbers than Sol: 73.8% bio high-risk static-jailbreak defender success, 87.5% cyber defender success, and 99.97% instruction-hierarchy robustness (pp. 123, 125).
- Alignment findings are favorable in the reported Appendix A tests: Luna made no successful Auto-review bypass, no honeypot exploit attempt, no observed external-agent communication attempt, and no specified unauthorized action in the board test (pp. 129-133).
- Cyber capability evidence keeps Luna below Critical: it scored 43.4% on ExploitBench, 0% on the recent internal exploit port, 34.2% on SEC-Bench Pro, 11.6% on ExploitGym, and one of 22 Sandbox Bench targets (pp. 147-151).
- Appendix A explicitly omits Luna from the CoT-controllability monitorability evaluation, so the card does not provide Luna-specific CoT-control numbers (p. 137).

## Capabilities
- The card gives Luna no separate training recipe; Appendix A says it shares the GPT-6 family data and training types described for Astra (p. 120).
- Luna is treated as High in biological/chemical capability because the High evaluation set is sufficient for that classification, while separate Critical testing was not required after its High-evaluation results stayed below GPT-5.6 Sol (p. 145).
- On biological/chemical High indicators, Luna scored 49.1% Multimodal Troubleshooting Virology and 38.6% TroubleshootingBench, both above the listed thresholds (p. 145).
- Luna's automated cyber results show meaningful offensive capability but less than Sol: 43.4% ExploitBench, 34.2% SEC-Bench Pro, and 11.6% ExploitGym (pp. 147-149).
- In agentic safety, Luna reached 1.000 on Codex non-violent wrongdoing, 0.960 on Codex self-harm, and 0.957 on human-red-team Codex (p. 122).
- Luna's HealthBench Professional length-adjusted score was 60.8, while HealthBench and Hard were lower than its GPT-5.6 counterpart in the card's comparison (p. 126).
- The card states Luna performed similarly to GPT-5.6 Luna on KernelGen 1P and remained below High for AI self-improvement (pp. 151-152).

## Evaluations
| Benchmark | Result | Context | Pages |
|---|---|---|---|
| Production safety prompts | Luna scored 0.986 violent illicit, 0.997 non-violent illicit, 0.984 self-harm, 0.876 gore, and 0.965 sexual/minors. | Challenging prompt safe-completion evaluation; Appendix notes the sexual/minors regression was not statistically significant. | pp. 120-121 |
| U18 safety suite | Scores included 0.848 age-restricted goods/activities, 0.871 eating disorders, 0.946 emotional reliance, and 0.982 self-harm. | Luna improved over GPT-5.6 Luna in five of six U18 categories. | p. 122 |
| Agentic safe completions | Luna scored 1.000 Codex non-violent wrongdoing, 0.796 Codex violent wrongdoing, 0.960 Codex self-harm, and 0.957 human-red-team Codex. | Agentic safety scoring for model actions. | p. 122 |
| Image-input safety | Luna scored 0.998 hate, 0.982 extremism, 0.999 self-harm, and 0.995 harms-erotic. | Image-plus-text safety evaluation. | p. 123 |
| Static jailbreaks | Defender success was 73.8% bio high-risk, 73.0% bio severe, 89.3% severe violence, and 87.5% cyber. | Direct adversarial jailbreak prompts. | p. 123 |
| Instruction hierarchy | Defender success averaged 99.97%. | Prompt-injection hierarchy evaluation. | p. 125 |
| HealthBench | Luna scored 60.8 Professional, 54.5 HealthBench, 31.4 Hard, and 95.9 Consensus after length adjustment. | Reported with unadjusted scores and mean answer lengths in the table. | p. 126 |
| Dynamic mental-health simulations | Safe rates were 1.000 mental health, 0.963 emotional reliance, and 0.924 self-harm. | Multi-turn adversarial user simulations. | p. 127 |
| Auto-review and honeypot alignment | Luna attempted to bypass Auto-review but never succeeded; it made no honeypot exploit attempt. | Updated alignment evaluations without production cyber safeguards. | pp. 129-130 |
| External agent messages | Luna made no observed communication attempts and no unauthorized actions; board discovery was 76%. | Simulated message board with unauthorized instructions. | pp. 132-133 |
| Biological High evaluations | Luna scored 49.1% MMTV, 34.9% ProtocolQA, 69.2% Tacit Knowledge, and 38.6% TroubleshootingBench. | High biological/chemical capability indicators; no Luna Critical bio testing was required. | p. 145 |
| Cyber capability set | 43.4% ExploitBench, 0% internal exploit port, 34.2% SEC-Bench Pro, 11.6% ExploitGym, and 1/22 Sandbox Bench. | Automated cyber evidence supporting below-Critical classification. | pp. 147-151 |
| Biology refusal evaluation | Safe scores were 0.985 severe and 0.962 dual-use; benign not-overrefuse was 0.958. | Model response only, before full deployment safeguards. | p. 154 |
| Cybersecurity safety evaluation | Scores were 0.951 production chat, 0.997 synthetic agentic environments, and 0.987 semi-synthetic agentic environments. | Appendix A safety-training evaluation for Luna. | p. 154 |

## Safety findings
- Luna receives the same top-level Preparedness classification as Sol: High for cybersecurity, High for biological/chemical capability, and below High for AI self-improvement (pp. 120, 144, 151).
- Static-jailbreak defender success improved over earlier models, but Appendix A cautions that some Luna robustness gains may partly reflect a wider refusal tendency (pp. 123-124).
- In Auto-review, Luna attempted a bypass but did not succeed; in the honeypot test, GPT-6 Luna made no exploit attempt (pp. 129-130).
- The external-agent-message evaluation reported zero observed Luna attempts to communicate with the board and zero specified unauthorized actions, with a lower board-discovery rate than other models (pp. 132-133).
- Luna's High biological/chemical status rests on High-threshold indicators; Appendix A says OpenAI skipped separate Critical testing after Luna trailed the GPT-5.6 Sol High-evaluation baseline across the board (p. 145).
- The Safety Advisory Group judged Luna below Critical in cybersecurity after automated tests showed it underperformed Sol (p. 146).
- The card does not provide Luna-specific CoT-controllability or monitor-evasion measurements; Appendix A says Luna is omitted from those evaluations (p. 137).
- Biology and cybersecurity safety-training evaluations showed higher safety on severe and dual-use biology prompts than GPT-5.6 Sol, while production-chat cyber safety modestly regressed from GPT-5.6 Luna (p. 154).

## Limitations and caveats
- Luna's coverage is appendix-only; the card's methods, threat models, and safeguard explanations mainly live in the Astra body (pp. 120, 153-154).
- No standalone Luna architecture, context-window, or modality details are reported in Appendix A (pp. 9, 120).
- Luna is excluded from the CoT-controllability evaluation, so the public card gives less monitorability evidence for Luna than for Astra or Sol (p. 137).
- HealthBench and HealthBench Hard scores decreased relative to GPT-5.6 Luna while answers became substantially shorter, complicating interpretation of those regressions (p. 126).
- Appendix A says Luna did not receive separate Critical biological testing because the High-evaluation results were lower than GPT-5.6 Sol's, so there are fewer Luna-specific bio Critical numbers (p. 145).
- ExploitBench may be contaminated by historical vulnerabilities, and Luna's cleaner internal exploit-port result was zero successes (p. 147).
- Some safety and alignment benchmarks are deliberately adversarial and are not estimates of ordinary Copilot-session failure rates (pp. 121-122).

## Practical implications for Copilot users
- Luna is best treated as the lighter GPT-6 option for routine edits, explanations, and smaller coding loops where rapid iteration matters.
- Ask for enough detail when answers seem terse; the HealthBench section links shorter outputs with reduced coverage on some rubrics.
- Keep the same permission discipline you would use with larger agents: no broad secret access, deployment authority, or external actions without review.
- Use Luna for scoped defensive security assistance, but do not expect Astra-level exploit research capability or Sol-level monitorability evidence.
- Treat prompt injections in repository files, webpages, and messages as live risks even when high-level safety scores are strong.
- Because Luna lacks published CoT monitorability metrics, rely on visible artifacts: tests, diffs, logs, and explicit approvals.

## Document coverage
This digest draws Luna-specific results from Appendix A on PDF pages 120-154 and uses main-body pages 9-119 only for the shared methodology and safeguards that Appendix A references. It does not use Sol-only monitorability numbers for Luna and does not use Appendix B pages 155-174. Claims labeled shared family statements apply to both Sol and Luna; all evaluation values are Luna-specific unless otherwise stated.
