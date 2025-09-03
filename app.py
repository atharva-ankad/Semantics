from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    query = None

    if request.method == "POST":
        query = request.form.get("query")  # get text from form
        # Temporary dummy results for testing
        results = [
            {"text": "haahahaha","score":0},
            {"text": "Its working yayyyy","score":1}
        ]

    return render_template("index.html", query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)
