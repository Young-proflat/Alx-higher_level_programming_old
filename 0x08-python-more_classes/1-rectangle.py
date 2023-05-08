#!/usr/bin/python3
""" This module accept part of a rectangle

    Function: def Rectangle(width, height):

    accept:
            width
            height

    Return:
            TypeError for Non-integers.
            ValueError for variable less than 0
"""

class Rectangle:
    def __init__(self,width = 0, height = 0):
        self.width = width
        self.height = height

# width function 
    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if not isinstance (value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

#height function
    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if not isinstance (value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
