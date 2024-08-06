# evaluate_model.py

import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from data_preprocessing import load_data

def load_model(model_path='saved_models/mnist_cnn_model.h5'):
    """
    Load a saved model from the specified path.
    
    Args:
        model_path (str): Path to the saved model file.
    
    Returns:
        model (tf.keras.Model): Loaded Keras model.
    """
    return tf.keras.models.load_model(model_path)

def evaluate_model(model, test_images, test_labels):
    """
    Evaluate the model on the test data.
    
    Args:
        model (tf.keras.Model): Trained Keras model.
        test_images (numpy.ndarray): Test images.
        test_labels (numpy.ndarray): Test labels (one-hot encoded).
    """
    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
    print(f'Test accuracy: {test_acc * 100:.2f}%')
    print(f'Test loss: {test_loss:.4f}')

if __name__ == "__main__":
    # Load and preprocess the data
    (train_images, train_labels), (test_images, test_labels) = load_data()
    
    # One-hot encode the labels
    test_labels = to_categorical(test_labels, 10)
    
    # Load the trained model
    model = load_model()
    
    # Evaluate the model
    evaluate_model(model, test_images, test_labels)
