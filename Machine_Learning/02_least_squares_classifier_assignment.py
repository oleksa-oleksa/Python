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
    def linear_distance(self, data, data_mean):
        return data - data_mean

    def mean(self, X_test):
        return np.mean(X_test)

    def fit(self, x, y):
        self.x = x
        self.y = y

    def predict(self, x_test, y_test):
        predictions = []
        distances_x = []
        distances_x_squared = []
        distances_y = []
        distances_xy = []
        x_mean = self.linear_distance(x_test)
        y_mean = self.linear_distance(y_test)

        for sample in x_test:
            delta_x = self.linear_distance(sample, x_mean)
            distances_x.append(delta_x)
            distances_x_squared.append(delta_x ** 2)

            delta_y = self.linear_distance(sample, y_mean)
            distances_y.append(delta_y)
            distances_xy.append(delta_y * distances_x[sample])

        # y = b0 + slope*x
        slope = np.sum(distances_xy) / np.sum(distances_x_squared)
        intercept = 

        predictions += [sample]

        print('Linear regression complete')
        return predictions


training_data = np.array(pd.read_csv('./datasets/zip.train', sep=' ', header=None, engine='python'))
test_data = np.array(pd.read_csv('./datasets//zip.test', sep=' ', header=None, engine='python'))

x_train, y_train = training_data[:,1:-1], training_data[:,0]
x_test, y_test = test_data[:,1:], test_data[:,0]


model = LeastSquares()
model.fit(x_train, y_train)

predictions = model.predict(x_test, y_test)