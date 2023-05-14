#!/usr/bin/python3
""" return True if the object is an instance of a class """


def inherits_from(obj, a_class):

    if isinstance (obj , a_class) and type(obj) != a_class:
        return True

    else:
        return False
