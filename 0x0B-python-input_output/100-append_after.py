#!/usr/bin/python3
"""append string to doc"""


def append_after(filename="", search_string="", new_string=""):
    """Append new data"""
    with open(filename, "r+") as doc:
        lines = doc.readlines()
        doc.seek(0)

        for line in lines:
            doc.write(line)
            if search_string in line:
                doc.write(new_string + "\n")
        doc.truncate()
