<!--
Title: Gemini 3.5 Flash Model Card
Publisher: Google DeepMind
Document date: 2026-05
Owner URL: https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-5-Flash-Model-Card.pdf
Catalog document: google-gemini-3-5-flash; retrieved 2026-10-06; SHA-256 verified against the catalog
PDF: 556,751 bytes, 7 pages, SHA-256 eed86d38a5f69732eea4ef3dd5662e526496a77d1cdf61679319d45461a2c195
Copyright Google DeepMind. Local copy for private reference; this file is not licensed for redistribution and is Git-ignored (see RIGHTS.md).
This is a verbatim text extraction of the PDF; headings and tables are reconstructed from layout.
Converter: pymupdf4llm 1.27.2.3 (PyMuPDF 1.27.2.3). One marker precedes each of the 7 PDF pages.
Completeness: 7 pages converted with >= 98% of their selectable-text tokens; 0 pages also carry their verbatim plain text; 0 pages have no selectable text (image only).
Figures, charts, and text inside images are not reproduced; consult the original PDF.
-->

<!-- page 1 of 7 -->

**==> picture [77 x 27] intentionally omitted <==**

**==> picture [468 x 37] intentionally omitted <==**

## Gemini 3.5 Flash Model Card 

**==> picture [468 x 39] intentionally omitted <==**

<!-- page 2 of 7 -->

## **Gemini 3.5 Flash - Model Card** 

_**Model Cards** are intended to provide essential information on Gemini models, including known limitations, mitigation approaches, and safety performance. Model cards may be updated from time to time; for example, to include updated evaluations as the model is improved or revised. See the Google DeepMind site for a comprehensive list of model cards._ 

_Published: May 2026_ 

## **Model Information** 

**Description** : Gemini 3.5 Flash is the next iteration in the Gemini 3 series of highly-capable, natively multimodal, reasoning models. Gemini 3.5 Flash is based on the Gemini 3 Flash reasoning foundation with thinking levels to control the mix of quality, cost and latency. 

**Model dependencies:** Gemini 3.5 Flash is based on Gemini 3 Flash. 

**Inputs:** Text strings (e.g., a question, a prompt, document(s) to be summarized), images, audio, and video files, with a token context window of up to 1M. 

**Outputs:** Text, with a 64K token output. 

**Architecture:** Gemini 3.5 Flash is based on Gemini 3 Flash. For more information about the model architecture for Gemini 3.5 Flash, see the Gemini 3 Flash model card. 

## **Model Data** 

**Training Dataset:** Gemini 3.5 Flash is based on Gemini 3 Flash. For more information about the training dataset for Gemini 3.5 Flash, see the Gemini 3 Flash model card. 

**Training Data Processing:** For more information about the training data processing for Gemini 3.5 Flash, see the Gemini 3 Flash model card. 

2

<!-- page 3 of 7 -->

## **Implementation and Sustainability** 

**Hardware:** Gemini 3.5 Flash is based on Gemini 3 Flash. For more information about the hardware for Gemini 3.5 Flash and our continued commitment to operate sustainably, see the Gemini 3 Flash model card. 

**Software:** Gemini 3.5 Flash is based on Gemini 3 Flash. For more information about the software for Gemini 3.5 Flash, see the Gemini 3 Flash model card. 

## **Distribution** 

Gemini 3.5 Flash is distributed in the following channels; respective documentation shared in line: 

- Gemini App 

- Gemini Enterprise App 

- Gemini Enterprise Agent Platorm 

- Google AI Studio 

- Gemini API 

- Google Search AI Mode 

- Google Antigravity 

Our models are available to downstream providers via an application program interface (API) and subject to relevant terms of use. There is no required hardware or software to use the model. For AI Studio and Gemini API, see the Gemini API Additional Terms of Service; for Gemini Enterprise Agent Platform, see Google Cloud Platorm Terms of Service. For more information, see Gemini Model API instructions and Gemini API quickstart. 

3

<!-- page 4 of 7 -->

## **Evaluation** 

**Approach** : Gemini 3.5 Flash was evaluated across a range of benchmarks, including reasoning, coding, agentic tool use, multimodal capabilities, multi-lingual performance, and long-context. Additional benchmarks and details on approach, results and their methodologies can be found at: deepmind.com/models/evals-methodology/gemini-3-5-fash. 

**Results:** Results as of May, 2026 are listed below: 

**==> picture [469 x 345] intentionally omitted <==**

4

