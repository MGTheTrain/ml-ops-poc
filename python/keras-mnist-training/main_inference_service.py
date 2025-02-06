import os
import uvicorn
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from src.inference import InferenceService
from src.utils import AzureBlobConnector

class InferenceRequest(BaseModel):
    data: list

class InferenceResponse(BaseModel):
    predictions: list

def load_environment_variables():
    """Load required environment variables."""
    model_file = os.getenv("MODEL_FILE", "models/mnist_model.h5")
    az_sa_connection_string = os.getenv("AZ_SA_CONNECTION_STRING")
    az_sa_container_name = os.getenv("AZ_SA_CONTAINER_NAME")
    blob_name = os.getenv("BLOB_NAME")
    port = os.getenv("PORT", 8080)

    if not all([model_file, az_sa_connection_string, az_sa_container_name, blob_name, port]):
        print("Missing required arguments for downloading model. Please ensure the following environment variables are set:")
        print("MODEL_FILE, AZ_SA_CONNECTION_STRING, AZ_SA_CONTAINER_NAME, BLOB_NAME, PORT")
        os.exit(1)
    
    return model_file, az_sa_connection_string, az_sa_container_name, blob_name, port

def download_model(az_sa_connection_string, model_file, az_sa_container_name, blob_name):
    """Download the model from Azure Blob Storage."""
    az_blob_connector = AzureBlobConnector(az_sa_connection_string)
    az_blob_connector.download(
        model_file=model_file,
        container_name=az_sa_container_name,
        blob_name=blob_name
    )

def create_inference_service(model_file):
    """Create and return the InferenceService instance."""
    return InferenceService(model_file)

def setup_fastapi(app, inference_service):
    """Set up FastAPI routes and prediction endpoint."""
    @app.post("/predict", response_model=InferenceResponse)
    async def predict(request: InferenceRequest):
        data = np.array(request.data).reshape(-1, 28, 28) 
        predictions = inference_service.predict(data)
        return InferenceResponse(predictions=predictions.tolist())

    @app.get("/health")
    async def health_check():
        return {"status": "healthy"}

def main():
    """Main function to set up the app."""
    app = FastAPI()
    model_file, az_sa_connection_string, az_sa_container_name, blob_name, port = load_environment_variables()
    download_model(az_sa_connection_string, model_file, az_sa_container_name, blob_name)
    inference_service = create_inference_service(model_file)
    setup_fastapi(app, inference_service)
    uvicorn.run(app, host="0.0.0.0", port=int(port))

if __name__ == "__main__":
    main()
