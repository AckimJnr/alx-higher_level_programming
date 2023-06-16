#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    multiplied_nums = {}

    for key, value in a_dictionary.items():
        multiplied_nums[key] = value * 2

    return multiplied_nums
