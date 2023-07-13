#!/usr/bin/python3
"""Adds all arguments of to a python list"""
import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


if "__name__"=="__main__":
    try:
        old_data = load_from_json_file('add_item.json')
    except FileNotFoundError:
        old_data = []
    
    new_data = old_data + sys.argv[1:]
    save_to_json_file(new_data, 'add_item.json')
