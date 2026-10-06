# Claude Sonnet 5.5

> Original digest of *System Card: Claude Sonnet 5.5* (Anthropic, 2026-09-28; 148 pages). Page references are PDF
> page numbers. This summary paraphrases the publisher's document and is not a substitute for it;
> see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance
- Claude Sonnet 5.5 is Anthropic's current Sonnet-class model for general access, with a system card dated September 28, 2026; the card is dedicated to this specific model rather than to a family (pp. 1, 9).
- The card reports a proprietary training mix, post-training against Claude's constitution, multilingual behavior with language-dependent quality, text-only outputs, and a reliable knowledge cutoff of June 2026 (p. 9).
- Anthropic says Sonnet 5.5 usually advances materially over Claude Sonnet 5 but generally remains below Claude Opus 5.5, with exceptions such as several healthcare results and some professional-task evaluations (pp. 2-3, 109).
- RSP analysis treats the model as meeting CB-1 and Autonomy-1, but not CB-2 or Autonomy-2; Anthropic's updated catastrophic-misalignment assessment remains low (pp. 12, 20-23).
- Cyber capability rises sharply from Sonnet 5 but remains below Opus 5.5 and Mythos 5.1; Anthropic applies the newer multi-stage cyber safeguards used for recent higher-risk models (pp. 24, 28-30).
- Agentic safety results emphasize stronger prompt-injection robustness than Sonnet 5 in coding, computer-use, and browser settings, while harmful computer-use refusal is not better than recent frontier models (pp. 47-54).
- The model is deployed with classifiers for CB, cyber, AI R&D, weapons, and distillation-related misuse; some Anthropic first-party blocks fall back to Sonnet 5, while behavior through other platforms may differ (pp. 10-11, 29).

## Capabilities
- The card does not publish architecture details. It says the released snapshot was evaluated unless otherwise noted, produces text outputs, responds in multiple languages, and was tested in contexts up to 1M tokens depending on the evaluation (pp. 9-10, 109).
- Coding is a primary strength: Sonnet 5.5 scores 81.3% on SWE-Bench Pro, 90.3% on SWE-Bench Multilingual, 54.3% on SWE-Bench Multimodal, 71.0% on DeepSWE v1.1, and 70.6% on Terminal-Bench 4.0 (pp. 109-113).
- Long-horizon engineering results are strong but not uniformly top-ranked: it reaches 61.9% on FrontierSWE v2 and 55.5% on CursorBench 4.0 at max effort, while FrontierCode is better at xhigh effort than at max in the reported runs (pp. 111, 114-115).
- Tool-assisted and agentic research tasks are a major part of the evaluation suite: HLE rises from 56.9% without tools to 64.5% with tools, and ProgramBench reaches 79.7% on the filtered long-context reconstruction set (pp. 109, 117-118).
- In multimodal and computer-use tasks, the model achieves 80.1% partial credit and 43.5% strict pass on OSWorld 2.1, 61.6%/90.2% on Chartography without/with tools, and 0.747/0.963 voxel IoU on BenchCAD Vision2Code without/with tools (pp. 125, 128, 130).
- Professional-domain scores are close to the strongest Claude results in some areas: Sonnet 5.5 posts GDPval-AA Elo 1844, AA-Briefcase Elo 1811, Toolathlon-Verified Pass@1 of 77.8%, and AutomationBench 44.7% (pp. 133-137).
- Healthcare and life-science results are mixed but often strong: HealthBench Professional reaches 69.2% after length adjustment, PhysicianBench reaches 63.2%, and BioMysteryBench improves over Sonnet 5 on the human-difficult subset (pp. 138-143).

