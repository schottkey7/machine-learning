from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

params = {
    'criterion': ['gini', 'entropy'],
    'splitter': ['best', 'random'],
    'max_depth': [1, 20],
    'min_samples_split': [2, 100]
}

clf = GridSearchCV(DecisionTreeClassifier(random_state=11), params)
clf.fit(X_train, y_train[y_train.columns[1]])
clf.score(X_test, y_test[y_test.columns[1]])
