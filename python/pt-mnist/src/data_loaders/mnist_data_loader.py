import os
import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from typing import Tuple
from data_loaders.data_loader_interface import DataLoaderInterface


class MNISTDataLoader(DataLoaderInterface):
    def load(self, data_set_path: str = "") -> Tuple[Tuple, Tuple]:
        """
        Loads the MNIST dataset. If a dataset path is provided, it attempts to load from there.
        Otherwise, it downloads the dataset from torchvision.

        :param data_set_path: Optional directory to load the dataset from.
        :return: A tuple of tuples containing (x_train, y_train) and (x_test, y_test).
        """
        transform = transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))]
        )

        if data_set_path != "":
            print(f"Attempting to load dataset from {data_set_path}")

            if os.path.exists(data_set_path):
                try:

                    train_dataset = datasets.MNIST(
                        root=data_set_path,
                        train=True,
                        download=False,
                        transform=transform,
                    )
                    test_dataset = datasets.MNIST(
                        root=data_set_path,
                        train=False,
                        download=False,
                        transform=transform,
                    )
                    print(f"Loaded dataset from {data_set_path}")
                except Exception as e:
                    print(f"Error loading dataset from {data_set_path}: {e}")
                    print("Falling back to downloading the dataset...")

                    train_dataset = datasets.MNIST(
                        root="./data", train=True, download=True, transform=transform
                    )
                    test_dataset = datasets.MNIST(
                        root="./data", train=False, download=True, transform=transform
                    )
            else:
                print(
                    f"Dataset directory {data_set_path} does not exist. Falling back to downloading the dataset..."
                )
                train_dataset = datasets.MNIST(
                    root="./data", train=True, download=True, transform=transform
                )
                test_dataset = datasets.MNIST(
                    root="./data", train=False, download=True, transform=transform
                )
        else:

            train_dataset = datasets.MNIST(
                root="./data", train=True, download=True, transform=transform
            )
            test_dataset = datasets.MNIST(
                root="./data", train=False, download=True, transform=transform
            )
            print("Loaded dataset using torchvision.datasets.MNIST")

        train_loader = DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)
        test_loader = DataLoader(dataset=test_dataset, batch_size=64, shuffle=False)

        x_train, y_train = zip(*[batch for batch in train_loader])
        x_test, y_test = zip(*[batch for batch in test_loader])

        x_train = torch.cat(x_train)
        y_train = torch.cat(y_train)
        x_test = torch.cat(x_test)
        y_test = torch.cat(y_test)

        print(f"x_train shape: {x_train.shape}")
        print(f"y_train shape: {y_train.shape}")
        print(f"x_test shape: {x_test.shape}")
        print(f"y_test shape: {y_test.shape}")

        return (x_train, y_train), (x_test, y_test)
