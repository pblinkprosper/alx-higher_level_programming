#!/usr/bin/python3
"""Function that converts a dictionary to JSON"""


import json


def to_json_string(my_obj):
    """Convert a dictionary to JSON format"""

    return (json.dumps(my_obj))
