
def studentRegression(ages_train, net_worths_train):
    from sklearn.linear_model import LinearRegression
    reg = LinearRegression()
    reg.fit(ages_train, net_worths_train)
    return reg


# get predictions, expects a list of values
reg.predict([[42]])
# slope
reg.coef_
# intercept
reg.intercept_
# r-squared score
reg.score(ages_test, net_worths_test)
reg.score(ages_train, net_worths_train)
