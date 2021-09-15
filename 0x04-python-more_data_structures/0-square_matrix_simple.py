#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
    Prints the items in a list of integers
    Parameters:
    my_list (list): The list of integers
    '''
    new_matrix = [[(m[i] ** 2) for i in range(3)] for m in matrix]
    print(new_matrix)
