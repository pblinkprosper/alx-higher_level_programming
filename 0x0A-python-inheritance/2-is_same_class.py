#!/usr/bin/python3
"""This program validate if the obj is the same the other class"""


def is_same_class(obj, a_class):
    return issubclass(a_class, type(obj))
