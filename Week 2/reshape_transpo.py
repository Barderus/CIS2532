'''
    Reshaping and Transposing
'''
import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90]])
print("Grades: ", grades)

# Reshape returns a view (shallow copy) of the original array with new dimensions
print("\nReshaped grades: ", grades.reshape(1,6))

# The original grades has not changed
print("Unmodified grades array:", grades)

grades.resize(1,6)
print("\nResized (modified) grades: ", grades)

# Grades has changed its dimension
print(grades)

''' Flatten method -> Produces a deep copy'''

print()
grades2 = np.array([[87, 96, 70], [100, 87, 90]])
print()
print("Grades2: ", grades2)

# Flatten a multi-dimensional array into a single dimension. Uses deep copy
flattened = grades2.flatten()
print("\nFlatenned deep copy: ", flattened)

flattened[0] = 100
print(f"\nBoth flatenned copy {flattened} and the original \ngrades {grades2}\n has changed.")

''' Ravel method -> Produces a shallow copy'''
print()
raveled = grades2.ravel()

print("Raveled copy of grades2: ", raveled)

# Changing the value only of ravel. It does not influence the original
raveled[0] *= 10

print("\nModified raveled array: ", raveled)
print("\nUnmodified  grades2: ", grades2)


''' Transposing rows and columns -> Exchange rows by the columns '''

print()
grades.T
print(grades)

''' Stacking arrays '''
print()
grades3 = np.array([[94, 77, 90], [100, 81, 82]])

# Horizontal stack -> Add more columns
print("Adding more columns:")
print(np.hstack((grades2, grades3)))
print()

# Vertical stack -> Add more rows
print("Adding more rows: ")
print(np.vstack((grades2, grades3)))