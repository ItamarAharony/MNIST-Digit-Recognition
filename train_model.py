import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from data_preprocessing import load_data
import os

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
        tf.keras.layers.Dropout(0.5),  # Dropout layer with a rate of 50%
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    return model

def train_model():
    """
    Train the CNN model on the MNIST dataset and save the trained model.
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
    model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_data=(test_images, test_labels))
    
    # Ensure the directory exists
    if not os.path.exists('saved_models'):
        os.makedirs('saved_models')
    
    # Save the model
    model.save('saved_models/mnist_cnn_model.h5')

if __name__ == "__main__":
    train_model()
