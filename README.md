# Phishing Email Detection

This is a comparison involving two models, designed for the Advanced Topics in AI and ML course (PROG74040).

We decide whether an email is legitimate or a phishing attempt, then compare the classic machine-learning baseline with the fine-tuned transformer, before deploying the better of the two as a live demonstration on Streamlit Community Cloud.

## The problem

Phishing remains one of the most frequently used types of attack, and most email filters rely on domain reputation, an approach that an attacker can overcome by using a trusted service such as Gmail. The principle is straightforward: use the words found in the email to automatically detect phishing attempts and provide users with a tool that flags suspicious messages rather than simply putting them in their inbox.

## The dataset

We used the same data as in Phase I: the [phishing-email-dataset](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset) available on Kaggle. This dataset comprises several well-known email collections (Enron, CEAS_08, SpamAssassin, Ling, Nazario, and the Nigerian_Fraud set), bringing the total number of emails to approximately **82,000**, of which about 43,000 are phishing emails, and 40,000 are legitimate. It's a well-balanced dataset, which in turn makes evaluation simple.

## The two models

**Baseline, Logistic Regression plus TF-IDF.** The emails are converted into vectors composed of TF-IDF word scores (for unigrams up to trigrams), and a logistic regression classifier is used to make the decision. The method is fast, inexpensive, and easy to explain, which is the reason we have retained it as our reference point.

**An advanced, finely tuned DistilBERT.** The same concept but with a smarter model; unlike bag-of-words models, which treat individual words in isolation, transformer models read the entire sentence in context and thus can pick up on expressions such as 'this is not a scam,' which a bag-of-words approach would fail to understand. We chose DistilBERT since it is a distilled form of BERT, approximately 40% smaller and 60% faster, without losing most of the accuracy. It is sufficient for a course project and can be trained in a few minutes on a GPU (or in under an hour on a laptop's CPU).

We completely avoid using TensorFlow; the entire advanced pipeline uses Hugging Face's `Trainer` API, the same tools we used in the week 10 and 11 labs.

## Results (test set)

| Model | Accuracy | Precision | Recall | F1 | AUC-ROC |
|---|---|---|---|---|---|
| Baseline (LR + TF-IDF) | 0.9841 | 0.9837 | 0.9858 | 0.9847 | 0.9983 |
| Fine-tuned DistilBERT | 0.9918 | 0.9948 | 0.9893 | 0.9921 | 0.9998 |

Both runs used the same test set of 8,249 emails and the same evaluation function. The transformer outperforms the baseline in every respect, as we had expected, since context-aware features are useful for phishing language that bag-of-words models cannot detect.

## Notebook

The full pipeline runs on Kaggle; view it here:

<a href="https://www.kaggle.com/code/paganmin226/phase2-phishing-detection" target="_blank" rel="noopener noreferrer">
  <img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle">
</a>

## Deployment

Following the training process, the notebook uploads the fine-tuned model to the Hugging Face Model Hub and sets up a Streamlit web app in the `streamlit_app/` directory. We use Streamlit Community Cloud (which is free) to host the demo since it can deploy directly from this public repository. The app enables you to paste in any email and obtain a legitimate or phishing verdict, together with a confidence score.

**Live demo:** https://phishing-email-detection-3y2tqd73il3zou5xczkwpj.streamlit.app/

**Model on the Hugging Face Hub:** https://huggingface.co/JacobSeed/phishing-email-distilbert

**How to use it:** open the app URL, paste an email into the text area, click **Analyze**, and read the verdict + confidence.

**Known limitations:** the model reads message text only, so it does not inspect headers, attachments, or links, and attacks whose intent is hidden outside the body can get through. It is also based on the historical Kaggle collections, so very new phrasing or novel social-engineering patterns may be misclassified. The demo runs on shared free-tier infrastructure, so after a period of inactivity the first request can be slow.

## The files

- `Phase2_Phishing_Detection.ipynb`, the entire pipeline: data, baseline, fine-tuning, comparison, and deployment
- `streamlit_app/`, a folder containing the Streamlit web app (`app.py` + `requirements.txt`) for deployment

## Team & contributions

Built by:
- **Jonathan Taylor**, fine-tuning pipeline (DistilBERT), model publishing to the Hugging Face Hub, Streamlit deployment
- **Isaiah Andrews**, dataset acquisition and preprocessing, baseline model (TF-IDF + logistic regression), evaluation harness

The two members worked together to compare the models, then reviewed the results and deployment together.

## Course

Advanced Topics in Artificial Intelligence and Machine Learning, PROG74040, Spring 2026.