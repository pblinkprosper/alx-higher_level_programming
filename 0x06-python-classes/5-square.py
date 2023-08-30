#!/usr/bin/python3
"""Print a square using Square class"""


class Square:
    """Class with size and proper validation"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if not self.__size:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
