#!/usr/bin/python3
"""Function that converts JSON to a dictionary"""


import json


def from_json_string(my_str):
    """Returns Python object represented by JSON string"""

    return json.loads(my_str)
