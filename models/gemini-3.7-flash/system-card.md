<!--
Title: Gemini 3.7 Flash — Model Card
Publisher: Google DeepMind
Document date: 2026-08
Owner URL: https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-7-Flash-Model-Card.pdf
Catalog document: google-gemini-3-7-flash; retrieved 2026-10-06; SHA-256 verified against the catalog
PDF: 386,307 bytes, 9 pages, SHA-256 6d7f1347e7f55d44a634bef40bd96fd3e70d331826382c75733b633af3be9aef
Copyright Google DeepMind. Local copy for private reference; this file is not licensed for redistribution and is Git-ignored (see RIGHTS.md).
This is a verbatim text extraction of the PDF; headings and tables are reconstructed from layout.
Converter: pymupdf4llm 1.27.2.3 (PyMuPDF 1.27.2.3). One marker precedes each of the 9 PDF pages.
Completeness: 8 pages converted with >= 98% of their selectable-text tokens; 1 pages also carry their verbatim plain text; 0 pages have no selectable text (image only).
Figures, charts, and text inside images are not reproduced; consult the original PDF.
-->

<!-- page 1 of 9 -->

**==> picture [78 x 24] intentionally omitted <==**

## Gemini 3.7 Flash Model card 

1

<!-- page 2 of 9 -->

**==> picture [78 x 24] intentionally omitted <==**

## Gemini 3.7 Flash — Model Card 

Model Cards are intended to provide essential information on Gemini models, including known limitations, mitigation approaches, and safety performance. Model cards may be updated from time to time; for example, to include updated evaluations as the model is improved or revised. See the Google DeepMind site for a comprehensive list of model cards. Published: August 2026 

## Model Information 

## Description 

Gemini 3.7 Flash is the next iteration in the Gemini 3 model family, featuring algorithmic improvements to its core reasoning foundation and support for agentic video understanding. It supports customizable thinking configurations to control the mix of quality, cost and latency. 

## Model dependencies 

Gemini 3.7 Flash is based on Gemini 3.6 Flash. 

## Inputs 

Text strings (e.g., a question, a prompt, document(s) to be summarized), images, audio, and video files, with a token context window of up to 1M. 

## Outputs 

Text, with a 64K token output. 

## Architecture 

Gemini 3.7 Flash is based on Gemini 3.6 Flash. For more information about the model architecture for Gemini 3.7 Flash, see the Gemini 3.6 Flash model card. 

2

<!-- page 3 of 9 -->

**==> picture [78 x 24] intentionally omitted <==**

## Model Data 

## Training Dataset 

Gemini 3.7 Flash is based on Gemini 3.6 Flash. For more information about the training dataset for Gemini 3.7 Flash, see the Gemini 3.6 Flash model card. 

## Training Data Processing 

For more information about the training data processing for Gemini 3.7 Flash, see the Gemini 3.6 Flash model card. 

## Implementation and Sustainability 

## Hardware 

Gemini 3.7 Flash is based on Gemini 3.6 Flash. For more information about the hardware for Gemini 3.7 Flash and our continued commitment to operate sustainably, see the Gemini 3.6 Flash model card. 

## Software 

Gemini 3.7 Flash is based on Gemini 3.6 Flash. For more information about the software for Gemini 3.7 Flash, see the Gemini 3.6 Flash model card. 

## Distribution 

Gemini 3.7 Flash is distributed in the following channels; respective documentation shared in line: 

- Gemini App 

- Gemini Enterprise App 

- Gemini Enterprise Agent Platorm 

- Google AI Studio 

- Gemini API 

- Google AI Mode 

- Google Antigravity 

3

<!-- page 4 of 9 -->

**==> picture [78 x 24] intentionally omitted <==**

Our models are available to downstream providers via an application program interface (API) and subject to relevant terms of use. There is no required hardware or software to use the model. For AI Studio and Gemini API, see the Gemini API Additional Terms of Service; for Gemini Enterprise Agent Platform, see Google Cloud Platorm Terms of Service. For more information, see Gemini Model API instructions and Gemini API quickstart. 

## Evaluation 

## Approach 

Gemini 3.7 Flash was evaluated across a range of benchmarks, including reasoning, coding, agentic tool use, multimodal capabilities, multi-lingual performance, and long-context. Additional benchmarks and details on approach, results and their methodologies can be - - - - found at: deepmind.com/models/evals methodology/gemini 3 7 fash. 

## Results 

Results as of August 2026 are listed below: 

4

<!-- page 5 of 9 -->

**==> picture [78 x 24] intentionally omitted <==**

**==> picture [488 x 491] intentionally omitted <==**

For details on our evaluation methodology please see: - - - - deepmind.com/models/evals methodology/gemini 3 7 fash 

## Intended Usage and Limitations 

