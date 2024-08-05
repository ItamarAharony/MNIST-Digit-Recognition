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





## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the training script: `python scripts/train_model.py`
4. Use the prediction script to predict your own hand-drawn digits: `python scripts/predict_digit.py`

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
```python train_model.py```

This will save the trained model as `saved_models/mnist_cnn_model.h5`.




## Acknowledgments
This project structure and initial code examples were inspired by guidance from ChatGPT.
