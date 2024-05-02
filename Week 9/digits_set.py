'''
    Case study: Classification with K neighbors and the Digits Dataset
'''
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import pandas as pd
import seaborn as sns
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

# Returns a Bunch object containing digit samples and metadata
digits = load_digits()

# DESCR attribute contains dataset's description.
#print(digits.DESCR)

# Bunch object's data and target attributes are Numpy arrays
# Data array: 1797 samples (digit images) with 64 features with values 0 to 16.
# Target array: The image's labels, classes, indicating which digit each image represents
#print(digits.target[::100]) # Target values of every 100th sample
# Output: [0 4 1 7 4 8 2 2 4 4 1 9 7 3 2 1 2 5]       

# Confirm number of samples and features(per sample) via data array's shape
#print(digits.data.shape)
# Output: (1797, 64)

# Confirm the number of target values matches number of samples via target array's shape
#print(digits.target.shape)

# images attribute: Each element is an 8-by-8 array representing a digit image’s pixel intensities
#print(digits.images[13]) # show array for sample image at index 13

# Return the preprocessed data ready for machine learning
# 8 by 8 array digits.images[13] correspondes to 1 by 64 array
#print(digits.data)

figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(6, 4))

for item in zip(axes.ravel(), digits.images, digits.target):
    axes, image, target = item 
    axes.imshow(image, cmap=plt.cm.gray_r)
    axes.set_xticks([])  # remove x-axis tick marks
    axes.set_yticks([])  # remove y-axis tick marks
    axes.set_title(target)
plt.tight_layout()
#plt.show()

# When training the model, it is useful to save a portion for testing to evalute
# the model's performance using unseen data.
# The function train_test_split splits the data to randomize it, then splits the samples in the data
# array and the target values in the target array into training and testing sets
#It returns a tuple of four elements in which the first two are the samples split into training and testing sets,
# and the last two are the corresponding target values into training and testing sets

# 75% of the data is for training, 25% for testing
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, random_state=11) # random_state for reproducibility

print(X_train.shape)
print(X_test.shape)

# Creating the model (estimator) using k-nearet neighbors algorithm
knn = KNeighborsClassifier()

# Load the sample training and target training set into the estimator
knn.fit(X=X_train, y = y_train)

# Return an array containing the predicted class of each test image:
predicted = knn.predict(X=X_test)
expected = y_test

print(predicted[:20])
print(expected[:20])
# Output:                              *
# [0 4 9 9 3 1 4 1 5 0 4 9 4 1 5 3 3 8 5 6]
# [0 4 9 9 3 1 4 1 5 0 4 9 4 1 5 3 3 8 3 6] 

wrong = [(p, e) for (p, e) in zip(predicted, expected) if p != e]
print("Wrong:", wrong)

# Returns an indicator of how well the estimator performs on test data
print(f'{knn.score(X_test, y_test):.2%}')

# Confusion Matrix
# Shows correct and incorrect predicted values (hits and misses) for a given class
confusion = confusion_matrix(y_true= expected, y_pred= predicted)
print("confusion:", confusion)
# Output:
# confusion: [[45  0  0  0  0  0  0  0  0  0]
# [ 0 45  0  0  0  0  0  0  0  0]
# [ 0  0 54  0  0  0  0  0  0  0]
# [ 0  0  0 42  0  1  0  1  0  0]
# [ 0  0  0  0 49  0  0  1  0  0]
# [ 0  0  0  0  0 38  0  0  0  0]
# [ 0  0  0  0  0  0 42  0  0  0]
# [ 0  0  0  0  0  0  0 45  0  0]
# [ 0  1  1  2  0  0  0  0 39  1]
# [ 0  0  0  0  1  0  0  0  1 41]]

'''
    Correct predictions shown on pricipal diagonal from top-left to bottom-right.
    Nonzero values not on principal diagonal indicate incorrect predictions
    Each row represents one distinct class (0-9)
    Nonzero values not on principal diagonal indicate incorrect predictions
    Columns specify how many test samples were classified into classes 0-9
    Row 0 shows digit class 0 - all 0s were predicted corretly
    Row 8 shows digit class 8 - five 8s were predicted incorrectly
'''

confusion_df = pd.DataFrame(confusion, index=range(10), columns=range(10))
figure = plt.figure(figsize=(7, 6))
axes = sns.heatmap(confusion_df, annot=True, 
                   cmap=plt.cm.nipy_spectral_r) 

plt.show()


# K-fold Cross-Validation
# Uses all of the data for training and testing.
# Splits the dataset into k equal-size folds
# Repeatedly trains your model with k-1 folds and test the model with the remaining fold

# Kfold class
kfold = KFold(n_splits=10, random_state=11, shuffle=True)

# Calling function cross_val_score to train and test model
'''
    Parameters:
        estimator = knn - estimator to validate
        X = digits.data - samples to use for training and testing
        y = digits.target - target predictions for the sample
        cv = kfold - cross-validation generator that defines how to split the samples and targets for training and testing    
'''

scores = cross_val_score(estimator=knn, X=digits.data, y=digits.target, cv=kfold)
print(f'Mean accuracy: {scores.mean():.2%}')

