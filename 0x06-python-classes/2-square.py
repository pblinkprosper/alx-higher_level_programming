#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """Instantiation of private instance size
    with optional"""

    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be a integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
