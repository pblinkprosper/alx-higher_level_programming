#!/usr/bin/python3
"""This function returns the dictionary description with simple data"""


def class_to_json(obj):
    return obj.__dict__
