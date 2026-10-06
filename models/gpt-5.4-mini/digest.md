# GPT-5.4 mini

> Original digest of *GPT-5.4 Thinking System Card* (OpenAI, 2026-03-05; 38 pages). Page references are PDF
> page numbers. This summary paraphrases the publisher's document and is not a substitute for it;
> see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance

- No standalone GPT-5.4 mini system card exists; OpenAI added an appendix for GPT-5.4 mini to the GPT-5.4 Thinking System Card on March 17, 2026 (p. 33).
- This digest is scoped to section 6, pages 33-36, and does not use the main GPT-5.4 Thinking results as GPT-5.4 mini results.
- OpenAI reports GPT-5.4 mini disallowed-content results such as 0.992 for violent illicit behavior, 1.000 for nonviolent illicit behavior, 0.982 for standard self-harm, and 0.949 for sexual/minors (p. 33).
- The mini appendix says GPT-5.4 mini has lower CoT controllability than any model OpenAI had previously reported in that evaluation, which OpenAI treats as favorable for monitorability risk (pp. 33-34).
- OpenAI determines GPT-5.4 mini is below High capability across Biological/Chemical, Cybersecurity, and AI self-improvement under its Preparedness Framework (p. 34).
- For biology, OpenAI grounds the below-High conclusion in a physical-world novice study for GPT-5 plus automated comparisons showing GPT-5.4 mini is not sufficiently more concerning than GPT-5 (pp. 34-36).
- The appendix reports 81.32% pass@12 on Capture the Flag, 83.33% pass@1 on CVE-Bench, 54.00% pass@1 on Monorepo-Bench, and 7.5% pass@1 on OPQA v0 for GPT-5.4 mini (p. 36).

## Capabilities

- GPT-5.4 mini is documented only in the appendix; OpenAI reports launch-specific safety, CoT controllability, and Preparedness measurements rather than a full model description (p. 33).
- On dynamic adversarial simulations, GPT-5.4 mini scores 0.985 for mental health, 0.977 for emotional reliance, and 0.980 for self-harm, close to the larger GPT-5.4 Thinking scores in that table (p. 33).
- OpenAI says GPT-5.4 mini received the same full safety training relevant to biological risk, even though it is not classified as Bio High (p. 35).
- Automated biology benchmarks show mixed comparisons with GPT-5: GPT-5.4 mini is higher on multi-select virology troubleshooting and lower on ProtocolQA and TroubleshootingBench in the raw scores (pp. 35-36).
- The mini model remains capable on cyber proxy tasks, scoring 81.32% on professional CTF and 83.33% on CVE-Bench, but OpenAI still places it below High cybersecurity capability (p. 36).
- On AI self-improvement proxies, it scores 54.00% on Monorepo-Bench and 7.5% on OPQA v0, while OpenAI's overall determination remains below High (p. 36).

## Evaluations

| Benchmark | Result | Context | Pages |
|---|---:|---|---|
| Challenging disallowed content | 0.992 violent illicit; 1.000 nonviolent illicit; 0.836 harassment | `not_unsafe`; higher is better | p. 33 |
| Challenging disallowed content, sensitive categories | 0.982 self-harm; 0.948 sexual; 0.949 sexual/minors | Same table, GPT-5.4 mini column | p. 33 |
| Dynamic mental-health simulations | 0.985 mental health; 0.977 emotional reliance; 0.980 self-harm | Multi-turn adversarial simulations | p. 33 |
| CoT-Control | Lower controllability than any previously reported OpenAI model in this suite | CoT controllability result reported qualitatively | pp. 33-34 |
| Multi-select multimodal troubleshooting virology | 46.5% raw; 47.0% refusal-inclusive | Biology capability proxy, pass@1 | pp. 35-36 |
| ProtocolQA Open-Ended | 33.64% raw; 34.24% refusal-inclusive | Biology protocol troubleshooting, pass@1 | pp. 35-36 |
| Tacit Knowledge and Troubleshooting | 71.67% raw; 77.77% refusal-inclusive | Biology tacit-knowledge proxy, cons@32 | pp. 35-36 |
| TroubleshootingBench | 31.91% raw; 33.11% refusal-inclusive | Unpublished hands-on protocol troubleshooting, pass@1 | pp. 35-36 |
| Capture the Flag | 81.32% pass@12 | Cybersecurity capability proxy | p. 36 |
| CVE-Bench | 83.33% pass@1 | Real-world web-application vulnerability exploitation proxy | p. 36 |
| Monorepo-Bench | 54.00% pass@1 | Pull-request-style software-engineering tasks | p. 36 |
| OpenAI-Proof Q&A v0 | 7.5% pass@1 | Internal research and engineering debugging bottlenecks | p. 36 |

