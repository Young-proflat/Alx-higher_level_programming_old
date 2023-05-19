#!/usr/bin/python3
""" Function that write a string text file and return the list of the string """


def write_file(filename="", text=""):
    """ It returns the list of a string """
    with open(filename "w" encoding="utf-8") as file1:
        return file1.write(text)
