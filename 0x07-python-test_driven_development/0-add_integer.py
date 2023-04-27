#!/usr/bin/pyhton3
"""
This module is composed of a function that adds two numbers
"""

def add_integer(a, b=98):
    """ Function that adds two int/float numbers

    Args:
        a: first number
        b: second number

    Returns:
        The addition of two numbers

    Raises:
        TypeErrors: If a and b aren't int or float number.

    """
     if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
