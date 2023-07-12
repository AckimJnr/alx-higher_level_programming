#!/usr/bin/python3
"""Write an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Using Json"""
    with open(filename, 'w', encoding="utf-8") as doc:
        doc.write(json.dumps(my_obj))
