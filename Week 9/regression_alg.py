import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#Load the data
nyc = pd.read_csv('ave_hi_nyc_jan_1895-2018.csv')
nyc.head(3)
nyc.columns = ['Date', 'Temperature', 'Anomaly']
nyc.Date = nyc.Date.floordiv(100)
nyc.head(3)

# Splitting the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(
    nyc.Date.values.reshape(-1, 1), nyc.Temperature.values, random_state=11)

# Confirm the 75% - 25% train-test split
print(X_train.shape) # 93 values for training
print(X_test.shape) # 31 values for testing

# Training the model
linear_regression = LinearRegression()
linear_regression.fit(X= X_train, y = y_train)

# y = mx + b - slope and intercet to make predictions
# slope is the estimator's coeff__
# intercept is the estimator's intercept_
print(linear_regression.coef_)
print(linear_regression.intercept_)

# Testing the model
predicted = linear_regression.predict(X_test)
expected = y_test
for p, e in zip(predicted[::5], expected[::5]):  # check every 5th element
    print(f'predicted: {p:.2f}, expected: {e:.2f}')

# Predicting Future Temperatures and Estimating Past temperatures

# lambda implements y = mx + b
predict = (lambda x: linear_regression.coef_ * x + 
                     linear_regression.intercept_)
print(f"Predict temperature for NYC Jan 1924: {predict(1924)}")
print(f"Predict temperature for NYC Jan 2024: {predict(2024)}")
print(f"Predict temperature for NYC Jan 2124: {predict(2124)}")


# Visualizing the dataset with seaborn
axes = sns.scatterplot(data=nyc, x='Date', y='Temperature',
    hue='Temperature', palette='winter', legend=False)  

axes.set_ylim(5, 70)  # scale y-axis 

x = np.array([min(nyc.Date.values), max(nyc.Date.values)])

y = predict(x)
line = plt.plot(x, y)

plt.show()

'''
    Overfitting / Underfitting
        They are common problems that prevent accurate predictions.

        Underfitting occurs when a model is too simple to make predictions, based on its training data
        Overfitting occur when a model is too complex
'''