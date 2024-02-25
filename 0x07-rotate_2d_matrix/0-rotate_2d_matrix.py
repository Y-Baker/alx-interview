#!/usr/bin/python3
"""Rotate Matrix"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise."""
    n = len(matrix)
    new = [[0 for i in range(n)] for _ in range(n)]
    r = 0
    c = n - 1
    for row in matrix:
        for col in row:
            new[r][c] = col
            r += 1
            if r == n:
                c -= 1
                r = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] = new[r][c]

    return matrix
