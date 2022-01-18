#!/usr/bin/python3
""" just playing with class Square"""


class Square:
    """ define class Square """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(value) is not tuple and len(value) != 2 or/
        type(value[0]) is not int and value[0] < 0 or/
        type(value[1]) is not int and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
