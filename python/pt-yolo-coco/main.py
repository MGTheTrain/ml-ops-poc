import argparse
from src import train, inference

def main():
    parser = argparse.ArgumentParser(description="Train or perform inference with the MNIST model")
    parser.add_argument("--mode", choices=["train", "inference"], help="Select 'train' to train the model or 'inference' to perform inference")
    parser.add_argument("--image_path", default="", help="When the inference mode is chosen, the image path is needed")
    args = parser.parse_args()

    if args.mode == "train":
        train.main()
    elif args.mode == "inference":
        if args.image_path != "":
            inference.main(args.image_path)


if __name__ == "__main__":
    main()
