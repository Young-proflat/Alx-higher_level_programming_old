#!/usr/bin/python3
""" writing a class"""


class Student:
    """Definng a class"""
    def __init__(self, first_name, last_name, age):
        """ initializing a class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ to convert to json"""
        return self.__dict__
