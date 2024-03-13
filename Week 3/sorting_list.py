''' Sorting List   '''

numbers = [10,3,7,1,9,4,2,8,5,6]
numbers.sort()  # Sorting the numbers in ascending order
print(numbers)

numbers.sort(reverse=True)  # Sort the numbers in descending order
print(f"\n{numbers}") 

numbers = [101, 213, 1234, 7, 125, 754, 29, 10, 12, 5]
ascending_numbers = sorted(numbers)     # Returns a sorted list
print(f"\nAscending numbers list: {ascending_numbers}\nNumbers list: {numbers}\n")


''' List method search '''

letters = ["a", "e", "t", "f", "q", "z", "p"]
print(f"Returns the index of the letter 't': {letters.index('t')}")