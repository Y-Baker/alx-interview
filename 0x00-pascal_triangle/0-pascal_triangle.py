#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
        Returns a list of lists of integers representing the Pascal’s
        triangle of n
    """
    if n <= 0:
        return []
    re = [[1]]
    for i in range(n - 1):
        li = [1]
        for j in range(i):
            li.append(re[i][j]+re[i][j+1])
        li.append(1)
        re.append(li)
    return re
