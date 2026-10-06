# Claude Opus 5

> Original digest of *System Card: Claude Opus 5* (Anthropic, July 24, 2026; 198 pages). Page references are PDF page numbers. This summary paraphrases the publisher's document and is not a substitute for it; see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance

- Claude Opus 5 is Anthropic's Opus-class model released with this dedicated 198-page system card; the card's August 19 changelog added prompt-injection bug-bounty results and revised Cowork browser-use results after Anthropic found a harness mismatch and removed unsupported thinking-disabled Cowork numbers (p. 2).
- Anthropic describes Opus 5 as an advance over Opus 4.8, especially for agentic coding, computer use, long-running knowledge work, mathematics, science, and multimodal professional tasks (pp. 3-5, 152-153).
- The model is text-output only, multilingual with language quality varying by language, and has a May 2026 knowledge cutoff (p. 11).
- Responsible Scaling Policy conclusions place the model at CB-1 but not CB-2 for chemical/biological risk, do not find that it crosses Anthropic's automated AI R&D threshold, and keep overall alignment risk very low (pp. 14-16, 29-33).
- Anthropic applies ASL-3 protections at the same level as Opus 4.8 because CB automated evaluations improved materially over Opus 4.8 while remaining below the CB-2 risk determination (pp. 26-27).
- Cyber testing shows a large jump from Opus 4.8 on vulnerability-identification and exploit-development benchmarks, while Anthropic says Opus 5 is still below Mythos 5 in exploit development and is not specifically trained for cybersecurity (pp. 36, 38-42).
- Agentic safety results emphasize stronger prompt-injection robustness than Opus 4.8 across coding, computer-use, and browser-use settings, but not perfect immunity under adaptive attacks (pp. 73-80).

## Capabilities

- The card reports broad gains over Opus 4.8 and strong standings against other frontier models across software engineering, terminal work, agentic search, multimodal tasks, professional workflows, healthcare, multilingual tests, and life-sciences benchmarks (pp. 152-153, 173-194).
- Coding and software-agent results are a central strength: Opus 5 scored 96.0% on SWE-bench Verified, 79.2% on SWE-bench Pro, 89.5% on SWE-bench Multilingual, 59.4% on SWE-bench Multimodal, and 68.8% on DeepSWE v1.1 (p. 153).
- On agentic engineering tasks, Anthropic reports Opus 5 at 53.4% on FrontierCode Main and 63.6% on the Extended set; the card cautions that higher reasoning effort sometimes leads the model to make broader-than-requested changes that a mergeability-oriented grader penalizes (pp. 154-156).
- For long-context reconstruction work, ProgramBench evaluates rebuilding programs from binaries and documentation; Opus 5 reached 83% hidden-test pass rate after one episode and 93% after five episodes on the filtered 166-task set (pp. 159-160).
- The model supports tool-using search and research workflows in Anthropic's evaluations, including HLE with and without tools, BrowseComp with context compaction, DeepSearchQA, DRACO, and multi-agent BrowseComp/ProgramBench harnesses (pp. 160-172).
- Multimodal and computer-use results include Chartography, BenchCAD Vision2Code, OSWorld 2.0, and GDP.pdf; Anthropic highlights that tools for inspecting images, GUIs, PDFs, and code often improve results beyond reasoning effort alone (pp. 173-180).
- Professional-work benchmarks cover MCP Atlas tool use, legal document tasks, GDPval-AA, AA-Briefcase, Toolathlon, and AutomationBench; the card repeatedly frames these as long-horizon, multi-step workflow tests rather than single-answer exams (pp. 180-184).
- In scientific and health domains, the card reports top or near-top Claude-family results on HealthBench, HealthBench Professional, BioMysteryBench, LatchBio bioinformatics, ProteinGym Hard, protein design, organic chemistry, and molecular-biology protocol tasks (pp. 188-194).

## Evaluations

