import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Phishing Email Detector", layout="centered")


@st.cache_resource
def load_classifier():
    # Load the fine-tuned DistilBERT model straight from the Hugging Face Hub
    return pipeline("text-classification", model="JacobSeed/phishing-email-distilbert")


classifier = load_classifier()

st.title("Phishing Email Detector")
st.write(
    "Fine-tuned DistilBERT that flags phishing emails. Trained on the Kaggle phishing-email dataset."
)

email = st.text_area("Paste an email here:", height=200)

if st.button("Analyze") and email.strip():
    result = classifier(email)[0]
    label = result["label"]
    score = result["score"]
    if label == "Legitimate":
        st.success(f"Legitimate ({score:.1%} confidence)")
    else:
        st.error(f"Phishing ({score:.1%} confidence)")
    st.markdown("---")
    st.caption("Model: fine-tuned distilbert-base-uncased | Metric: label + confidence")
