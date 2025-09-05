from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model=SentenceTransformer('all-MiniLM-L6-v2')


with open(r"C:\Users\ankad\Documents\Project1\clean_solar_data.txt", "r") as f:
    sentences = f.readlines()
sentences =[s.strip() for s in sentences]

embeddings=model.encode(sentences)

def search(query,n):
    enquery=model.encode(query)
    enquery = enquery.reshape(1, -1)
    scores=cosine_similarity(enquery,embeddings)[0]
    results = list(zip(sentences, scores))
    sorted_results = sorted(results, key=lambda x: x[1], reverse=True)[:n]
    return sorted_results
