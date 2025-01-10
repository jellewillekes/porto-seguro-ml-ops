import requests


def prediction_endpoint():
    # Define the API endpoint
    url = "http://localhost:8080/predict"

    # Sample feature vector for the Porto Seguro dataset
    payload = {
        "features": [
            0.5, 1.3, 0.0, 2.1, 0.0, 1.0, 0.2, 0.8, 0.0, 0.5,
            1.7, 1.0, 2.4, 1.3, 0.0, 0.0, 3.2, 0.5, 0.7, 1.1,
            2.3, 0.0, 1.5, 0.3, 0.8, 0.9, 1.2, 2.0, 1.0, 0.0,
            0.3, 0.6, 0.4, 0.8, 1.9, 0.7, 0.2, 1.4, 0.0, 1.3,
            2.5, 0.0, 1.8, 0.0, 1.0, 0.4, 0.2, 1.6, 0.9, 0.0,
            1.2, 0.7, 1.5, 0.3, 1.9, 0.6, 0.8
        ]
    }

    # Send POST request to the endpoint
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an error for HTTP status codes 4xx/5xx

        # Print the prediction response
        print("Response from the API:")
        print(response.json())
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    prediction_endpoint()
