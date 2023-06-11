#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if not my_list:
        print("".format(), end='')
    list_copy = my_list.copy()
    list_copy.reverse()

    for num in list_copy:
        print("{:d}".format(num))
