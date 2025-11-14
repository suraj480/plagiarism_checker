import os
import subprocess
import streamlit as st
import joblib
from utils import calculate_cosine_similarity
from utils import highlight_matching_text

# Auto-create data & model if missing
if not os.path.exists("plagiarism_dataset.csv"):
    st.info("📘 Creating dataset...")
    subprocess.run(["python", "data_prep.py"])

if not os.path.exists("plagiarism_model.pkl"):
    st.info("🧠 Training model...")
    subprocess.run(["python", "model.py"])

# Load model
model = joblib.load("plagiarism_model.pkl")

st.title("📄 Plagiarism Checker")

file1 = st.file_uploader("Upload Original File", type=["txt"])
file2 = st.file_uploader("Upload Submission File", type=["txt"])

if file1 and file2:
    text1 = file1.read().decode("utf-8")
    text2 = file2.read().decode("utf-8")

    similarity = calculate_cosine_similarity(text1, text2)
    prediction = model.predict([[similarity]])[0]
    prob = model.predict_proba([[similarity]])[0][1]

    st.markdown(f"**Cosine Similarity Score:** `{similarity:.2f}`")
    st.markdown(f"**Plagiarism Probability:** `{prob:.2f}`")

    # Three-tier feedback
    if similarity >= 0.85:
        st.error("🔴 This submission is very likely plagiarized.")
    elif 0.6 <= similarity < 0.85:
        st.warning("🟠 This submission may be partially plagiarized or paraphrased.")
    else:
        st.success("🟢 This submission seems original.")

           # Highlighted Text Display
    st.subheader("📌 Highlighted Matching Text")
    highlighted1, highlighted2 = highlight_matching_text(text1, text2)

    st.markdown("**Original File (Highlighted):**", unsafe_allow_html=True)
    st.markdown(f"<div style='background-color:#f9f9f9;padding:10px;border-radius:8px'>{highlighted1}</div>", unsafe_allow_html=True)

    st.markdown("**Submission File (Highlighted):**", unsafe_allow_html=True)
    st.markdown(f"<div style='background-color:#f0f0f0;padding:10px;border-radius:8px'>{highlighted2}</div>", unsafe_allow_html=True)
