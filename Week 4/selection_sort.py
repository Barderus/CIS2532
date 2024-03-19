''' Selection sort 
    A simple, but inefficient sorting algorithm
    1. Select smallest element in the aray and swaps it with the first element
    2. Select the second smallest element in the array and swaps with the second element
    3. It continnues until the second-largest element is swaped with the second-to-last index
'''

import numpy as np

def selection_sort(data):
    """Sort array using selection sort."""
    # loop over len(data) - 1 elements      
    for index1 in range(len(data) - 1):
        smallest = index1  # first index of remaining array

        # loop to find index of smallest element                      
        for index2 in range(index1 + 1, len(data)): 
            if data[index2] < data[smallest]:
                smallest = index2
                                              
        # swap smallest element into position
        data[smallest], data[index1] = data[index1], data[smallest]  
        print_pass(data, index1 + 1, smallest)

def print_pass(data, pass_number, index): 
    """Print a pass of the algorithm."""
    label = f'after pass {pass_number}: '
    print(label, end='')

    # output elements up to selected item
    print('  '.join(str(d) for d in data[:index]), 
        end='  ' if index != 0 else '') 

    print(f'{data[index]}* ', end='')  # indicate swap with *

    # output rest of elements
    print('  '.join(str(d) for d in data[index + 1:len(data)]))

    # underline elements that are sorted after this pass_number
    print(f'{" " * len(label)}{"--  " * pass_number}') 

def main(): 
    data = np.array([34, 56, 14, 20, 77, 51, 93, 30, 15, 52])
    print(f'Unsorted array: {data}\n')
    selection_sort(data) 
    print(f'\nSorted array: {data}\n')

main()