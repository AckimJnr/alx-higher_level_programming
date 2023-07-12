#!/usr/bin/python3
"""Append data to a file"""


def append_write(filename="", text=""):
    """Returns number of characters added"""
    num_chars = 0

    with open(filename, 'a', encoding='utf-8') as doc:
        return doc.write(text)
