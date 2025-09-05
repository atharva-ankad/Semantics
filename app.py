from flask import Flask, render_template, request, jsonify
from backend.semantic_search import search
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# Load small model to embed user queries
# This is okay on Render if you choose a small model like 'all-MiniLM-L6-v2'
model = SentenceTransformer('all-MiniLM-L6-v2')

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search_api():
    data = request.json
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "No query provided"}), 400

    query_embedding = model.encode([query])  # 1x384 vector
    results = search(query_embedding, top_n=5)
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
