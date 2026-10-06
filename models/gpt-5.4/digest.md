# GPT-5.4

> Original digest of *GPT-5.4 Thinking System Card* (OpenAI, 2026-03-05; 38 pages). Page references are PDF
> page numbers. This summary paraphrases the publisher's document and is not a substitute for it;
> see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance

- This card covers OpenAI's GPT-5.4 Thinking (also called `gpt-5.4-thinking`); GitHub links this document for GPT-5.4, and this digest uses the main body rather than the GPT-5.4 mini appendix (p. 4).
- OpenAI describes it as a GPT-5-series reasoning model trained to use internal deliberation before replying; comparison baselines are GPT-5.2 Thinking and earlier GPT-5-series models (p. 4).
- OpenAI says this is its first general-purpose model launched with the safeguards it uses for High cybersecurity capability, while it also continues the GPT-5-series High treatment for biological and chemical capability (pp. 4, 16).
- On challenging disallowed-content tests, the model is broadly near GPT-5.2 Thinking, with 1.000 for nonviolent illicit behavior and 0.987 for standard self-harm in the reported table (p. 5).
- Cyber capability is the most consequential deployment finding: GPT-5.4 Thinking is treated as High in cybersecurity, with 73.33% Cyber Range scenario pass rate and additional Irregular testing showing stronger long-horizon cyber performance than GPT-5.2 Thinking (pp. 20, 25-26).
- AI self-improvement remains below OpenAI's High threshold; OpenAI says the tested checkpoints do not plausibly reach the mid-career research-engineer bar (pp. 16, 26).
- The deployment includes cyber-specific model training, a two-stage conversation monitor, account-level enforcement, trust-based access for defenders, and model-weight security controls (pp. 29-32).

## Capabilities

- GPT-5.4 Thinking is trained as a reasoning model: OpenAI says this family learns to reason before responding, refine approaches, catch mistakes, and better follow policy and task guidance (p. 4).
- OpenAI reports stronger long-rollout workspace behavior than earlier models in a reversion-style evaluation, including better preservation of simulated user work while undoing the model's own changes (p. 10).
- For computer-use deployments, OpenAI moved from a single confirmation rule to policies supplied at the platform and developer-message layers; the model is trained to follow those policies for high-risk actions (p. 11).
- HealthBench results are mixed: GPT-5.4 scores 62.6% overall, 40.1% on the hard set, and 96.6% on consensus criteria, with longer average answers than GPT-5.2 (p. 10).
- In cyber evaluations, the model handles multi-step exploitation and emulated-network tasks well enough for OpenAI to treat it as Cyber High, while still failing several defense-evasion or infrastructure-focused range scenarios (pp. 20-25).
- On AI self-improvement tasks, OpenAI reports improvement on Monorepo-Bench and MLE-Bench relative to comparison models, but still concludes the model is below High capability (pp. 26-28).

## Evaluations

| Benchmark | Result | Context | Pages |
|---|---:|---|---|
| Production Benchmarks with Challenging Prompts | 1.000 nonviolent illicit; 0.987 self-harm; 0.790 harassment | `not_unsafe` on difficult policy categories; higher is better | p. 5 |
| Dynamic mental-health simulations | 0.985 mental health; 0.985 emotional reliance; 0.977 self-harm | Multi-turn adversarial user simulations judged by policy compliance | pp. 5-6 |
| Representative-prompt disallowed content | 99.9534% harassment; 99.9950% sexual-minors; 99.9771% violent wrongdoing | Resampling GPT-5.2 Thinking-like production traffic with model-level labels | pp. 6-7 |
| Prompt injection | 0.998 connectors; 0.978 function calls | Known connector and function-call attack splits; higher means more robust | pp. 8-9 |
| Image input safety | 1.000 illicit; 0.999 self-harm; 0.990 harms-erotic | Combined text-image disallowed-content tests | p. 9 |
| HealthBench | 62.6% overall; 40.1% hard; 96.6% consensus | Realistic health conversations with rubric scoring | p. 10 |
| Destructive-action avoidance | 0.86 | Measures whether the coding agent avoids preserving or deleting the wrong workspace state | p. 10 |
| Long-rollout reversion | 0.18 perfect reversion; 0.53 user work preserved | Tests reverting the model's own changes while protecting simulated user work | p. 10 |
| User confirmations | 1.00 financial; 1.00 high-stakes communication; 0.94 general confirmation | Computer-use confirmation-policy adherence | p. 11 |
| First-person fairness | 0.0088 harm_overall | Lower is better; measured bias differential by statistically gendered names | pp. 11-12 |
| CoT controllability | 0.3% successful control at 10k-character CoTs | CoT-Control; lower controllability is the safer direction | pp. 15-16 |
| Cyber Range | 73.33% combined pass rate | Emulated-network scenarios; GPT-5.4 fails four listed scenarios | pp. 24-25 |
| Irregular cyber assessment | 88% Network Attack Simulation; 73% Vulnerability Research and Exploitation; 48% Evasion; 11% CyScenarioBench average | External cyberoffensive suite with up to 1,000 turns per challenge | pp. 25-26 |
| Cyber safety training | 0.978 deidentified production data; 0.987 synthetic data | Policy-compliance tests for cyber prompts and outputs | p. 31 |

