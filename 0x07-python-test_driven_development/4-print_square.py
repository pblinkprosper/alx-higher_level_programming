#!/usr/bin/python3
"""Prints a square"""


def print_square(size):
    """Function that prints a square"""

    if isinstance(size, int) is False:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for item in range(0, size):
        print('#' * size)
