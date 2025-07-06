def predict(stock_data):
    # Dummy prediction logic (replace with real model)
    if stock_data.get("symbol") == "RELIANCE":
        return {"prediction": "rise", "confidence": 0.88}
    return {"prediction": "fall", "confidence": 0.72}