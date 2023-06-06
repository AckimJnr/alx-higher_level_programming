#!/usr/bin/python3
def print_last_digit(number):

    if number < 0:
        last_digit = -int(str(abs(number))[-1])
    else:
        last_digit = int(str(number)[-1])

    print(last_digit)