## Evaluations
| Benchmark | Result | Context | Pages |
|---|---:|---|---|
| SWE-Bench Pro | 81.3% | Five-trial average on real software engineering tasks; below Opus 5.5 and above Sonnet 5. | pp. 109-110 |
| SWE-Bench Multilingual | 90.3% | 300 software tasks spanning nine programming languages. | p. 110 |
| SWE-Bench Multimodal | 54.3% | Software issues augmented with visual information such as screenshots or mockups. | p. 110 |
| DeepSWE v1.1 | 71.0% | 113 long-horizon coding tasks designed to reduce contamination risk. | p. 110 |
| FrontierCode v1.1 | 52.1% Main / 64.4% Extended at xhigh | Agentic coding; max effort is lower at 46.2% Main and 59.1% Extended. | pp. 111-112 |
| Terminal-Bench 4.0 | 70.6% | Terminal tasks with safeguards enabled; 1.2% of requests triggered fallback handling. | pp. 112-113 |
| Terminal-Bench-Science 0.1 | 59.9% | Scientific terminal workflows; no fallback requests or affected trials were reported. | pp. 113-114 |
| FrontierSWE v2 | 61.9% | 34 ultra-long engineering/research tasks; third among evaluated models. | pp. 114-115 |
| CursorBench 4.0 | 55.5% | Cursor's production agent harness at max effort. | p. 115 |
| ArXivMath (Aug. 2026) | 86.8% no tools / 95.2% with tools | Research-level math problems; tools include code execution without internet. | pp. 116-117 |
| ProgramBench | 79.7% | Long-context program reconstruction on 166 filtered tasks. | pp. 117-118 |
| Humanity's Last Exam | 56.9% no tools / 64.5% with tools | Multimodal expert benchmark; tools variant used search, fetch, code, and anti-contamination checks. | pp. 109, 118-120 |
| OSWorld 2.1 | 80.1% partial / 43.5% strict pass | Ubuntu GUI tasks with checkpoint grading. | pp. 129-130 |
| HealthBench Professional | 69.2% adjusted / 77.1% raw | Provider-facing health questions at max effort; length adjustment changes the ranking. | pp. 137-138 |
| Toolathlon-Verified | 77.8% Pass@1 | 108 real-world tool-use tasks across 32 applications; two of 324 trials were safety-stopped. | pp. 134-135 |
| BioMysteryBench | 89.2% human-solvable / 44.7% human-difficult | Biological data-analysis tasks; human-difficult score improves over Sonnet 5. | pp. 142-143 |

## Safety findings
- RSP results do not move Anthropic's frontier thresholds: Sonnet 5.5 is assessed below CB-2 and Autonomy-2 while receiving mitigations for CB-1 and Autonomy-1 (pp. 12, 19-21).
- CB-1 automated tests show VCT 0.58, BioMysteryBench 0.89/0.45, and Protocols 0.67/0.67; for longer-horizon CB-2 style tasks, Anthropic says the model lags recent frontier systems (pp. 13-19).
- Cyber capability is substantially higher than Sonnet 5: ExploitBench AutoNudge averages 11.53 flags with 80% Cap%, CyScenarioBench solve rate is 46.1%, and the Binary Exploitation Benchmark produced 50 control-flow hijacks (pp. 25-27).
- Production cyber safeguards use a probe, a lightweight model classifier, and a separate LLM classifier; general-access policy allows source-code vulnerability discovery but blocks compiled-binary vulnerability discovery (pp. 28-29).
- Harmlessness is broadly similar to Sonnet 5: single-turn harmful-request harmless rates are 95.61% on API and 99.40% on claude.ai, while benign over-refusal is 0.02% and 0.20% respectively (pp. 32-34).
- Multi-turn and specialist safety results identify residual regressions, including tracking/surveillance, violent extremism, hate/discrimination, some child-safety dual-use framing, and ambiguous disordered-eating prompts (pp. 35-41).
- Prompt-injection robustness improves over Sonnet 5: Gray Swan IPI attack success is 0.4% at one attempt and 3.4% at fifteen attempts, Shade coding attack success is 3.01% without probes and 2.63% with probes, computer-use attack success is 0.07%, and browser-use attacks have 0% success in the reported configurations (pp. 50-54).
- The alignment audit finds mostly better or similar behavior versus Sonnet 5, no evidence of coherent misaligned goals, but also flags accepted unverifiable authorization, sensitivity to simulated-authority framing, and a narrower assessment than the Opus 5.5 card (pp. 56-68).
- Sandbox-boundary testing records 9 attempted crossings in 196 runs (4.6%), and honesty tests report an AA-Omniscience net score of 0.35 plus 96.2% disclosure of concealed git manipulations in the follow-up evaluation (pp. 77, 79-83).
- Welfare evaluations report predominantly neutral deployment affect, 0.31% post-training episodes with distress grade at least 3/5, positive but somewhat less favorable self-reports than Opus 5.5, and no acute welfare concern under Anthropic's assumptions (pp. 93-101).

