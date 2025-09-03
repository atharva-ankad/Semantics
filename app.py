from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "pizza"

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

        # Save in session (temporary storage)
        session["query"] = query
        session["results"] = results

        return redirect(url_for("index"))

    # GET request (after redirect)
    query = session.pop("query", None)
    results = session.pop("results", None)

    return render_template("index.html", query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)
