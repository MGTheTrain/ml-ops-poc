import argparse
import os
from training.mnist_training import MNISTTraining
from inferences.mnist_inference import MNISTInference
from inferences.mnist_onnx_runtime_inference import MNISTONNXRuntimeInference
from utils.azure_blob_conector import AzureBlobConnector
from utils.onnx_exporter import ONNXExporter


def parse_cli_args() -> argparse.Namespace:
    """
    Parse command-line arguments.

    :return: The parsed arguments as an argparse.Namespace object
    """
    parser = argparse.ArgumentParser(description="Train or perform inference")
    parser.add_argument(
        "--mode",
        choices=["train", "inference", "upload-model", "download-model", "export-onnx"],
        help="Select 'train' to train the model, 'inference' to perform inference, 'upload-model' to upload trained models, 'download-model' to download trained models and 'export-onnx' for exprting onnx files",
    )
    parser.add_argument(
        "--model_path",
        default="../models/mnist_model.h5",
        help="Set the model path in which to store after training or load the model for inference",
    )
    parser.add_argument(
        "--data_set_path",
        default="",
        help="Set the data set path which to load for training",
    )
    parser.add_argument(
        "--connection_string",
        help="Azure connection string. Required in case mode is either 'upload-model' or 'download-model'",
    )
    parser.add_argument(
        "--container_name",
        help="Azure container name. Required in case mode is either 'upload-model' or 'download-model'",
    )
    parser.add_argument(
        "--blob_name",
        help="Blob name. Required in case mode is either 'upload-model' or 'download-model'",
    )

    return parser.parse_args()


def set_from_env(args: argparse.Namespace) -> argparse.Namespace:
    """
    Override CLI arguments with environment variables if they exist.

    :param args: The argparse Namespace object containing the parsed arguments
    :return: The updated argparse Namespace object with environment variables, if set
    """
    if "MODE" in os.environ:
        args.mode = os.environ["MODE"]
    if "MODEL_PATH" in os.environ:
        args.model_path = os.environ["MODEL_PATH"]
    if "DATA_SET_PATH" in os.environ:
        args.data_set_path = os.environ["DATA_SET_PATH"]
    if "AZ_SA_CONNECTION_STRING" in os.environ:
        args.az_sa_connection_string = os.environ["AZ_SA_CONNECTION_STRING"]
    if "AZ_SA_CONTAINER_NAME" in os.environ:
        args.az_sa_container_name = os.environ["AZ_SA_CONTAINER_NAME"]
    if "BLOB_NAME" in os.environ:
        args.blob_name = os.environ["BLOB_NAME"]
    return args


def main():
    # Parse CLI arguments first
    args = parse_cli_args()

    # Override with environment variables if those exist
    args = set_from_env(args)

    if args.mode == "train":
        mnist_training = MNISTTraining()
        mnist_training.train(
            model_path=args.model_path, data_set_path=args.data_set_path
        )
    elif args.mode == "inference":
        if ".h5" in args.model_path:
            mnist_inference = MNISTInference()
            mnist_inference.infer(model_path=args.model_path)
        elif ".onnx" in args.model_path:
            mnist_inference = MNISTONNXRuntimeInference()
            mnist_inference.infer(model_path=args.model_path)

    elif args.mode == "upload-model":
        az_blob_connector = AzureBlobConnector(args.az_sa_connection_string)
        az_blob_connector.upload(
            model_path=args.model_path,
            container_name=args.az_sa_container_name,
            blob_name=args.blob_name,
        )
    elif args.mode == "download-model":
        az_blob_connector = AzureBlobConnector(args.az_sa_connection_string)
        az_blob_connector.download(
            model_path=args.model_path,
            container_name=args.az_sa_container_name,
            blob_name=args.blob_name,
        )
    elif args.mode == "export-onnx":
        onnx_exporter = ONNXExporter()
        onnx_exporter.export(args.model_path)

if __name__ == "__main__":
    main()
