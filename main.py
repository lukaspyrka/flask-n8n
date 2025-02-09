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
    data = request.json  # Pobiera dane JSON z n8n
    #print("Otrzymano dane z n8n:", get_view_count(data))  # Logowanie do konsoli

    return jsonify({"status": "success", "received": get_view_count(data)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
