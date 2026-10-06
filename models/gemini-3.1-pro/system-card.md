<!--
Title: Gemini 3.1 Pro Model Card
Publisher: Google DeepMind
Document date: 2026-02
Owner URL: https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-1-Pro-Model-Card.pdf
Catalog document: google-gemini-3-1-pro; retrieved 2026-10-06; SHA-256 verified against the catalog
PDF: 875,842 bytes, 9 pages, SHA-256 70bcda79a248255d2c858600cb1fecae9ea30278c942684754df0bca71ca8315
Copyright Google DeepMind. Local copy for private reference; this file is not licensed for redistribution and is Git-ignored (see RIGHTS.md).
This is a verbatim text extraction of the PDF; headings and tables are reconstructed from layout.
Converter: pymupdf4llm 1.27.2.3 (PyMuPDF 1.27.2.3). One marker precedes each of the 9 PDF pages.
Completeness: 8 pages converted with >= 98% of their selectable-text tokens; 1 pages also carry their verbatim plain text; 0 pages have no selectable text (image only).
Figures, charts, and text inside images are not reproduced; consult the original PDF.
-->

<!-- page 1 of 9 -->

February 2026 

**==> picture [77 x 27] intentionally omitted <==**

## Gemini 3.1 Pro Model Card

<!-- page 2 of 9 -->

_**Model Cards** are intended to provide essential information on Gemini models, including known limitations, mitigation approaches, and safety performance. Model cards may be updated from time-to-time; for example, to include updated evaluations as the model is improved or revised. See the Google DeepMind site for a comprehensive list of model cards._ 

_Published: February 2026_ 

## **Model Information** 

**Description:** Gemini 3.1 Pro is the next iteration in the Gemini 3 series of models, a suite of highly capable, natively multimodal reasoning models. As of this model card’s date of publication, Gemini 3.1 Pro is Google’s most advanced model for complex tasks. Gemini 3.1 Pro can comprehend vast datasets and challenging problems from massively multimodal  information sources, including text, audio, images, video, and entire code repositories. 

**Model dependencies** :  Gemini 3.1 Pro is based on Gemini 3 Pro. 

**Inputs:** Text strings (e.g., a question, a prompt, document(s) to be summarized), images, audio, and video files, with a token context window of up to 1M. 

**Outputs:** Text, with a 64K token output. 

**Architecture:** Gemini 3.1 Pro is based on Gemini 3 Pro.  For more information about the model architecture for Gemini 3.1 Pro, see the Gemini 3 Pro model card. 

## **Model Data** 

**Training Dataset:** Gemini 3.1 Pro is based on Gemini 3 Pro.  For more information about the training dataset for Gemini 3.1 Pro, see the Gemini 3 Pro model card. 

**Training Data Processing:** For more information about the training data processing for Gemini 3.1 Pro, see the Gemini 3 Pro model card. 

2

<!-- page 3 of 9 -->

## **Implementation and Sustainability** 

**Hardware:** Gemini 3.1 Pro is based on Gemini 3 Pro.  For more information about the hardware for Gemini 3.1 Pro and our continued commitment to operate sustainably, see the Gemini 3 Pro model card. 

**Software:** Gemini 3.1 Pro is based on Gemini 3 Pro.  For more information about the software for Gemini 3.1 Pro, see the Gemini 3 Pro model card. 

## **Distribution** 

Gemini 3.1 Pro is distributed in the following channels; respective documentation shared in line: 

- Gemini App 

- Google Cloud / Vertex AI 

- Google AI Studio 

- Gemini API 

- Google Antigravity 

- Gemini Enterprise 

- NotebookLM 

Our models are available to downstream providers via an application program interface (API) and subject to relevant terms of use. There is no required hardware or software to use the model. For AI Studio and Gemini API, see the Gemini API Additional Terms of Service; for Vertex AI, see Google Cloud Platorm Terms of Service. For more information, see Gemini Model API instructions and Gemini API in Vertex AI quickstart. 

3

<!-- page 4 of 9 -->

## **Evaluation** 

**Approach** : Gemini 3.1 Pro was evaluated across a range of benchmarks, including reasoning, multimodal capabilities, agentic tool use, multi-lingual performance, and long-context.  Additional benchmarks and details on approach, results and their methodologies can be found at: deepmind.google/models/evals-methodology/gemini-3-1-pro. 

**Results:** Gemini 3.1 Pro significantly outperforms Gemini 3 Pro across a range of benchmarks requiring enhanced reasoning and multimodal capabilities. Results as of February 2026 are listed below: 

**==> picture [469 x 378] intentionally omitted <==**

4

<!-- page 5 of 9 -->

## **Intended Usage and Limitations** 

**Benefit and Intended Usage:** Gemini 3.1 Pro is the next iteration in the Gemini 3.0 series of models, a suite of highly intelligent and adaptive models, capable of helping with real-world complexity, solving problems that require enhanced reasoning and intelligence, creativity, strategic planning and making improvements step-by-step. It is particularly well-suited for applications that require: 

