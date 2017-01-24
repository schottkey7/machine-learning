from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
clf.fit(X_train, y_train[y_train.columns[1]])
pred = clf.predict(X_test)
clf.score(X_test, y_test[y_test.columns[1]])
