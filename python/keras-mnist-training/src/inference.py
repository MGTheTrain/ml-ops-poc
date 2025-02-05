import os
import numpy as np
from tensorflow.keras.models import load_model
from .data_loader import load_data

def main(model_file: str) -> None:
    model = load_model(model_file)

    (x_train, y_train), (x_test, y_test) = load_data()
    
    predictions = model.predict(x_test)
    predicted_labels = np.argmax(predictions, axis=1)
    
    print("Predicted labels:", predicted_labels)

class InferenceService:
    def __init__(self, model_file: str):
        self.model = load_model(model_file)

    def predict(self, data: np.ndarray) -> np.ndarray:
        predictions = self.model.predict(data)
        return np.argmax(predictions, axis=1)