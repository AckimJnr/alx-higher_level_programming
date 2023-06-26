#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError:
        print("{} is not an interger".format(value))
        return False
