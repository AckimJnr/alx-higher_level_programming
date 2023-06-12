#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None or len(matrix) == 0:
        return
    num_rows = len(matrix)
    num_cols = len(matrix[0] if len(matrix) > 0 else 0)

    if any(len(row) != num_cols for row in matrix):
        return

    for row in matrix:
        for i, item in enumerate(row):
            if i == len(row) - 1:
                print("{:d}".format(item), end='')
            else:
                print("{:d}".format(item), end=' ')
        print()
