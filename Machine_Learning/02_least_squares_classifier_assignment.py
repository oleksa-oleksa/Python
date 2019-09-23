"""
Implementation of Least-Squares Linear Regression
Using the closed-form expression from the lecture, implement Linear Regression in Python
(incl. Numpy, Pandas, Matplotlib) on a Jupyter Notebook.

Train on the training set of the "ZIP code"-Dataset and test on its test set.

(a) Print out the Confusion Matrix and the accuracy. (b) What is a good way of encoding the labels?
(c) What is the problem with using Linear Regression for Classification?
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


class Classifier:
    def accuracy(self, labels, predictions):
        # Compute the arithmetic mean along the specified axis
        return np.mean(labels == predictions)

    def confusion_matrix(self, labels, predictions):
        # set() method is used to convert any of the iterable to the distinct element
        # and sorted sequence of iterable elements, commonly called Set.
        size = len(set(labels))
        matrix = np.zeros((size, size))
        # map the similar index of multiple containers so that they can be used just using as single entity.
        for correct, predicted in zip(labels.astype(int), predictions):
            matrix[correct][predicted] += 1
        return matrix


class LeastSquares(Classifier):
    def linear_distance_x(self, x, x_mean):
        return np.sum((x_1 - x_2) ** 2, axis=1)

    def mean(self, X_test):
        return np.mean(X_test)

    def fit(self, X, y):
        self.X = X
        self.y = y

    def predict(self, X_test, Y_test):
        predictions = []
        x_mean = self.linear_distance(X_test)
        y_mean = self.linear_distance(Y_test)

        for sample in X_test:
            predictions += [sample]

        print('Linear regression complete')
        return predictions


training_data = np.array(pd.read_csv('./datasets/zip.train', sep=' ', header=None, engine='python'))
test_data = np.array(pd.read_csv('./datasets//zip.test', sep=' ', header=None, engine='python'))

X_train, y_train = training_data[:,1:-1], training_data[:,0]
X_test, y_test = test_data[:,1:], test_data[:,0]


model = LeastSquares()
model.fit(X_train, y_train)

predictions = 