import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Działa!"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Pobiera port z Railway
    app.run(host="0.0.0.0", port=port)
@app.route("/health")
def health():
    return "OK", 200