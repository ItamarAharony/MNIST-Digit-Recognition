# MNIST Digit Recognition

This project is a convolutional neural network (CNN) implementation to recognize handwritten digits using the MNIST dataset. This is a simplification of a freelance project whose complete implementation has been kept confidential.

## Project Structure

mnist_digit_recognition/ <br />
│ <br />
├── saved_models/ <br />
│ └── mnist_cnn_model.h5 <br />
│ <br />
├── data <br />
│ └── images of hand-drawn digits <br />
│ <br />
├──  data_preprocessing.py <br />
├──  train_model.py <br />
├── evaluate_model.py <br />
├──  draw_digit.py <br />
├── predict_digit.py <br />
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

#### First-Time activation
This project uses Python version 3.8, any other version may have conflicting dependencies between Tensorflow and NumPy. 


```conda create -n py38 python=3.8```

```activate py38```



Ensure you have the required dependencies installed. You can create a virtual environment and install the dependencies using the provided `requirements.txt` file:


```pip install -r requirements.txt```

To exit the virtual environment:

```deactivate```


#### Returning to the Virtual Environment
If you have already completed the first-time activation, enter it by typing the command:


```activate py38```


and exit by typing:


```deactivate```

### 2. Train the Model

To train the model on the MNIST dataset, run the `train_model.py` script:

```python train_model.py```,
which will train the model for 5 epochs by default.
It is recommended to use 50 epochs or more to obtain a more accurate model (may take a while to run).
To run the program for 50 epochs,
type into the command line: 
  
  ```python train_model.py --epochs 50```

After train_model.py finishes running, it will save the trained model as `saved_models/mnist_cnn_model.h5`.

### 3. Evaluate the Model
To test a trained model's ability to predict digits from the MNISt database, run the `evaluate_model.py` script:

```python evaluate_model.py```

### 4. Predict Digits

#### Drawing and Predicting Digits
To draw a digit on a canvas and predict it, use the `draw_digit.py` script:

```python draw_digit.py```


#### Using Pre-existing Digit Images

1. Draw and save your digit image (e.g., `my_digit.png`).
2. Place it in the `data` directory or specify its path in the `predict_digit.py` script.
3. Run the prediction script:

```python predict_digit.py --image_path data/my_digit.png```



## Acknowledgments
This project structure and initial code examples were inspired by guidance from ChatGPT.
