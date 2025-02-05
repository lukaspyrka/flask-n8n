from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_data():
    data = request.json  # Pobranie danych z n8n
    text = data.get("text", "")
    factor = data.get("factor", 1)

    # Przetworzenie danych
    result = text.upper() * factor

    return jsonify({"result": result})  # Odesłanie wyniku do n8n

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)