import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()


# #########################################################################
# apply(object)######################### DECISION TREE #################################

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)

acc = clf.score(features_test, labels_test)
# ## be sure to compute the accuracy on the test set


def submitAccuracies():
    return {"acc": round(acc, 3)}



### your code goes here--now create 2 decision tree classifiers,
### one with min_samples_split=2 and one with min_samples_split=50
### compute the accuracies on the testing data and store
### the accuracy numbers to acc_min_samples_split_2 and
### acc_min_samples_split_50, respectively

clf2 = DecisionTreeClassifier(min_samples_split=50)
clf2.fit(features_train, labels_train)

acc_min_samples_split_2 = acc
acc_min_samples_split_50 = clf2.score(features_test, labels_test)


def submitAccuracies():
  return {"acc_min_samples_split_2":round(acc_min_samples_split_2,3),
          "acc_min_samples_split_50":round(acc_min_samples_split_50,3)}
