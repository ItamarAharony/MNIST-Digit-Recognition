import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import os

def load_model(model_path='saved_models/mnist_cnn_model.h5'):
    """
    Load the trained model from the specified path.
    
    Args:
        model_path (str): Path to the saved model.
        
    Returns:
        model (tf.keras.Model): Loaded Keras model.
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"No model found at {model_path}")
    return tf.keras.models.load_model(model_path)

def preprocess_image(img_path):
    """
    Preprocess the input image to the required format for prediction.
    
    Args:
        img_path (str): Path to the image file.
        
    Returns:
        numpy.ndarray: Preprocessed image array.
    """
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"No image found at {img_path}")
        
    img = image.load_img(img_path, target_size=(28, 28), color_mode='grayscale')
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img.astype('float32') / 255.0
    return img

def predict_digit(img_path):
    """
    Predict the digit in the given image.
    
    Args:
        img_path (str): Path to the image file.
        
    Returns:
        int: Predicted digit.
    """
    model = load_model()
    img = preprocess_image(img_path)
    prediction = model.predict(img)
    return np.argmax(prediction)

if __name__ == "__main__":
    img_path = 'data/drawn_digit.png'
    try:
        predicted_digit = predict_digit(img_path)
        print(f'The predicted digit is: {predicted_digit}')
        
        # Display the image and prediction
        img = image.load_img(img_path, target_size=(28, 28), color_mode='grayscale')
        plt.imshow(img, cmap='gray')
        plt.title(f'Predicted Digit: {predicted_digit}')
        plt.axis('off')
        plt.show()
        
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")
