#!/usr/bin/python3
""" This module print out a statement """
def say_my_name(first_name, last_name=" "):
    
    """ Args
            first_name: first name
            last_name: last name

         return 
            Both first_name and last_name

         Raise
            TypeError: when name is not a string
    """
    if not isinstance (first_name, str):
        raise TypeError ('first_name must be a string')

    if not isinstance (last_name, str):
        raise TypeError ('last_name must be a string')

    print(f'My name is {first_name} {last_name}')

