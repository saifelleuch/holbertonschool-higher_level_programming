#!/usr/bin/python3
""" playing with class Square """


class Square:
    """ define Square size """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise TypeError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        return (self.__size ** 2)
