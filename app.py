from flask import Flask, request, render_template, jsonify
import requests
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/resolve", methods=["POST"])
def resolve_url():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400
    try:
        parts = url.rsplit('/', 1)
        last_digit = parts[-1]
        modified_url = url.replace('/' + last_digit, '/3')
        return jsonify({"result": modified_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False)
