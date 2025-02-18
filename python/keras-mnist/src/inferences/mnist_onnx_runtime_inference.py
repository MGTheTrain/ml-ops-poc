import numpy as np
import onnxruntime as ort
from data_loaders.mnist_data_loader import MNISTDataLoader
from inferences.inference_interface import InferenceInterface

class MNISTONNXRuntimeInference(InferenceInterface):
    
    def infer(self, model_path: str = "../models/mnist_model.onnx") -> None:
        # Load the ONNX model using ONNX Runtime
        session = ort.InferenceSession(model_path)

        data_loader = MNISTDataLoader()
        (x_train, y_train), (x_test, y_test) = data_loader.load()

        # Prepare input data (need to make sure the data is in the correct shape)
        input_name = session.get_inputs()[0].name
        x_test = x_test.astype(np.float32)

        # Run inference with the ONNX model
        predictions = session.run(None, {input_name: x_test})

        # Convert predictions into labels
        predicted_labels = np.argmax(predictions[0], axis=1)

        print("Predicted labels:", predicted_labels)

    def predict(self, data: np.ndarray, model_path: str = "../models/mnist_model.onnx") -> np.ndarray:
        # Load the ONNX model using ONNX Runtime
        session = ort.InferenceSession(model_path)

        # Prepare the input data for prediction (ensure the correct shape and dtype)
        input_name = session.get_inputs()[0].name
        data = np.array(data).reshape(-1, 28, 28, 1).astype(np.float32)

        # Run inference and return predicted labels
        predictions = session.run(None, {input_name: data})
        return np.argmax(predictions[0], axis=1)
