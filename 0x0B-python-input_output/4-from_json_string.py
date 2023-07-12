#!/usr/bin/python3
import json
"""Json module"""


def from_json_string(my_str):
    """Returns json formated object from string"""
    return json.loads(my_str)
