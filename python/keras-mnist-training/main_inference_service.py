from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from src.inference import InferenceService

app = FastAPI()
 
model_file = os.getenv("MODEL_FILE", "models/mnist_model.h5")
az_sa_connection_string = os.getenv("AZ_SA_CONNECTION_STRING")
az_sa_container_name = os.getenv("AZ_SA_CONTAINER_NAME")
blob_name = os.getenv("BLOB_NAME")
port = os.getenv("PORT", 8080)

if not all([model_file, az_sa_connection_string, az_sa_container_name, blob_name, port]):
    print("Missing required arguments for downloading model. Please ensure the following environment variables are set:")
    print("MODEL_FILE, AZ_SA_CONNECTION_STRING, AZ_SA_CONTAINER_NAME, BLOB_NAME, PORT")

az_blob_connector = utils.AzureBlobConnector(az_sa_connection_string)
az_blob_connector.download(
    model_file=model_file,
    container_name=az_sa_container_name,
    blob_name=blob_name
)

inference_service = InferenceService(model_file)

class InferenceRequest(BaseModel):
    data: list 

class InferenceResponse(BaseModel):
    predictions: list 

@app.post("/predict", response_model=InferenceResponse)
async def predict(request: InferenceRequest):
    data = np.array(request.data).reshape(1, -1) 
    predictions = inference_service.predict(data)
    return InferenceResponse(predictions=predictions.tolist())

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)