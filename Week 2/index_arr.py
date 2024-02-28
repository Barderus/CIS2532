'''
    Index and Slicing
'''
import numpy as np

# 2D array          r1  r2  r3
grades = np.array([[87, 96, 70],        # row 0
                   [100, 87, 90],       # row 1
                   [94, 77, 90],        # row 2
                   [100, 81, 82]])      # row 3

print("Row 0 and column 1: ", grades[0, 1]) # Row 0, column 1
print("Row 3, column 2: ", grades[3,2])

# To select only a single row
print("Row 1: ", grades[1])

# Multiple sequential rows
print("Row 0 and 1: ", grades[0:2])

# Non-sequential rows
print("\nRow 1 and Row 3: ", grades[[1,3]])

# Subset of a 2D array columns
print("\nColumn 0: ", grades[:,0])      # Column 0:  [ 87 100  94 100]
print("\n Column 1 and 3: ", grades[:, 1:3])  # Confused
print("\nColumn 0 and 2: ", grades[:,[0,2]])    # Confused