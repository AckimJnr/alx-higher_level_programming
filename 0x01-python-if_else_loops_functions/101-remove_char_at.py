#!/usr/bin/python3

def remove_char_at(str, n):
    strlen = len(str)
    if n < 0 or n >= strlen:
        return str
    new_str = ""

    for i in range(strlen):
        if i != n:
            new_str += str[i]
    return new_str
