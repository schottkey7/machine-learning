from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV

params = {
    'loss': ['hinge', 'log', 'modified_huber', 'squared_hinge', 'perceptron'],
    'penalty': ['l2', 'l1', 'elasticnet']
}

clf = GridSearchCV(SGDClassifier(random_state=11, alpha=1e-5), params)
clf.fit(X_train, y_train[y_train.columns[1]])
clf.score(X_test, y_test[y_test.columns[1]])


clf = SGDClassifier(
    alpha=1e-05, average=False, class_weight=None, epsilon=0.1,
    eta0=0.0, fit_intercept=True, l1_ratio=0.15,
    learning_rate='optimal', loss='hinge', n_iter=5, n_jobs=1,
    penalty='elasticnet', power_t=0.5, random_state=11, shuffle=True,
    verbose=0, warm_start=False)

clf.fit(X_train, y_train[y_train.columns[1]])
clf.score(X_test, y_test[y_test.columns[1]])
