import argparse
import os
from training.mnist_training import MNISTTraining
from inferences.mnist_inference import MNISTInference

def parse_cli_args() -> argparse.Namespace:
    """
    Parse command-line arguments.
    
    :return: The parsed arguments as an argparse.Namespace object
    """
    parser = argparse.ArgumentParser(
        description="Train or perform inference"
    )
    parser.add_argument(
        "--mode",
        choices=["train", "inference"],
        help="Select 'train' to train the model or 'inference' to perform inference",
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
    
    return parser.parse_args()

def set_from_env(args: argparse.Namespace) -> argparse.Namespace:
    """
    Override CLI arguments with environment variables if they exist.

    :param args: The argparse Namespace object containing the parsed arguments
    :return: The updated argparse Namespace object with environment variables, if set
    """
    if 'MODE' in os.environ:
        args.mode = os.environ['MODE']
    if 'MODEL_PATH' in os.environ:
        args.model_path = os.environ['MODEL_PATH']
    if 'DATA_SET_PATH' in os.environ:
        args.data_set_path = os.environ['DATA_SET_PATH']
    return args

def main():
    # Parse CLI arguments first
    args = parse_cli_args()
    
    # Override with environment variables if those exist
    args = set_from_env(args)

    if args.mode == "train":
        mnist_training = MNISTTraining()
        mnist_training.train(model_path=args.model_path, data_set_path=args.data_set_path)
    elif args.mode == "inference":
        mnist_inference = MNISTInference()
        mnist_inference.infer(model_path=args.model_path)

if __name__ == "__main__":
    main()