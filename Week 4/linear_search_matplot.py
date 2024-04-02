import matplotlib.pyplot as plt
import numpy as np

# Create a list of numbers to search
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Define the target value to search for
target = int(input("Enter a number between 1 and 10"))

# Create a function to perform linear search
def linear_search(data, search_key):
    for index, value in enumerate(data):
        if value == search_key:
            return index
    return "Not found"

# Perform linear search
index = linear_search(numbers, target)

# Plot the results by making an animation
