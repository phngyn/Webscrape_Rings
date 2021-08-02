""" 
Work in progress: develop linear regression of ring values

References:
https://towardsdatascience.com/linear-regression-in-6-lines-of-python-5e1d0cd05b8d

"""

import os
import json
import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dir_path = os.path.dirname(os.path.realpath(__file__))
ring_data = dir_path + "\\ring_data.json"

data = []

with open(ring_data) as rdata:
    for line in rdata:
        data.append(json.loads(line))

df = pd.DataFrame(data)
X = df.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
Y = df.iloc[:, 1].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column

print(X, Y)

# linear_regressor = LinearRegression()  # create object for the class
# linear_regressor.fit(X, Y)  # perform linear regression
# Y_pred = linear_regressor.predict(X)  # make predictions

# plt.scatter(X, Y)