#!/usr/bin/python3
""" Matrix multiplication """

def matrix_mul(m_a, m_b):
    """
        Args: Enter a list of integer/float for m_a.
              Enter a list of integer/float for m_b.

        Return: A list of multiplied matrix.

        Raise:
               TypeError if any of the argument is not a list
               TypeError if any of the argument is not a list of list.
               ValueError if the list is an empty list
               ValueError if the argument cant be multiplied

    """

    if not isinstance (m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance (m_b, list):
        raise TypeError('m_b must be a list')
        
        for elem1 in m_a:
            if not isinstance(elem1, list):
                raise TypeError('m-a must be a list of list')
            if not type(elem1) in (int, float):
                raise TypeError('m_a should contain only integer/float')
        for elem2 in m_b:
            if not isinstance(elem2, list):
                raise TypeError('m_b must be a list of list')
            if not type(elem2) in (int, float):
                raise TypeError('m_b should contain only integer/float')
        if m_a == [] or m_a == [[]]:
            raise ValueError('m_a cant be empty')
        
        if m_b == [] or m_b == [[]]:
            raise ValueError('m_b cant be empty')
        
        if not all(len(row) == len(m_a[0]) for row in m_a):
            raise TypeError("each row of m_a must should be of the same size")
        if not all(len(row) == len(m_b[0]) for row in m_b):
            raise TypeError("each row of m_b must should be of the same size")

        if len(m_a[0]) != len(m_b):
            raise ValueError('m_a and m_b cant be multiplied')

    inverted_b = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
