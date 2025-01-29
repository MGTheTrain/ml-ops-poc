import os
import numpy as np
from tensorflow.keras.models import load_model
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from .src.data_loader import load_data

app = FastAPI()

model_path = os.path.join("models", "mnist_model.h5")
model = load_model(model_path)

(x_train, y_train), (x_test, y_test) = load_data()

# Pydantic model to represent input data
class InferenceRequest(BaseModel):
    data: List[List[float]] 

# Inference function
def perform_inference(input_data: np.ndarray):
    predictions = model.predict(input_data)
    predicted_labels = np.argmax(predictions, axis=1)
    return predicted_labels.tolist()

# API endpoint to trigger inference
@app.post("/predict/")
async def predict(request: InferenceRequest):
    input_data = np.array(request.data)

    predictions = perform_inference(input_data)
    
    return {"predictions": predictions}