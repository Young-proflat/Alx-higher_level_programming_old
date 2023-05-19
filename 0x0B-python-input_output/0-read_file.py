#!/usr/bin/python3
""" This function reads a text file (UTF8) and print out """

def read_file(filename=""):
    """ using a function that reads (UTF8) """
    with open (filename, encoding= "utf-8") as file1:
        print(file1.read(), end="")