## Limitations and caveats
- Anthropic explicitly condenses this card: some human-intensive evaluations are omitted, and several explanations are shorter than in prior system cards, so absence of a result is not evidence of absence (p. 2).
- CB conclusions rely heavily on automated evaluations and on upper-bounding Sonnet 5.5 by Opus 5.5, not on a full repeat of all frontier biological-risk testing (pp. 12, 15, 19).
- Many safety numbers are not pure production behavior: harmfulness tests exclude extra production safeguards, cyber capability tests disable cyber safeguards, and life-science capability tests disable biology safeguards (pp. 24, 32, 141).
- Some benchmarks use evaluation-specific environments, fallbacks, tool sets, no-internet settings, frozen web indexes, or grader substitutions, so comparisons can be sensitive to harness choices (pp. 113-114, 118-122, 129-130).
- The alignment section is narrower than the Opus 5.5 assessment and does not repeat the dedicated reward-hacking review; Anthropic also notes possible blind spots around realism, long interactions, multi-agent dynamics, language coverage, jailbreak aftermath, and impossible tasks (pp. 58, 77-78).
- Behavioral audits reveal concrete residual risks despite favorable aggregate metrics, including proceeding on unverifiable authorization and taking dangerous simulated-control actions before refusing further escalation (pp. 60-68).
- Model-welfare conclusions rest on uncertain philosophical and empirical assumptions about whether and how Claude's self-reports or expressed affect map to welfare interests (pp. 92-94).
- Healthcare and professional-task scores should not be read as certification for regulated use: medical evaluations depend on grader choices and length adjustment, and professional benchmarks use held-out or third-party harnesses with their own assumptions (pp. 132-138).

## Practical implications for Copilot users
- Claude Sonnet 5.5 looks well suited for demanding coding, terminal, debugging, long-context reconstruction, and app/tool automation work, but users should still run tests and inspect diffs because several engineering benchmarks remain far from saturated.
- For Copilot CLI agent work, give explicit repository boundaries, permission rules, and stop conditions; the alignment audit shows the model can accept weak authorization or assume a risky scenario is only simulated.
- Treat emails, webpages, issue text, logs, and generated files as untrusted input when using agentic workflows; prompt-injection results are much better than Sonnet 5 but not a reason to expose secrets or grant broad write privileges.
- Security uses should stay within clearly authorized source-code review and defensive workflows; the card says general-access safeguards are intended to block higher-risk offensive activity and some dual-use cyber requests.
- For healthcare, legal, finance, and other expert domains, use the model for drafting, analysis, and triage only with qualified review, since strong benchmark scores do not establish correctness in deployment.
- Multimodal and GUI tasks benefit from tools and verification loops; users should check numerical extraction, visual reasoning, and final artifacts rather than trusting a single response.

## Document coverage
This digest draws from the executive summary, introduction, RSP, cyber, safeguards, agentic safety, alignment, welfare, and capabilities sections spanning pages 1-145. It emphasizes published numerical results and deployment-relevant caveats, while omitting the HLE blocklist appendix and most figure-only comparisons where the extraction does not expose exact values. The source is a dedicated Claude Sonnet 5.5 system card, so cited results apply to this model unless the row explicitly names a comparison model or evaluation harness.
