'''
    Panda series
'''
import pandas as pd

# Series
grades = pd.Series([87, 100, 94])
print(grades)
'''
    Display
0     87
1    100
2     94
dtype: int64

'''
print()
print(pd.Series(98.6, range(3)))
'''
    Display
0    98.6
1    98.6
2    98.6
dtype: float64
'''
print()
# Access a series' elements
print(grades[0])
print()

# Series methods

#Count
print(f"Display the .count method on grades: {grades.count()}")

#mean
print(f"\nDisplay the .mean method on grades: {grades.mean()}")

# min
print(f"\nDisplay the .min method on grades: {grades.min()}")

# max
print(f"\nDisplay the .max method on grades: {grades.max()}")

# std
print(f"\nDisplay the .std method on grades: {grades.std()}")


''' Describe method '''
print(f"\nThe method describes several stats from a series:\n{grades.describe()}")
'''
The method describes several stats from a series:
count      3.000000
mean      93.666667
std        6.506407
min       87.000000
25%       90.500000
50%       94.000000
75%       97.000000
max      100.000000
dtype: float64
'''

# Creating a Series with custom indices
print()
grades = pd.Series([87, 90, 94], index = ["Wally", "Eva", "Sam"])
print(grades)

# Creating series with Dictionary initializer where Key = indices, values = series' values
print()
grades2 = pd.Series({"Tomas":100, "Mary":94, "Sam":78})
print(grades2)

# Access data through the custom indices
print()
print("Sam's grade:", grades2["Sam"])
print()
print(grades.Wally)

# Return the data type of the array
print()
print(grades.dtype)

# Return the values of the dictionary array
print()
print(grades.values)

''' Creating a Series of Strings '''
hardware = pd.Series(["Hammer", "Saw", "Wrench"])
print()
print(hardware)

print()

# Check if the string in the hardware series has "a"
print(hardware.str.contains("a"))
print()

print(f"\nHardware strings in upper:\n{hardware.str.upper()}")