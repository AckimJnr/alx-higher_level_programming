#!/usr/bin/python3

for number in range(00, 100):
    if number == 99:
        endchar = "\n"
    else:
        endchar = ", "
    print("{:02}".format(number), end=endchar)
