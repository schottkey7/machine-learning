from sklearn.naive_bayes import GaussianNB

# Initialize classifier
clf = GaussianNB()

# Fit the training data
clf.fit(X_train, y_train[y_train.columns[1]])

# Predict using the testing data
pred = clf.predict(X_test)

expected = y_test[y_test.columns[1]]

# Accuracy score
clf.score(X_test, expected)

# Print reports
print(metrics.classification_report(expected, pred))

# Print confusion matrix
print(metrics.confusion_matrix(expected, pred))
