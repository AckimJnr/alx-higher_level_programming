#!/usr/bin/python3
"""Writes data to a file"""


def write_file(filename="", text=""):
    """Returns the number of bytes written"""
    bytes_written = 0
    with open(filename, 'w', encoding="utf-8") as doc:
        bytes_written = doc.write(text)
    return bytes_written
