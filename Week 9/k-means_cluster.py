# k-Means Clustering is the simplest unsupervised machine learning algorithm
# Analyze unlabeled samples and attempt to place them in clusters
# k --> number of cluster to impose on the data

'''
    Iris Dataset
This data sets consists of 3 different types of irises’ (Setosa, Versicolour, and Virginica) petal 
and sepal length, stored in a 150x4 numpy.ndarray

The rows being the samples and the columns being: 
Sepal Length, Sepal Width, Petal Length and Petal Width.
'''
from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN, MeanShift,\
    SpectralClustering, AgglomerativeClustering
import numpy as np

# Loading Iris Dataset
iris = load_iris()

# Iris description
print(iris.DESCR)

# Checking the number of samples, features, and targets
print("\n", iris.data.shape)
print("\n", iris.target.shape)
print("\n", iris.target_names)
print("\n", iris.feature_names)

# Exploring the Iris Dataset with Pandas
# Use feature_names as the column names
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)

# List comprehension uses each value in target array to look up the corresponing
# species name in target_names array
iris_df['species'] = [iris.target_names[i] for i in iris.target]
# Peek at the first 5
print(iris_df.head())

pd.set_option('display.precision', 2)  # 2 digit precision for floats
print(iris_df.describe())

# Calling describe on the species column confirm that it contains 3 unique value
iris_df['species'].describe()

# Visualizing the Dataset with a Seaborn pairplot
sns.set_style('whitegrid')
grid = sns.pairplot(data=iris_df, vars=iris_df.columns[0:4], hue='species')
plt.show()
'''
    data — The DataFrame (or two-dimensional array or list) containing the data to plot.
    vars — A sequence containing the names of the variables to plot. For a DataFrame, these are the names of the columns to plot. 
        Here, we use the first four DataFrame columns, representing the sepal length, sepal width, petal length and petal width, respectively.
    hue — The DataFrame column that’s used to determine colors of the plotted data. 
        In this case, we’ll color the data by Iris species.
'''

# Using KMeans Estimator
# When training a KMeans estimator, it calculates for each cluster a centroied representing the cluster's center data point
kmeans = KMeans(n_clusters=3, random_state=11)

# Fitting the model via the KMeans object's fit method
kmeans.fit(iris.data)

# Comparing the cluster labels to the Iris Dataset's target values

# First 50 samples should be one cluster
print(kmeans.labels_[0:50])

# Second 50 samples should a second cluster
print(kmeans.labels_[50:100]) # Two values are not

# Last 50 samples should be a third cluster
print(kmeans.labels_[100:150])  # 14 are not

# Use PCA estimator to perform dimensionality reduction from 4 to 2
pca = PCA(n_components=2, random_state=11)

# Transforming the Iris dataset feature into 2D
pca.fit(iris.data)  # trains estimator once
# Calling transform again to reduce the cluster centroid to 2D for plotting
iris_pca = pca.transform(iris.data)

print(iris_pca.shape)

# Visualizing the Reduced data
# Place reduced data in a DataFrame and add a species column that can be used to determine dot colors
iris_pca_df = pd.DataFrame(iris_pca, 
                           columns=['Component1', 'Component2'])
iris_pca_df['species'] = iris_df.species

axes = sns.scatterplot(data=iris_pca_df, x='Component1', 
    y='Component2', hue='species', legend='brief') 

# reduce centroids to 2 dimensions
iris_centers = pca.transform(kmeans.cluster_centers_)

# plot centroids as larger black dots
dots = plt.scatter(iris_centers[:,0], iris_centers[:,1], s=100, c='k')

plt.show()

# Choosing the best clustering estimator
estimators = {
    'KMeans': kmeans,
    'DBSCAN': DBSCAN(),
    'MeanShift': MeanShift(),
    'SpectralClustering': SpectralClustering(n_clusters=3),
    'AgglomerativeClustering': 
        AgglomerativeClustering(n_clusters=3)
}

for name, estimator in estimators.items():
    estimator.fit(iris.data)
    print(f'\n{name}:')
    for i in range(0, 101, 50):
        labels, counts = np.unique(
            estimator.labels_[i:i+50], return_counts=True)
        print(f'{i}-{i+50}:')
        for label, count in zip(labels, counts):
            print(f'   label={label}, count={count}') 
