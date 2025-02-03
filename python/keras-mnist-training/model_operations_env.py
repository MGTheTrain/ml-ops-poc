import os
from src import train, inference, utils

def main():
    mode = os.getenv("MODE", "train")  
    model_file = os.getenv("MODEL_FILE", "models/mnist_model.h5")
    connection_string = os.getenv("AZURE_CONNECTION_STRING")
    container_name = os.getenv("AZURE_CONTAINER_NAME")
    blob_name = os.getenv("AZURE_BLOB_NAME")
    
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
        if not all([model_file, connection_string, container_name, blob_name]):
            print("Missing required arguments for uploading model. Please ensure the following environment variables are set:")
            print("MODEL_FILE, AZURE_CONNECTION_STRING, AZURE_CONTAINER_NAME, AZURE_BLOB_NAME")
            return
        azure_blob_connector = utils.AzureBlobConnector(connection_string)
        azure_blob_connector.upload(
            model_file=model_file,
            container_name=container_name,
            blob_name=blob_name
        )
    
    elif mode == "download-model":
        if not all([model_file, connection_string, container_name, blob_name]):
            print("Missing required arguments for downloading model. Please ensure the following environment variables are set:")
            print("MODEL_FILE, AZURE_CONNECTION_STRING, AZURE_CONTAINER_NAME, AZURE_BLOB_NAME")
            return
        azure_blob_connector = utils.AzureBlobConnector(connection_string)
        azure_blob_connector.download(
            model_file=model_file,
            container_name=container_name,
            blob_name=blob_name
        )

if __name__ == "__main__":
    main()