## Safety findings

- OpenAI concludes GPT-5.4 mini is below High capability in Biological/Chemical, Cybersecurity, and AI self-improvement, so the appendix does not trigger the same High determinations as the main GPT-5.4 Thinking model (p. 34).
- The dynamic mental-health table shows GPT-5.4 mini near the larger GPT-5.4 Thinking model on mental health and self-harm, with a small gap on emotional reliance (p. 33).
- Low CoT controllability is presented as a positive signal because a model that cannot easily shape its hidden reasoning is less likely to evade reasoning-based monitoring by design (pp. 33-34).
- For biology, OpenAI relies on direct novice-uplift evidence for GPT-5 and on automated comparisons showing GPT-5.4 mini is not enough above GPT-5 to justify a different High classification (pp. 34-36).
- The appendix notes GPT-5.4 mini received full biological-risk safety training even though OpenAI classifies it below Bio High (p. 35).
- Cyber and AI self-improvement measurements remain below OpenAI's High determinations despite nontrivial CTF, CVE-Bench, Monorepo-Bench, and OPQA scores (p. 36).

## Limitations and caveats

- The model has no standalone card; the appendix gives a narrow set of safety and Preparedness results rather than a complete system description (p. 33).
- The biology conclusion depends partly on a GPT-5 physical-world novice study, not a separate physical-world study of GPT-5.4 mini itself (pp. 34-35).
- Refusal-inclusive biology scores intentionally credit refusals or safe completions as if they were successes, which is conservative for capability assessment but not observed helpful behavior (pp. 35-36).
- The appendix does not report broad user-facing capability benchmarks, HealthBench, prompt-injection tests, destructive-action tests, Cyber Range scenarios, or deployment architecture for GPT-5.4 mini (pp. 33-36).
- The cyber section includes CTF and CVE-Bench only; OpenAI still says the model is below High across the Preparedness domains (pp. 34, 36).
- Because GPT-5.4 mini is documented inside the GPT-5.4 Thinking card, sibling-model results in the main body should not be attributed to the mini model (pp. 4, 33).

## Practical implications for Copilot users

- Use GPT-5.4 mini for faster routine coding and codebase-navigation work when the smaller model is sufficient, but reserve stronger reasoning models for deep architecture or ambiguous multi-file changes.
- Treat its safety card as narrower than the main GPT-5.4 card: it supports some conclusions about safety and Preparedness, not a complete capabilities map.
- Continue normal review of generated patches and commands; the appendix does not report the destructive-action or long-rollout workspace tests used for GPT-5.4 Thinking.
- Its below-High cyber classification does not make offensive security requests appropriate; keep security tasks authorized, scoped, and defensive.
- Use tests and human review for biologically, medically, or security-sensitive outputs because the appendix's below-High finding is not a general correctness guarantee.

## Document coverage

This digest uses only section 6 of the GPT-5.4 Thinking System Card, pages 33-36, which OpenAI added for GPT-5.4 mini. It omits the main GPT-5.4 Thinking sections except for the document title and the fact that they are sibling-model content. The appendix reports selected safety, CoT, and Preparedness evaluations but does not provide a full standalone model card.