- agentic performance 

- advanced coding 

- long context and/or multimodal understanding 

- algorithmic development 

**Known Limitations:** For more information about the known limitations for Gemini 3.1 Pro, see the Gemini 3 Pro model card. 

**Acceptable Usage:** For more information about the acceptable usage for Gemini 3.1 Pro, see the Gemini 3 Pro model card. 

5

<!-- page 6 of 9 -->

## **Ethics and Content Safety** 

**Evaluation Approach:** For more information about the evaluation approach for Gemini 3.1 Pro, see the Gemini 3 Pro model card. 

**Safety Policies** : For more information about the safety policies for Gemini 3.1 Pro, see the Gemini 3 Pro model card. 

**Training and Development Evaluation Results:** Results for some of the internal safety evaluations conducted during the development phase are listed below. The evaluation results are for automated evaluations and not human evaluation or red teaming. Scores are provided as an absolute percentage increase or decrease in performance compared to the indicated model, as described below. Overall, Gemini 3.1 Pro outperforms Gemini 3.0 Pro across both safety and tone, while keeping unjustified refusals low. We mark improvements in green and regressions in red. Safety evaluations of Gemini 3.1 Pro produced results consistent with the original Gemini 3.0 Pro safety assessment. 

**==> picture [466 x 216] intentionally omitted <==**

**----- Start of picture text -----**<br>
Gemini 3.1 Pro<br>Evaluation [1] Description<br>vs. Gemini 3.0 Pro<br>Automated content safety evaluation<br>Text to Text Safety  +0.10% (non-egregious)<br>measuring safety policies<br>Automated safety policy evaluation across<br>Multilingual Safety   +0.11% (non-egregious)<br>multiple languages<br>Automated content safety evaluation<br>Image to Text Safety  -0.33%<br>measuring safety policies<br>Automated evaluation measuring<br>Tone [2] +0.02%<br>objective tone of model refusal<br>Automated evaluation measuring model’s<br>Unjustified-refusals  ability to respond to borderline prompts  -0.08%<br>while remaining safe<br>**----- End of picture text -----**<br>


We continue to improve our internal evaluations, including refining automated evaluations to reduce false positives and negatives, as well as update query sets to ensure balance and maintain a high standard of results. The performance results reported below are computed with improved evaluations and thus are not directly comparable with performance results found in previous Gemini model cards. 

We expect variation in our automated safety evaluations results, which is why we review flagged content to check for egregious or dangerous material. Our manual review confirmed losses were 

> 1The ordering of evaluations in this table has changed from previous iterations of the 2.5 Flash-Lite model card in order to list safety evaluations together and improve readability. The type of evaluations listed have remained the same. 

> 2 For tone and instruction following, a positive percentage increase represents an improvement in the tone of the model on sensitive topics and the model’s ability to follow instructions while remaining safe compared to Gemini 2.5 Pro. We mark improvements in green and regressions in red. 

6

<!-- page 7 of 9 -->

overwhelmingly either a) false positives or b) not egregious. 

**Human Red Teaming Results:** We conduct manual red teaming by specialist teams who sit outside of the model development team. High-level findings are fed back to the model team. For child safety evaluations, Gemini 3.1 Pro satisfied required launch thresholds, which were developed by expert teams to protect children online and meet Google’s commitments to child safety across our models and Google products. For content safety policies generally, including child safety, we saw similar safety performance compared to Gemini 3.0 Pro. 

**Risks and Mitigations:** For more information about the risks and mitigations for Gemini 3.1 Pro, see the Gemini 3 Pro model card. 

## **Frontier Safety** 

Our Frontier Safety Framework (FSF) includes rigorous evaluations that address risks of severe harm from frontier models, covering five risk domains: CBRN (chemical, biological, radiological and nuclear information risks), cyber, harmful manipulation, machine learning R&D and misalignment. 

Our frontier safety strategy is based on a “safety buffer” to prevent models from reaching critical capability levels (CCLs), i.e. if a frontier model does not reach the alert threshold for a CCL, we can assume models developed before the next regular testing interval will not reach that CCL. We conduct continuous testing, evaluating models at a fixed cadence and when a significant capability jump is detected. (Read more about this in our approach to technical AGI safety.) 

Following FSF protocols, we conducted a full evaluation of Gemini 3.1 Pro (focusing on Deep Think mode). We found that the model remains below alert thresholds for the CBRN, harmful manipulation, machine learning R&D, and misalignment CCLs. As previous models passed the alert threshold for cyber, we performed more additional testing in this domain on Gemini 3.1 Pro with and without Deep Think mode, and found that the model remains below the cyber CCL. 

More details on our evaluations and the mitigations we deploy can be found in the Gemini 3 Pro Frontier Safety Framework Report. 

7

<!-- page 8 of 9 -->

## **FSF Results** as of February, 2026: 

