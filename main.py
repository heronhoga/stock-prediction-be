from flask import Flask, request, jsonify
from flask_cors import CORS
from predict import predict
import pandas as pd

app = Flask(__name__)
CORS(app=app, origins=["http://localhost:3000", "http://127.0.0.1:3000"])

@app.route("/predict", methods=["POST"])
def handle_predict():
    try:
        data = request.files['file_csv']
        df = pd.read_csv(data)
        print(df.tail(1))
        
        if pd.notnull(df.tail(1).iloc[0]['Open']) and pd.notnull(df.tail(1).iloc[0]['Close']) and pd.notnull(df.tail(1).iloc[0]['High']) and pd.notnull(df.tail(1).iloc[0]['Low']) and pd.notnull(df.tail(1).iloc[0]['Date']):
            splittedMonth = df.tail(1)['Date'].str.split('-', expand=True)
            
            dataInput = [df.tail(1)['Open'] - df.tail(1)['Close'], df.tail(1)['Low'] - df.tail(1)['High'], splittedMonth[1].astype('int')]
            print(dataInput)
            result = predict(dataInput)
            return jsonify(result)
        else:
            return jsonify({"error": "No data provideded"}), 400    
        

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
