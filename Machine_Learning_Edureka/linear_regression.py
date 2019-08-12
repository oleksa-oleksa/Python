import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
boston = pd.read_csv("/datasets/BostonHousing.csv")

# setting the dependent und independent variables
x = boston.iloc[:,0:13]
y = boston["medv"]

# Compute pairwise correlation of columns, excluding NA/null values.
names = []
correlations = boston.corr()

# Plot rectangular data as a color-encoded matrix.
sns.heatmap(correlations, square=True, cmap="YiGnBu")
plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.show()

