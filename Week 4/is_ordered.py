''' 5.14 Is a sequence sorted? 
    Create a function is_ordered that receives a sequence and return True if the element are in sorted order. 
    Test the function with sorted and unsorted lists, tuple and strings.
'''

def is_ordered(sequence):
     return list(sequence) == sorted(list(sequence))

def seq_list():
    unsorted_list = [1, 0, 2, 9, 3, 8, 4, 7, 5, 6]
    sorted_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("Is unsorted_list ordered?", is_ordered(unsorted_list))
    print("Is sorted_list ordered?", is_ordered(sorted_list))
    print()

def seq_tuple():
    unsorted_tuple = (0, 9, 8, 1, 2, 3, 7, 6, 5, 4)
    sorted_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

    print("Is unsorted_tuple ordered?", is_ordered(unsorted_tuple))
    print("Is sorted_tuple ordered?", is_ordered(sorted_tuple))
    print()

def seq_strings():
    unsorted_string = "hello"
    sorted_string = "ehllo"

    print("Is unsorted_string ordered?", is_ordered(unsorted_string))
    print("Is sorted_string ordered?", is_ordered(sorted_string))

def main():
    seq_list()
    seq_tuple()
    seq_strings()

if __name__ == "__main__":
    main()