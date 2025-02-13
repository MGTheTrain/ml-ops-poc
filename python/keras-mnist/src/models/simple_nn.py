from tensorflow.keras import layers, models
from models.model_interface import ModelInterface


class SimpleNN(ModelInterface):
    def build(self):
        model = models.Sequential(
            [
                layers.Flatten(input_shape=(28, 28)),
                layers.Dense(128, activation="relu"),
                layers.Dense(10, activation="softmax"),
            ]
        )
        model.summary()
        return model
