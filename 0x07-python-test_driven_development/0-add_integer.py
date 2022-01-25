#!/usr/bin/python3
""" this is the add_integer module with function add_integer(). """


def add_integer(a, b=98):
    """ function to add two integer """
    if type(a) is not int or float:
        raise TypeError("a must be an integer")
    if type(b) is not int or float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    else:
        return (a + b)
