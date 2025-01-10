from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

class PredictionInput(BaseModel):
    features: list[float]


# Load the trained model
model_path = "models/xgboost_test_gini0.2538.pkl"
with open(model_path, 'rb') as f:
    model = pickle.load(f)


@app.post("/predict")
def predict(input: PredictionInput):
    # Parse the input features
    data = np.array(input.features).reshape(1, -1)
    prob = model.predict_proba(data)[:, 1][0]
    return {"prediction_probability": float(prob)}
