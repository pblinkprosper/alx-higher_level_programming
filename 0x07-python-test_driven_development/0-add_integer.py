#!/usr/bin/python3
"""Addition of integers"""


def add_integer(a, b=98):
    """Add two integers"""

    if isinstance(a, (int, float)) is False:
        raise TypeError('a must be an integer')
    if isinstance(b, (int, float)) is False:
            raise TypeError('b must be an integer')
    return int(a) + int(b)
