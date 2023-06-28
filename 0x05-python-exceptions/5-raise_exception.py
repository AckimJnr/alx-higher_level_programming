#!/usr/bin/python3

def raise_exception():
    num = 6

    try:
        num += "z"
    except TypeError:
        raise
