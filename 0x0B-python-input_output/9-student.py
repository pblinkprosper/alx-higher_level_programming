#!/usr/bin/python3
"""Program of a class Student that defines a student"""


class Student():
    """Class of a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the student"""
        return self.__dict__
