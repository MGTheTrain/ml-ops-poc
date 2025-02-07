import os
import requests
from src.data_loader import load_data

url = os.getenv("INFERENCE_SERVICE_URL", "http://localhost:8080/predict")

def load_image_data(x_test):
    """
    Preprocess the image data for prediction.
    Reshapes the 28x28 images to the correct format.
    """    
    x_test = x_test.reshape(x_test.shape[0], 28, 28)  
    return x_test  

def submit_prediction(image_data):
    """
    Submit the prediction request to the inference service.
    """
    payload = {
        "data": image_data.tolist()  
    }

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
    (x_train, y_train), (x_test, y_test) = load_data()
    image_data = load_image_data(x_test)  
    submit_prediction(image_data)  

if __name__ == "__main__":
    if not url:
        print("Error: Missing INFERENCE_SERVICE_URL environment variable.")
        exit(1)
    
    main()
