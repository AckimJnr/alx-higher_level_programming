#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_num = 0
    total_weight = 0

    for num, weight in my_list:
        total_num += num * weight
        total_weight += weight

    avg = total_num / total_weight

    return avg