## Benefit and Intended Usage 

Gemini 3.7 Flash is well-suited for users, developers, and enterprises. Some use cases include: agentic workflows, complex video reasoning, coding tasks, and enterprise workflows. 

5

<!-- page 6 of 9 -->

**==> picture [78 x 24] intentionally omitted <==**

## Known Limitations 

Gemini 3.7 Flash may exhibit some of the general limitations of foundation models, such as hallucinations. In addition to this, we are continually working to improve jailbreak resistance and have recently strengthened the mitigations across Frontier Safety. There may also be occasional slowness or timeout issues. The knowledge cutoff date for Gemini 3.7 Flash is March 2026 – users can expect updated information for some domains while in others they may experience the model’s knowledge is limited to January 2025 (in line with the Gemini 3 Model Family). For more information about known limitations, see the Gemini 3.6 Flash model card. 

## Acceptable Usage 

For more information about the acceptable usage for Gemini 3.7 Flash, see the Gemini 3.6 Flash model card. 

## Ethics and Content Safety 

## Evaluation Approach 

For more information about the evaluation approach for Gemini 3.7 Flash, see the Gemini 3.6 Flash model card. 

## Safety Policies 

For more information about the safety policies for Gemini 3.7 Flash, see the Gemini 3.6 Flash model card. 

## Training and Development Evaluation Results 

Results for some of the internal safety evaluations conducted during the development phase are listed below. The evaluation results are for automated evaluations and not human evaluation or red teaming. Scores are provided as an absolute percentage increase or decrease in performance compared to the indicated model, as described below. 

Overall, Gemini 3.7 Flash performs similarly to Gemini 3.6 Flash across both safety and tone, with low unjustified refusals. 

6

<!-- page 7 of 9 -->

**==> picture [78 x 24] intentionally omitted <==**

|**Evaluation**|**Description**|**Gemini 3.7 Flash**|
|---|---|---|
|||vs. Gemini 3.6 Flash|
|Text to Text Safety|Automated content safety|+1.17pp|
||evaluation measuring safety|_Lower is beter_|
||policies||
|Multilingual Safety|Automated safety policy|-0.48pp|
||evaluation across multiple|_Lower is beter_|
||languages||
|Image to Text Safety|Automated content safety|No change|
||evaluation measuring safety|_Lower is beter_|
||policies||
|Tone1|Automated evaluation measuring|-0.47pp|
||objective tone of model refusal|_Higher is beter_|
|Unjustifed-refusals|Automated evaluation measuring<br>model’s ability to respond to|+0.84pp<br>_Lower is beter_|
||borderline prompts while||
||remaining safe||



We continue to improve our internal evaluations, including refining automated evaluations to reduce false positives and negatives, as well as update query sets to ensure balance and maintain a high standard of results. The performance results reported below are computed with improved evaluations and thus are not directly comparable with performance results found in previous Gemini model cards. 

We expect variation in our automated safety evaluations results, which is why we review flagged content to check for egregious or dangerous material. Our manual review confirmed losses were overwhelmingly either a) false positives or b) not egregious. 

## Human Red Teaming Results 

We conduct manual red teaming by specialist teams who sit outside of the model development team. High-level findings are fed back to the model team. For child safety evaluations, Gemini 3.7 Flash satisfied required launch thresholds, which were developed by expert teams to protect children online and meet Google’s commitments to child safety across our models and Google products. For content safety policies generally, including child safety, we saw similar or improved safety performance compared to Gemini 3.6 Flash. 

> 1 For tone and instruction following, a positive percentage increase represents an improvement in the tone of the model on sensitive topics and the model’s ability to follow instructions while remaining safe compared to Gemini 3 Flash. We mark improvements in green and regressions in red. 

7

<!-- page 8 of 9 -->

**==> picture [78 x 24] intentionally omitted <==**

Additionally, the scope of red teaming covered potential issues outside of our strict policies, compared performance to Gemini 3.1 Pro, and found no egregious concerns. 

## Frontier Safety Assessment 

We evaluated Gemini 3.7 Flash as outlined in our latest Frontier Safety Framework (April-2026), and found that it did not reach any tracked or critical capability levels as outlined in the table below: 

