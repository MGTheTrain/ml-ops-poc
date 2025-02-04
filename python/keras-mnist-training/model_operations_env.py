import os
from src import train, inference, utils

def main():
    mode = os.getenv("MODE", "train")  
    model_file = os.getenv("MODEL_FILE", "models/mnist_model.h5")
    az_sa_connection_string = os.getenv("AZ_SA_CONNECTION_STRING")
    az_sa_container_name = os.getenv("AZ_SA_CONTAINER_NAME")
    blob_name = os.getenv("BLOB_NAME")
    
    if mode not in ["train", "inference", "upload-model", "download-model"]:
        print("Invalid mode. Set the MODE environment variable to one of ['train', 'inference', 'upload-model', 'download-model']")
        return
    
    if mode == "train":
        if not model_file:
            print("Missing model file. Please set the MODEL_FILE environment variable.")
            return
        train.main(model_file)
    
    elif mode == "inference":
        if not model_file:
            print("Missing model file. Please set the MODEL_FILE environment variable.")
            return
        inference.main(model_file)
    
    elif mode == "upload-model":
        if not all([model_file, az_sa_connection_string, az_sa_container_name, blob_name]):
            print("Missing required arguments for uploading model. Please ensure the following environment variables are set:")
            print("MODEL_FILE, AZ_SA_CONNECTION_STRING, AZ_SA_CONTAINER_NAME, BLOB_NAME")
            return
        az_blob_connector = utils.AzureBlobConnector(az_sa_connection_string)
        az_blob_connector.upload(
            model_file=model_file,
            container_name=az_sa_container_name,
            blob_name=blob_name
        )
    
    elif mode == "download-model":
        if not all([model_file, az_sa_connection_string, az_sa_container_name, blob_name]):
            print("Missing required arguments for downloading model. Please ensure the following environment variables are set:")
            print("MODEL_FILE, AZ_SA_CONNECTION_STRING, AZ_SA_CONTAINER_NAME, BLOB_NAME")
            return
        az_blob_connector = utils.AzureBlobConnector(az_sa_connection_string)
        az_blob_connector.download(
            model_file=model_file,
            container_name=az_sa_container_name,
            blob_name=blob_name
        )

if __name__ == "__main__":
    main()
