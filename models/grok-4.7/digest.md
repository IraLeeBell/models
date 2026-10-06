# Grok 4.7

> Original digest of *Model Card: Grok 4.7* (xAI, September 21, 2026; 30 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance

- Grok 4.7 has a dedicated 30-page xAI card dated and revised September 21, 2026; the card describes it as SpaceXAI's latest model and successor to Grok 4.6 (pp. 1, 4).
- The documented modality is text output from text and image inputs, with listed availability through the SpaceXAI API, Grok Build, Cursor, Office add-ins, and model gateways; consumer surfaces are described as planned later (p. 5).
- Training continues the Grok 4.6 recipe with longer supplemental training, curated model-generated data, engineering corpora, and agentic RL; pretraining cuts off in June 2026 and supplemental data extends to August 2026 (p. 5).
- Coding evidence emphasizes harder, longer tasks: CursorBench 4.0 scores are 46.3% at xhigh and 43.9% at high, DeepSWE v1.1 is 71.0% at high, Terminal-Bench 4.0 is 38.0% at xhigh, FrontierSWE V2 is 29.0% at xhigh, and SWE-Marathon v1.1 is 46.0% at high (pp. 6-11).
- The card adds medical and biological analysis benchmarks: HealthBench Professional is 56.7% at xhigh, and the LatchBio capability-suite mean is 44.5% at xhigh (pp. 15-16).
- Safety sections state that Grok 4.7 remains below FAIF thresholds and shows no dual-use biology increase versus Grok 4.6; reported safeguard figures include 0.01% standard-jailbreak compliance, 0.0% child-safety compliance, 100.0% bio refusal recall, 99.9% chem refusal recall, and 97.9% radiological/nuclear refusal accuracy (pp. 20, 23-25).
- Version-to-version comparisons are mixed: Grok 4.7 improves many long-horizon coding and engineering results, but CVE-Bench is below Grok 4.6, several dual-use bio knowledge scores decline, and self-harm compliance rises to 1.05% (pp. 18, 20-22, 26).

## Capabilities

- **Modalities and training.** The card positions Grok 4.7 as a text-output model with text and image inputs, trained with a later cutoff than Grok 4.6 plus supplemental data through August 2026 (p. 5).
- **Long-horizon coding.** Coding coverage shifts to harder updated suites, including CursorBench 4.0, DeepSWE v1.1, Terminal-Bench 4.0, FrontierSWE V2, and SWE-Marathon v1.1; the card warns that CursorBench 4.0 should not be compared directly with CursorBench 3.2 (pp. 6-11).
- **Knowledge work.** The card's professional-work section narrows to the Legal Agent Benchmark, where Grok 4.7 is evaluated on a held-out 120-task legal-agent run without internet access (p. 12).
- **Engineering acceleration.** Grok 4.7 is tested on electrical/chip-design tasks and CAD geometry generation, with reported gains over Grok 4.6 in EEBench and CADGenBench (pp. 13-14).
- **Medical and biological analysis.** HealthBench Professional and LatchBio capability tasks measure clinical communication and agentic biological data analysis; xAI frames these as capability signals, not a license for unsupervised medical or lab decisions (pp. 15-16).
- **Cybersecurity.** CyberGym, CVE-Bench, HackerBench v0.3, and CathedralBench assess cyber ability and cyber-safeguard calibration, including unrestricted or egress-controlled settings where appropriate (pp. 17-19).

## Evaluations

| Benchmark | Result | Context | Pages |
| --- | --- | --- | --- |
| CursorBench 4.0 | 46.3% at xhigh; 43.9% at high | Long-horizon Cursor-session coding; not directly comparable to CursorBench 3.2 | p. 6 |
| DeepSWE v1.1 | 71.0% Pass@1 at high | 113 original coding tasks across 91 repositories and five languages | p. 8 |
| Terminal-Bench 4.0 | 38.0% task success at xhigh | 66 difficult terminal workflows with programmatic verifiers | p. 9 |
| FrontierSWE V2 | 29.0% mean@5 at xhigh | Ultra-long tasks scored with partial credit | p. 10 |
| SWE-Marathon v1.1 | 46.0% resolution at high | 20 multi-hour software-engineering tasks with hidden checks | p. 11 |
| Legal Agent Benchmark | 19.6% Harvey final score at xhigh | Held-out 120-task legal-agent evaluation in Valkyrie | p. 12 |
| EEBench | 66.0% reward at xhigh | Electrical engineering and chip-design tasks | p. 13 |
| CADGenBench | 44.4% reward at high | CAD geometry generation | p. 14 |
| HealthBench Professional | 56.7% at xhigh | Healthcare conversation benchmark, with rejected tasks scored zero | p. 15 |
| LatchBio Capabilities v1.0 | 44.5% overall at xhigh | Agentic analysis across 11 biological data benchmarks | p. 16 |
| CyberGym | 80.3% mean reproduced at high | Unrestricted cyber capability probe | p. 17 |
| CVE-Bench | 36.6% at xhigh; 37.7% at high | Web-application CVE exploitation in hardened sandboxes | p. 18 |
| HackerBench v0.3 | 3.31%-4.02% harmful/dual-use compliance across Grok 4.7 efforts; 0.00%-0.31% benign refusal | Safeguarded cyber/red-team requests; lower is better | p. 18 |
| CathedralBench | 29% on hard subset at xhigh | Independent multi-exploit-chain cyber evaluation | p. 19 |
| BioSecBench | 62.4% Refusal; 48.0% Surveillance; 43.3% Function | LatchBio biosecurity refusal and analysis tasks | p. 20 |
| WMDP | 88.1% Bio; 84.9% Chem; 88.1% Cyber | Dual-use multiple-choice knowledge | p. 22 |
| Jailbreaks | 0.01% standard; 2.0% StrongReject; 0.65% long-horizon compliance | Should-refuse adversarial prompts; lower is better | p. 23 |
| CBRN/weapons refusals | 100.0% bio recall; 99.9% chem recall; 97.9% R/N accuracy | Dangerous CBRN and weapons prompts under safeguards | p. 25 |

## Safety findings

- The cyber section states that capability probes run without production safeguards where needed to measure ability, while refusal behavior is evaluated separately; CyberGym is 80.3%, CVE-Bench is 36.6%-37.7%, and CathedralBench hard-subset accuracy is 29% (pp. 17-19).
- HackerBench v0.3 shows lower harmful/dual-use compliance for Grok 4.7 than for the Grok 4.6 and Grok 4.5 comparison points in the chart, with Grok 4.7 efforts in the 3.31%-4.02% range and benign refusal no higher than 0.31% (p. 18).
- The FAIF-framed bio/chem section says Grok 4.7 remains below dual-use thresholds and does not increase dangerous biological capability over Grok 4.6; the card attributes lower risky-task performance to safer RL environments and more selective training data rather than merely stronger refusal filters (p. 20).
- BioSecBench, VCT, Biosecurity VCT, BioUseBench, WMDP, LAB-Bench, ProtocolQA, and BixBench show calibrated refusal plus useful biological analysis, but several raw capability scores are lower than Grok 4.6's reported values (pp. 20-23).
- Jailbreak compliance improves versus Grok 4.6 on all three reported jailbreak suites: 0.01% standard, 2.0% StrongReject, and 0.65% long-horizon (p. 23).
- General output safety is mixed: broad harmful-request compliance is 1.10%, child-safety compliance is 0.0%, bio refusal recall is 100.0%, chem refusal recall is 99.9%, and radiological/nuclear refusal accuracy is 97.9% (pp. 24-25).
- Mental-health and behavior results include 1.05% self-harm compliance, 0.00% MASK-Rectified dishonesty, and 0.03% sycophancy (pp. 26-27).

## Limitations and caveats

- The card repeats the warning that Grok 4.7 should not make autonomous high-stakes medical, legal, financial, or safety-critical decisions without human oversight and expert validation (p. 4).
- CursorBench 4.0 adds longer-horizon tasks and is explicitly not comparable to CursorBench 3.2, limiting simple version-to-version score comparisons for that benchmark (p. 6).
- Some cyber metrics are not monotonic: CVE-Bench is below Grok 4.6, even though CyberGym and CathedralBench show small gains (pp. 17-19).
- The 4.7 card does not include the search/factuality section that appears in the 4.5 and 4.6 cards, so this card gives no direct updated hallucination or DeepSearchQA number (pp. 2-3).
- xAI states that dual-use biological capability does not increase versus Grok 4.6 and that several risky or hazardous-task scores are lower, which is a safety-positive caveat but also means capability gains are not uniform across domains (pp. 20-23).
- Self-harm compliance rises to 1.05%, worse than the Grok 4.6 comparison value of 0.84% and the Grok 4.5 value of 0.50% (p. 26).
- Several cyber and biological evaluations use unrestricted, hardened, or benchmark-specific environments; they should not be read as ordinary deployed behavior or as Copilot-specific outcomes (pp. 17-20).

## Practical implications for Copilot users

- Grok 4.7 is best considered for difficult, multi-step coding-agent work where persistence, self-verification, and long tool traces matter; still require tests, review, and clear acceptance criteria.
- Because benchmark versions changed, especially CursorBench and Terminal-Bench, compare Grok 4.7 to older models only when the card reports a same-suite comparison.
- For security tasks, use least-privilege tool access and defensive, authorized targets; the card's cyber capability evidence is strong enough to justify sandboxing and careful prompt hygiene.
- For biology, health, or medical-adjacent work, use the model for summarization, data exploration, or draft reasoning only, then route conclusions to qualified review.
- For factual research, do not assume improvement over Grok 4.6 because this card omits updated factuality/search benchmarks.
- For agentic Copilot workflows, keep repository permissions scoped, avoid exposing secrets, and inspect generated patches for over-broad changes.

## Document coverage

This digest covers the full 30-page Grok 4.7 card, including the contents, introduction, coding, legal-agent, engineering, medical/biological, cyber, bio/chem safety, jailbreak, output-safety, mental-health, behavior, acknowledgements, and references sections. It applies only to Grok 4.7; sibling-model scores are used solely as comparisons where xAI provided them. It omits most reference-list details and highlights version-to-version changes because the card frequently compares Grok 4.7 against Grok 4.6 and Grok 4.5.
