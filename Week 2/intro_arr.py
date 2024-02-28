'''
Intro to Arrays and NumPy
'''

import numpy as np

# Initialize a 1D NumPy array using a Python list
numbers = np.array([2, 3, 5, 7, 11])

print(type(numbers))  # numpy.ndarray

# Initialize a 2D NumPy array using a Python list
array_int = np.array([[1,2,3], [4,5,6]])

array_float = np.array([0.1, 0.0, 0.02, 0.301, 0.40])

print(f"Print the first array: {numbers}")

print(f"Print the second array: {array_int}")

print(f"Printing array 3: {array_float}")

# Determining an array's number of elements and element size

print(f"\nDisplay the size of an integer array: {array_int.size}")
print(f"Display the number of bytes required to store each element: {array_int.itemsize}")

print(f"\nDisplay the size of a float array: {array_float.size}")
print(f"Display the number of bytes required to store each element: {array_float.itemsize}")

# Iterating through a Multidemnstional array of elements
#Method 1
print("\nMethod 1")
'''
    It prints:
    1 2 3
    4 5 6
'''
for row in array_int:
    for column in row:
        print(column, end = " ")
    print()
    
# Method 2
print("\nMethod 2")
for i in array_int.flat:
    print(i, end = "")

