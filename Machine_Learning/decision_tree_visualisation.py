"""Goal:
Import dataset
Train a classifier
Predict label for new flower
Visualise the tree
"""

import pandas as pd
from sklearn import tree

iris = pd.read_csv("./datasets/iris_train.csv")
headers = iris.columns.tolist()
print(headers)

# setting the dependent und independent variables


# The data will not be split because the separate dataset for train and test were provided

clf = tree.DecisionTreeClassifier()
#clf.fit(iris)