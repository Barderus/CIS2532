'''
    List vs Array performance
    Arrays perform significantly faster than list
'''
import random
import timeit
import numpy as np

def create_rolls_list():
    rolls_list = [random.randrange(1, 7) for i in range(0, 6_000_000)]
    
def create_rolls_arr():
    rolls_array = np.random.randint(1, 7, 6_000_000)
    

print("Timing the Creation of a List Containing Results of 6,000,000 Die Rolls:")
print(timeit.timeit(create_rolls_list, number= 1))
print("\nTiming the Creation of an array Containing Results of 6,000,000 Die Rolls:")
print(timeit.timeit(create_rolls_arr, number= 1))
'''
Timing the Creation of a List Containing Results of 6,000,000 Die Rolls:
20.126756299985573

Timing the Creation of an array Containing Results of 6,000,000 Die Rolls:
0.15014339998015203
'''


