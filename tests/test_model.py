import unittest
import requests
import pandas as pd


class TestPredictionEndpoint(unittest.TestCase):
    """
    Unit test for testing the /predict endpoint of the FastAPI app.
    """
    API_URL = "http://localhost:8080/predict"
    OBSERVATION_FILE = "data/observation.csv"

    def setUp(self):
        """
        Set up the test by loading a single observation from the CSV file.
        """
        try:
            # Load the single observation from the CSV file
            self.df = pd.read_csv(self.OBSERVATION_FILE)
            if self.df.empty:
                raise ValueError("The input file is empty. Cannot perform prediction.")

            # Extract features from the first row as a list of floats
            self.features = self.df.iloc[0].tolist()
        except FileNotFoundError:
            self.fail(f"Input file '{self.OBSERVATION_FILE}' not found.")
        except ValueError as ve:
            self.fail(str(ve))

    def test_valid_payload(self):
        """
        Test the /predict endpoint with a valid payload.
        """
        payload = {"features": self.features}

        response = requests.post(self.API_URL, json=payload)
        self.assertEqual(response.status_code, 200, f"Expected status code 200, got {response.status_code}")
        response_json = response.json()
        self.assertIn("prediction_probability", response_json, "Response does not contain 'prediction_probability'")
        self.assertIsInstance(response_json["prediction_probability"], float,
                              "Prediction probability should be a float")
        print(f"Valid Payload Test Passed: {response_json['prediction_probability']}")

    def test_missing_features(self):
        """
        Test the /predict endpoint with missing 'features' in the payload.
        """
        payload = {}
        response = requests.post(self.API_URL, json=payload)
        self.assertEqual(response.status_code, 422, f"Expected status code 422, got {response.status_code}")
        print("Missing Features Test Passed")

    def test_extra_features(self):
        """
        Test the /predict endpoint with more features than expected.
        """
        payload = {"features": self.features + [0.1]}  # Add one extra feature
        response = requests.post(self.API_URL, json=payload)
        self.assertEqual(response.status_code, 422, f"Expected status code 422, got {response.status_code}")
        print("Extra Features Test Passed")

    def test_fewer_features(self):
        """
        Test the /predict endpoint with fewer features than expected.
        """
        payload = {"features": self.features[:-1]}  # Remove one feature
        response = requests.post(self.API_URL, json=payload)
        self.assertEqual(response.status_code, 422, f"Expected status code 422, got {response.status_code}")
        print("Fewer Features Test Passed")

    def test_invalid_data_types(self):
        """
        Test the /predict endpoint with invalid data types in the features.
        """
        invalid_features = ["string"] * len(self.features)
        payload = {"features": invalid_features}
        response = requests.post(self.API_URL, json=payload)
        self.assertEqual(response.status_code, 422, f"Expected status code 422, got {response.status_code}")
        print("Invalid Data Types Test Passed")

    def test_empty_payload(self):
        """
        Test the /predict endpoint with an empty payload.
        """
        payload = {}
        response = requests.post(self.API_URL, json=payload)
        self.assertEqual(response.status_code, 422, f"Expected status code 422, got {response.status_code}")
        print("Empty Payload Test Passed")

    def test_large_feature_values(self):
        """
        Test the /predict endpoint with extremely large feature values.
        """
        large_features = [1e6] * len(self.features)
        payload = {"features": large_features}
        response = requests.post(self.API_URL, json=payload)
        self.assertEqual(response.status_code, 200, f"Expected status code 200, got {response.status_code}")
        response_json = response.json()
        self.assertIn("prediction_probability", response_json, "Response does not contain 'prediction_probability'")
        print(f"Large Feature Values Test Passed: {response_json['prediction_probability']}")

    def test_negative_feature_values(self):
        """
        Test the /predict endpoint with negative feature values.
        """
        negative_features = [-1.0] * len(self.features)
        payload = {"features": negative_features}
        response = requests.post(self.API_URL, json=payload)
        self.assertEqual(response.status_code, 200, f"Expected status code 200, got {response.status_code}")
        response_json = response.json()
        self.assertIn("prediction_probability", response_json, "Response does not contain 'prediction_probability'")
        print(f"Negative Feature Values Test Passed: {response_json['prediction_probability']}")


if __name__ == "__main__":
    unittest.main()
