import os
import logging
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    return jsonify({"status": "running"})

@app.route("/info")
def info():
    return jsonify({
        "service": "internal-api",
        "version": "1.2.3",
        "maintainer": os.getenv("EMAIL")
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    logging.info(f"Starting service on port {port}")
    app.run(host="0.0.0.0", port=port)
