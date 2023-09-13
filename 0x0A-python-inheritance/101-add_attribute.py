#!/usr/bin/python3
"""Program that tries to add attributes to classes if possible"""


def add_attribute(obj, key, value):
    """Function tries to add attribute or raise error"""

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, key, value)
