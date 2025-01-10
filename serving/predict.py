from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# Load the trained model (update to your best model filename)
model_path = "models/xgboost_test_gini0.2840.pkl"
with open(model_path, 'rb') as f:
    model = pickle.load(f)


@app.post("/predict")
def predict(features: list[float]):
    data = np.array(features).reshape(1, -1)
    prob = model.predict_proba(data)[:, 1][0]
    return {"prediction_probability": float(prob)}