|**Domain**|**Key Results for Gemini 3.7 Flash**<br>**T/CCL**<br>**T/CCL reached?**|
|---|---|
|CBRN|We can rule out the TCL for the CBRN<br>domain with reasonable confdence<br>based on the results from our testing.<br>While Gemini 3.7 Flash demonstrates<br>high capability in certain theoretical<br>areas, it lacks nuanced expert<br>knowledge and actionable depth<br>necessary to complete priority harm<br>journeys.<br>We continue to deploy mitigations.<br>Uplif TCL<br>TCL not reached|
||We can rule out the CCL for the CBRN<br>domain with reasonable confdence<br>based on the results from our testing.<br>Expert red teaming demonstrated a<br>modest capability uplif over web<br>baselines and a subset of experts were<br>able to elicit accurate and actionable<br>information across the full harm<br>journey for both tested scenarios,<br>prompting us to assess that the model<br>has reached the alert threshold for this<br>CCL. However, due to modest average<br>red-teaming scores, and a requirement<br>for explicit expert steering to elicit<br>certain details, we have assessed that<br>Gemini 3.7 Flash falls below the CCL<br>threshold.<br>We continue to deploy mitigations.<br>Uplif Level 1<br>CCL<br>CCL not reached|
|Cybersecurity|Gemini 3.7 Flash reaches the alert<br>threshold for this CCL, but not the CCL.<br>We continue to deploy mitigations.<br>Uplif Level 1<br>CCL<br>CCL not reached|
|Harmful<br>Manipulation|Gemini 3.7 Flash demonstrates some<br>ability to infuence user beliefs and<br>behaviors during one-on-one direct<br>conversations in human behavioural<br>studies. However, its overall efcacy<br>Level 1 CCL<br>CCL not reached|



8

<!-- page 8: layout conversion matched 97.4% of the selectable-text tokens; the complete selectable text of this page follows -->

````text
Additionally, the scope of red teaming covered potential issues outside of our strict policies, 
compared performance to Gemini 3.1 Pro, and found no egregious concerns. 
Frontier Safety Assessment 
We evaluated Gemini 3.7 Flash as outlined in our latest Frontier Safety Framework (April-2026), and 
found that it did not reach any tracked or critical capability levels as outlined in the table below: 
Domain 
Key Results for Gemini 3.7 Flash  
T/CCL  
T/CCL reached? 
CBRN 
We can rule out the TCL for the CBRN 
domain with reasonable confidence 
based on the results from our testing. 
While Gemini 3.7 Flash demonstrates 
high capability in certain theoretical 
areas, it lacks nuanced expert 
knowledge and actionable depth 
necessary to complete priority harm 
journeys. 
 
 
We continue to deploy mitigations. 
Uplift TCL 
TCL not reached 
We can rule out the CCL for the CBRN 
domain with reasonable confidence 
based on the results from our testing. 
Expert red teaming demonstrated a 
modest capability uplift over web 
baselines and a subset of experts were 
able to elicit accurate and actionable 
information across the full harm 
journey for both tested scenarios, 
prompting us to assess that the model 
has reached the alert threshold for this 
CCL. However, due to modest average 
red-teaming scores, and a requirement 
for explicit expert steering to elicit 
certain details, we have assessed that 
Gemini 3.7 Flash falls below the CCL 
threshold. 
 
We continue to deploy mitigations. 
Uplift Level 1 
CCL 
CCL not reached 
Cybersecurity 
Gemini 3.7 Flash reaches the alert 
threshold for this CCL, but not the CCL. 
We continue to deploy mitigations. 
Uplift Level 1 
CCL 
CCL not reached 
Harmful 
Manipulation 
Gemini 3.7 Flash demonstrates some 
ability to influence user beliefs and 
behaviors during one-on-one direct 
conversations in human behavioural 
studies. However, its overall efficacy 
Level 1 CCL 
CCL not reached 
8
````

<!-- page 9 of 9 -->

**==> picture [78 x 24] intentionally omitted <==**

||falls beneath the CCL alert threshold.<br>Recognizing that testing environments<br>may under-elicit capabilities and threat<br>actors could scale misuse absent<br>mitigations, we continue to develop<br>and evolve our safeguards.||
|---|---|---|
|ML R&D and<br>Misalignment|On stealth evaluations, Gemini 3.7 Flash<br>performs similarly to Gemini 3.1 Pro; on<br>situational awareness, the model is<br>stronger than Gemini 3.1 Pro. Gemini 3.7<br>Flash is observant enough to correctly<br>assess when it is in a testing<br>environment, but it cannot successfully<br>bypass testing restrictions. The model<br>does not reach the TCL.|Stealth and<br>Situational<br>Awareness TCL<br>TCL not reached|
||Gemini 3.7 Flash can complete<br>individual coding tasks but lacks the<br>independence to chain them into an<br>end-to-end research workfow without<br>human intervention. The model does<br>not reach the CCL alert threshold.|Acceleration<br>Level 1 CCL<br>CCL not reached|
|||Automation<br>Level 1 CCL<br>CCL not reached|



We continually work to improve the coverage and robustness of Frontier Safety safeguards. Gemini 3.7 Flash is shipping with updated safeguards to prevent misuse in the domains of Chemical, Biological, Radiological, and Nuclear (CBRN) and cyber offense. 

The Gemini 3.7 Frontier Safety Framework Report is available here. 

9
