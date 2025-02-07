import argparse
from src import train, inference

def main():
    parser = argparse.ArgumentParser(description="Train or perform inference with the MNIST model")
    parser.add_argument("--mode", choices=["train", "inference"], help="Select 'train' to train the model or 'inference' to perform inference")
    args = parser.parse_args()

    if args.mode == "train":
        train.main()
    elif args.mode == "inference":
        inference.main()

if __name__ == "__main__":
    main()
