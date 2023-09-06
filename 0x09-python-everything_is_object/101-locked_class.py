#!/usr/bin/python3
"""LockedClass that prevents dynamic attributes creation"""


class LockedClass:

    __slots__ = "first_name"

    def __init__(self):
        pass
