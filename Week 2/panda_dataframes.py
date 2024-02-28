'''
    Pandas DataFrames
'''
import pandas as pd

# Create a DataFrame from a dictionary
grades_dict = ({"Wally":[87, 96, 70], "Eva":[100, 87, 90],
                "Sam":[94, 77, 90], "Katie":[100, 81, 82],
                "Bob":[83, 65, 85]})

grades = pd.DataFrame(grades_dict)
print(f"Grades in DataFrame:")
print(grades)

# Customizing a DataFrame indices with the Index attribute
grades.index = ["Test1", "Test2", "Test3"]
print()
print(grades)

# Acessing a DataFrame's columns
print(f"\nEva's test result:\n{grades['Eva']}")

# Accessing DataFrame's row -- .loc["Name of the row (str)"]
print(f"\nTest1 result:\n{grades.loc['Test1']}")

# Accessing DataFrame's row --iloc[integer index]
print(f"\nTest 2 result:\n{grades.iloc[1]}")

# Selecting row via Slices and Lists
print(f"\nTest1 to test3 result:\n{grades.loc['Test1':'Test3']}")
print(f"\nTest 2 result:\n{grades.iloc[0:2]}")  # Excludes the high index

# Selecting specific rows with a list
print(f"\nTest1 to test3 result:\n{grades.loc[['Test1', 'Test3']]}")
print(f"\nTest 2 result:\n{grades.iloc[0,2]}")  


''' Boolean Indexing '''
# Display only grades > 90 or A
print(f"\nGrades >= 90:\n{grades[grades >= 90]} ")

# Display only grades between 80 and 90
print(f"\nB grades:\n{grades[(grades >= 80) & (grades < 90)]}") 

# Describe DataFrame data
#pd.set_option('precision', 2)
print(f"\nUsing the describe method to summarize data:\n{grades.describe()}")
