from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

params = {
    'criterion': ['gini', 'entropy'],
    'splitter': ['best', 'random'],
    'max_depth': range(1, 21),
    'min_samples_split': range(2, 101)
}

clf = GridSearchCV(DecisionTreeClassifier(random_state=11), params)
clf.fit(X_train, y_train[y_train.columns[1]])
clf.score(X_test, y_test[y_test.columns[1]])


DecisionTreeClassifier(
    class_weight=None,
    criterion='entropy', max_depth=20,
    max_features=None, max_leaf_nodes=None,
    min_impurity_split=1e-07, min_samples_leaf=1,
    min_samples_split=100, min_weight_fraction_leaf=0.0,
    presort=False, random_state=11, splitter='best')


# ----------------------------------------------------------------------------- #
# Use a DecisionTreeClassifier directly and obtain feature importances
clf = DecisionTreeClassifier(
    class_weight=None, criterion='entropy', max_depth=20,
    max_features=None, max_leaf_nodes=None,
    min_impurity_split=1e-07, min_samples_leaf=1,
    min_samples_split=100, min_weight_fraction_leaf=0.0,
    presort=False, random_state=11, splitter='best')

clf.fit(X_train, y_train[y_train.columns[1]])
clf.score(X_test, y_test[y_test.columns[1]])


most_important = clf.feature_importances_
fi = zip(most_important, X_train.columns)
print sorted(fi, key=lambda tup: tup[0], reverse=True)[:20]

# ----------------------------------------------------------------------------- #
# Feature importances
from sklearn.ensemble import ExtraTreesClassifier

model = ExtraTreesClassifier()
model.fit(X_train, y_train[y_train.columns[1]])
print(model.feature_importances_)
model.score(X_test, y_test[y_test.columns[1]])
