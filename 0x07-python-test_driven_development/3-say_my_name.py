#!/usr/bin/python3
"""Print full-name"""


def say_my_name(first_name, last_name=""):
    """This function prints a full-name"""

    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
