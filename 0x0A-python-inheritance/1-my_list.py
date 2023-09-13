#!/usr/bin/python3
"""Program creates class called MyList that inherits the class List"""


class MyList(list):
    """This class inherits from MyList class"""

    def print_sorted(self):
        print(sorted(self))
