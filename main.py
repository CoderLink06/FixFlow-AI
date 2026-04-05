from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route("/")
def home():
    # This serves your UI directly to the judges!
    return send_file("dashboard.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    # Using gunicorn in production, but this works for basic Cloud Run
    app.run(host="0.0.0.0", port=port)