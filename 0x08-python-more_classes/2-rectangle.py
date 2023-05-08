#!/usr/bin/python3

""" Creating an Area and Perimeter of a rectangle """
class Rectangle:
    """ A class rectangle """

    def __init__(self, width= 0, height= 0):
        """ initializating the class """
        self.width = width
        self.height = height

        """ Accept variable for width """
    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance (value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    """ Get/set the height of the rectangle """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance (value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    """ calculate the area of a rectangle """
    def area(self):
        return (self.width * self.height)

    """ calculate the perimeter of a rectangle """
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
