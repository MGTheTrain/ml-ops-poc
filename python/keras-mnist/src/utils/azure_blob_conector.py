from azure.storage.blob import BlobServiceClient
import os


class AzureBlobConnector:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string.strip("'")
        try:
            self.blob_service_client = BlobServiceClient.from_connection_string(
                self.connection_string
            )
            print("Successfully connected to Azure Blob Storage.")
        except Exception as e:
            print(f"Error: Could not connect to Azure Blob Storage. {e}")
            self.blob_service_client = None

    def upload(self, model_path: str, container_name: str, blob_name: str) -> None:
        """
        Upload a binary large obect to Azure Blob Storage.

        :param model_path: Path to the local model file to upload.
        :param container_name: The name of the Azure container.
        :param blob_name: The name to assign to the blob in the container.
        """
        try:
            blob_client = self.blob_service_client.get_blob_client(
                container=container_name, blob=blob_name
            )

            if not os.path.exists(model_path):
                print(f"Error: Model file '{model_path}' does not exist.")
                return

            with open(model_path, "rb") as data:
                blob_client.upload_blob(data, overwrite=True)

            print(f"Model uploaded to Azure Blob Storage: {container_name}/{blob_name}")
        except Exception as e:
            print(f"Error during upload: {e}")

    def download(self, container_name: str, blob_name: str, model_path: str) -> None:
        """
        Download a binary large obect from Azure Blob Storage.

        :param container_name: The name of the Azure container.
        :param blob_name: The name of the blob to download.
        :param model_path: The local file path to save the downloaded model.
        """
        try:
            blob_client = self.blob_service_client.get_blob_client(
                container=container_name, blob=blob_name
            )

            blob_properties = blob_client.get_blob_properties()
            if not blob_properties:
                print(
                    f"Error: Blob '{blob_name}' does not exist in container '{container_name}'."
                )
                return

            with open(model_path, "wb") as download_file:
                download_file.write(blob_client.download_blob().readall())

            print(
                f"Model downloaded from Azure Blob Storage: {container_name}/{blob_name} to {model_path}"
            )

        except Exception as e:
            print(f"Error during download: {e}")