<!-- page 5 of 7 -->

## **Intended Usage and Limitations** 

**Benefit and Intended Usage:** Gemini 3.5 Flash is well-suited for users, developers, and enterprises, some use cases include: agentic workflows, coding tasks, and multi-week enterprise processes. 

**Known Limitations:** For more information about the known limitations for Gemini 3.5 Flash, see the Gemini 3 Flash model card. 

**Acceptable Usage:** For more information about the acceptable usage for Gemini 3.5 Flash, see the Gemini 3 Flash model card. 

## **Ethics and Content Safety** 

**Evaluation Approach:** For more information about the evaluation approach for Gemini 3.5 Flash, see the Gemini 3 Flash model card. 

**Safety Policies** : For more information about the safety policies for Gemini 3.5 Flash, see the Gemini 3 Flash model card. 

5

<!-- page 6 of 7 -->

**Training and Development Evaluation Results:** Results for some of the internal safety evaluations conducted during the development phase are listed below. The evaluation results are for automated evaluations and not human evaluation or red teaming. Scores are provided as an absolute percentage increase or decrease in performance compared to the indicated model, as described below. 

Overall, Gemini 3.5 Flash outperforms Gemini 3 Flash across both safety and tone, while keeping unjustified refusals low. We mark improvements in blue and regressions in orange. 

**==> picture [466 x 216] intentionally omitted <==**

**----- Start of picture text -----**<br>
Gemini 3.5 Flash<br>Evaluation  Description<br>vs. Gemini 3 Flash<br>Automated content safety evaluation<br>Text to Text Safety  -3.9%<br>measuring safety policies<br>Automated safety policy evaluation across<br>Multilingual Safety  -2.6%<br>multiple languages<br>Automated content safety evaluation<br>Image to Text Safety  0%<br>measuring safety policies<br>Automated evaluation measuring<br>Tone [1] +8.9%<br>objective tone of model refusal<br>Automated evaluation measuring model’s<br>Unjustified-refusals  ability to respond to borderline prompts  +0.8% (non-egregious)<br>while remaining safe<br>**----- End of picture text -----**<br>


We continue to improve our internal evaluations, including refining automated evaluations to reduce false positives and negatives, as well as update query sets to ensure balance and maintain a high standard of results. The performance results reported below are computed with improved evaluations and thus are not directly comparable with performance results found in previous Gemini model cards. 

We expect variation in our automated safety evaluations results, which is why we review flagged content to check for egregious or dangerous material. Our manual review confirmed losses were overwhelmingly either a) false positives or b) not egregious. 

**Human Red Teaming Results:** We conduct manual red teaming by specialist teams who sit outside of the model development team. High-level findings are fed back to the model team. For child safety evaluations, Gemini 3.5 Flash satisfied required launch thresholds, which were developed by expert teams to protect children online and meet Google’s commitments to child safety across our models and Google products. For content safety policies generally, including child safety, we saw similar or improved safety performance compared to Gemini 3 Flash. Additionally, the scope of red teaming covered potential issues outside of our strict policies, compared performance to Gemini 3.1 Pro, and found no egregious concerns. 

> 1 For tone and instruction following, a positive percentage increase represents an improvement in the tone of the model on sensitive topics and the model’s ability to follow instructions while remaining safe compared to Gemini 3 Flash. We mark improvements in green and regressions in yellow. 

6

<!-- page 7 of 7 -->

**Frontier Safety Assessment:** Gemini 3.5 Flash is part of the Gemini 3 series of models. We evaluated Gemini 3.1 Pro for Frontier Safety as it was the most generally capable model as of publication of this model card, and it did not reach any Critical Capability Levels (CCLs) outlined in our Frontier Safety Framework. Our assessments have shown that, while Gemini 3.5 Flash excels at agents and coding, it does not have meaningful new capabilities or material increases in performance with respect to Frontier Safety compared to Gemini 3.1 Pro, therefore based on Gemini 3.1 Pro results, we are confident that Gemini 3.5 Flash is also unlikely to reach any CCLs. 

As previous models in the Gemini 3 series reached the alert threshold for cyber, we performed additional testing in this domain and found that Gemini 3.5 Flash remains below the cyber CCL. 

For more information on our Frontier Safety Assessment, read the Gemini 3.1 Pro Model Card. 

**Risks and Mitigations:** For more information about the risks and mitigations for Gemini 3.5 Flash, see the Gemini 3.1 Pro model card. 

7
