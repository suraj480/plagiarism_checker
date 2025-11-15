# ✍️ Plagiarism Checker Application

This repository contains a simple, interactive Plagiarism Checker built using Python, primarily utilizing the Streamlit framework for the user interface.

The application allows users to upload or input two text files (an "Original File" and a "Submission File") and calculates the probability of plagiarism based on content similarity.

---

## ✨ Features

* **Interactive UI:** Built with Streamlit for easy file upload and feedback display.
* **Similarity Scoring:** Calculates a probabilistic score indicating the likelihood of plagiarism.
* **Tiered Feedback:** Provides tiered feedback based on the similarity score:
    * High similarity (e.g., `>= 0.85`): Marked as **"very likely plagiarized."**
    * Medium similarity (e.g., `0.6 <= similarity < 0.85`): Marked as **"may be partially plagiarized or paraphrased."**
    * Low similarity: Marked as **"seems original."**
* **Text Highlighting:** Displays both the Original and Submission texts with matching sections highlighted for visual inspection.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.7+
* `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [Your Repository URL]
    cd plagiarism_checker
    ```

2.  **Install dependencies:**
    The necessary libraries (including `streamlit`, `scikit-learn`, etc.) are listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application Locally

The application runs directly via Streamlit on port `8501`.

```bash
streamlit run app.py
