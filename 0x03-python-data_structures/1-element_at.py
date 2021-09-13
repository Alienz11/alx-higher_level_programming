#!/usr/bin/python3
def element_at(my_list, idx):
    '''
    Prints specific items in a list of integers
    Parameters:
    my_list (list): The list of integers
    idx: positioning number to identify specific list item.
    '''
    if idx < 0:
        return None
    elif (idx < 0) and (idx > len(my_list)):
        return None
    else:
        return my_list[idx]
