from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

logistic = LogisticRegression(C=1e6, penalty='l2', random_state=11)

logistic.fit(X_train, y_train[y_train.columns[1]])
logistic.score(X_test, y_test[y_test.columns[1]])


# With grid search
params = {
    'penalty': ['l2'],
    'C': np.arange(1e-6, 1, 1e-2),
    'solver': ['newton-cg', 'lbfgs', 'liblinear', 'sag']
}

clf = GridSearchCV(LogisticRegression(random_state=11), params)
clf.fit(X_train, y_train[y_train.columns[1]])
clf.score(X_test, y_test[y_test.columns[1]])

# ----------------------------------------------------------------------------- #
# Best estimator
'''
LogisticRegression(C=0.99000100000000002, class_weight=None, dual=False,
          fit_intercept=True, intercept_scaling=1, max_iter=100,
          multi_class='ovr', n_jobs=1, penalty='l2', random_state=11,
          solver='liblinear', tol=0.0001, verbose=0, warm_start=False)
'''

# ----------------------------------------------------------------------------- #
# Feature selection
from sklearn.feature_selection import RFE
model = LogisticRegression()
rfe = RFE(model, 5)
rfe = rfe.fit(X_train, y_train[y_train.columns[1]])

print(rfe.support_)
print(rfe.ranking_)

rfe.score(X_test, y_test[y_test.columns[1]])

# ----------------------------------------------------------------------------- #
# Feature importances
from sklearn.ensemble import ExtraTreesClassifier

model = ExtraTreesClassifier()
model.fit(X_train, y_train[y_train.columns[1]])
print(model.feature_importances_)
model.score(X_test, y_test[y_test.columns[1]])
