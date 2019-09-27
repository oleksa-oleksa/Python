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
        for correct, predicted in zip(labels.astype(int), np.round(predictions)):
            matrix[correct][predicted] += 1
        return matrix


class LeastSquares(Classifier):
    def linear_distance(self, data, data_mean):
        return data - data_mean

    def fit(self, x, y):
        self.x = x
        self.y = y

    def predict(self, x_test):
        predictions = []
        distances_x = []
        distances_x_squared = []
        distances_y = []
        distances_xy = []
        x_mean = np.mean(self.x)
        y_mean = np.mean(self.y)

        for sample in x_test:
            delta_x = self.linear_distance(sample, x_mean)
            distances_x.append(delta_x)
            delta_x_squared = delta_x ** 2
            distances_x_squared.append(delta_x_squared)

            delta_y = self.linear_distance(sample, y_mean)
            distances_y.append(delta_y)
            distances_xy.append(delta_y * delta_x_squared)

        # y = intercept + slope * x
        slope = np.sum(distances_xy) / np.sum(distances_x_squared)
        intercept = y_mean - slope * x_mean

        for sample in x_test:
            predictions.append(intercept + slope * sample)

        print('Linear regression complete')
        return predictions


def show_numbers(X):
    num_samples = 90
    # Generates a random sample from a given 1-D array
    indices = np.random.choice(range(len(X)), num_samples)
    sample_digits = X[indices]

    fig = plt.figure(figsize=(20, 6))

    for i in range(num_samples):
        ax = plt.subplot(6, 15, i + 1)
        img = 255 - sample_digits[i].reshape((16, 16))
        plt.axis('off')
        plt.imshow(img, cmap='gray')
    plt.show()


training_data = np.array(pd.read_csv('./datasets/zip.train', sep=' ', header=None, engine='python'))
test_data = np.array(pd.read_csv('./datasets//zip.test', sep=' ', header=None, engine='python'))

x_train, y_train = training_data[:,1:-1], training_data[:,0]
x_test, y_test = test_data[:,1:], test_data[:,0]

model = LeastSquares()
model.fit(x_train, y_train)

predictions = model.predict(x_test)

print(model.confusion_matrix(y_test, predictions))
misclassified = x_test[(predictions != y_test)]
show_numbers(misclassified)
