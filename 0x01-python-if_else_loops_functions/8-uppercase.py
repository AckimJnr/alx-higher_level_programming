#!/usr/bin/python3

def uppercase(str):
    if not str:
        print("\n")

    strlen = len(str)
    i = 0

    for char in str:
        if i == strlen - 1:
            endchar = "\n"
        else:
            endchar = ""
        if ord(char) >= 97 and ord(char) <= 122:
            print("{}".format(chr(ord(char) - 32)), end=endchar)
        else:
            print("{}".format(char), end=endchar)
        i += 1
