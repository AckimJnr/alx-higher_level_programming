#!/usr/bin/python3

for num in range(9):
    for nextnum in range(num + 1, 10):
        if num != 8 or nextnum != 9:
            endchar = ", "
        else:
            endchar = "\n"
        print("{:d}{:d}".format(num, nextnum), end=endchar)
