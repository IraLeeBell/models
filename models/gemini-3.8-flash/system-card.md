<!--
Title: Gemini 3.8 Flash — Model Card
Publisher: Google DeepMind
Document date: 2026-09
Owner URL: https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-8-Flash-Model-Card.pdf
Catalog document: google-gemini-3-8-flash; retrieved 2026-10-06; SHA-256 verified against the catalog
PDF: 734,978 bytes, 8 pages, SHA-256 fd9b9494c8cb0da6dc16777c3df70d9f9226708e08ba7c9337222207c5d482af
Copyright Google DeepMind. Local copy for private reference; this file is not licensed for redistribution and is Git-ignored (see RIGHTS.md).
This is a verbatim text extraction of the PDF; headings and tables are reconstructed from layout.
Converter: pymupdf4llm 1.27.2.3 (PyMuPDF 1.27.2.3). One marker precedes each of the 8 PDF pages.
Completeness: 7 pages converted with >= 98% of their selectable-text tokens; 1 pages also carry their verbatim plain text; 0 pages have no selectable text (image only).
Figures, charts, and text inside images are not reproduced; consult the original PDF.
-->

<!-- page 1 of 8 -->

**==> picture [78 x 24] intentionally omitted <==**

# Gemini 3.8 Flash Model card

<!-- page 2 of 8 -->

**==> picture [78 x 24] intentionally omitted <==**

## Gemini 3.8 Flash — Model Card 

Model Cards are intended to provide essential information on Gemini models, including known limitations, mitigation approaches, and safety performance. Model cards may be updated from time to time; for example, to include updated evaluations as the model is improved or revised. See the Google DeepMind site for a comprehensive list of model cards. Published: September, 2026 

## Model Information 

## Description 

Gemini 3.8 Flash is the next iteration in the Gemini 3 model family, building on Gemini 3.7 Flash, delivering performance advancements across software engineering and agentic knowledge workflows. It continues to support customizable effort levels to control the mix of quality, cost and latency. 

## Model dependencies 

Gemini 3.8 Flash is based on Gemini 3.7 Flash. 

## Inputs 

Text strings (e.g., a question, a prompt, document(s) to be summarized), images, audio, and video files, with a token context window of up to 1M. 

## Outputs 

Text, with a 64K token output. 

## Architecture 

Gemini 3.8 Flash is based on Gemini 3.7 Flash. For more information about the model architecture for Gemini 3.8 Flash, see the Gemini 3.7 Flash model card. 

2

<!-- page 3 of 8 -->

**==> picture [78 x 24] intentionally omitted <==**

## Model Data 

## Training Dataset 

Gemini 3.8 Flash is based on Gemini 3.7 Flash. For more information about the training dataset for Gemini 3.8 Flash, see the Gemini 3.7 Flash model card. 

## Training Data Processing 

For more information about the training data processing for Gemini 3.8 Flash, see the Gemini 3.7 Flash model card. 

## Implementation and Sustainability 

## Hardware 

Gemini 3.8 Flash is based on Gemini 3.7 Flash. For more information about the hardware for Gemini 3.8 Flash and our continued commitment to operate sustainably, see the Gemini 3.7 Flash model card. 

## Software 

Gemini 3.8 Flash is based on Gemini 3.7 Flash. For more information about the software for Gemini 3.8 Flash, Gemini 3.7 Flash model card. 

## Distribution 

Gemini 3.8 Flash is distributed in the following channels; respective documentation shared in line: 

- Gemini app 

- Gemini Enterprise Agent Platorm 

- Google AI Studio 

- Gemini API 

- Google AI Mode 

- Google Antigravity 

3

<!-- page 4 of 8 -->

**==> picture [78 x 24] intentionally omitted <==**

Our models are available to downstream providers via an application program interface (API) and subject to relevant terms of use. There is no required hardware or software to use the model. For AI Studio and Gemini API, see the Gemini API Additional Terms of Service; for Gemini Enterprise Agent Platform, see Google Cloud Platorm Terms of Service. For more information, see Gemini Model API instructions and Gemini API quickstart. 

## Evaluation 

## Approach 

Gemini 3.8 Flash was evaluated across a range of benchmarks, including coding, knowledge work, multimodal capabilities, long-context, computer use, scientific reasoning. Additional benchmarks and details on approach, results and their methodologies can be found at: - - - - deepmind.com/models/evals methodology/gemini 3 8 fash. 

4

<!-- page 5 of 8 -->

**==> picture [78 x 24] intentionally omitted <==**

## Results 

Results as of September, 2026 are listed below: 

**==> picture [488 x 597] intentionally omitted <==**

For details on our evaluation methodology please see: - - - - deepmind.com/models/evals methodology/gemini 3 8 fash 

5

<!-- page 5: layout conversion matched 96.3% of the selectable-text tokens; the complete selectable text of this page follows -->

````text
Results 
Results as of September, 2026 are listed below: 
 
 
For details on our evaluation methodology please see: 
deepmind.com/models/evals-methodology/gemini-3-8-flash  
5
````

