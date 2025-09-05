from sentence_transformers import SentenceTransformer
import numpy as np
import pickle

# Load model locally
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load dataset
with open("clean_solar_data.txt", "r") as f:
    sentences = [s.strip() for s in f.readlines()]

# Compute embeddings
embeddings = model.encode(sentences)

# Save embeddings and sentences
np.save("embeddings/clean_solar_data.npy", embeddings)

with open("embeddings/clean_solar_sentences.pkl", "wb") as f:
    pickle.dump(sentences, f)
