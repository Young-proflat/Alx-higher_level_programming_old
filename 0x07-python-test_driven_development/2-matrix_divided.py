#!/usr/bin/python3

""" It print out a matrix output divided 
    by 2 in two decimal figure
"""
def matrix_divided(matrix, div):
    

    if not type(div) in (int, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance (matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    len_elem = 0
    for elems in matrix:
        if not elems or not isinstance (elems, list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len_elem != 0 and len(elems) != len_elem:
            raise TypeError('Each row of the matrix must have the same size')

        for num in elems:
            if not type(num) in (int, float):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        len_elems = len(elems)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
