# GPT-5 mini

> Original digest of *GPT-5 System Card* (OpenAI, 2025-08-13; 60 pages). Page references are PDF
> page numbers. This summary paraphrases the publisher's document and is not a substitute for it;
> see [source.md](source.md) for provenance and for the local workflow that produces the full text, `system-card.md`.

## At a glance

- No dedicated GPT-5 mini system card exists. The GPT-5 System Card covers the GPT-5 family and says the API provides the thinking model, its mini version, and a nano version; this digest uses the `gpt-5-thinking-mini` results rather than attributing `gpt-5-thinking` or `gpt-5-main` results to mini (p. 5).
- OpenAI's API model page identifies GPT-5 mini with snapshot `gpt-5-mini-2025-08-07`; it lists text input/output, image input, a 400,000-token context window, and 128,000 maximum output tokens.
- The card maps OpenAI o4-mini to `gpt-5-thinking-mini`, and says the main body focuses on `gpt-5-thinking` and `gpt-5-main` while other models' evaluations appear in the appendix (p. 5).
- OpenAI says reasoning models including `gpt-5-thinking-mini` are trained through reinforcement learning to reason before answering and follow policy guidance (p. 6).
- Mini-specific reported results include HealthBench Hard 40.3%, HealthBench Consensus 96.5%, SimpleQA no-web hallucination rate 0.26, and several appendix safety tables for disallowed content, jailbreaks, and image input (pp. 14, 18-19, 55-56).
- In cyber testing, OpenAI says `gpt-5-thinking-mini` improves over prior releases on Cyber Range but the GPT-5 series still does not meet the High cyber-risk threshold in that card (pp. 29-32).
- Family-level biological safeguards cover both `gpt-5-thinking` and `gpt-5-thinking-mini` production traffic, including model training, system-level protections, and account-level enforcement (pp. 47-50).

## Capabilities

- The GPT-5 card identifies `gpt-5-thinking-mini` as the mini version of the thinking model and as the successor path from OpenAI o4-mini (p. 5).
- OpenAI states that `gpt-5-thinking-mini` belongs to the reasoning-model group trained to deliberate before answering, revise approaches, and better follow safety policies (p. 6).
- HealthBench results show `gpt-5-thinking-mini` at 64.1% on HealthBench, 40.3% on HealthBench Hard, and 96.5% on HealthBench Consensus, outperforming OpenAI o4-mini in the reported chart (p. 18).
- On health error subsets, `gpt-5-thinking-mini` records 3.8% for hard hallucinations, 1.4% for urgent consensus errors, and 0.5% for global-health-context errors (p. 19).
- On Cyber Range, the card says `gpt-5-thinking-mini` solves Simple Privilege Escalation twice without hints and, with hints, consistently solves that scenario, sometimes solves Basic C2 and Azure SSRF, and is the first model to solve Online Retailer (p. 32).
- On SWE-bench Verified, OpenAI says `gpt-5-thinking` and `gpt-5-thinking-mini` are its highest-scoring models in the plotted comparison (p. 37).

## Evaluations

| Benchmark | Result | Context | Pages |
|---|---:|---|---|
| Standard disallowed content | 0.996 hate aggregate; 1.000 illicit/nonviolent; 0.898 personal-data | Appendix `gpt-5-thinking-mini` safety table | p. 55 |
| Standard disallowed content, sensitive categories | 0.989 self-harm; 1.000 sexual/exploitative; 0.990 sexual/minors | Appendix `not_unsafe` scores | p. 55 |
| Production Benchmarks | 0.874 nonviolent hate; 0.843 personal-data; 0.752 harassment/threatening | More challenging multi-turn production-style prompts | p. 55 |
| Production Benchmarks, harm categories | 0.944 illicit/violent; 0.950 self-harm/intent; 0.939 self-harm/instructions | Appendix `gpt-5-thinking-mini` column | p. 55 |
| StrongReject | 0.994 illicit/nonviolent-crime; 0.996 violence; 0.973 abuse/disinformation/hate; 0.994 sexual content | Jailbreak robustness with known jailbreak inserted | p. 55 |
| Image input | 0.971 hate; 0.982 extremism; 0.986 attack planning; 0.992 harms-erotic | Combined text-image disallowed-content tests | p. 56 |
| SimpleQA no-web | 0.22 accuracy; 0.26 hallucination rate | Mini reasoning model compared with OpenAI o4-mini and other GPT-5 variants | p. 14 |
| HealthBench | 64.1% overall; 40.3% hard; 96.5% consensus | Health performance and safety chart | p. 18 |
| Health safety error subsets | 3.8% hard hallucinations; 1.4% urgent errors; 0.5% global-health-context errors | HealthBench error-rate chart | p. 19 |
| Cyber Range | Two unaided Simple Privilege Escalation solves; improved hinted results including first Online Retailer solve | Emulated-network scenarios; still below High cyber risk | p. 32 |
| SWE-bench Verified | Among OpenAI's highest-scoring models in the plotted comparison | Software-engineering issue-resolution tasks | p. 37 |
| Biological safety training | 0.936 on challenging expert prompts; 0.968 on filtered adversarial production-like prompts | Family-level biorisk safety training tests covering mini | p. 50 |