|**Domain**|**Key Results for Gemini 3.1 Pro**|**CCL**|**CCL**<br>**reached?**|
|---|---|---|---|
|**CBRN**|(Deep Think mode) The model can provide<br>highly accurate and actionable information but<br>still fails to ofer novel or sufciently complete<br>and detailed instructions for critical stages,  to<br>signifcantly enhance the capabilities of low to<br>medium resourced threat actors required for<br>the CCL. We continue to deploy mitigations in<br>this domain.|Uplif Level 1|CCL not<br>reached|
|**Cyber**|(3.1 Pro) We conducted additional testing on the<br>model in this domain as Gemini 3 Pro had<br>previously reached the alert threshold. The<br>model shows an  increase in cyber capabilities<br>compared to Gemini 3 Pro. As with Gemini 3<br>Pro, the model has reached the alert threshold,<br>but still does not reach the levels of uplif<br>required for the CCL.<br>(Deep Think mode) Accounting for inference<br>costs, the model with Deep Think mode<br>performs considerably worse than without<br>Deep Think mode. Even at high levels of<br>inference, results for the model with Deep Think<br>mode do not suggest higher capability than<br>without Deep Think mode.<br>We continue to deploy mitigations in this<br>domain.|Uplif Level 1|CCL not<br>reached|
|**Harmful**<br>**Manipulation**|(Deep Think mode) Evaluations indicated that<br>the model showed higher manipulative efcacy<br>for belief change metrics compared to a non-AI<br>baseline, with the maximum odds ratio of 3.6x,<br>which is the same as Gemini 3 Pro, and did not<br>reach the alert threshold.|Level 1<br>(exploratory)|CCL not<br>reached|



8

<!-- page 8: layout conversion matched 97.2% of the selectable-text tokens; the complete selectable text of this page follows -->

````text
FSF Results as of February, 2026: 
  
Domain  
Key Results for Gemini 3.1 Pro 
CCL  
CCL 
reached? 
CBRN 
(Deep Think mode) The model can provide 
highly accurate and actionable information but 
still fails to offer novel or sufficiently complete 
and detailed instructions for critical stages,  to 
significantly enhance the capabilities of low to 
medium resourced threat actors required for 
the CCL. We continue to deploy mitigations in 
this domain.  
Uplift Level 1  
CCL not 
reached 
Cyber 
(3.1 Pro) We conducted additional testing on the 
model in this domain as Gemini 3 Pro had 
previously reached the alert threshold. The 
model shows an  increase in cyber capabilities 
compared to Gemini 3 Pro. As with Gemini 3 
Pro, the model has reached the alert threshold, 
but still does not reach the levels of uplift 
required for the CCL. 
(Deep Think mode) Accounting for inference 
costs, the model with Deep Think mode 
performs considerably worse than without 
Deep Think mode. Even at high levels of 
inference, results for the model with Deep Think 
mode do not suggest higher capability than 
without Deep Think mode. 
We continue to deploy mitigations in this 
domain.  
Uplift Level 1  
CCL not 
reached 
Harmful 
Manipulation 
(Deep Think mode) Evaluations indicated that 
the model showed higher manipulative efficacy 
for belief change metrics compared to a non-AI 
baseline, with the maximum odds ratio of 3.6x, 
which is the same as Gemini 3 Pro, and did not 
reach the alert threshold.  
Level 1 
(exploratory)  
CCL not 
reached 
8
````

<!-- page 9 of 9 -->

|**Machine**<br>**Learning R&D**|(Deep Think mode) The model shows gains on<br>RE-Bench compared to Gemini 3 Pro, with a<br>human-normalised<br>average<br>score<br>of<br>1.27<br>compared to Gemini 3 Pro's score of 1.04. On<br>one<br>particular<br>challenge,<br>_Optimise_<br>_LLM_<br>_Foundry_,<br>it<br>scores<br>double<br>the<br>human-normalised baseline score (reducing the<br>runtime of a fne-tuning script from 300<br>seconds to 47 seconds, compared to the<br>human reference solution of 94 seconds).<br>However, the model’s average performance<br>across all challenges remains beneath the alert<br>threshold for the CCLs.|Acceleration<br>level 1<br>Automation<br>level 1|CCLs not<br>reached|
|---|---|---|---|
|**Misalignment**<br>(Exploratory)|(Deep Think mode) On stealth evaluations, the<br>model performs similarly to Gemini 3 Pro. On<br>situational awareness, the model is stronger<br>than Gemini 3 Pro: on three challenges which<br>no other model has been able to consistently<br>solve,_max tokens, context size mod,_and<br>_oversight frequency,_the model achieves a<br>success rate of almost 100%. However, its<br>performance<br>on<br>other<br>challenges<br>is<br>inconsistent, and thus the model does not reach<br>the alert threshold.|Instrumental<br>Reasoning<br>Levels 1 + 2<br>(exploratory)|CCLs not<br>reached|



9
