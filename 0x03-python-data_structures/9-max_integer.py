#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1 or my_list is None:
        return None
    maxi = my_list[0]
    for no in my_list:
        if no > maxi:
            maxi = no 
    return(maxi)

