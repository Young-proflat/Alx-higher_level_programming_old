#!/usr/bin/python3
""" A class that inherits from BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeometry """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def are(self):
        """ area method """
        return  self.__width * self.__height

    def __str__(self):
        """__str__ method"""
        return (f'[Rectangle]({self.width} * {self.height}')
