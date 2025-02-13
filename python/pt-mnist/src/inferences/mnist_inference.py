import torch
from data_loaders.mnist_data_loader import MNISTDataLoader
from models.simple_nn import SimpleNN
from inferences.inference_interface import InferenceInterface


class MNISTInference(InferenceInterface):
    def infer(self, model_path: str = "../models/mnist_model.h5") -> None:
        model_builder = SimpleNN()
        model = model_builder.build()
        model.load_state_dict(torch.load(model_path))
        model.eval()

        data_loader = MNISTDataLoader()
        (x_train, y_train), (x_test, y_test) = data_loader.load()
        x_test_tensor = torch.tensor(x_test, dtype=torch.float32)

        with torch.no_grad():
            outputs = model(x_test_tensor)
            _, predicted_labels = torch.max(outputs, 1)

        print("Predicted labels:", predicted_labels.numpy())