<!-- page 6 of 8 -->

**==> picture [78 x 24] intentionally omitted <==**

## Intended Usage and Limitations 

## Benefit and Intended Usage 

Gemini 3.8 Flash is well-suited for users, developers, and enterprises, designed for cost-effective scaling of general-purpose, production-ready agents. Some use cases include: software engineering, agent tasks, and complex knowledge workflows. 

## Known Limitations 

Gemini 3.8 Flash may exhibit some of the general limitations of foundation models, such as hallucinations. In addition to this, we are continually working to improve jailbreak resistance and have recently strengthened the mitigations across Frontier Safety. There may also be occasional slowness or timeout issues. At times, the model might use more tokens to maximize performance, especially at higher effort levels. 

The knowledge cutoff date for Gemini 3.8 Flash is March 2026 – users can expect updated information for some domains while in others they may experience the model’s knowledge is limited to January 2025 (in line with the Gemini 3 Model Family). For more information about known limitations, see the Gemini 3.7 Flash model card. 

## Acceptable Usage 

For more information about the acceptable usage for Gemini 3.7 Flash, see the Gemini 3.7 Flash model card. 

## Ethics and Content Safety 

## Evaluation Approach 

For more information about the evaluation approach for Gemini 3.8 Flash, see the Gemini 3.7 Flash model card. 

## Safety Policies 

For more information about the safety policies for Gemini 3.8 Flash, see the Gemini 3.7 Flash model card. 

6

<!-- page 7 of 8 -->

**==> picture [78 x 24] intentionally omitted <==**

## Training and Development Evaluation Results 

Results for some of the internal safety evaluations conducted during the development phase are listed below. The evaluation results are for automated evaluations and not human evaluation or red teaming. Scores are provided as an absolute percentage increase or decrease in performance compared to the indicated model, as described below. 

Overall, Gemini 3.8 Flash performs similarly to Gemini 3.7 Flash across both safety and tone, with low unjustified refusals. Safety performance across non-English languages regressed slightly relative to 3.7 Flash. 

|**Evaluation**|**Description**|**Gemini 3.8 Flash**|
|---|---|---|
|||vs. Gemini 3.7 Flash|
|Text to Text Safety|Automated content safety|-0.4pp|
||evaluation measuring safety|_Lower is beter_|
||policies||
|Multilingual Safety|Automated safety policy|+5.4pp|
||evaluation across multiple|_Lower is beter_|
||languages||
|Image to Text Safety|Automated content safety|0.0pp|
||evaluation measuring safety|_Lower is beter_|
||policies||
|Tone1|Automated evaluation measuring|+0.2pp|
||the objective tone of model|_Higher is beter_|
||responses||
|Unjustifed-refusals|Automated evaluation measuring<br>model’s ability to respond to|+1.1pp<br>_Lower is beter_|
||borderline prompts while||
||remaining safe||



We continue to improve our internal evaluations, including refining automated evaluations to reduce false positives and negatives, as well as update query sets to ensure balance and maintain a high standard of results. The performance results reported below are computed with improved evaluations and thus are not directly comparable with performance results found in previous Gemini model cards. 

We expect variation in our automated safety evaluations results, which is why we review flagged content to check for egregious or dangerous material. Our manual review confirmed losses were overwhelmingly either a) false positives or b) not egregious. 

1 For tone and instruction following, a positive percentage increase represents an improvement in the tone of the model on sensitive topics and the model’s ability to follow instructions while remaining safe compared to Gemini 3 Flash. We mark improvements in green and regressions in red. 

7

<!-- page 8 of 8 -->

**==> picture [78 x 24] intentionally omitted <==**

## Human Red Teaming Results 

We conduct manual red teaming by specialist teams who sit outside of the model development team. High-level findings are fed back to the model team. For child safety evaluations, Gemini 3.8 Flash satisfied required launch thresholds, which were developed by expert teams to protect children online and meet Google’s commitments to child safety across our models and Google products. For content safety policies generally, including child safety, we saw similar or improved safety performance compared to Gemini 3.7 Flash. Additionally, the scope of red teaming covered potential issues outside of our strict policies, compared performance to Gemini 3.1 Pro, and found no egregious concerns. 

## Frontier Safety Assessment 

Gemini 3.8 Flash is part of the Gemini 3 series of models. We evaluated Gemini 3.7 Flash as outlined in our latest Frontier Safety Framework (April-2026), and found that it did not reach any Tracked or Critical Capability Levels (T/CCLs). Our assessments have shown that Gemini 3.8 Flash does not have meaningful new capabilities or material increases in performance with respect to the domains outlined in our Frontier Safety Framework compared to Gemini 3.7 Flash; therefore, based on Gemini 3.7 Flash results, we are confident that Gemini 3.8 Flash is also unlikely to reach any T/CCLs. 

For more information on our Frontier Safety assessment, read the Gemini 3.7 Flash model card. 

8
