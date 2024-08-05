# data_preprocessing.py

import tensorflow as tf
from tensorflow.keras import datasets
import numpy as np

def load_data():
    """
    Load the MNIST dataset and normalize the images.

    Returns:
        tuple: A tuple containing training and test data:
               (train_images, train_labels), (test_images, test_labels)
    """
    # Load the MNIST dataset
    (train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

    # Normalize the images to [0, 1] range
    train_images = train_images / 255.0
    test_images = test_images / 255.0

    # Add a channel dimension (since the images are grayscale)
    train_images = np.expand_dims(train_images, axis=-1)
    test_images = np.expand_dims(test_images, axis=-1)

    return (train_images, train_labels), (test_images, test_labels)

def preprocess_images(images):
    """
    Preprocess the input images.

    Args:
        images (numpy.ndarray): Array of images to preprocess.

    Returns:
        numpy.ndarray: Preprocessed images.
    """
    # Normalize the images to [0, 1] range
    images = images / 255.0

    # Add a channel dimension if not already present
    if len(images.shape) == 3:
        images = np.expand_dims(images, axis=-1)

    return images

if __name__ == "__main__":
    # Load and preprocess the data
    (train_images, train_labels), (test_images, test_labels) = load_data()

    # Example usage of preprocess_images
    sample_images = np.array([train_images[0], train_images[1]])
    preprocessed_images = preprocess_images(sample_images)

    # Print shapes to verify
    print("Train images shape:", train_images.shape)
    print("Test images shape:", test_images.shape)
    print("Preprocessed sample images shape:", preprocessed_images.shape)
