#!/usr/bin/python3
""" A class on BaseGeometry the accept an Area """

class BaseGeometry:
    """ Creating a class of Geometry """

    pass

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
        raise TypeError('<name> must be an integer')
    if value <= 0:
        raise TypeError('<name> must be greate than 0')
