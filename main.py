import os
os.system("apt-get update && apt-get install -y libc6")
import subprocess
import os
import requests
from flask import Flask, request, jsonify
from playwright.sync_api import sync_playwright

def get_view_count(url):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()
        
        page.goto(url)
        page.wait_for_selector(".view-count")
        
        view_count = page.locator(".view-count").first.inner_text()
        
        browser.close()
        return view_count



app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Działa!"})

@app.route("/send-data", methods=["POST"])
def receive_data():
    try:
        data = request.json
        if not data or "url" not in data or not isinstance(data["url"], str):
            return jsonify({"error": "Brak poprawnego URL w żądaniu"}), 400  

        url = data["url"]
        view_count = get_view_count(url)
        return jsonify({"status": "success", "view_count": view_count})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
