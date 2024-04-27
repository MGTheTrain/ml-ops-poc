import os
import numpy as np
from tensorflow.keras.models import load_model
from .data_loader import load_data  # Import the data loading function if needed

def main():
    # Load saved model
    model_path = os.path.join("models", "mnist_model.h5")
    model = load_model(model_path)

    # Load data for inference
    (x_train, y_train), (x_test, y_test) = load_data()
    
    # Perform inference
    predictions = model.predict(x_test)
    predicted_labels = np.argmax(predictions, axis=1)
    
    # Output predictions or perform further processing
    print("Predicted labels:", predicted_labels)