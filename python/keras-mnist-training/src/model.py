import tensorflow as tf
from tensorflow.keras import layers, models

def build_model():
    model = models.Sequential([
        layers.Dense(64, activation='relu', input_shape=(28, 28)),
        layers.Dense(10, activation='softmax')
    ])
    return model