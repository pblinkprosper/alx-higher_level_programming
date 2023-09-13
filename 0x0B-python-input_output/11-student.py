#!/usr/bin/python3
"""Program of a class Student that defines a student"""


class Student():
    """Class of a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the student"""
        element = {}

        if attrs is None:
            return self.__dict__

        for attr in attrs:
            value = self.__dict__.get(attr)
            if value is not None:
                element[attr] = value
        return element

    def reload_from_json(self, json):
        """Update all public instance attributes"""
        self.__dict__.update(json)
