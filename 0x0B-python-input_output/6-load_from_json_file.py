#!/usr/bin/python3
"""Create object from json"""
import json


def load_from_json_file(filename):
    """from json file ofcoz"""
    with open(filename, 'r', encoding="UTF-8") as doc:
        return json.load(doc)
