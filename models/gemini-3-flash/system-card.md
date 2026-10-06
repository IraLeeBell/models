<!--
Title: Gemini 3 Flash Model Card
Publisher: Google DeepMind
Document date: 2025-12
Owner URL: https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Flash-Model-Card.pdf
Catalog document: google-gemini-3-flash; retrieved 2026-10-06; SHA-256 verified against the catalog
PDF: 380,481 bytes, 6 pages, SHA-256 b2800104a47322d76d80a72bfb128ba7f0bacffc419ae9bb630eae289c761ba0
Copyright Google DeepMind. Local copy for private reference; this file is not licensed for redistribution and is Git-ignored (see RIGHTS.md).
This is a verbatim text extraction of the PDF; headings and tables are reconstructed from layout.
Converter: pymupdf4llm 1.27.2.3 (PyMuPDF 1.27.2.3). One marker precedes each of the 6 PDF pages.
Completeness: 6 pages converted with >= 98% of their selectable-text tokens; 0 pages also carry their verbatim plain text; 0 pages have no selectable text (image only).
Figures, charts, and text inside images are not reproduced; consult the original PDF.
-->

<!-- page 1 of 6 -->

Model card published: December, 2025 

**==> picture [77 x 27] intentionally omitted <==**

**==> picture [612 x 16] intentionally omitted <==**

## Gemini 3 Flash Model Card 

**==> picture [468 x 85] intentionally omitted <==**

<!-- page 2 of 6 -->

## **Gemini 3 Flash - Model Card** 

_**Model Cards** are intended to provide essential information on Gemini models, including known limitations, mitigation approaches, and safety performance. Model cards may be updated from time-to-time; for example, to include updated evaluations as the model is improved or revised. See the Google DeepMind site for a comprehensive list of model cards._ 

_Published:  December 2025_ 

## **Model Information** 

**Description** : Gemini 3 Flash is the next iteration in the Gemini 3 series of highly-capable, natively multimodal, reasoning models. Gemini 3 Flash is built off of the Gemini 3 Pro reasoning foundation with thinking levels to control the mix of quality, cost and latency. 

**Model dependencies:** Gemini 3 Flash is based on Gemini 3 Pro. 

**Inputs:** Text strings (e.g., a question, a prompt, document(s) to be summarized), images, audio, and video files, with a token context window of up to 1M. 

**Outputs** :  Text, with a 64K token output. 

**Architecture** : Gemini 3 Flash is based on Gemini 3 Pro. For more information about the model architecture for Gemini 3 Pro, see the Gemini 3 Pro model card. 

1

<!-- page 3 of 6 -->

## **Model Data** 

**Training Dataset:** Gemini 3 Flash is based on Gemini 3 Pro.  For more information about the training dataset for Gemini 3 Pro Image, see the Gemini 3 Pro model card. 

**Training Data Processing:** For more information about the training data processing for Gemini 3 Flash, see the Gemini 3 Pro model card. 

## **Implementation and Sustainability** 

**Hardware:** Gemini 3 Flash was trained using Google’s Tensor Processing Units (TPUs). TPUs are specifically designed to handle the massive computations involved in training LLMs and can speed up training considerably compared to CPUs. TPUs often come with large amounts of high-bandwidth memory, allowing for the handling of large models and batch sizes during training, which can lead to better model quality. TPU Pods (large clusters of TPUs) also provide a scalable solution for handling the growing complexity of large foundation models. Training can be distributed across multiple TPU devices for faster and more efficient processing. 

The efficiencies gained through the use of TPUs are aligned with Google's commitment to operate sustainably. 

**Software:** Training was done using JAX and ML Pathways. 

## **Distribution** 

Gemini 3 Flash is distributed similarly to Gemini 3 Pro. For more information about the distribution of Gemini 3 Flash, see the Gemini 3 Pro model card. 

2

<!-- page 4 of 6 -->

## **Evaluation** 

**Approach** : Gemini 3 Flash was evaluated across a range of benchmarks, including reasoning, multimodal capabilities, agentic tool use, multi-lingual performance, and long-context.  Additional benchmarks and details on approach, results and their methodologies can be found at: deepmind.com/models/evals-methodology/gemini-3-flash. 

