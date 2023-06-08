#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    funs = [add, sub, mul, div]
    ops = ['+', '-', '*', '/']
    a = 10
    b = 5
    i = 0
    while (i < 5):
        print(a, ops[i], b, "=", funs[i](a, b))
        i += 1
