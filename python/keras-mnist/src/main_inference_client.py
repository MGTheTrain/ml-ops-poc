import os
import requests
from data_loaders.mnist_data_loader import MNISTDataLoader
import numpy as np
from typing import Any

url = os.getenv("INFERENCE_SERVICE_URL", "http://localhost:8080/predict")


def load_image_data(x_test: np.ndarray) -> np.ndarray:
    """
    Preprocess the image data for prediction.
    Reshapes the 28x28 images to the correct format.

    :param x_test: NumPy array of image data (shape: [n_samples, 28, 28])
    :return: Reshaped NumPy array of image data (shape: [n_samples, 28, 28])
    """
    x_test = x_test.reshape(x_test.shape[0], 28, 28)
    return x_test


def submit_prediction(image_data: Any) -> None:
    """
    Submit the prediction request to the inference service.

    :param image_data: List-like or array-like object containing image data.
    :return: None (handles printing the prediction results or errors)
    """
    payload = {"data": image_data.tolist()}

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            predictions = response.json()
            print(f"Predictions: {predictions}")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while sending the request: {e}")


def main() -> None:
    """
    Main entry point for loading data, preprocessing it, and submitting the prediction request.

    :return: None
    """
    data_loader = MNISTDataLoader()
    (x_train, y_train), (x_test, y_test) = data_loader.load(data_set_path="")
    image_data = load_image_data(x_test)
    submit_prediction(image_data)


if __name__ == "__main__":
    if not url:
        print("Error: Missing INFERENCE_SERVICE_URL environment variable.")
        exit(1)

    main()
