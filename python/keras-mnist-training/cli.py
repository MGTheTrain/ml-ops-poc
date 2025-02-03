import argparse
from src import train, inference, utils

def main():
    parser = argparse.ArgumentParser(description="Train or perform inference with the MNIST model")
    
    parser.add_argument("--mode", required=True, choices=["train", "inference", "upload-model", "download-model"],
                        help="Select 'train' to train the model, 'inference' to perform inference, 'upload-model' to upload the model, or 'download-model' to download the model")

    parser.add_argument("--model_file", default="models/mnist_model.h5", help="Path to the model file")
    parser.add_argument("--connection_string", help="Azure connection string. Required in case mode is either 'upload-model' or 'download-model'")
    parser.add_argument("--container_name", help="Azure container name. Required in case mode is either 'upload-model' or 'download-model'")
    parser.add_argument("--blob_name", help="Blob name. Required in case mode is either 'upload-model' or 'download-model'")

    args = parser.parse_args()

    if args.mode == "train":
        if not args.model_file:
            parser.print_help()
            return
        train.main(args.model_file)

    elif args.mode == "inference":
        if not args.model_file:
            parser.print_help()
            return
        inference.main(args.model_file)

    elif args.mode == "upload-model":
        if not all([args.model_file, args.connection_string, args.container_name, args.blob_name]):
            parser.print_help()
            return

        azure_blob_connector = utils.AzureBlobConnector(args.connection_string)
        azure_blob_connector.upload(
            model_file=args.model_file,
            container_name=args.container_name,
            blob_name=args.blob_name
        )
    
    elif args.mode == "download-model":
        if not all([args.model_file, args.connection_string, args.container_name, args.blob_name]):
            parser.print_help()
            return

        azure_blob_connector = utils.AzureBlobConnector(args.connection_string)
        azure_blob_connector.download(
            model_file=args.model_file,
            container_name=args.container_name,
            blob_name=args.blob_name
        )

if __name__ == "__main__":
    main()
