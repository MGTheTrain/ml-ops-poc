import numpy as np
from tensorflow.keras.models import load_model
from data_loaders.mnist_data_loader import MNISTDataLoader
from inferences.inference_interface import InferenceInterface


class MNISTInference(InferenceInterface):
    def infer(self, model_path: str = "../models/mnist_model.h5") -> None:
        model = load_model(model_path)

        data_loader = MNISTDataLoader()
        (x_train, y_train), (x_test, y_test) = data_loader.load()

        predictions = model.predict(x_test)
        predicted_labels = np.argmax(predictions, axis=1)

        print("Predicted labels:", predicted_labels)

    def predict(self, data: np.ndarray, model_path: str = "../models/mnist_model.h5") -> np.ndarray:
        model = load_model(model_path)
        data = np.array(data).reshape(-1, 28, 28)
        predictions = model.predict(data)
        return np.argmax(predictions, axis=1)
