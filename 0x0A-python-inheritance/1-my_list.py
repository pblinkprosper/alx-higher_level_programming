#!/usr/bin/python3
"""Program creates a class called MyList that inherits of the class List"""


class MyList(list):
    """This class inherits from MyList class"""

    def print_sorted(self):
        print(sorted(self))
