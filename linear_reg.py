""" 
Work in progress: develop linear regression of ring values

References:
https://towardsdatascience.com/linear-regression-in-6-lines-of-python-5e1d0cd05b8d

"""
import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd  # To read data
from sklearn.linear_model import LinearRegression


import os
import json
import pprint
import pandas as pd

dir_path = os.path.dirname(os.path.realpath(__file__))
ring_data = dir_path + "\\ring_data.json"

data = []

with open(ring_data) as rdata:
    for line in rdata:
        data.append(json.loads(line))

df = pd.DataFrame(data)

# data = pd.read_csv('data.csv')  # load data set
X = df.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
Y = df.iloc[:, 1].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column

print(X, Y)

# linear_regressor = LinearRegression()  # create object for the class
# linear_regressor.fit(X, Y)  # perform linear regression
# Y_pred = linear_regressor.predict(X)  # make predictions

# plt.scatter(X, Y)