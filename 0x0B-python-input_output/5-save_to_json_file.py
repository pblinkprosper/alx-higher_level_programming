#!/usr/bin/python3
"""Function that writes in to a file in JSON format"""


import json


def save_to_json_file(my_obj, filename):
    """Saves a file in JSON format, if file don't exist, creates it"""

    with open(filename, mode="w", encoding="utf-8") as _f:
        _f.write(json.dumps(my_obj))
