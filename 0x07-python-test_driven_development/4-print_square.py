#!/usr/bin/python3
""" This module print the square with a character """

def print_square(size):
    """
    Args
    size : Integers

    return
    Square: square of a character(#)

    TypeError
    Error: in input if not int
    Error: if size less than 0.

    """
    if not isinstance (size, int):
        raise TypeError ('size must be an integer')
    if size < 0:
        raise ValueError ('size must be >= 0')

    for i in range(size):
        print('#' * size)