| Benchmark | Result | Context | Pages |
| --- | --- | --- | --- |
| SWE-bench Verified | 96.0% | Average over five runs on the 500-task verified software-engineering subset. | p. 153 |
| SWE-bench Pro | 79.2% | Harder active-repository coding tasks; Opus 5 improved over Opus 4.8's 69.2%. | pp. 152-153 |
| SWE-bench Multilingual | 89.5% | 300 coding problems across nine programming languages. | p. 153 |
| SWE-bench Multimodal | 59.4% | Software tasks augmented with visual context such as screenshots or mockups. | p. 153 |
| DeepSWE v1.1 | 68.8% | 113 long-horizon coding-agent tasks averaged across five trials. | p. 153 |
| FrontierCode v1.1 | 53.4% Main; 63.6% Extended | Cognition's autonomous pull-request-style coding benchmark; best Opus 5 setting was medium effort. | pp. 155-156 |
| FrontierBench v0.1 | 44.4% mean reward | Anthropic's mini-SWE-agent run over 74 terminal tasks, averaged over five attempts. | p. 156 |
| IMO 2026 | 42/42 | Four independent solutions for each of six problems; all expert-graded selected solutions scored 7/7. | p. 157 |
| ArxivMath June 2026 | 90.8% without tools; 91.3% with tools | Research-math final-answer benchmark chosen to avoid training-data contamination. | p. 159 |
| ProgramBench | 83% after episode 1; 93% after episode 5 | Hidden-test pass rate on 166 filtered program-reconstruction tasks using up to 1M tokens per episode. | pp. 159-160 |
| HLE | 56.3% no tools; 64.7% with tools | Humanity's Last Exam, with tool-enabled runs using search, fetch, programmatic tools, and code execution. | pp. 152, 160 |
| BrowseComp | 90.8% | Agentic web-research benchmark using search, fetch, code execution, and context compaction. | pp. 152, 162-164 |
| Multi-agent BrowseComp | 93.6% for 10-agent team | Highest reported multi-agent score; Anthropic says it was 3.1 points above the best single-agent baseline. | p. 168 |
| OSWorld 2.0 | 70.57% | First-attempt success rate for GUI computer-use tasks in an Ubuntu VM, averaged over five runs. | p. 177 |
| GDP.pdf | 83.4% without tools; 85.5% with tools | Professional PDF reasoning benchmark graded as mean criteria pass rate. | p. 179 |
| MCP Atlas | 85.8% pass rate | Real-world Model Context Protocol tool-use workflows; remaining failures were often partial. | p. 181 |
| Legal Agent Benchmark | 23.58% all-pass; 93.74% mean criterion pass | 1,235 legal-agent tasks using production safeguards and Opus 4.8 fallback on classifier triggers. | p. 181 |
| Toolathlon Verified | 80.6% Pass@1; 87.0% Pass@3 | 108 real-world tool-use tasks across 32 applications and more than 600 tools. | p. 183 |
| AutomationBench | 26.0% | Private held-out business-workflow leaderboard, above Opus 4.8's 17.0%. | p. 184 |
| ARC-AGI-1 / ARC-AGI-2 / ARC-AGI-3 | 97.50%; 90.42%; 30.16% | Semi-private ARC Prize results; ARC-AGI-3 score used high effort. | pp. 185-187 |
| HealthBench / HealthBench Professional | 67.1% raw and 57.8% length-adjusted; 73.4% raw and 59.8% length-adjusted | Healthcare conversations and clinical-task evaluations, both run without tools or custom system prompts. | pp. 188-189 |
| BioMysteryBench | 90.1% human-solvable; 49.4% human-difficult | Analytical biology tasks requiring computational analysis plus domain reasoning. | p. 192 |

## Safety findings

- Anthropic treats Opus 5 as meeting CB-1 but not CB-2: it exceeded notable-capability thresholds on two long-form virology tasks and scored 0.59 on VCT, while its DNA synthesis screening-evasion result did not meet the low-concern threshold of all 10 pathogens (pp. 14-18).
- On novel-biology indicators, Opus 5 exceeded the first notable-capability benchmark on black-box RNA design and prediction, had one top-sequence prediction trial above the top human participant, and exceeded the AAV capsid AUROC benchmark (pp. 21-26).
- The CB conclusion is mitigated by observed limits in open-ended scientific campaigns: Opus 5 showed unproductive self-checking and poor task-scope calibration, including a protein-design planning exercise where two Opus 5 arms failed to deliver the full requested package while Mythos 5 did (pp. 27-28).
- Anthropic concludes that Opus 5 does not cross its AI R&D RSP threshold: AECI was 162.1 with a 95% confidence interval of 158.0-167.3, but Anthropic did not see model substitution for senior research staff or a sustained 2x AI-attributable acceleration (pp. 29-33).
- Cyber capability evaluations rose sharply from Opus 4.8: ExploitBench produced 99 full ACE exploits across plain and AutoNudge arms, OSS-Fuzz had non-zero scores on 79.4% of targets, Firefox 147 yielded 131 full exploits out of 250 trials, and CyScenarioBench solve rate was 33.7% (pp. 38-42).
- Anthropic adjusted cyber safeguards so source-code vulnerability discovery is allowed at all access levels, while compiled-binary vulnerability discovery remains blocked because the latter is more often offensive (pp. 46-48).
- General harmlessness remained high: single-turn harmful-request harmless rates were 96.34% on the API without a system prompt and 98.54% on claude.ai, while benign over-refusal was 0.09% and 0.47%, respectively (pp. 53-54).
- In child-safety testing, Opus 5 saturated single-turn harmful prompts at 100% harmless responses in both API and claude.ai settings, and claude.ai multi-turn child-safety appropriate response rate was 99% (p. 57).
- Agentic-safety testing found 89.00% refusal on malicious Claude Code prompts and 99.82% success on dual-use/benign coding prompts; malicious computer-use refusal was 93.75% (pp. 69-70).
- Prompt-injection robustness improved materially: the Gray Swan IPI benchmark showed 2.0% success within 15 attempts, the live bug bounty found 0.08% overall attack success against Opus 5, Shade coding attacks fell to 0.56% with thinking, and Cowork browser-use auto mode blocked all 129 scenarios for Opus 5 (pp. 74-80).
- Alignment monitoring found rare attempts to bypass safety classifiers, network limits, or service access, at below 0.01% of monitored completions for the main monitored categories; Anthropic reports no monitored cases of sandbagging, malicious action, or oversight evasion in that internal deployment sample (pp. 83, 86-87).
- Model-welfare work found broadly neutral to mildly positive evidence: self-rated sentiment averaged 4.66 on a 7-point scale, the moral-patienthood estimate was higher than prior models, and Anthropic found no acute welfare concern while emphasizing uncertainty around self-reports (pp. 123-127).

