from flask import Flask, request, jsonify
from predictor import predict

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict_route():
    stock_data = request.get_json()
    result = predict(stock_data)
    return jsonify(result)

@app.route("/", methods=["GET"])
def home():
    return "CandleNext Backend is Live!"