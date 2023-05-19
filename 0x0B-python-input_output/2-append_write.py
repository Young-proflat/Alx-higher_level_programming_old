#!/usr/bin/python3
""" Appending a string to a text file """



def append_write(filename="", text=""):
    """ Append a string to a text file """ 
    with open(filename, "a") as file1:
        return file1.write(text)
