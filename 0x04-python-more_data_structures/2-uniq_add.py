#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_of_unique_numbers = 0
    uniq_nom = set(my_list)

    for no in uniq_nom:
        list_of_unique_numbers += no
    return(list_of_unique_numbers)
