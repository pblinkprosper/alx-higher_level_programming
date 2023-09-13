#!/usr/bin/python3
"""A function that defines a class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry definition"""

    def __init__(self):
        """Constructor"""
        pass

    def area(self):
        """Raise an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates for integers"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
