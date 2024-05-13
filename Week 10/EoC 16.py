from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPooling2D 
from tensorflow.keras.utils import plot_model

'''
    16.1 Modify this chapter's covnet example to load and process Fashion-MNIST rather than MNIST. 
    How does the model perform on Fashion-MNIST compared to MNIST? How do the training model compare?
'''

# Load training and testing sets
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
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

# Training the data
X_train = X_train.reshape((60000, 28, 28, 1)) 
print(X_train.shape)
X_test = X_test.reshape((10000, 28, 28, 1))
print(X_test.shape)

X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255
X_train.shape
X_test.shape

y_train = to_categorical(y_train)
y_train.shape

y_train[0]  # one sample’s categorical data
y_test.shape

cnn = Sequential() 
cnn.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu', 
               input_shape=(28, 28, 1)))

cnn.add(MaxPooling2D(pool_size=(2, 2)))

cnn.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))

cnn.add(MaxPooling2D(pool_size=(2, 2)))
cnn.add(Flatten())
cnn.add(Dense(units=128, activation='relu'))
cnn.add(Dense(units=10, activation='softmax'))
cnn.summary()

# Compiling the model
cnn.compile(optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy'])

# Training and evaluating the model
cnn.fit(X_train, y_train, epochs=5, batch_size=64, validation_split=0.1)

# Make Predictions with the Model's predict method
predictions = cnn.predict(X_test)
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

for index, probability in enumerate(predictions[0]):
  print(f'{class_names[index]}: {probability:.10%}')

'''
    16.2 - Change the kernel size from 3x3 to 5x5. Re-execute the model. How does this change the prediction accuracy?
'''

# Loading the data for training and testing
(X_train, y_train), (X_test, y_test) = mnist.load_data()
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

X_train = X_train.reshape((60000, 28, 28, 1)) 
print(X_train.shape)
X_test = X_test.reshape((10000, 28, 28, 1))
print(X_test.shape)

X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255
X_train.shape
X_test.shape

y_train = to_categorical(y_train)
y_train.shape

y_train[0]  # one sample’s categorical data
y_test.shape

cnn = Sequential() 
cnn.add(Conv2D(filters=64, kernel_size=(5, 5), activation='relu', 
               input_shape=(28, 28, 1)))    # Changing the kernel size from 3x3 to 5x5

cnn.add(MaxPooling2D(pool_size=(2, 2)))

cnn.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))

cnn.add(MaxPooling2D(pool_size=(2, 2)))
cnn.add(Flatten())
cnn.add(Dense(units=128, activation='relu'))
cnn.add(Dense(units=10, activation='softmax'))
cnn.summary()

cnn.compile(optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy'])

# Training and evaluating the model
cnn.fit(X_train, y_train, epochs=5, batch_size=64, validation_split=0.1)

# Make Predictions with the Model's predict method
predictions = cnn.predict(X_test)

for index, probability in enumerate(predictions[0]):
  print(f'{class_names[index]}: {probability:.10%}')

'''
    16.3 Re-execute the model for batch sizes of 32 and 128. How do these values change the prediction accuracy?
'''

# Batch size: 32
# Loading the data for training and testing
(X_train, y_train), (X_test, y_test) = mnist.load_data()
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

X_train = X_train.reshape((60000, 28, 28, 1)) 
print(X_train.shape)
X_test = X_test.reshape((10000, 28, 28, 1))
print(X_test.shape)

X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255
X_train.shape
X_test.shape

y_train = to_categorical(y_train)
y_train.shape

y_train[0]  # one sample’s categorical data
y_test.shape

cnn = Sequential() 
cnn.add(Conv2D(filters=64, kernel_size=(5, 5), activation='relu', 
               input_shape=(28, 28, 1)))

cnn.add(MaxPooling2D(pool_size=(2, 2)))

cnn.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))

cnn.add(MaxPooling2D(pool_size=(2, 2)))
cnn.add(Flatten())
cnn.add(Dense(units=128, activation='relu'))
cnn.add(Dense(units=10, activation='softmax'))
cnn.summary()

cnn.compile(optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy'])

# Training and evaluating the model
cnn.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.1) # Change the batch size to 32

# Make Predictions with the Model's predict method
predictions = cnn.predict(X_test)

for index, probability in enumerate(predictions[0]):
  print(f'{class_names[index]}: {probability:.10%}')

# Batch size: 128
(X_train, y_train), (X_test, y_test) = mnist.load_data()
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

X_train = X_train.reshape((60000, 28, 28, 1)) 
print(X_train.shape)
X_test = X_test.reshape((10000, 28, 28, 1))
print(X_test.shape)

X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255
X_train.shape
X_test.shape

y_train = to_categorical(y_train)
y_train.shape

y_train[0]  # one sample’s categorical data
y_test.shape

cnn = Sequential() 
cnn.add(Conv2D(filters=64, kernel_size=(5, 5), activation='relu', 
               input_shape=(28, 28, 1)))

cnn.add(MaxPooling2D(pool_size=(2, 2)))

cnn.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))

cnn.add(MaxPooling2D(pool_size=(2, 2)))
cnn.add(Flatten())
cnn.add(Dense(units=128, activation='relu'))
cnn.add(Dense(units=10, activation='softmax'))
cnn.summary()

cnn.compile(optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy'])

# Training and evaluating the model
cnn.fit(X_train, y_train, epochs=5, batch_size=128, validation_split=0.1)

# Make Predictions with the Model's predict method
predictions = cnn.predict(X_test)

for index, probability in enumerate(predictions[0]):
  print(f'{class_names[index]}: {probability:.10%}')

'''
    16.4 - Remove the first Dense layer in this chapter's covnet model. 
    How does this change the prediction accuracy? Several Keras petrained convnets contain Dense layers with 4096 neurons. 
    Add such a layer befoe the two Dense layers in this chapter's covnet model. 
    How does this change the mmodel with the complete training dataset?
'''
(X_train, y_train), (X_test, y_test) = mnist.load_data()
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

X_train = X_train.reshape((60000, 28, 28, 1)) 
print(X_train.shape)
X_test = X_test.reshape((10000, 28, 28, 1))
print(X_test.shape)

X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255
X_train.shape
X_test.shape

y_train = to_categorical(y_train)
y_train.shape

y_train[0]  # one sample’s categorical data
y_test.shape

cnn = Sequential() 
cnn.add(Conv2D(filters=64, kernel_size=(5, 5), activation='relu', 
               input_shape=(28, 28, 1)))

cnn.add(MaxPooling2D(pool_size=(2, 2)))

cnn.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))

cnn.add(MaxPooling2D(pool_size=(2, 2)))
cnn.add(Flatten())
# First Dense layer with 4096 neurons and ReLU activation
cnn.add(Dense(units=4096, activation='relu'))
# Second Dense layer with 128 neurons and ReLU activation
cnn.add(Dense(units=128, activation='relu'))
# Output layer with 10 neurons and softmax activation
cnn.add(Dense(units=10, activation='softmax'))
cnn.summary()

cnn.compile(optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy'])

# Training and evaluating the model
cnn.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.1)

# Make Predictions with the Model's predict method
predictions = cnn.predict(X_test)

for index, probability in enumerate(predictions[0]):
  print(f'{class_names[index]}: {probability:.10%}')