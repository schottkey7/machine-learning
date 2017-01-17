import numpy as np
import pandas as pd

# Load the dataset
from sklearn.datasets import load_linnerud
from sklearn import cross_validation

linnerud_data = load_linnerud()
X = linnerud_data.data
y = linnerud_data.target

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error as mae
from sklearn.linear_model import LinearRegression

# TODO: split the data into training and testing sets,
# using the standard settings for train_test_split.
# Then, train and test the classifiers with your newly split data instead of X and y.
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(
    X, y)

reg1 = DecisionTreeRegressor()
reg1.fit(features_train, labels_train)
decision_tree = mae(labels_test, reg1.predict(features_test))
print "Decision Tree mean absolute error: {:.2f}".format(decision_tree)

reg2 = LinearRegression()
reg2.fit(features_train, labels_train)
linear_regression = mae(labels_test, reg2.predict(features_test))
print "Linear regression mean absolute error: {:.2f}".format(linear_regression)

results = {
    "Linear Regression": linear_regression,
    "Decision Tree": decision_tree
}
