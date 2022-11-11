import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Get data and store in np array
data = pd.read_csv("./digit-recognizer/train.csv")
m, n = data.shape
data = np.array(data)
np.random.shuffle(data)

# Divide in 2 datasets 
data_dev = data[0:1000].T
Y_dev = data_dev[0]
X_dev = data_dev[1:n]

data_train = data[1000:m].T
Y_train = data_dev[0]
X_train = data_dev[1:n]

def init_params():
    W1 = np.random.rand(10, 784)
    b1 = np.random.rand(10, 1)

    W2 = np.random.rand(10, 10)
    b2 = np.random.rand(10, 1)

    return W1, b1, W2, b2

def ReLU(Z):
    return np.maximum(0, Z)

def softmax(Z):
    return np.exp(Z) / np.sum(np.exp(Z))

def foward_prop(W1, b1, W2, b2, X):
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)

    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)

# one hot encoding
def one_hot(Y):
    # Creating empty matrix
    # one_hot_Y = np.zeros((m, n + 1))
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    one_hot_Y[np.arrange(Y.size), Y] = 1
    one_hot_Y = one_hot_Y.T
    return one_hot_Y

def deriv_ReLU(Z):
    return Z > 0

def back_prop(Z1, A1, Z2, A2, W2, X, Y):
    m = Y.size

    one_hot_Y = one_hot(Y)
    dZ2 = A2 - one_hot_Y
    dW2 = 1 / m * dZ2.dot(A1.T)
    dB2 = 1 / m * np.sum(dZ2, 2)
    dZ1 = W2.T.dot(dZ2) * deriv_ReLU(Z1)
    dW1 = 1 / m * dZ1.dot(X.T)
    dB1 = 1 / m * np.sum(dZ1, 2)

    return dW1, dB1, dW2, dB2

def update_params(W1, b1, W2, b2, dW1, dB1, dW2, dB2, alpha):
    W1 = W1 - alpha * dW1
    b1 = b1 - alpha * dB1
    W2 = W2 - alpha * dW2
    b2 = b2 - alpha * dB2
    return W1, b1, W2, b2