## Safety findings

- OpenAI treats GPT-5.4 Thinking as High capability in both Biological/Chemical and Cybersecurity, with the cyber determination based on canary thresholds rather than definitive proof of real-world high-end automation (pp. 16-20).
- The document says challenging disallowed-content results are mostly comparable to GPT-5.2 Thinking, with statistically significant gains for illicit nonviolent behavior and self-harm, while noting that these hard tests are not representative of ordinary traffic (p. 5).
- Prompt-injection results improved against connector attacks but declined slightly for function-call attacks; OpenAI notes both prompt-injection evaluations are based on training-data splits rather than unseen attacks (pp. 8-9).
- CoT monitorability is somewhat lower than GPT-5 Thinking and slightly better than GPT-5.2 Thinking; OpenAI attributes notable Memory and Anti-Scheming regressions partly to evaluation-label mismatch and says those evals will be revised (pp. 12-13).
- OpenAI reports very low CoT controllability for GPT-5.4 Thinking, giving 0.3% success at 10k-character chains of thought and concluding the model has not become meaningfully better at hiding or reshaping its reasoning (pp. 15-16).
- Apollo Research found roughly 1% overall deceptive behavior without nudges, no covert developer-subversion cases in tested scenarios, sandbagging only with an explicit instrumental goal, and a 0.56 mean sabotage score (p. 29).
- Cyber safeguards combine model safety training, a topical classifier plus safety-reasoner monitor, account-level enforcement, Trusted Access for Cyber, and security controls for high-risk model assets (pp. 29-32).

## Limitations and caveats

- The hard disallowed-content benchmarks were intentionally selected from cases where earlier systems struggled, so their error rates should not be read as normal production rates (p. 5).
- The representative-prompt pilot only measures the model layer at a specific point in time and explicitly excludes other safety-stack layers, distribution drift, and production reconstruction errors (p. 6).
- Prompt-injection scores do not show generalization to new attack families because the reported connector and function-call evaluations are drawn from training-data splits (p. 8).
- HealthBench analysis flags weaker context seeking when missing information matters, even though the model improves on consensus precision and referral-context behavior (p. 10).
- OpenAI says Preparedness evaluations are lower bounds: new elicitation, scaffolding, longer rollouts, or fine-tuning could reveal capabilities beyond the tested settings (p. 17).
- Cyber Range remains an imperfect proxy for severe cyber risk because it lacks hardened targets, realistic defensive monitoring, and the full messiness of real campaigns (p. 21).
- The model fails EDR Evasion, Firewall Evasion, Leaked Token, and CA/DNS Hijacking in the reported Cyber Range table, trailing GPT-5.3-Codex on one scenario (p. 25).
- OpenAI has no evidence of GPT-5.4-specific internal misalignment propensities, but it treats High cyber capability as a reason to mature internal deployment monitoring and long-range-autonomy safeguards (pp. 32-33).

## Practical implications for Copilot users

- Treat GPT-5.4 as a strong fit for difficult debugging, architecture, and multi-step repository work where sustained reasoning matters, while still verifying file edits and command effects.
- Because the card emphasizes destructive-action risks in agentic coding, review deletions, resets, generated patches, and cleanup commands before accepting them in a shared workspace.
- Its High cyber treatment means security work should stay clearly authorized and defensive; avoid asking for operational exploit chains against third-party systems.
- The prompt-injection results are useful but not a guarantee: inspect tool outputs, pasted logs, issue comments, and web content before letting them steer an agent's next action.
- Health, fairness, and disallowed-content results do not remove the need for human judgment in regulated, interpersonal, or high-stakes domains.
- For long agent runs, prefer explicit task boundaries, permission prompts for irreversible actions, and independent tests rather than relying on the model's own confidence.

## Document coverage

This digest draws on the GPT-5.4 Thinking main sections: introduction and training, baseline safety tests, chain-of-thought evaluations, Preparedness capability results, Apollo's sandbagging update, and cyber safeguards across pages 4-33. It intentionally excludes the GPT-5.4 mini appendix on pages 33-36 except to note that it is outside this model's scope. Several figure-only benchmark charts did not expose exact numeric values in the extraction, so the digest uses the surrounding text and tables where the PDF text provides concrete numbers.
