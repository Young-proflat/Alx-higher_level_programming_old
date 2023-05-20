#!/usr/bin/python3
""" A function that returuns a dictionary description of a data"""


def class_to_json(obj):
    """ returens a dictionary description with simple data structure"""
    return obj.__dict__
