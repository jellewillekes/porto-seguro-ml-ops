import requests
import pandas as pd


def load_observation_and_predict():
    url = "http://127.0.0.1:56920/predict"
    input_file = "data/observation.csv"

    try:
        # Load the observation
        df = pd.read_csv(input_file)
        if df.empty:
            raise ValueError("The input file is empty. Cannot perform prediction.")

        features = df.iloc[0].tolist()

        # Validate feature length
        if len(features) != 91:
            raise ValueError(f"Feature count mismatch. Expected 91, but got {len(features)}")

        payload = {"features": features}

        # Log the payload
        print("Payload:", payload)

        # Send POST request
        response = requests.post(url, json=payload)
        response.raise_for_status()

        print("Prediction Response:", response.json())
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    load_observation_and_predict()
