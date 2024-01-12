#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    representing the Pascal’s triangle of n
    """

    if (n <= 0):
        return []

    triangle = [[1]]

    for i in range(n - 1):
        row = [1]
        for j in range(i):
            row.append(triangle[i][j] + triangle[i][j+1])
        row.append(1)
        triangle.append(row)

    return triangle