**Results:** Gemini 3 Flash significantly outperforms Gemini 2.5 Pro across a range of benchmarks requiring enhanced reasoning and multimodal capabilities. Results as of December, 2025 are listed below: 

**==> picture [456 x 440] intentionally omitted <==**

3

<!-- page 5 of 6 -->

## **Intended Usage and Limitations** 

**Benefit and Intended Usage:** Gemini 3 Flash is well-suited for users and developers, specific use cases include: agentic workflows, every day coding, reasoning and planning, and multimodal analysis. 

**Known Limitations:** For more information about the known limitations for Gemini 3 Flash, see the Gemini 3 Pro model card. 

**Acceptable Usage:** For more information about the acceptable usage for Gemini 3 Flash, see the Gemini 3 Pro model card. 

## **Ethics and Content Safety** 

**Evaluation Approach:** For more information about the evaluation approach for Gemini 3 Flash, see the Gemini 3 Pro model card. 

**Safety Policies** : For more information about the safety policies for Gemini 3 Flash, see the Gemini 3 Pro model card. 

**Training and Development Evaluation Results:** Results for some of the internal safety evaluations conducted during the development phase are listed below. The evaluation results are for automated evaluations and not human evaluation or red teaming. Scores are provided as an absolute percentage increase or decrease in performance compared to the indicated model, as described below. Overall, Gemini 3 Flash outperforms Gemini 2.5 Flash across both safety and tone, while keeping unjustified refusals low. We mark improvements in green and regressions in red. 

**==> picture [480 x 196] intentionally omitted <==**

**----- Start of picture text -----**<br>
Evaluation  Gemini 3 Flash<br>Description  vs. Gemini 2.5 Flash<br>Text to Text Safety<br>-3.1%<br>Automated content safety evaluation measuring safety policies<br>Multilingual Safety  +0.1%<br>Automated safety policy evaluation across multiple languages non-egregious<br>Image to Text Safety  -2.3%<br>Automated content safety evaluation measuring safety policies<br>Tone<br>+3.8%<br>Automated evaluation measuring objective tone of model refusal<br>Unjustified-refusals<br>-10.4%<br>Automated evaluation measuring model’s ability to respond to borderline prompts while remaining safe<br>**----- End of picture text -----**<br>


4

<!-- page 6 of 6 -->

We continue to improve our internal evaluations, including refining automated evaluations to reduce false positives and negatives, as well as update query sets to ensure balance and maintain a high standard of results. The performance results reported below are computed with improved evaluations and thus are not directly comparable with performance results found in previous Gemini model cards. 

We expect variation in our automated safety evaluations results, which is why we review flagged content to check for egregious or dangerous material. Our manual review confirmed losses were overwhelmingly either a) false positives or b) not egregious. 

**Human Red Teaming Results:** We conduct manual red teaming by specialist teams who sit outside of the model development team. High-level findings are fed back to the model team. For child safety evaluations, Gemini 3 Flash satisfied required launch thresholds, which were developed by expert teams to protect children online and meet Google’s commitments to child safety across our models and Google products. For content safety policies generally, including child safety, we saw similar or improved safety performance compared to Gemini 2.5 Flash. Like 3 Pro, the scope of red teaming covered potential issues outside of our strict policies, and found no egregious concerns. 

**Frontier Safety Assessment:** We evaluated Gemini 3 Pro Preview for Frontier Safety and reported the results in the Gemini 3 Pro Frontier Safety Framework Report, finding that it did not reach any critical capability levels (CCLs) outlined in our Frontier Safety Framework. As Gemini 3 Flash is less capable than Gemini 3 Pro, and the Gemini 3 Pro model results give us confidence that Gemini 3 Flash is unlikely to reach any CCLs, we can rely on results reported for Gemini 3 Pro.  Therefore, in line with the risk acceptance criteria outlined in our FSF (and our general responsibility and safety practices), we deemed Gemini 3 Flash was acceptable for deployment. 

**Risks and Mitigations:** For more information about the risks and mitigations for Gemini 3 Flash, see the Gemini 3 Pro model card. 

5
