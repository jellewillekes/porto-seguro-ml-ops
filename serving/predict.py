from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np
import json
import os

app = FastAPI()


class PredictionInput(BaseModel):
    features: list[float]


# Load model and metadata
model_path = "models/xgboost_test_gini0.2538.pkl"
metadata_path = "models/model_metadata.json"

try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    if not os.path.exists(metadata_path):
        raise RuntimeError("Metadata file not found. Ensure the training script has saved it.")

    with open(metadata_path, 'r') as f:
        metadata = json.load(f)

    expected_n_features = metadata["n_features"]
except Exception as e:
    raise RuntimeError(f"Error loading model or metadata: {e}")


@app.post("/predict")
def predict(input: PredictionInput):
    try:
        data = np.array(input.features)

        print(f"Received {len(data)} features")

        # Validate feature count
        if len(data) != expected_n_features:
            raise ValueError(f"Expected {expected_n_features} features, but got {len(data)}")

        data = data.reshape(1, -1)

        # Make prediction
        prob = model.predict_proba(data)[:, 1][0]
        return {"prediction_probability": float(prob)}
    except ValueError as ve:
        print(f"Validation Error: {ve}")
        raise HTTPException(status_code=422, detail=str(ve))
    except Exception as e:
        print(f"Prediction Error: {e}")
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")


@app.get("/health")
def health():
    """
    Health check endpoint.
    """
    try:
        if model is None or expected_n_features is None:
            raise RuntimeError("Model or metadata is not loaded properly.")
        return {"status": "healthy"}
    except Exception as e:
        print(f"Health Check Error: {e}")
        raise HTTPException(status_code=500, detail=f"Health check failed: {e}")
