"""
Aufgabe 1. Implementierung eines k-NN-Classifiers
Implementieren Sie einen k-NN-Classifier in Python (inkl. numpy, pandas, matplotlib)
auf der Jupyter Notebook-Umgebung. Nutzen Sie den „ZIP code“-Datensatz mit den Trainings- daten als Referenz
für die Nachbarschaft. Testen Sie auf den Testdaten.

Geben Sie die Konfusionsmatrix und die Klassifikationsgenauigkeit aus.

Geben Sie mithilfe von Matplotlib ein paar der falsch klassifizierten Zahlen aus.
Testen Sie, bei welchem k ist der Klassifizierer am besten ist.
Was sind Vor- und Nachteile des k-NN-Classifiers?

===========================

About the dataset:
Normalized handwritten digits, automatically
scanned from envelopes by the U.S. Postal Service. The original
scanned digits are binary and of different sizes and orientations; the
images  here have been deslanted and size normalized, resulting
in 16 x 16 grayscale images (Le Cun et al., 1990).

The data are in two gzipped files, and each line consists of the digit
id (0-9) followed by the 256 grayscale values.

There are 7291 training observations and 2007 test observations,
distributed as follows:
         0    1   2   3   4   5   6   7   8   9 Total
Train 1194 1005 731 658 652 556 664 645 542 644 7291
 Test  359  264 198 166 200 160 170 147 166 177 2007

or as proportions:
         0    1   2    3    4    5    6    7    8    9
Train 0.16 0.14 0.1 0.09 0.09 0.08 0.09 0.09 0.07 0.09
 Test 0.18 0.13 0.1 0.08 0.10 0.08 0.08 0.07 0.08 0.09


Alternatively, the training data are available as separate files per
digit (and hence without the digit identifier in each row)

The test set is notoriously "difficult", and a 2.5% error rate is
excellent. These data were kindly made available by the neural network
group at AT&T research labs (thanks to Yann Le Cunn).

"""


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def show_numbers(X):
    num_samples = 90
    indices = np.random.choice(range(len(X)), num_samples)
    sample_digits = X[indices]

    fig = plt.figure(figsize=(20, 6))

    for i in range(num_samples):
        ax = plt.subplot(6, 15, i + 1)
        img = 255 - sample_digits[i].reshape((16, 16))
        plt.imshow(img, cmap='gray')
        plt.axis('off')


training_data = np.array(pd.read_csv('./datasets/zip.train', sep=' ', header=None, engine='python'))
test_data = np.array(pd.read_csv('./datasets//zip.test', sep=' ', header=None, engine='python'))

X_train, y_train = training_data[:,1:-1], training_data[:,0]
X_test, y_test = test_data[:,1:], test_data[:,0]

show_numbers(X_train)

print(training_data.shape)
print(test_data.shape)

