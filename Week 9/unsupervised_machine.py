from sklearn.datasets import load_digits
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Loading the Digits dataset
digits = load_digits()

# TSNE estimator uses an algorithm called t-distributed Stochastic Neighbor Embedding (t-SNE) to analyze a dataset's feature and reduce them to the specified number of dimensions
# Create a TSNE object that reduces a dataset's feature to two dimensions.
# random_state for reproducibility of the "render sequence" when we display the digit clusters
tsne = TSNE(n_components=2, random_state=11)

# Transforming the Digits dataset feature into two dimensions
# Two steps:
#   Train the estimator with the dataset
#   Use the estimator to transform the data into the specified number of dimensions
# Returns array with same number of rows as digits.data and two columns (2 features)
reduced_data = tsne.fit_transform(digits.data)
print(reduced_data.shape)

# Visualizing the Reduced Data using scatterplot
figure = plt.figure(figsize=(5, 5))
dots = plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c='black')

# Adding different colors for each digit so it's easier to represent
figure = plt.figure(figsize=(6, 5))

dots = plt.scatter(reduced_data[:, 0], reduced_data[:, 1],
    c=digits.target, cmap=plt.cm.get_cmap('nipy_spectral_r', 10))
 
colorbar = plt.colorbar(dots) 

plt.show()
