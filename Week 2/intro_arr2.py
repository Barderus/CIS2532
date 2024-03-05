'''
    Intro to Array part 2
'''
import numpy as np

zero_arr = np.zeros(5)
print(f"Display an array of 5 zeros: {zero_arr}")

array_int = np.ones((2,4), dtype= int)
print(f"\nDisplay a 2D array of four 1s:")
for row in array_int:
    for column in row:
        print(column, end = " ")
    print()
    
second_arr = np.full((3,5), 13)
print(f"Display a 3D array of five 13s:")
for r in second_arr:
    for c in r:
        print(c, end = " ")
    print()
    
# Creating an array from Ranges
print()

arr_five = np.arange(5) # Create an array from 0 to 4, not inclusive
arr_ranges = np.arange(5,10) # Create an array from 5 to 9, not inclusive
decr_array = np.arange(10, 1, -2) # Create an array from 10 to 1

print(f"\nArray1 : {arr_five}\nArray 2: {arr_ranges}\n Decrement array: {decr_array}")

# Creating an array with floats
arr_floats = np.linspace(0.0, 1.0, num = 5) # Array = [0.0, 0.25, 0.5, 0.75, 1.0] Inclusive
print(f"Create a float array from 0.0 to 1.0 incrementin by 0.25:\n{arr_floats}")

# Reshape array into different number of dimensions
reshape_arr = np.arange(1,21).reshape(4,5) # Create a 4 by 5 array from 1 to 21 not inclusive
print(f"\n4D array of 5 elements:")
for x in reshape_arr:
    for i in x:
        print(i, end = " ")
    print()
    
    
# Displaying large arrays
'''
It displays:
[[     1      2      3 ...  24998  24999  25000]
 [ 25001  25002  25003 ...  49998  49999  50000]
 [ 50001  50002  50003 ...  74998  74999  75000]
 [ 75001  75002  75003 ...  99998  99999 100000]]
 '''
large_arr = np.arange(1, 100001).reshape(4,25000)
print(large_arr)
print()
large_arr2 = np.arange(1, 100001).reshape(100, 1000)
print("\n",large_arr2)