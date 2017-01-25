from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=100)

clf = clf.fit(X_train, y_train)
clf.score(X_test, y_test)
