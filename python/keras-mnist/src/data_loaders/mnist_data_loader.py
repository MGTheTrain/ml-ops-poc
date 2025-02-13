from data_loaders.data_loader_interface import DataLoaderInterface
import tensorflow as tf
import numpy as np
import os
from typing import Tuple


class MNISTDataLoader(DataLoaderInterface):
    def load(self, data_set_path: str = "") -> Tuple[Tuple, Tuple]:
        """
        Loads the MNIST dataset. If a dataset directory is provided, it attempts to load from there.
        Otherwise, it loads the dataset using `tf.keras.datasets.mnist.load_data()`.

        :param data_set_path: Optional directory to load the dataset from.
        :return: A tuple of tuples containing (x_train, y_train) and (x_test, y_test).
        """
        if data_set_path != "":
            print(f"Attempting to load dataset from {data_set_path}")

            if os.path.exists(data_set_path):
                try:
                    data = np.load(os.path.join(data_set_path))  # e.g. mnist_data.npz
                    x_train, y_train = data["x_train"], data["y_train"]
                    x_test, y_test = data["x_test"], data["y_test"]
                    print(f"Loaded dataset from {data_set_path}")
                except Exception as e:
                    print(f"Error loading dataset from {data_set_path}: {e}")
                    print("Falling back to tf.keras.datasets.mnist...")
                    (x_train, y_train), (x_test, y_test) = (
                        tf.keras.datasets.mnist.load_data()
                    )
            else:
                print(
                    f"Dataset directory {data_set_path} does not exist. Falling back to tf.keras.datasets.mnist..."
                )
                (x_train, y_train), (x_test, y_test) = (
                    tf.keras.datasets.mnist.load_data()
                )
        else:
            (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
            print("Loaded dataset from tf.keras.datasets.mnist")

        x_train, x_test = x_train / 255.0, x_test / 255.0

        x_train = x_train[..., tf.newaxis]
        x_test = x_test[..., tf.newaxis]

        print("x_train shape:", x_train.shape)
        print("y_train shape:", y_train.shape)
        print("x_test shape:", x_test.shape)
        print("y_test shape:", y_test.shape)

        return (x_train, y_train), (x_test, y_test)
