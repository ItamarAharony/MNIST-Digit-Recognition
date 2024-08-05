# evaluate_model.py

import tensorflow as tf
from tensorflow.keras import datasets
import numpy as np

def load_data():
    (train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()
    test_images = test_images / 255.0
    test_images = np.expand_dims(test_images, axis=-1)  # Add channel dimension
    return test_images, test_labels

def load_model(model_path='mnist_cnn_model.h5'):
    return tf.keras.models.load_model(model_path)

def evaluate_model(model, test_images, test_labels):
    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
    print(f'Test accuracy: {test_acc * 100:.2f}%')
    print(f'Test loss: {test_loss:.4f}')

if __name__ == "__main__":
    test_images, test_labels = load_data()
    model = load_model()
    evaluate_model(model, test_images, test_labels)
