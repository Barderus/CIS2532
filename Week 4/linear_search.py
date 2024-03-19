''' Linear Search '''
import numpy as np

def linear_search(data, search_key):
    for index, value in enumerate(data):
        if value == search_key:
            return index
    return "Not found"
    
np.random.seed(11)
values = np.random.randint(10, 91, 10)
print(values)

print(linear_search(values, 23))
print(linear_search(values, 61))
print(linear_search(values, 34))
