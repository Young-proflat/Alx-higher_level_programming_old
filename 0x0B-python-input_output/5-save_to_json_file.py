#!/usr/bin/python3
""" Function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file, using a JSON representation"""
    with open (filename, "w") as file1:
        return file1.write(json.load(my_obj))
