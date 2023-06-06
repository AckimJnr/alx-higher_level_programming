#!/usr/bin/python3

i, j = 122, 1
while (i > 96):
    if j % 2 == 0:
        char = i - 32
    else:
        char = i

    print("{}".format(chr(char)), end="")
    i -= 1
    j += 1
