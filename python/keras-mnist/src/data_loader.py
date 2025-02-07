import tensorflow as tf

def load_data():
    # Load MNIST dataset
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    
    # Print shapes of loaded data
    print("x_train shape:", x_train.shape)
    print("y_train shape:", y_train.shape)
    print("x_test shape:", x_test.shape)
    print("y_test shape:", y_test.shape)
    
    # Normalize pixel values to the range [0, 1]
    x_train, x_test = x_train / 255.0, x_test / 255.0
    
    # Reshape images to have a channel dimension
    x_train = x_train[..., tf.newaxis]
    x_test = x_test[..., tf.newaxis]
    
    return (x_train, y_train), (x_test, y_test)