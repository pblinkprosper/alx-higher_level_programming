#!/usr/bin/python3
"""A function that reads text file and prints to stdout"""


def read_file(filename=""):
    """Print content of the file"""

    with open(filename, encoding="utf-8") as _f:
        print(_f.read(), end="")
