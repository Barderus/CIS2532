from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import seaborn as sns
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

digits = load_digits()

# Train the data
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, random_state=11) # random_state for reproducibility

# Creating the model (estimator) using k-nearet neighbors algorithm
knn = KNeighborsClassifier()

estimators = {
    'KNeighborsClassifier': knn, 
    'SVC': SVC(gamma='scale'),
    'GaussianNB': GaussianNB()}

for estimator_name, estimator_object in estimators.items():
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    scores = cross_val_score(estimator=estimator_object, 
        X=digits.data, y=digits.target, cv=kfold)
    print(f'{estimator_name:>20}: ' + 
          f'mean accuracy={scores.mean():.2%}; ' +
          f'standard deviation={scores.std():.2%}')
    
'''
    KNeighborsClassifier: mean accuracy=98.72%; standard deviation=0.75%
    SVC: mean accuracy=98.72%; standard deviation=0.79%
    GaussianNB: mean accuracy=84.48%; standard deviation=3.47%
'''
# KNeighborsClassifier and SVC are pretty similar. So we'll do Hyperparameter Tuning.
# Hyperparameter Tuning - Choose values that produce the best possible predictions
# Scikit-learn has automated hyperparameter tuning capabilities

for k in range(1, 20, 2):  # k is an odd value 1-19; odds prevent ties
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(estimator=knn, 
        X=digits.data, y=digits.target, cv=kfold)
    print(f'k={k:<2}; mean accuracy={scores.mean():.2%}; ' +
          f'standard deviation={scores.std():.2%}')
    