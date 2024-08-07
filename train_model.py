import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from data_preprocessing import load_data
import os
import argparse

def build_model():
    """
    Build and return a CNN model with dropout layers to avoid overfitting.
    
    Returns:
        model (tf.keras.Model): Compiled CNN model.
    """
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dropout(0.1),  # Dropout layer with a rate of 10%
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    return model

def train_model(numEpochs):
    """
    Train the CNN model on the MNIST dataset and save the trained model.
    
    Args:
        numEpochs (int): Number of epochs to train the model.
    """
    # Load and preprocess the data
    (train_images, train_labels), (test_images, test_labels) = load_data()
    
    # One-hot encode the labels
    train_labels = to_categorical(train_labels, 10)
    test_labels = to_categorical(test_labels, 10)
    
    # Build and compile the model
    model = build_model()
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    
    # Train the model
    model.fit(train_images, train_labels, epochs=numEpochs, batch_size=64, validation_data=(test_images, test_labels))
    
    # Ensure the directory exists
    if not os.path.exists('saved_models'):
        os.makedirs('saved_models')
    
    # Save the model
    model.save('saved_models/mnist_cnn_model.h5')

if __name__ == "__main__":
    # Parse command-line arguments
    """
    Recommended to use 50 epochs or more (may take a while to run).
    To run the program with 50 epochs, type into the command line: 
    python train_model.py --epochs 50
    """
    parser = argparse.ArgumentParser(description='Train a CNN model on the MNIST dataset.')
    parser.add_argument('--epochs', type=int, default=5, help='Number of epochs to train the model.')
    args = parser.parse_args()
    
    # Train the model with the specified number of epochs
    train_model(args.epochs)
