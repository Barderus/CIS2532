from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.linear_model import ElasticNet, Lasso, Ridge
from sklearn.model_selection import KFold, cross_val_score

'''
    Datase: California Housing Prices
    "This dataset was derived from the 1990 U.S. census, using one row per census block group.
    "A block group is the smallest geographical unit for which the U.S. 
    Census Bureau publishes sample data (typically has a population of 600 to 3,000 people)."

    The dataset has 20,640 samples, one per block group, with eight feaures each:
        * median income—in tens of thousands, so 8.37 would represent $83,700
        * median house age—in the dataset, the maximum value for this feature is 52
        * average number of rooms
        * average number of bedrooms
        * block population
        * average house occupancy
        * house block latitude
        * house block longitude
'''

# Target - mediam house value in hundreds of thousands
california = fetch_california_housing()  # Bunch object 
print(california.DESCR)

print(california.data.shape)
print(california.target.shape)
print(california.feature_names)

# Exploring the data with a Pandas
pd.set_option('display.precision', 4)  # 4 digit precision for floats
california_df = pd.DataFrame(california.data, 
                             columns=california.feature_names)
california_df['MedHouseValue'] = pd.Series(california.target)


print()
california_df.head()  # peek at first 5 rows

print()
print(california_df.describe())

# Visualizing the features
# Using the DataFrame method sample to randomly select 10% of the 20,640 samples
sample_df = california_df.sample(frac=0.1, random_state=17)
sns.set_style('whitegrid')                                    
for feature in california.feature_names:
    plt.figure(figsize=(8, 4.5))  # 8"-by-4.5" Figure
    sns.scatterplot(data=sample_df, x=feature, 
                    y='MedHouseValue', hue='MedHouseValue', 
                    palette='cool', legend=False)
    
#plt.show()

# Splitting the Data for Training and Testing
X_train, X_test, y_train, y_test = train_test_split(
    california.data, california.target, random_state=11)

X_train.shape
X_test.shape

# Training the model
linear_regression = LinearRegression()
linear_regression.fit(X=X_train, y=y_train)

for i, name in enumerate(california.feature_names):
    print(f'{name:>10}: {linear_regression.coef_[i]}')  

linear_regression.intercept_

# Testing the model
predicted = linear_regression.predict(X_test)
expected = y_test

print(predicted[:5])  # first 5 predictions
print(expected[:5])   # first five targets 

# Testing the Model with the Estimator's predict method
# In classification, prediction were distinct classes that matched existing classes in the dataset
# In regression, it's tough to get exact predition, because you have continous outputs
df = pd.DataFrame()

df['Expected'] = pd.Series(expected)
df['Predicted'] = pd.Series(predicted)

figure = plt.figure(figsize=(9, 9))

axes = sns.scatterplot(data=df, x='Expected', y='Predicted', 
    hue='Predicted', palette='cool', legend=False)

start = min(expected.min(), predicted.min())

end = max(expected.max(), predicted.max())

axes.set_xlim(start, end)

axes.set_ylim(start, end)

line = plt.plot([start, end], [start, end], 'k--')

#plt.show()

# Regression Model Metrics
print(metrics.r2_score(expected, predicted))

# Trying with different models
estimators = {
    'LinearRegression': linear_regression,
    'ElasticNet': ElasticNet(),
    'Lasso': Lasso(),
    'Ridge': Ridge()
}
print()
for estimator_name, estimator_object in estimators.items():
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    scores = cross_val_score(estimator=estimator_object, 
        X=california.data, y=california.target, cv=kfold,
        scoring='r2')
    print(f'{estimator_name:>16}: ' + 
          f'mean of r2 scores={scores.mean():.3f}')