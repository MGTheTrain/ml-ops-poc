import os
import numpy as np
from tensorflow.keras.models import load_model
from .data_loader import load_data

def main(model_file: str) -> None:
    model = load_model(model_file)

    # Load data for inference
    (x_train, y_train), (x_test, y_test) = load_data()
    
    # Perform inference
    predictions = model.predict(x_test)
    predicted_labels = np.argmax(predictions, axis=1)
    
    # Output predictions or perform further processing
    print("Predicted labels:", predicted_labels)