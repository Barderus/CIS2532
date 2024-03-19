''' Insertion Sort 
        Simple, but inefficient algorithm.
        1. Takes the second element in the array and, if it's less than the first element, swaps it with the first element.
        2. Looks the third element and inserts it into the correct position with respect to the first two.
'''
import numpy as np

def insertion_sort(data):
    """Sort an array using insertion sort."""
    # loop over len(data) - 1 elements      
    for next in range(1, len(data)):
        insert = data[next]  # value to insert 
        move_item = next  # location to place element

        # search for place to put current element         
        while move_item > 0 and data[move_item - 1] > insert:  
            # shift element right one slot
            data[move_item] = data[move_item - 1]         
            move_item -= 1                                      
                                              
        data[move_item] = insert  # place inserted element 
        print_pass(data, next, move_item)  # output pass of algorithm

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
    insertion_sort(data) 
    print(f'\nSorted array: {data}\n')

main()