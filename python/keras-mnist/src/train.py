import os
from .data_loader import load_data
from .model import build_model

def main(model_file: str) -> None:
    (x_train, y_train), (x_test, y_test) = load_data()
    
    model = build_model()
    
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    model.fit(x_train, y_train, epochs=10, batch_size=32)

    model.save(model_file)