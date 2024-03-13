''' Filter, Map and Reduce function '''

''' Filter '''
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

def is_odd(x):
    # Returns True if x is odd.
    return x % 2 != 0

for num in numbers:
    print(is_odd(num), end=" ")     # Print False True True True True False False False True False 

print("\nFiltering out to display only the true elements:")
print(list(filter(is_odd, numbers)))    # Only display the True values

# Using list comprehension
print("\nUsing list comprehension:")
print([item for item in numbers if is_odd(item)])

# Using lambda
print("\nUsing lambda:")
print(list(filter(lambda x: x % 2 != 0, numbers)))          # Lambda syntax = lambda parameter: expression

''' Map '''
print()
print(f"\nNumbers: {numbers}")

print(list(map(lambda x: x ** 2, numbers)))     # Map is sorta like list comprehension. But it requires a function.
# [item ** 2 for item in numbers]

''' Combining filter and map '''
combined = list(map(lambda x: x** 2, filter(lambda x: x % 2 != 0, numbers)))  # Get the odd numbers and then power 2
print(f"\nCombining filter and map: {combined}")