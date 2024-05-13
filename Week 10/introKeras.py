from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPooling2D



# Load training and testing sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Check dimensions of the training set images (X_train), training set labels (y_train), testing set images (X_test) and testing set labels (y_test):
print('MNIST Dataset Shape:')
print('X_train: ' + str(X_train.shape))
print('Y_train: ' + str(y_train.shape))
print('X_test:  '  + str(X_test.shape))
print('Y_test:  '  + str(y_test.shape))

# Visuaizing the 24 MNIST training set images

index = np.random.choice(np.arange(len(X_train)), 24, replace=False)  # 24 indices
figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(16, 9))

for item in zip(axes.ravel(), X_train[index], y_train[index]):
    axes, image, target = item
    axes.imshow(image, cmap=plt.cm.gray_r)
    axes.set_xticks([])  # remove x-axis tick marks
    axes.set_yticks([])  # remove y-axis tick marks
    axes.set_title(target)

plt.tight_layout()
plt.show()

# Channels: represent more complex features, lke edges, curves, and lines
# Numpy array method reshape receies a tuple representing the new tuple
X_train = X_train.reshape((60000, 28, 28, 1)) 
print(X_train.shape)
X_test = X_test.reshape((10000, 28, 28, 1))
print(X_test.shape)

# Normalizing the data
#Deep learning networks perform better on data that's normalized into the range 0.0-1.0, or 
#a range for which the data’s mean is 0.0 and its standard deviation is 1.0
# * Divide each pixel value by 255 to normalize into the range 0.0-1.0:
X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255
X_train.shape
X_test.shape

#Transform y_train and y_test into two-dimensional arrays of categorical data
y_train = to_categorical(y_train)
y_train.shape

y_train[0]  # one sample’s categorical data
y_test.shape

'''
Creating the Neural Network
* Configure a convolutional neural network
* Sequential model** stacks layers to execute sequentially
    * output of  one layer becomes input to the next
    * Feed-forward network
'''
cnn = Sequential() 
# Adding a convolution layer
cnn.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu', 
               input_shape=(28, 28, 1)))

# Adding a pooling layer
cnn.add(MaxPooling2D(pool_size=(2, 2)))
cnn.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))
cnn.add(MaxPooling2D(pool_size=(2, 2)))

# Flatten layer's output will be 1-by-3200 (5 × 5 × 128
cnn.add(Flatten())

# The following Dense layer creates 128 neurons (units) that learn from the 3200 outputs of the previous layer 
cnn.add(Dense(units=128, activation='relu'))

# Addinng another layer to produce the output
cnn.add(Dense(units=10, activation='softmax'))

# Printing the model summary
print(cnn.summary())

# Compiling the model
cnn.compile(optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy'])

# Training and evaluating the model
cnn.fit(X_train, y_train, epochs=5, batch_size=64, validation_split=0.1)

# Make Predictions with the Model's predict method
predictions = cnn.predict(X_test)

# Display the probablity of getting the values right
for index, probability in enumerate(predictions[0]):
    print(f'{index}: {probability:.10%}')


# Locating the wrong predictions
images = X.test.reshape((10000, 28, 28))
incorrect_predictions = []

for i, (p, e) in enumerate(zip(predictions, y_test)):
    predicted, expected = np.argmax(p), np.argmax(e)
    if predicted != expected:  # prediction was incorrect
        incorrect_predictions.append((i, images[i], predicted, expected))

len(incorrect_predictions)  # number of incorrect predictions

# Display the 24 of the incorrect images labeleb with each image's index, predicted value (p) and expected value (e)
figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(16, 12))

for axes, item in zip(axes.ravel(), incorrect_predictions):
    index, image, predicted, expected = item
    axes.imshow(image, cmap=plt.cm.gray_r)
    axes.set_xticks([])  # remove x-axis tick marks
    axes.set_yticks([])  # remove y-axis tick marks
    axes.set_title(f'index: {index}\np: {predicted}; e: {expected}')
plt.tight_layout()
plt.show()

## Displaying the probabilities for several incorrect predictions
def display_probabilities(prediction):
    for index, probability in enumerate(prediction):
        print(f'{index}: {probability:.10%}')

display_probabilities(predictions[340])

# Saving the model
cnn.save('mnist_cnn.h5')