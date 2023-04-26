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

    if not isinstance (a, int) or not isinstance (a, float):
        raise TypeError('a must be an integer')
    a = int(a)
    if not isinstance (b, int) or not isinstance (b, float):
        raise TypeError('b must be an integer')
    b = int(b)
    return(a + b)
