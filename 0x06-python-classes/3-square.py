#!/usr/bin/python3
"""Define the area of a square"""


class Square:
    """Square class with size and proper validation"""

    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate the area of the square"""
        return (self.__size * self.__size)
