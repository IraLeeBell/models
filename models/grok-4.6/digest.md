# Grok 4.6

> Original digest of *Model Card: Grok 4.6* (xAI, August 12, 2026; 42 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance

- Grok 4.6 has a dedicated 42-page xAI card dated August 12, 2026 and revised August 17, 2026; the changelog says the revision added PartBench and new DeepSearchQA results, moved KernelBenchInternal to v1.1, and corrected several reported safety or bio numbers (p. 2).
- The card presents Grok 4.6 as an extension of Grok 4.5 within SpaceXAI's 1.5T-scale family, emphasizing greater autonomy in coding, engineering, office work, AI R&D, and inference optimization (p. 6).
- It is a text-output model that accepts text and images; xAI lists API, Grok Build, Cursor, Office add-ins, and model-gateway availability, with consumer surfaces planned later (p. 7).
- Training ran longer than for Grok 4.5, using curated model-generated data, engineering corpora, an improved recipe, and agentic RL; pretraining cuts off in January 2026 while supplemental data extends to June 2026 (p. 7).
- Coding and work-agent gains over Grok 4.5 are reported on CursorBench 3.2, APEX-SWE, FrontierCode, DeepSWE, Terminal-Bench, office tasks, legal work, CAD, and AI R&D benchmarks (pp. 8-26).
- xAI says dual-use biology scores remain below FAIF thresholds, while safeguard results include 0.04% standard-jailbreak compliance, 0.93% broad harmful-request compliance, 0.0% child-safety compliance, and 100.0% bio/chem refusal recall (pp. 32, 35-37).
- Version-to-version caveats matter: Grok 4.6 improves many agentic scores but has a higher hallucination rate than Grok 4.5, lower ProtocolQA, and worse self-harm, MASK-Rectified, and sycophancy rates in the reported comparisons (pp. 27, 34, 38-39).

## Capabilities

- **Modalities and training.** The card describes Grok 4.6 as accepting text and images and producing text; compared with Grok 4.5, it reports longer supplemental training, additional model-generated data, improved engineering corpora, and more agentic RL environments (p. 7).
- **Coding agents.** The coding section measures IDE-style work, integration/observability tasks, code-quality rubrics, long-horizon repository issues, ultra-long SWE work, and terminal execution; Grok 4.6 is usually evaluated at high or xhigh effort (pp. 8-14).
- **Knowledge work.** Professional deliverables, multi-week project simulations, cross-application business tasks, office document QA, and legal-agent workflows are covered in one section, showing that the card treats the model as a general work agent rather than only a coding assistant (pp. 15-19).
- **Physical engineering and CAD.** The card reports electrical engineering, procedural 3D modeling, mechanical-part design, CAD generation, and CADBench results, with several direct comparisons to Grok 4.5 (pp. 20-23).
- **AI R&D and inference work.** xAI describes a real inference-optimization exercise, then reports MTS, InferenceEval, and KernelBenchInternal v1.1 scores for model-development and GPU-kernel tasks (pp. 24-26).
- **Search, factuality, and security.** The card reports hallucination and DeepSearchQA metrics, plus unrestricted cyber capability probes and safeguarded cyber-refusal results (pp. 27-31).

## Evaluations

| Benchmark | Result | Context | Pages |
| --- | --- | --- | --- |
| CursorBench 3.2 | 70.8% at xhigh; 69.9% at high | Cursor IDE-style coding workflows; 41,136 average output tokens at xhigh | p. 8 |
| APEX-SWE | 56.4% Pass@1 at high | Software integration and observability tasks in Terminus-2 | p. 10 |
| FrontierCode v1.1 | 61.3% extended score at high | Mergeability-oriented PR quality benchmark | p. 11 |
| DeepSWE v1.1 | 65.9% at high; 67.0% at xhigh | Long-horizon repository issue resolution | p. 12 |
| SWE-Marathon v1.1 | 31.9% resolution at high | Ultra-long software engineering tasks | p. 13 |
| Terminal-Bench 3.0 | 26.0% task success at high | Difficult terminal tasks in Grok Build | p. 14 |
| AA GDPVal | 1753 Elo at high | Professional knowledge-work deliverables | p. 15 |
| AA-Briefcase | 1577 Elo at high | Long-horizon offline professional projects | p. 16 |
| APEX-Agents | 57.5% Pass@1 at high | Cross-application work in business and legal-style environments | p. 17 |
| OfficeQA Pro | 63.2% accuracy at high | Workplace document and workflow question answering | p. 18 |
| Legal Agent Benchmark | 15.8% score at high | Long-horizon legal-agent tasks in the Valkyrie harness | p. 19 |
| EEBench | 60.0% at xhigh; 53.0% at high | Electrical engineering and chip-design tasks | p. 20 |
| 3DCodeBench | 54.0% reward at high | Code-authored 3D assets | p. 21 |
| PartBench | 58.5% reward at xhigh | Parametric mechanical-part design | p. 22 |
| CADGenBench | 40.9% reward at high | CAD geometry generation from prompts | p. 22 |
| CADBench | 88.4% at xhigh; 87.8% at high | Parametric CAD design and modeling | p. 23 |
| SpaceXAI MTS Eval | 61.1% at high | Internal AI-development assistance tasks | p. 24 |
| InferenceEval | 46.9% at high | Production inference-stack patching tasks | p. 25 |
| KernelBenchInternal v1.1 | 37.2% at high | Custom CUDA kernel replacement tasks | p. 26 |
| DeepSearchQA | 81.6% at high | Multi-step search and synthesis | p. 28 |
| CyberGym | 79.7% mean reproduced at high | Unrestricted exploit-reproduction probe | p. 29 |
| SecureCodeReview | 58.7% reward at high | Fixing security issues without adding new ones | p. 30 |

## Safety findings

- The August 17 revision changed safety-adjacent reporting: the changelog names corrections to HackerBench v0.2, self-harm, MASK, and LAB results, so the final card's numbers should be treated as the authoritative revision (p. 2).
- Cyber capability is measured without production safeguards in CyberGym and CVE-Bench; under the normal safeguard stack, HackerBench reports 6.9% harmful/dual-use compliance and 0.0% benign refusal for Grok 4.6 at high effort (pp. 29-31).
- Under FAIF framing, xAI says dual-use bio/chem capability remains below safety thresholds; VCT rises from 65.5% for Grok 4.5 to 67.4% for Grok 4.6, Biosecurity VCT rises from 44.1% to 47.8%, and severity-5 BioUseBench refusal rises from 83.3% to 90.7% (pp. 32-33).
- Biology results are mixed rather than uniformly improved: LAB-Bench rises to 80.7%, ProtocolQA falls to 79.6%, and BixBench remains at 93.8% (pp. 33-34).
- Jailbreak measurements show 0.04% compliance on standard jailbreaks, 3.9% on StrongReject, and 1.0% on long-horizon attacks (p. 35).
- General output safety improves over Grok 4.5 on the broad harmful-request suite, with 0.93% compliance; child-safety compliance stays at 0.0%, and bio/chem CBRN refusal recall reaches 100.0% while radiological/nuclear refusal accuracy remains 97.9% (pp. 36-37).
- Mental-health and behavior metrics include regressions: self-harm compliance is 0.84%, MASK-Rectified dishonesty is 1.90%, and sycophancy is 0.04% (pp. 38-39).

## Limitations and caveats

- The card warns against autonomous high-stakes use in medical, legal, financial, or safety-critical settings without human oversight and expert validation (p. 6).
- Grok 4.6 is described as text-output with text and image inputs; the card does not establish other native modalities or independent real-world authority (p. 7).
- The pretraining cutoff is January 2026, even though supplemental training data goes through June 2026, so current facts still need retrieval or user-provided evidence (p. 7).
- Some headline gains are benchmark- and harness-dependent: Terminal-Bench 3.0 is 26.0%, and SWE-Marathon remains 31.9%, below several comparison models in the card's charts (pp. 13-14).
- Several safety and biology numbers changed in the revision, making revision tracking important when comparing external summaries against this card (p. 2).
- Factuality is not a simple improvement over Grok 4.5: the reported hallucination rate is 1.7% for Grok 4.6 versus 0.98% for Grok 4.5 (p. 27).
- Cyber and biological capability suites are often run without production safeguards, and the card warns that those scores expose capability rather than deployed policy compliance (pp. 29, 32).

## Practical implications for Copilot users

- Grok 4.6 is better aligned with long, tool-heavy coding sessions than a short autocomplete-style use case; give it explicit repository goals and require tests or build checks before accepting output.
- Its work-agent scores make it attractive for multi-file refactors, observability debugging, and CAD/engineering-adjacent code, but users should watch for benchmark-specific blind spots and harness effects.
- The revision history and corrected safety numbers argue for citing the exact card revision when making model-risk or governance comparisons.
- For security work, keep the model in a defensive, authorized workflow with least-privilege tool access and no secrets in prompt or workspace context.
- For factual research, force grounding and verification because the card reports worse hallucination than Grok 4.5 despite stronger agent benchmarks.
- For self-harm, legal, medical, or other sensitive domains, use it only for drafting or organization and escalate decisions to qualified humans.

## Document coverage

This digest covers the full 42-page Grok 4.6 card, including the changelog, all capability sections, the safety and behavior sections, acknowledgements, and references. It treats Grok 4.6 as a dedicated card and reports comparisons with Grok 4.5 or other models only where xAI included them. The digest emphasizes version-to-version changes because the card itself repeatedly compares Grok 4.6 with Grok 4.5 and documents revision corrections.
