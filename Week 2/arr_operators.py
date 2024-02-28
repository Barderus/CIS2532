'''
    Array operators
'''
import numpy as np

# Create a 1D array from 1 to 6 not inclusive
numbers = np.arange(1,6)

# Multiply the elements of numbers by 2
numbers2 = numbers * 2     # Broadcasting = [1,2,3,4,5] * [2,2,2,2,2]

# Each element to the power of 3
numbers3 = numbers ** 3

# Add 10 to each element
numbers10 = numbers + 10

# Arithmetic operations between arrays
numbers_float = np.linspace(1.1, 5.5, 5)
result = numbers * numbers_float

# Comparing arrays
# Check if any array is equal or bigger than 13
compare_size = numbers >= 13     # Returns: [False False False False False]
print(compare_size)

# Compare two arrays
compare_arr = numbers < numbers2    #Returns: [ True  True  True  True  True]
print(compare_arr)

# Check if arrays have the same value
compare_values = numbers == numbers2        #Returns: [False False False False False]
compare_values = numbers == numbers         # Returns: [ True  True  True  True  True]
print(compare_values)

