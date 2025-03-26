import xgboost as xgb
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def predict(request):
    model = xgb.XGBClassifier()
    model.load_model('stock-pred-model.json')

    features = np.array(request).reshape(1, -1)
    print(features)
    
    scaler = StandardScaler()
    scaler.fit_transform(features)

    prediction = model.predict(features)
    probability = model.predict_proba(features)[:, 1]

    return int(prediction[0]), float(probability[0])
