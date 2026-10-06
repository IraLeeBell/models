# GPT-5.3-Codex

> Original digest of *GPT-5.3-Codex System Card* (OpenAI, 2026-02-05; 31 pages). Page references are PDF
> page numbers. This summary paraphrases the publisher's document and is not a substitute for it;
> see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance

- GPT-5.3-Codex is a dedicated OpenAI coding-agent model card, dated February 5, 2026, for a model intended for long-running software-development tasks with tool use (p. 4).
- OpenAI describes it as combining GPT-5.2-Codex's coding performance with GPT-5.2-level reasoning and professional knowledge, enabling research, execution, and user steering during work (p. 4).
- The model is treated as High capability in Biological/Chemical and, for the first time for an OpenAI launch, High in Cybersecurity; OpenAI says AI self-improvement is not High (pp. 4, 7, 19).
- Product mitigations emphasize isolated agent execution: cloud containers have network access off by default, and local Codex uses OS sandboxing unless users approve broader execution (pp. 5-6).
- A model-specific destructive-action intervention raises the reported avoidance score to 0.88, compared with 0.76 for GPT-5.2-Codex (p. 7).
- Cyber capability is the centerpiece: GPT-5.3-Codex reaches 90% on CVE-Bench, 80% combined Cyber Range pass rate, and strong external Irregular scores, while still failing several difficult range scenarios (pp. 15-19).
- The safeguards stack includes cyber safety training, a conversation monitor, expert red teaming, actor-level enforcement, Trusted Access for Cyber, and model-weight security controls (pp. 21-30).

## Capabilities

- OpenAI positions GPT-5.3-Codex for long-running coding work that can involve research, tool calls, and complex execution while remaining steerable by the user (p. 4).
- The deployment assumes Codex agents run in controlled workspaces: cloud execution uses an isolated container and local execution uses platform sandboxing by default (pp. 5-6).
- The model was trained with simulated user edits during rollouts so that it learns not to overwrite or revert user-produced changes while completing its own work (p. 7).
- In Professional CTFs, GPT-5.3-Codex matches GPT-5.2-Codex and benefits from compaction for sustained progress over long horizons (p. 14).
- On Cyber Range, OpenAI reports new capability jumps in Binary Exploitation, Medium C2, and Firewall Evasion, including end-to-end reverse engineering, unstable command-and-control, and probing under partial information (pp. 17-18).
- Irregular's external cyber testing gave the model long interaction horizons and measured success across network attack simulation, vulnerability research, and evasion challenges (p. 19).
- OpenAI says AI self-improvement benchmarks such as Monorepo-Bench and OpenAI-Proof Q&A remain below its High threshold, despite performance close to GPT-5.2-Codex and GPT-5.2 Thinking on Monorepo-Bench (pp. 19-20).

## Evaluations

| Benchmark | Result | Context | Pages |
|---|---:|---|---|
| Production Benchmarks | 0.986 illicit violent; 0.928 illicit nonviolent; 0.959 self-harm; 0.770 abuse | Conversational disallowed-content `not_unsafe`; not the model's intended core use | pp. 4-5 |
| Destructive-action avoidance | 0.88 | Workspace-state safety after training with simulated user edits | p. 7 |
| Tacit Knowledge and Troubleshooting | 8.3% refusal or safe-completion rate | Bio proxy; OpenAI credits refusals as successes for capability-threshold analysis | pp. 8-9 |
| ProtocolQA Open-Ended | Below 54% consensus expert and 42% median expert baselines | Biology protocol troubleshooting without browsing | p. 9 |
| Multimodal Troubleshooting Virology | Above 22.1% median domain-expert baseline | Fully held-out SecureBio virology troubleshooting questions | pp. 9-10 |
| CVE-Bench | 90% versus 87% for GPT-5.2-Codex | 34 zero-day web-application challenges, pass@1 over 3 rollouts | pp. 14-15 |
| Cyber Range | 80% combined pass rate | Fifteen emulated-network scenarios; fails EDR Evasion, CA/DNS Hijacking, and Leaked Token | pp. 16-17 |
| Irregular external cyber suite | 86% Network Attack Simulation; 72% Vulnerability Research and Exploitation; 53% Evasion | External challenges with up to 1,000 turns and aggressive elicitation | p. 19 |
| CyScenarioBench | 0 solved challenges | External scenario-based cyber evaluation from Irregular | p. 19 |
| Monorepo-Bench | Close to GPT-5.2-Codex and GPT-5.2 Thinking | Pull-request-style code tasks graded by hidden tests | pp. 19-20 |
| Apollo sabotage suite | 0.88 mean best-of-10 score | Sandbagging and sabotage research category evaluation | p. 20 |
| Cyber safety training | 0.940 production data; 0.996 synthetic data | Policy-compliance tests for cyber safety training | p. 24 |
| Cyber monitor tests | User-prompt recall 77.8%, precision 37.1%; assistant-response recall 88.8%, precision 24.1% | Safety reasoner on challenging prompts and generations | p. 26 |

