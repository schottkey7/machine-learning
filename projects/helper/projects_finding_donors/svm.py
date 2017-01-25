from sklearn import svm

clf = svm.SVC()
clf.fit(X_train, y_train[y_train.columns[1]])
clf.score(X_test, y_test[y_test.columns[1]])

# 0.83007186290768376
