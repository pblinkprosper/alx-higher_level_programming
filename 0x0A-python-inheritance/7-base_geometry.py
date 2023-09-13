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
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
