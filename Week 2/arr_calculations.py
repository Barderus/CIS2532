'''
    Numpy calculation methods
'''
import numpy as np

# 2D array
grades = np.array([[87, 96, 70], 
                   [100, 87, 90],       
                   [94, 77, 90], 
                   [100, 81, 82]])
print(grades)
print(f"Sum of the grades: {grades.sum()}")
print(f"Lowest grade {grades.min()}")
print(f"Highest grade {grades.max()}")
print(f"Mean of the grades: {grades.mean()}")
print(f"Standard deviation of the grades: {grades.std()}")
print(f"Variance of the grades: {grades.var()}")

# Calculations by row or column
# Display the highest value in the three columns
print(f"Highest grade of test1, test2, and test3: {grades.max(axis=0)}")     # Display: [ 100  96 90]  
print(f"Highest grade of each student: {grades.max(axis=1)}")               # Display:  [ 96 100  94 100]  
