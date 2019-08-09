import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
boston = pd.read_csv("/datasets/BostonHousing.csv")

# setting the dependent und independent variables
x = boston.iloc[:,0:13]
y = boston["medv"]
