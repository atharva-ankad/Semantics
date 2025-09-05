import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

# Load precomputed embeddings and sentences
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMB_PATH = os.path.join(BASE_DIR, "embeddings/clean_solar_data.npy")
SENT_PATH = os.path.join(BASE_DIR, "embeddings/clean_solar_sentences.pkl")

embeddings = np.load(EMB_PATH)
with open(SENT_PATH, "rb") as f:
    sentences = pickle.load(f)

def search(query_embedding, top_n=5):
    """
    Returns top_n sentences based on cosine similarity
    query_embedding: 1xN numpy array
    """
    scores = cosine_similarity(query_embedding, embeddings)[0]
    results = list(zip(sentences, scores))
    sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
    return [{"sentence": s, "score": float(sc)} for s, sc in sorted_results[:top_n]]
