# MNIST Digit Recognition

This project is a convolutional neural network (CNN) implementation to recognize handwritten digits using the MNIST dataset.

## Project Structure

mnist_digit_recognition/ <br />
│ <br />
├── data/ <br />
│ ├── raw/ <br />
│ └── processed/ <br />
│ <br />
├── notebooks/ <br />
│ ├── 01_data_exploration.ipynb <br />
│ ├── 02_model_training.ipynb <br />
│ └── 03_model_evaluation.ipynb <br />
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

1. **Data Preprocessing:** `scripts/data_preprocessing.py`
2. **Model Training:** `scripts/train_model.py`
3. **Model Evaluation:** `notebooks/03_model_evaluation.ipynb`
4. **Predicting Hand-Drawn Digits:** `scripts/predict_digit.py`
