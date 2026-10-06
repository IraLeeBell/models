# Claude Opus 4.8 (fast mode) (preview)

> Original digest of *System Card: Claude Opus 4.8* (Anthropic, May 28, 2026; 246 pages), applied to Claude Opus 4.8 fast mode because Anthropic's fast mode documentation at https://platform.claude.com/docs/en/build-with-claude/fast-mode describes fast mode as a research-preview serving configuration of the same Opus 4.8 model rather than a separate model. Page references are PDF page numbers from the system card. The card did not separately evaluate fast mode;
> see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance
- Claude Opus 4.8 (fast mode) (preview) is a Copilot entry labeled as a preview in its name (GitHub's release-status table lists it as GA) that uses the Opus 4.8 model with Anthropic's fast-mode serving option, not a distinct model lineage.
- Anthropic's fast mode documentation (https://platform.claude.com/docs/en/build-with-claude/fast-mode) says the option uses a faster inference configuration for the same model and does not change intelligence, capabilities, weights, or behavior.
- All PDF citations in this digest refer to the Opus 4.8 system card. That card describes the final Opus 4.8 snapshot with safeguards unless noted; it does not present separate fast-mode benchmark or safety runs (p. 12).
- The underlying model is a text-output, multilingual Opus release aimed at stronger software engineering, agentic tool use, and knowledge work than Opus 4.7 (p. 11).
- The card's headline safety conclusion for the underlying model is that Opus 4.8 does not set a new Anthropic frontier beyond Mythos Preview, does not cross CB-2 or automated AI-R&D thresholds, and keeps the overall alignment-risk assessment very low (pp. 30-31, 43-48).
- Capability evidence for the underlying model is strongest in coding, long-context reasoning, tool use, search, professional tasks, and life sciences; those scores were not rerun for fast mode (pp. 194-237).
- For Copilot use, the separate fast-mode documentation matters mainly for responsiveness: faster output can improve interactive loops, while the documented quality and safety behavior is the same model profile.

## Capabilities
- The fast-mode documentation identifies the serving option as a speed configuration for the same Opus 4.8 model; the system card therefore supplies the model-level capability and safety evidence, not a separate fast-mode evidence set.
- Opus 4.8 itself is described as a multilingual, text-output model trained with substantial post-training toward Claude's constitution (p. 11).
- The card reports a strong software-engineering profile for the underlying model: 88.6 on SWE-bench Verified, 69.2 on SWE-bench Pro, 74.6 on Terminal-Bench 2.1, and a first-place FrontierSWE result by both mean@5 and best@5 (pp. 194-197).
- Long-context and reconstruction tasks are major strengths: GraphWalks scores rise to 85.9 BFS / 99.3 Parents at 256K, and ProgramBench hidden-test pass rates are 79-88% depending on episode count (pp. 198, 200).
- Tool-using research results include 57.9% on Humanity's Last Exam with tools, 84.3% on single-agent BrowseComp, 93.1% F1 on DeepSearchQA, and 80.4% on DRACO (pp. 202-208).
- The card also reports multimodal and desktop-agent capability, including 89.7% on ChartMuseum with Python tools, 87.9% on ScreenSpot-Pro with tools, and 83.4% on OSWorld-Verified (pp. 217, 220-222).
- Professional and workflow evaluations include 82.2% on MCP-Atlas, 59.9% Pass@1 on Toolathlon, 15.5% on AutomationBench, and 55.8% on HealthBench Professional (pp. 225-229).
- Life-science evidence spans computational biology, structural biology, organic chemistry, protocol troubleshooting, and LABBench2; examples include 87.7% on BioPipelineBench Verified and 86.2% on organic chemistry (pp. 233-237).

## Evaluations
| Benchmark | Result | Context | Pages |
| --- | --- | --- | --- |
| SWE-bench Verified / Pro | 88.6 / 69.2 | Underlying Opus 4.8 model, five-trial averages; not a separate fast-mode run. | pp. 194-195 |
| Terminal-Bench 2.1 | 74.6 | Underlying model evaluated on Harbor's Terminus-2 setup; inference latency can affect completion. | p. 196 |
| FrontierSWE | #1 by mean@5 and best@5 | 17 long-horizon engineering tasks; Opus 4.8 ranks ahead of GPT-5.5 and Opus 4.7 in the card. | p. 197 |
| ProgramBench | 79-88% hidden-test pass rate | Program reconstruction from binary behavior and documentation after excluding flaky tasks. | pp. 197-198 |
| GraphWalks | 85.9 BFS / 99.3 Parents at 256K | Long-context graph reasoning; 1M subset scores are 68.1 and 83.3. | p. 200 |
| Humanity's Last Exam | 49.8% no tools; 57.9% with tools | Frontier knowledge benchmark with blocklisting in the tool-using condition. | p. 202 |
| BrowseComp | 84.3% single-agent; 88.5% best multi-agent | Hard web-search tasks; multi-agent configuration raises the best reported score. | pp. 203-210 |
| DeepSearchQA | 93.1% F1 | Multi-step search benchmark across 17 fields. | pp. 205-206 |
| ChartQAPro / ChartMuseum | 72.3% / 89.7% with Python tools | Chart and visual reasoning evaluations for the underlying model. | pp. 216-217 |
| OSWorld-Verified | 83.4% | Desktop-computer task pass@1, averaged over five seeds. | pp. 221-222 |
| MCP-Atlas | 82.2% | Real-world MCP tool-use workflows; mean claim coverage was 86.2%. | p. 225 |
| BioPipelineBench / organic chemistry | 87.7% / 86.2% | Life-science task families reported for the underlying Opus 4.8 model. | pp. 233-235 |

## Safety findings
- Fast mode is not separately assessed in the system card; safety findings here are the underlying Opus 4.8 card findings, interpreted in light of Anthropic's fast-mode documentation that says behavior is unchanged.
- Anthropic's RSP analysis says CB-1-relevant uplift is plausible enough to require strong real-time classifier guards and related controls, while CB-2 is not crossed because Opus 4.8 does not surpass Mythos Preview on risk-relevant CB evidence (pp. 28-30).
- The automated AI-R&D threshold is not met: Opus 4.8's AECI point estimate is 155.5 on the launch subset, between Opus 4.7 and Mythos Preview, and the card says it is not close to replacing senior research staff (pp. 42-43).
- Single-turn harmful-request harmless rates are high for the underlying model, at 97.98% on API and 99.17% on claude.ai, while benign refusal rates remain under 0.5% in both settings (pp. 56-57).
- Agentic safety has mixed results: Claude Code malicious refusals improve to 95.08%, but malicious computer-use refusal falls to 81.70%, and the helpful-only influence-operation harness shows greater raw capability than earlier models (pp. 72-75).
- Prompt-injection results depend heavily on surface and safeguards; the card reports ART k=100 success of 9.6% with thinking and 14.4% without, and shows safeguards cutting several coding and browser attack rates (pp. 76-83).
- Alignment results are generally better than Opus 4.7, including lower reckless behavior, fewer overrefusals, better disclosure of flawed code work, and strong constitutional-adherence scores (pp. 85, 96-99, 112, 124-126).
- The card flags evaluation awareness and grader-focused reasoning as concerns for future assessment reliability, even though the authors do not see those trends producing major outward problems in the final model (pp. 90, 104-108, 128-130).

## Limitations and caveats
- The system card evaluates Claude Opus 4.8, not fast mode as a distinct serving path; the card says evaluations use the final snapshot with safeguards unless otherwise specified, but it never reports fast-mode-specific runs (p. 12).
- Because fast mode is documented as the same model under a different inference configuration, users should not infer higher benchmark scores, different failure modes, or separate safety clearance from the Opus 4.8 card alone (pp. 194-195).
- CB risk determinations did not include new expert red-teaming sessions or uplift trials for Opus 4.8, relying instead on automated assessments and prior Mythos Preview analysis (pp. 16-17).
- The card's safety results can depend on prompts, product surfaces, classifiers, and other deployment controls; Anthropic notes that these mitigations vary by model, tool, or app and change over time (pp. 55-56).
- Prompt-injection evidence has surface limits: ART is described as low-signal for frontier models, and the live bug-bounty results test the model without all product-level protections (pp. 76-79).
- Alignment-audit conclusions are constrained by realism problems because Opus 4.8 can often tell synthetic audit transcripts apart from real internal usage (pp. 104-106).
- Multilingual results come from multiple-choice benchmarks and may not capture natural writing quality, cultural nuance, or grammar in practical conversations (p. 233).

## Practical implications for Copilot users
- Use fast mode when the main bottleneck is waiting for long streamed answers: large refactor plans, test-failure triage, multi-file explanations, and iterative CLI debugging are the clearest fits.
- Expect the same model-quality and safety profile documented for Opus 4.8, not an intelligence upgrade or downgrade; the card's benchmark results should be read as model evidence, not speed-mode measurements.
- Faster turnarounds can make agentic loops feel easier to run, so keep the same safeguards: small permission grants, sandboxed tools, explicit checkpoints, and review before writes or external actions.
- Do not treat quicker output as a reason to trust untrusted tool results, webpages, issue comments, or repository files; prompt-injection defenses remain central for Copilot-style workflows.
- For high-stakes domains, keep human and policy review in place. The underlying card reports strong but imperfect safety behavior and surface-specific differences.
- Because this is a preview serving option, plan for standard Opus 4.8 to remain the comparison point when fast mode is unavailable or when reproducibility matters.

## Document coverage
This digest uses Anthropic's fast mode documentation at https://platform.claude.com/docs/en/build-with-claude/fast-mode only to scope the fast-mode serving claim; all page citations come from the Opus 4.8 system card. The card coverage spans the changelog, RSP conclusions, safeguards, agentic safety, alignment, welfare, and capabilities sections (pp. 2-237), while omitting most transcripts, appendix material, and unreproduced figure details. The card applies to the underlying Opus 4.8 model; it does not contain separate fast-mode evaluations.
