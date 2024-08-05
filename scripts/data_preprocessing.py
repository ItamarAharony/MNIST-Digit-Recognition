import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

numTrain=60000 #number of training images
numTest=10000  #number of test images 

def load_and_preprocess_data():
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
    train_images = train_images.reshape((numTrain, 28, 28, 1)).astype('float32') / 255
    test_images = test_images.reshape((numTest, 28, 28, 1)).astype('float32') / 255
    train_labels = to_categorical(train_labels)
    test_labels = to_categorical(test_labels)
    return (train_images, train_labels), (test_images, test_labels)

if __name__ == "__main__":
    load_and_preprocess_data()
