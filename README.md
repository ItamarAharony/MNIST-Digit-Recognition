# MNIST Digit Recognition

This project is a convolutional neural network (CNN) implementation to recognize handwritten digits using the MNIST dataset.

## Project Structure

mnist_digit_recognition/ <br />
│ <br />
├── scripts/ <br />
│ ├── data_preprocessing.py <br />
│ ├── train_model.py <br />
│ ├── evaluate_model.py <br />
│ ├── draw_digit.py <br />
│ └── predict_digit.py <br />
│ <br />
├── saved_models/ <br />
│ └── mnist_cnn_model.h5 <br />
│ <br />
├── README.md <br />
├── requirements.txt <br />
└── .gitignore <br />



## Dependencies

- TensorFlow
- NumPy
- Matplotlib
- Jupyter
- Pillow

## Usage

### 1. Set Up the Environment
Ensure you have the required dependencies installed. You can create a virtual environment and install the dependencies using the provided `requirements.txt` file:

```pip install -r requirements.txt```

### 2. Train the Model

To train the model on the MNIST dataset, run the `train_model.py` script:

```python scripts/train_model.py```

This will save the trained model as `saved_models/mnist_cnn_model.h5`.

### 3. Evaluate the Model
To evaluate the trained model, run the `evaluate_model.py` script:

```python scripts/evaluate_model.py```

### 4. Predict Digits

#### Drawing and Predicting Digits
To draw a digit on a canvas and predict it, use the `draw_digit.py` script:

```python scripts/draw_digit.py```


#### Using Pre-existing Digit Images

1. Draw and save your digit image (e.g., `my_digit.png`).
2. Place it in the `data` directory or specify its path in the `predict_digit.py` script.
3. Run the prediction script:

```python scripts/predict_digit.py --image_path data/my_digit.png```



## Acknowledgments
This project structure and initial code examples were inspired by guidance from ChatGPT.
