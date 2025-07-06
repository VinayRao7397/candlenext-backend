from flask import Flask, request, jsonify
from flask_cors import CORS
from predictor import predict

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend can access backend

@app.route("/predict", methods=["POST"])
def predict_route():
    stock_data = request.get_json()
    result = predict(stock_data)
    return jsonify(result)

@app.route("/", methods=["GET"])
def home():
    return "CandleNext Backend is Live!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)