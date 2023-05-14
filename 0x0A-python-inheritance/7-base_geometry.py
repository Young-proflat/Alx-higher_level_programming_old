#!/usr/bin/python3
""" A class on BaseGeometry the accept an Area """

class BaseGeometry:
    """
    Creating a class of Geometry 
    """

    def area(self):
        """
        area method
    
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ 
        creating a public instance integer_validator 
    
        """
        if type(value) is not (int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
