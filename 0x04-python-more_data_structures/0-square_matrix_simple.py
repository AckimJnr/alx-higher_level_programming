#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0])

    new_matrix = [[0] * cols for _ in range(rows)]

    for r_item in range(rows):
        for c_item in range(cols):
            new_matrix[r_item][c_item] = matrix[r_item][c_item] ** 2
    return new_matrix
