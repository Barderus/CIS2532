'''
    Shallow and Deep copies
        ** Shallow copy creates a new object with the same values
            as the original object
            It creates a new array that poitts to the same elements as the
                original array
        ** A deep copy creates a new object that contains copies of
            the original object
            It is completely independent of the original array. They do not share
                any data
'''
import numpy as np

numbers = np.arange(1,6)
print("Numbers: ", numbers)

# Create a shallow copy of numbers
numbers2 = numbers.view()
print("Numbers2: ", numbers2)

# id unction to see that numbers and numbers2 are different objects
print("Numbers ID: ", id(numbers))
print("Numbers2 ID: ", id(numbers2))

# Modifting an element in the original array also changes the view and vice-versa
numbers[1] *= 10
numbers2[3] *= 5
print(numbers)
print(numbers2)

# Slice also create views
numbers2 = numbers[0:3]
print(numbers2)

''' Deep copies '''
print()
num = np.arange(5, 11)
print("Num values: ", num)

num2 = num.copy()
print("Num2 values: ", num2)

num[2] *= 5 # Multiply the third element by 5
num2[0] += 10 # Add 10 to the first element

# Note that in a deep copy, they do not share the same values
print("\nNew num value", num)
print("New num2 value", num2)