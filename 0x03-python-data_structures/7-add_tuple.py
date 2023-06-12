#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tmp_a = tuple_a + (0, 0)
    tmp_b = tuple_b + (0, 0)

    sum_tuple = (tmp_a[0] + tmp_b[0], tmp_a[1] + tmp_b[1])

    return sum_tuple
