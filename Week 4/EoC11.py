import numpy as np

 # 11.1 What does the following code do?
def mystery(a, b):
    if b == 1:
        return a
    else:
        print(a)
        return a + mystery(a, b-1)

# This mystery function keeps adding 2 to a for 10 times. Resulting in 20.
print((mystery(2, 10)))

# 11.2 Find the logic error(s) in the following recursive functions, and explain how to correct it (them). 
#   This function should find the sum of the values from 0 to n. 
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)

print(sum(3))
# The function sum would go forever, because it would never reach 0. Thus, addding - 1 to the parameter inside the recursion fix the issue.


# 11.3 What does the following code do?
def mystery(a_array, size):
    if size == 1:
        return a_array[0]
    else:
        return a_array[size -1] + mystery(a_array, size - 1)
    
numbers = np.arange(1,11)
mystery(numbers, len(numbers))
# This function goes down each index and add each number of the array together such as 1+2+3+4+5+6+7+8+9+10 = 55


''' 11.4 In section 11.3 we presented a recursive factorial function. What happens if you remove the if statement
from the factorial function, then call the function?

# If you remove the if statement, it removes the recursion control of the function, allowing it to be called until stack overflow occurs.
'''

# 11.5 Write a recursive function power(base, exponent) that when called, returns base^exponent
# For example, power(3, 4) = 3*3*3*3. Assume that exponent is an integer greater than or equal to 1. 
# Exits recursion when exponent is equal to 1

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent-1)
    
print(power(3, 4))