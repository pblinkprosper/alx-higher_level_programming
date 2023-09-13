#!/usr/bin/python3
"""This program validate if the obj is the same the other class"""


def is_same_class(obj, a_class):
    """Check is object is exactly instance of class"""

    if type(obj) == a_class:
        return True
    return False
