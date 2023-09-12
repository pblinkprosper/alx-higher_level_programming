#!/usr/bin/python3
"""Function that appends text to file and create file"""


def append_write(filename="", text=""):
    """Appends text to file's end and create if not exist"""

    with open(filename, mode="a", encoding="utf-8") as _file:
        _file.write(text)

    return (len(text))
