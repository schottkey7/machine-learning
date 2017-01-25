
# ----------------------------------------------------------------------------- #
# Random forest
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=200, criterion='entropy',random_state=11)

clf.fit(X_train, y_train[y_train.columns[1]])
clf.score(X_test, y_test[y_test.columns[1]])


# ----------------------------------------------------------------------------- #
# Gradient boosting
from sklearn.ensemble import GradientBoostingClassifier
clf = GradientBoostingClassifier(n_estimators=200, random_state=11)
clf.fit(X_train, y_train[y_train.columns[1]])
clf.score(X_test, y_test[y_test.columns[1]])


# Gradient boosting with grid search
from sklearn.model_selection import GridSearchCV

params = {
    'n_estimators': np.arange(100,201, 10),
    'max_depth': np.arange(3, 4)
}

clf = GridSearchCV(GradientBoostingClassifier(random_state=11), params)
clf.fit(X_train, y_train[y_train.columns[1]])
clf.score(X_test, y_test[y_test.columns[1]])


# ----------------------------------------------------------------------------- #
# Ada Boost
from sklearn.ensemble import AdaBoostClassifier

clf = AdaBoostClassifier(n_estimators=200, random_state=11)
clf.fit(X_train, y_train[y_train.columns[1]])
clf.score(X_test, y_test[y_test.columns[1]])
