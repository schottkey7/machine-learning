# As with the previous exercises, let's look at the performance of a couple of classifiers
# on the familiar Titanic dataset. Add a train/test split, then store the results in the
# dictionary provided.

import numpy as np
import pandas as pd

# Load the dataset
X = pd.read_csv('titanic_data.csv')

X = X._get_numeric_data()
y = X['Survived']
del X['Age'], X['Survived']


from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import recall_score as recall
from sklearn.metrics import precision_score as precision
from sklearn.naive_bayes import GaussianNB
from sklearn import cross_validation

# TODO: split the data into training and testing sets,
# using the standard settings for train_test_split.
# Then, train and test the classifiers with your newly split data instead of X and y.
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(
    X, y)


clf1 = DecisionTreeClassifier()
clf1.fit(features_train, labels_train)
decision_tree = [
    recall(labels_test, clf1.predict(features_test)),
    precision(labels_test, clf1.predict(features_test))
]
print "Decision Tree recall: {:.2f} and precision: {:.2f}".format(*decision_tree)

clf2 = GaussianNB()
clf2.fit(features_train, labels_train)
naive_bayes = [
    recall(labels_test, clf2.predict(features_test)),
    precision(labels_test, clf2.predict(features_test))
]
print "GaussianNB recall: {:.2f} and precision: {:.2f}".format(*naive_bayes)

results = {
    "Naive Bayes Recall": naive_bayes[0],
    "Naive Bayes Precision": naive_bayes[1],
    "Decision Tree Recall": decision_tree[0],
    "Decision Tree Precision": decision_tree[1]
}
