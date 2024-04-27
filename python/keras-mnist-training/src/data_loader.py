import tensorflow as tf

def load_data():
    # Load MNIST dataset
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    
    # Normalize pixel values to the range [0, 1]
    x_train, x_test = x_train / 255.0, x_test / 255.0
    
    # Add channel dimension for convolutional networks
    x_train = x_train[..., tf.newaxis]
    x_test = x_test[..., tf.newaxis]
    
    return (x_train, y_train), (x_test, y_test)
