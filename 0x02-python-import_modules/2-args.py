#!/usr/bin/python3

def prefix(argc):
    if argc == 0:
        return ("s.")
    elif argc == 1:
        return (":")
    elif argc > 1:
        return ("s:")


if __name__ == "__main__":
    import sys

    argc = len(sys.argv[1:])
    argprefix = prefix(argc)

    print("{} argument{}".format(argc, argprefix))

    for i in range(1, argc + 1):
        print("{}: {}".format(i, sys.argv[i]))
