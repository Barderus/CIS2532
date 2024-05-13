'''
15.1 (Using PCA To Help visualize the digits dataset) 
Reimplement the TSNE estimator example, but this time, use the PCA estmiator, then graph the results.
How do the cluster compare to the diagram from the example?
'''
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Loading the Digits dataset
digits = load_digits()

# Use PCA estimator to perform dimensionality reduction to 2
pca = PCA(n_components=2, random_state=11)
pca.fit(digits.data)
digits_pca = pca.fit_transform(digits.data)

# Visualizing the Reduced Data using scatterplot
dots = plt.scatter(digits_pca[:, 0], digits_pca[:, 1], c='black')

# Adding different colors for each digit so it's easier to represent
dots = plt.scatter(digits_pca[:, 0], digits_pca[:, 1],
    c=digits.target, cmap=plt.cm.get_cmap('nipy_spectral_r', 10))
 
colorbar = plt.colorbar(dots) 
# Response: Using TNSE estimator seems to be a best model, altough there were some overlaps, it did not compare on how many overlaps were 
# when using the PCA estimator.

'''
15.2 - (Using TSNE to Help vizualize the Iris Dataset)
    Reimplement the Iris example, but this time use the TNSE estimator, then graph the results. How do they compare?
'''
from sklearn.datasets import load_iris
from sklearn.manifold import TSNE
import pandas as pd
import seaborn as sns
import numpy as np

# Loading Iris Dataset
iris = load_iris()

# Create a TNSE estimator object
tsne = TSNE(n_components=2, random_state=11)

tsne.fit(iris.data)  # trains estimator once
# Calling transofrm again to reduce the cluster centroid to 2D for plotting
iris_tsne = tsne.fit_transform(iris.data)

iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Visualizing the Reduced data
iris_tsne_df = pd.DataFrame(iris_tsne, columns=['Component1', 'Component2'])
iris_tsne_df['species'] = iris.target

# Create a NumPy array with species names
species_names = np.array(['setosa', 'versicolor', 'virginica'])
# Use NumPy indexing to replace target labels with species names
iris_tsne_df['species'] = species_names[iris_tsne_df['species']]

axes = sns.scatterplot(data=iris_tsne_df, x='Component1', 
    y='Component2', hue='species', legend='brief') 

# Visualizing the Reduced data
sns.scatterplot(data=iris_tsne_df, x='Component1', y='Component2', hue='species', legend='brief')
# Response: TSNE and PCA proved to be very similar, the setosa is in its own cluster while versicolor and virginica has some overlaps as seen in the example.

'''
15.3 (Seaborn pairplot graph)
    Create a seaborn pairplot graph for the California Housing dataset
'''

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

california = fetch_california_housing()  # Bunch object 

# Exploring the data with a Pandas
pd.set_option('display.precision', 4)  # 4 digit precision for floats
california_df = pd.DataFrame(california.data, 
                             columns=california.feature_names)
california_df['MedHouseValue'] = pd.Series(california.target)

# Using the DataFrame method sample to randomly select 10% of the 20,640 samples
sample_df = california_df.sample(frac=0.1, random_state=17) 

# Visualizing the Dataset with a Seaborn pairplot
sns.set_style('whitegrid')
grid = sns.pairplot(data=sample_df, vars=california.feature_names, hue='MedHouseValue', diag_kind='kde')
plt.show()

'''
15-4 ( Human Recognition of Handwriting digits)
    Create a script that randoly select and display individual images and ask the user to enter a digit from 0 through 9 specifying the digit the image represents.
Keep track of the user's accuracy. How does the user compare to the k-nearest neighbors machine-learning algorithm.
'''

import random
from sklearn.neighbors import KNeighborsClassifier

def load_data():
    # Load the Digits dataset
    digits = load_digits()
    return digits

def train_classifier(X_train, y_train):
    # Train a k-nearest neighbors classifier on the training set
    knn = KNeighborsClassifier()
    knn.fit(X_train, y_train)
    return knn

def display_image(image):
    # Display the image
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()

def evaluate_guess(user_input, actual_digit, matches, misses):
    # Check if the user's input matches the actual digit
    if int(user_input) == actual_digit:
        print("Correct!")
        matches += 1
    else:
        print(f"Incorrect. The digit was {actual_digit}.")
        misses += 1
    return matches, misses

def main():
    # Load data
    digits = load_data()

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

    # Train classifier
    knn = train_classifier(X_train, y_train)

    # Initialize variables to keep track of user's accuracy
    matches = 0
    misses = 0

    # Loop through the user experience until the user indicates to stop
    while True:
        # Randomly select an image from the testing set
        index = random.randint(0, len(X_test)-1)
        image = X_test[index].reshape(8, 8)
        actual_digit = y_test[index]

        # Display the image
        display_image(image)

        # Ask the user to enter the digit it represents
        user_input = input("Please enter the digit represented by this image: ")

        # Evaluate the user's guess
        matches, misses = evaluate_guess(user_input, actual_digit, matches, misses)

        # Calculate and print the user's current accuracy
        total = matches + misses
        accuracy = matches / total if total > 0 else 0
        print(f"Current accuracy: {accuracy:.2f}\n")

        # Ask the user if they want to continue
        user_input = input("Do you want to continue? (y/n)")
        if user_input.lower() != 'y':
            break

if __name__ == "__main__":
    main()

'''
    15.5 (Using TSNE to visualize the Digits Dataset in 3D)
In this exercise you will create a 3D scatter plot using TSNE and Matplotlib AXES 3D for plotting in 3D.
'''
from mpl_toolkits.mplot3d import Axes3D

# Loading the Digits dataset
digits = load_digits()

# Instantiate the t-SNE estimator
tsne = TSNE(n_components=3, random_state=11)

# Transforming the Digits dataset features into three dimensions
reduced_data = tsne.fit_transform(digits.data)
print(reduced_data.shape)  # Print the shape to confirm it's (n_samples, 3)

# Visualizing the Reduced Data using a 3D scatterplot
figure = plt.figure(figsize=(9, 9))
axes = figure.add_subplot(111, projection="3d")
# Scatter plot
dots = axes.scatter(xs=reduced_data[:, 0], ys=reduced_data[:, 1], zs=reduced_data[:, 2], c=digits.target, cmap='nipy_spectral_r')
# Add a colorbar
colorbar = plt.colorbar(dots)

plt.show()