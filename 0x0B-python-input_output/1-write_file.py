#!/usr/bin/python3
""" Write a string to a text file(UTF8) """


def write_file(filename="", text=""):
    """ It returns the list of a string """
    with open(filename, "w", encoding="utf-8") as file1:
        return file1.write(text)
