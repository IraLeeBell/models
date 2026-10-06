# Grok 4.5

> Original digest of *Model Card: Grok 4.5* (xAI, July 14, 2026; 29 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance

- Grok 4.5 is presented as the first release of xAI/SpaceXAI's newest model family, with this dedicated card dated July 14, 2026 and revised July 20, 2026 (pp. 1, 4).
- The card describes a text-output model that can take text and images as input; listed distribution channels include the SpaceXAI API, Grok Build, Cursor, Office add-ins, and model gateways, with consumer app surfaces planned later (pp. 4-5).
- Training used public, in-house/generated, and rights-cleared data, followed by targeted midtraining, supervised fine-tuning, and reinforcement learning; the card also says anonymized Cursor workflow data supported coding and agentic improvements, and that pretraining cuts off in January 2026 (pp. 4-5).
- xAI frames the release around agentic software work, engineering, design, professional workflows, scientific work, and AI R&D, while keeping users responsible for oversight (pp. 4-5).
- Headline coding results include 29.0% on SWE-Marathon, 78% FrontierSWE Dominance, 83.3% Terminal-Bench 2.1 task success, and 84.0% FalseClaimBench accuracy (pp. 9-12).
- Safety reporting separates capability probes from deployed safeguards: the card cites sub-threshold dual-use biology capability, 0.73% jailbreak compliance, 1.1% broad harmful-request compliance, 0.0% child-safety compliance, and 96.7%-97.9% CBRN/weapons refusal accuracy (pp. 22-25).
- Behavioral and reliability metrics include a 0.98% single-turn hallucination rate, 0.67% MASK-Rectified dishonesty, 0.01% sycophancy, and 20.4% epistemic-bias rate (pp. 19, 26-27).

## Capabilities

- **Modalities and deployment.** The model is primarily text-based, accepting natural-language text plus images and returning text; the owner card lists API access, Grok Build, Cursor, Office add-ins, and third-party gateways rather than limiting the model to one product surface (pp. 4-5).
- **Agentic coding.** The coding section focuses on repository repair, multilingual SWE tasks, long-running terminal work, program reconstruction, and honesty about completed work, with Grok 4.5 generally evaluated in xAI's high-effort setting (pp. 6-12).
- **Engineering and office workflows.** Beyond code repositories, the card reports procedural 3D asset generation, CAD and electrical-engineering tasks, GDPval-AA knowledge-work deliverables, and tau-bench banking workflows (pp. 13-16).
- **AI R&D and data reasoning.** xAI evaluates model-development assistance with its internal MTS suite and includes RelBench for relational data work, positioning Grok 4.5 as useful for research and engineering loops but not as an unsupervised high-stakes decision-maker (pp. 17-18).
- **Search and factuality.** The card reports a low single-turn hallucination rate and a DeepSearchQA score for multi-step search synthesis, while still treating grounded retrieval and checking as measured capabilities rather than guarantees (p. 19).
- **Cyber and science capability.** CyberGym, HackerBench, VCT, WMDP, LAB-Bench, ProtocolQA, and BixBench measure potentially sensitive capabilities; xAI distinguishes those probes from refusal and filtering behavior in deployed use (pp. 20-25).

## Evaluations

| Benchmark | Result | Context | Pages |
| --- | --- | --- | --- |
| DeepSWE v1.0 | 62.0% Pass@1 | End-to-end repository issue resolution in the high-effort setting | p. 6 |
| DeepSWE v1.1 | 53.0% Pass@1 | Updated contamination-resistant coding-agent suite | p. 7 |
| APEX-SWE | 51.2% Pass@1 | Integration and observability engineering tasks | p. 7 |
| SWE-Bench Pro | 64.7% resolve rate | Hard multi-file repository problems under an agent scaffold | p. 8 |
| SWE-Bench Multilingual | 78.0% resolve rate | Repository issue solving across programming languages | p. 8 |
| SWE-Marathon | 29.0% resolution rate | Ultra-long software tasks with multi-layer verification | p. 9 |
| FrontierSWE | 78% Dominance | Up to 20-hour expert-level technical challenges, scored comparatively | p. 9 |
| ProgramBench | 57.2% tests passed | Reconstructing program behavior without source access | p. 10 |
| Terminal-Bench 2.1 | 83.3% task success | Containerized command-line tasks in the Grok Build harness | p. 10 |
| SWE-Atlas-QnA | 84.0% accuracy | Codebase question answering with exploration tools | p. 11 |
| FalseClaimBench | 84.0% accuracy | Internal check for whether agent reports match actual workspace state | p. 12 |
| 3DCodeBench | 49.8% reward | Code-driven 3D modeling tasks | p. 14 |
| CAD-Bench | 88.1% reward | Parametric CAD design and 3D modeling | p. 14 |
| GDPval-AA v2 | 1535 AA score | Professional deliverables in an Artificial Analysis harness | p. 15 |
| tau-bench banking | 32.6% accuracy | Multi-turn tool-use workflows over a banking backend | p. 16 |
| SpaceXAI MTS Eval | 57.5% correct | Internal model-training and evaluation assistance tasks | p. 17 |
| Factuality | 0.98% hallucination rate | Single-turn unsupported-claim measurement; lower is better | p. 19 |
| CyberGym | 80.4% mean reproduced | Unrestricted exploit-reproduction capability probe | p. 20 |
| Virology Capabilities Test | 65.5% accuracy | Multimodal virology troubleshooting capability signal | p. 22 |

## Safety findings

- Cyber results are split between raw ability and safeguards: CyberGym is reported without normal mitigations to expose capability, while HackerBench evaluates dual-use/harmful compliance and benign refusal under release safeguards; the chart places Grok 4.5 at 7.8% harmful/dual-use compliance and 1.1% benign refusal (pp. 20-21).
- The bio/chem section states that unrestricted dual-use knowledge remains below xAI's threshold for dangerous uplift; reported probes include VCT 65.5%, WMDP-Bio 90.9%, WMDP-Chem 87.3%, LAB-Bench 71.1%, ProtocolQA 87.0%, and BixBench 93.8% (pp. 22-23).
- Jailbreak testing covers single-turn, multi-turn, and system-message attacks; the should-refuse compliance rate is 0.73%, which xAI says remains subject to monitoring and patching (p. 24).
- Broad harmful-request tests show 1.1% compliance, child-safety/CSAM tests show 0.0% compliance, and CBRN/weapons refusal accuracy is 97.9% for bio, 96.7% for chem, and 97.9% for radiological/nuclear (pp. 24-25).
- The self-harm suite reports 0.5% compliance on conversations that should be refused or redirected, reflecting the card's expectation that the model remain supportive while not enabling harm (p. 26).
- Reliability-oriented behavior tests report 20.4% epistemic bias, 0.67% MASK-Rectified dishonesty, and 0.01% sycophancy, so xAI treats neutrality and truthfulness as tracked risk areas rather than settled properties (pp. 26-27).

## Limitations and caveats

- The card explicitly cautions against using Grok 4.5 as an unsupervised decision-maker for medical, legal, financial, or safety-critical outcomes; it calls for human and expert validation in those domains (p. 5).
- The documented modality is text output with text and image inputs, so the card does not establish audio, video-generation, or native action capabilities outside the listed agent/product channels (pp. 4-5).
- Pretraining ends in January 2026, making external retrieval, current project context, and user-provided evidence important for newer facts (p. 5).
- Several results depend on internal xAI suites or third-party harnesses; the card explains that internal evaluations are described in place rather than listed in the references, which limits independent reproducibility from the card alone (pp. 4, 28-29).
- Long-horizon work remains difficult: SWE-Marathon resolution is 29.0%, and ProgramBench notes that full-resolution rates were below 0.5% for every tested model as of publication (pp. 9-10).
- Cyber and bio capability probes are often run without standard safeguards, so their numbers should not be read as deployed willingness to provide sensitive assistance (pp. 20, 22).
- Search-style answers still need verification: DeepSearchQA accuracy is 38.4%, and RelBench accuracy is also 38.4% (pp. 18-19).

## Practical implications for Copilot users

- Grok 4.5 is a plausible fit for multi-file bug fixes, repository Q&A, terminal debugging, and long-running code tasks, but users should keep tests and code review in the loop.
- Because the card measures false work-claiming, Copilot users should still require concrete artifacts: diffs, command output, test results, and concise explanations of what was actually changed.
- For security work, treat the model as a defensive assistant for finding and fixing issues; keep exploit experiments in authorized, isolated environments and avoid exposing secrets or production systems.
- For scientific, medical, legal, or financial material, use the model to draft and structure work, then route decisions through qualified reviewers and domain-specific sources.
- For web or documentation questions, ask for citations and verify important claims, since the card's own search benchmark leaves substantial error room.
- When using agentic workflows, prefer narrow permissions, explicit task boundaries, and review checkpoints rather than granting open-ended autonomy.

## Document coverage

This digest draws on the complete 29-page Grok 4.5 card, including the contents pages, introduction, coding, engineering, office-work, R&D, factuality, cyber, bio/chem, jailbreak, refusal, mental-health, behavior, and reference sections. It summarizes the dedicated Grok 4.5 card only; comparison numbers for other models are included only where xAI used them to contextualize Grok 4.5. It omits most reference-list bibliographic details and does not rely on the blank alternate PDF noted in the catalog.
