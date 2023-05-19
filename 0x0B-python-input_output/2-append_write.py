#!/usr/bin/python3
""" Appending a string to a text file """



def append_write(filename="", text=""):
    """ Append a string to a text file 
    """ 
    with open(filename, "a", encoding="utf-8") as file1:
        return file1.write(text)
