import pandas as pd
from utils import calculate_cosine_similarity

# Balanced training data
data = [
    # Plagiarized / identical
    ("The quick brown fox jumps over the lazy dog.", "The quick brown fox jumps over the lazy dog.", 1),
    ("Climate change affects weather and biodiversity.", "Climate change affects weather and biodiversity.", 1),
    ("Artificial intelligence is changing how we live.", "Artificial intelligence is changing how we live.", 1),

    # Paraphrased (still plagiarized)
    ("Machine learning algorithms can learn from data.", "Algorithms in machine learning improve by studying data.", 1),
    ("Global warming leads to rising temperatures worldwide.", "The planet is heating due to global warming.", 1),

    # Similar theme but original
    ("The sun provides energy to the earth.", "Solar panels convert sunlight into electricity.", 0),
    ("Water is essential for life.", "Plants need water, sunlight, and carbon dioxide to grow.", 0),

    # Completely different topics
    ("Python is a popular programming language.", "Mount Everest is the tallest mountain.", 0),
    ("He loves to play cricket.", "Artificial intelligence can beat humans at chess.", 0),
    ("I enjoy listening to music.", "Quantum computing uses qubits.", 0),
]

# Compute similarity and label
rows = []
for original, submission, label in data:
    sim = calculate_cosine_similarity(original, submission)
    rows.append([original, submission, sim, label])

df = pd.DataFrame(rows, columns=["Original", "Submission", "Similarity", "Label"])
df.to_csv("plagiarism_dataset.csv", index=False)