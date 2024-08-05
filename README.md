# MNIST Digit Recognition

This project is a convolutional neural network (CNN) implementation to recognize handwritten digits using the MNIST dataset.

## Project Structure

mnist_digit_recognition/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── notebooks/
│ ├── 01_data_exploration.ipynb
│ ├── 02_model_training.ipynb
│ └── 03_model_evaluation.ipynb
│
├── scripts/
│ ├── data_preprocessing.py
│ ├── train_model.py
│ ├── evaluate_model.py
│ ├── draw_digit.py
│ └── predict_digit.py
│
├── saved_models/
│ └── mnist_cnn_model.h5
│
├── README.md
├── requirements.txt
└── .gitignore





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