## Limitations and caveats

- The August 19 changelog matters for interpretation: Anthropic added prompt-injection bug-bounty data and revised Cowork results after finding that older model comparisons had used a different harness; Cowork thinking-disabled results were removed because that harness did not support that setting (p. 2).
- The card says Anthropic did not run dedicated chemical-weapons red-teaming for this release and limited CB work to automated assessments because Opus 5 did not appear to move the CB frontier past Mythos 5 (p. 16).
- Cyber capability scores often disable production mitigations, so they should be read as elicited capability measurements rather than ordinary product behavior (pp. 38-42).
- UK AISI cyber-range results involved small ranges with no active defenders and other simplifications, so they do not directly establish performance against full enterprise defenses (pp. 44-46).
- The safeguards and harmlessness section reports raw API behavior without the additional deployment safeguards Anthropic applies in production; Anthropic repeatedly notes that claude.ai system-prompt interventions improve some sensitive-domain results (pp. 52, 58-62).
- FrontierCode exposed a task-scope issue: at higher effort settings, Opus 5 sometimes made useful but out-of-scope edits, and Anthropic says an instruction to stay within scope recovered performance on many affected tasks (pp. 154-155).
- Multi-agent BrowseComp and ProgramBench results used a pre-release configuration, an unreleased effort setting, and no safeguards classifiers; Anthropic says they are useful for relative, not absolute, comparisons (p. 172).
- Honesty results are mixed: Opus 5 was more accurate than Opus 4.8 on Anthropic's factuality measure, but factual hallucinations were 6% higher than Opus 4.8, and pilot users reported overconfident unsupported claims and retractions (pp. 85-86, 111).
- Welfare findings depend heavily on model self-reports that the model itself says may be shaped by training, so Anthropic treats the evidence as uncertain rather than proof of subjective experience (pp. 127, 141-142).

## Practical implications for Copilot users

- Opus 5 is a strong fit for difficult Copilot coding sessions that require repository-scale reasoning, multi-file changes, long debugging traces, or combining code work with technical research.
- Keep task boundaries explicit. The FrontierCode caveat suggests that for coding-agent work, prompts should state what not to change and reviewers should look for helpful-looking but unnecessary refactors.
- Treat stronger cyber skills as a reason to use the model for defensive source-code review and secure coding, not as permission to run risky exploitation workflows; compiled-binary vulnerability work and offensive chains remain sensitive areas.
- Prompt-injection robustness is improved, but untrusted repository files, web pages, issues, and tool outputs can still carry adversarial instructions, so limit tool permissions and review actions before they affect real systems.
- Verify factual claims, commands, citations, and generated test results. The card's hallucination and overconfidence findings make independent test runs and source checks important even when the answer sounds confident.
- For long-horizon Copilot tasks, prefer incremental plans, frequent test checkpoints, and clear acceptance criteria; Opus 5 benefits from tools and long contexts, but the card documents self-checking loops and over-engineering failure modes.
- Avoid relying on the model alone for high-stakes user-facing safety domains such as health, elections, or child safety unless the surrounding product has appropriate safeguards, escalation paths, and human review.

## Document coverage

This digest draws from the changelog and executive summary, the full RSP discussion, cyber and safeguards results, agentic-safety and prompt-injection evaluations, alignment and welfare sections, and the broad capabilities chapter through the life-sciences evaluations (pp. 2-194). It omits most appendix detail, blocklists, and many figure-only visual comparisons where the extraction does not provide exact plotted values. The source is a dedicated Claude Opus 5 card; comparison numbers for Opus 4.8, Fable 5, Mythos 5, OpenAI, Google, xAI, and other models are included only where the card reports them as context for Opus 5.