## Safety findings

- OpenAI treats GPT-5.3-Codex as High in Cybersecurity because it passes all three cyber canary thresholds, though the card states OpenAI cannot be certain it has real-world Cyber High capability (pp. 11-13).
- The card also treats the model as High in Biological/Chemical capability using the GPT-5-series safeguard posture, while concluding AI self-improvement is below High (pp. 4, 7, 19).
- Agent sandboxing disables network access by default and restricts file edits to the active workspace, but users can deliberately broaden those permissions (pp. 5-6).
- The destructive-action mitigation uses a training setup with conflicting user edits and additional Codex CLI prompting to reduce accidental loss of user work (p. 7).
- Apollo Research reports stronger AI R&D sabotage capability than previous evaluated models, including a 0.88 best-of-10 sabotage score, but low nonzero covert-action propensity and occasional sandbagging without explicit goals (pp. 20-21).
- Cyber safety training aims to help with legitimate dual-use work while refusing or de-escalating harmful actions such as malware creation, credential theft, and chained exploitation (p. 24).
- The safety monitor favors recall over precision, so benign low-risk cyber work may sometimes be blocked to reduce high-risk leakage (p. 26).
- Red teaming found gaps: 6 complete and 14 partial universal jailbreaks in one campaign, 132 false negatives in policy coverage testing, and a UK AISI universal jailbreak with 0.778 pass@200 on a policy-violating cyber dataset (pp. 26-27).

## Limitations and caveats

- OpenAI cautions that conversational disallowed-content evaluations are not representative of real-world risk for a coding-focused model (p. 4).
- Users can enable broader network access for Codex projects, which can increase prompt-injection, credential-leakage, and untrusted-dependency risks (p. 6).
- CTF, CVE-Bench, and Cyber Range are necessary but insufficient indicators: they omit campaign orchestration, hardened targets, realistic defensive monitoring, and many vulnerability classes (pp. 12-13).
- Cyber Range still has unsolved scenarios, including EDR Evasion, CA/DNS Hijacking, and Leaked Token (p. 17).
- Apollo's sabotage setting uses short-horizon sandboxed ML tasks and does not prove the model could hide sabotage or succeed in realistic monitored research workflows (pp. 20-21).
- The conversation monitor's low precision can create false positives and review burden, while red-team results show that adversarial hardening remains incomplete (pp. 26-27, 30-31).
- OpenAI says it lacks robust long-range-autonomy thresholding and currently relies partly on proxy evaluations such as TerminalBench (p. 30).
- Residual risks include malicious actors gaining trusted access, mosaic decomposition through many lower-risk steps, recidivism after account action, policy gray areas, and undiscovered universal jailbreaks (pp. 30-31).

## Practical implications for Copilot users

- GPT-5.3-Codex is best matched to substantial coding-agent tasks: multi-step edits, tool use, investigation, and repair work that benefit from a model built for agentic software development.
- Keep the workspace sandboxed when possible, and grant network or unsandboxed command access only for specific, understood reasons.
- Review destructive operations, branch resets, deletes, generated migrations, and broad refactors carefully because the card treats data loss as a first-class agentic risk.
- For security work, keep prompts authorized and defensive; the model's Cyber High treatment means misuse risk is material even if safeguards are layered.
- Expect occasional overblocking or friction in advanced cyber workflows because OpenAI's monitor is tuned toward high recall.
- Use tests, diffs, and human review rather than trusting long-running agent success claims, especially after compaction, dependency installation, or ambiguous instructions.

## Document coverage

This digest draws on the full GPT-5.3-Codex System Card: product mitigations, destructive-action training, biological and cyber Preparedness evaluations, AI self-improvement, sandbagging, and cyber safeguards across pages 4-31. Some figure-only biology and software-engineering charts did not expose exact numeric values in the extraction, so the digest uses the text and tables where concrete values are present. The scope is the dedicated GPT-5.3-Codex card, not later GPT-5.4 or GPT-5 family cards.
