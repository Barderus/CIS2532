''' Intro to Recursion  '''

def factorial(number):
    ''' Return factorial of a number '''
    if number <= 1:
        return 1
    return number * factorial(number - 1)

print(factorial(4)) # Print 4! = 24
print()
for i in range(11):
    print(f'{i}! = {factorial(i)}')

print()

''' Fibonacci '''
def fibonacci(n):
    if n in (0,1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

for n in range(10):
    print(f'Fibonacci({n}) = {fibonacci(n)}')