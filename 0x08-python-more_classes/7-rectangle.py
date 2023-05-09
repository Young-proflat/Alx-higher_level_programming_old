#!/usr/bin/python3
""" Printing a symbol variable """

class Rectangle:
    """ printing a string character class """

    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width = 0, height = 0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if not isinstance (value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise TypeError('width must be >= 0')
        self.__height = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if not isinstance (value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise TypeError('height must be >= 0')
        self.__height = value
    
    def area(self):
        return(self.__width * self.__height)

    def perimeter(self):
        """printing the perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return(self.__width + self.__height) * 2

    def __str__(self):
        total = ""
        if self.__height == 0 or self.__width == 0:
            return total
        for i in range(self.__height):
            total += (str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                total += "\n"
        return total

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
