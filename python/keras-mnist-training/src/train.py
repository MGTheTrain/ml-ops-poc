from .data_loader import load_data
from .model import build_model

def main():
    # Load data
    (x_train, y_train), (x_test, y_test) = load_data()
    
    # Build model
    model = build_model()
    
    # Compile model
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    # Train model using training data
    model.fit(x_train, y_train, epochs=10, batch_size=32)