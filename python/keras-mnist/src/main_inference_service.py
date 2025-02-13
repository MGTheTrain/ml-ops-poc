import os
from typing import Tuple
import uvicorn
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from inferences.mnist_inference import MNISTInference
from utils.azure_blob_conector import AzureBlobConnector


class InferenceRequest(BaseModel):
    data: list


class InferenceResponse(BaseModel):
    predictions: list


def load_environment_variables() -> Tuple[str, str, str, str, int]:
    """Load required environment variables."""
    model_path = os.getenv("MODEL_PATH", "../models/mnist_model.h5")
    az_sa_connection_string = os.getenv("AZ_SA_CONNECTION_STRING")
    az_sa_container_name = os.getenv("AZ_SA_CONTAINER_NAME")
    blob_name = os.getenv("BLOB_NAME")
    port = os.getenv("PORT", 8080)

    if not all([model_path, port]):
        print(
            "Missing required arguments for downloading model. Please ensure the following environment variables are set:"
        )
        print("MODEL_PATH, PORT")
        os.exit(1)

    return model_path, az_sa_connection_string, az_sa_container_name, blob_name, port


def download_model(
    az_sa_connection_string: str,
    model_path: str,
    az_sa_container_name: str,
    blob_name: str,
) -> None:
    """Download the model from Azure Blob Storage."""
    az_blob_connector = AzureBlobConnector(az_sa_connection_string)
    az_blob_connector.download(
        model_path=model_path, container_name=az_sa_container_name, blob_name=blob_name
    )


def setup_fastapi(app: FastAPI, inference_service: MNISTInference, model_path: str) -> None:
    """Set up FastAPI routes and prediction endpoint."""

    @app.post("/predict", response_model=InferenceResponse)
    async def predict(request: InferenceRequest) -> InferenceResponse:
        predictions = inference_service.predict(request.data, model_path)
        return InferenceResponse(predictions=predictions.tolist())

    @app.get("/health")
    async def health_check():
        return {"status": "healthy"}


def main():
    """Main function to set up the app."""
    app = FastAPI()
    model_path, az_sa_connection_string, az_sa_container_name, blob_name, port = (
        load_environment_variables()
    )
    if az_sa_connection_string or az_sa_container_name or blob_name:
        download_model(
            az_sa_connection_string, model_path, az_sa_container_name, blob_name
        )
    inference_service = MNISTInference()
    setup_fastapi(app, inference_service, model_path)
    uvicorn.run(app, host="0.0.0.0", port=int(port))


if __name__ == "__main__":
    main()
