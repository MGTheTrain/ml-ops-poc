import tensorflow as tf
from tensorflow.keras.models import load_model
import tf2onnx
import os

class ONNXExporter:
    def export(self, model_path: str) -> None:
        """
        Exports a Keras model to an ONNX file.
        Takes the path to the Keras model, loads the model, and then converts it to ONNX.
        The ONNX file is saved with the same name as the Keras model, but with a .onnx extension.

        :param model_path: Path to the saved Keras model
        """
        try:
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"The model file does not exist at: {model_path}")

            model = load_model(model_path)
            model.output_names=['output'] # NOTE: See https://github.com/onnx/tensorflow-onnx/issues/2319
            onnx_model_path = os.path.splitext(model_path)[0] + ".onnx"
            input_signature = [tf.TensorSpec([None, 28, 28, 1], tf.float32, name="input")]
            
            onnx_model = tf2onnx.convert.from_keras(
                model,
                input_signature=input_signature,
                output_path=onnx_model_path  
            )
            
        except Exception as e:
            print(f"Error exporting model to ONNX: {e}")
