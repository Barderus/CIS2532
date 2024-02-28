'''
    Universal Functions
        ** Functions that operates on arrays in an element by element fashion
'''
import numpy as np

# Get the square root of each element
numbers = np.array([1, 4, 9, 16, 25, 36])
print("Square root of the elements of numbers: ", np.sqrt(numbers))

#Create an array from 1 to 7, exclusive and multiply by 10
numbers2 = np.arange(1,7) * 10
print("Numbers from 1 to 6 and multiply them by 10: ", numbers2)

# Add numbers and numbers2
print("\nAdd numbers and numbers2: ", np.add(numbers, numbers2))

# Multiply the value of numbers2 by 5
print("\n", np.multiply(numbers2, 5))

# Reshape the array into two rows and 3 columns.
numbers3 = numbers2.reshape(2,3)
print("\n",numbers3)

# Multiply row1,column 1 by 2 
# Multiply row1, column2 by 4
# Multiply row1, columnn3 by 6
# So on...
numbers4 = np.array([2,4,6])
print("\n", np.multiply(numbers3, numbers4))