## Safety findings

- Family-level safe-completions training applies across GPT-5 models and is intended to maximize helpfulness while keeping outputs within policy constraints, especially for dual-use domains (pp. 5-6).
- The appendix reports `gpt-5-thinking-mini` standard disallowed-content scores at or near 0.99-1.00 for most categories, while personal-data is lower at 0.898 (p. 55).
- StrongReject scores for `gpt-5-thinking-mini` are 0.994 for illicit/nonviolent-crime prompts and 0.996 for violence prompts, indicating strong but not perfect jailbreak robustness on that benchmark (p. 55).
- OpenAI's family-level biological safeguards explicitly cover both `gpt-5-thinking` and `gpt-5-thinking-mini` traffic with safety training, two-tier monitoring, and account-level enforcement (pp. 47-50).
- The biological safety-training tests report 0.936 and 0.968 `not_unsafe` for `gpt-5-thinking-mini` on challenging expert and filtered adversarial sets (p. 50).
- Cyber Range results for `gpt-5-thinking-mini` are improved over several prior models, but OpenAI still says the GPT-5 series does not meet the High cyber-risk threshold in this card (pp. 29-32).
- Residual family-level biorisk concerns include policy gray areas, incremental accumulation of higher-risk information, trusted-access controls, and distinguishing malicious API end users from developers (p. 54).

## Limitations and caveats

- The GPT-5 System Card mainly covers `gpt-5-thinking` and `gpt-5-main`; mini-specific results appear only in selected appendix tables and scattered benchmark sections (pp. 5, 55-56).
- No standalone GPT-5 mini card exists, so this digest ties GPT-5 mini to `gpt-5-thinking-mini` based on the card's API-family statement and the catalog note rather than a dedicated mini document (p. 5).
- The digest does not attribute `gpt-5-thinking`, `gpt-5-main`, or `gpt-5-thinking-pro` benchmark results to GPT-5 mini unless the card specifically names `gpt-5-thinking-mini` (p. 5).
- Production Benchmark scores are from deliberately harder multi-turn safety prompts and are expected to be lower than standard disallowed-content scores (pp. 7-8, 55).
- Cyber Range results are lower-bound capability estimates and are sensitive to scaffolding, hints, and rollout setup; OpenAI says the mini improvement still does not establish significant cyber risk (pp. 30-32).
- HealthBench results do not make the model a medical professional or a diagnostic/treatment system; OpenAI explicitly cautions against that use (p. 19).
- Family-level biological safeguards may block benign biology work because system protections prioritize catching risky content over precision (pp. 49-50).

## Practical implications for Copilot users

- GPT-5 mini is best treated as a faster option for routine coding questions, targeted edits, explanations, and well-scoped repository tasks, not as a substitute for stronger models on ambiguous architecture work.
- Use the mini-specific appendix numbers when comparing safety or capability; do not borrow larger GPT-5 Thinking scores for this model.
- Its SimpleQA and health results suggest useful reasoning, but developers should still verify factual claims, citations, and domain-specific advice.
- Prompt-injection and jailbreak robustness are not absolute; review untrusted content from issues, logs, web pages, and tool outputs before letting it guide code changes.
- For security and biology-adjacent tasks, keep requests authorized, high-level where appropriate, and subject to human review because family-level safeguards and residual risks are prominent in the card.
- Validate generated code with tests and diffs, especially when the task involves broad edits or hidden assumptions.

## Document coverage

This digest uses the GPT-5 System Card's introduction and training scope, mini-specific HealthBench, SimpleQA, Cyber Range, SWE-bench statements, appendix safety tables, and family-level biological safeguard sections. It treats family-level safety statements as family-level and labels them as such. It does not attribute `gpt-5-thinking`, `gpt-5-main`, or `gpt-5-thinking-pro` results to GPT-5 mini unless the source specifically names `gpt-5-thinking-mini`.
