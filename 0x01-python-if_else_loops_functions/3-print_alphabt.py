#!/usr/bin/python3

i = 97
while (i < 123):
    if i == ord('q') or i == ord('e'):
        i += 1
        continue
    print("{}".format(chr(i)), end="")
    i += 1
