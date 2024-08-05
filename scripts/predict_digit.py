import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

def load_model():
    return tf.keras.models.load_model('saved_models/mnist_cnn_model.h5')

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(28, 28), color_mode='grayscale')
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img.astype('float32') / 255
    return img

def predict_digit(img_path):
    model = load_model()
    img = preprocess_image(img_path)
    prediction = model.predict(img)
    return np.argmax(prediction)

if __name__ == "__main__":
    img_path = 'data/drawn_digit.png' #'path_to_your_handdrawn_digit.png'
    predicted_digit = predict_digit(img_path)
    print(f'The predicted digit is: {predicted_digit}')
