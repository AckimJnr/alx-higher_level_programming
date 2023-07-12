#!/usr/bin/python3
"""Reads text from a file and print to stdout"""


def read_file(filename=""):
    """Open with 'with' to automatically handle file closing"""
    with open(filename, "r", encoding="utf-8") as doc:
        for line in doc:
            print(line, end="")
