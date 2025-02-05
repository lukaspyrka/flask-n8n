import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Działa!"})

@app.route("/send-data", methods=["POST"])
def receive_data():
    data = request.json  # Pobiera dane JSON z n8n
    print("Otrzymano dane z n8n:", data)  # Logowanie do konsoli


    return jsonify({"status": "success", "received": data})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
