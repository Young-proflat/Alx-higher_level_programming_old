#!/usr/bin/python3
"""Function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """ It create an object from JSON file"""
    with open(filename, 'r') as file1:
        return json.load(file1)
