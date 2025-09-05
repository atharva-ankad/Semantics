from flask import Flask, request, jsonify, render_template
import semantic_search  #ML code

app = Flask(__name__)

# Serve HTML frontend
@app.route("/")
def home():
    return render_template("index.html")

# REST API endpoint
@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    
    if not query:
        return jsonify({"error": "Please provide a query"}), 400
    
    results = semantic_search.search(query,5)
    
    response = {
        "query": query,
        "results": [
            {"sentence": sent, "score": float(score)} for sent, score in results
        ]
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
