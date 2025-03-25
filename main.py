from flask import Flask, request, jsonify
from predict import predict

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def handle_predict():
    try:
        data = request.get_json()
        features = data["features"]
        result = predict(features)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
