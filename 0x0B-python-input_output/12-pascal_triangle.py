#!/usr/bin/python3
"""Defines a Pascal's triangle function"""


def pascal_triangle(n):
    """Represents a Pascal's triangle of size n"""

    if (n <= 0):
        return []
    elif (n == 1):
        return [1]
    elif (n == 2):
        return [[1], [1, 1]]

    triangle = [[1], [1, 1]]

    for i in range(1, n - 1):
        the_list = []
        the_list.append(1)
        for y in range(1, len(triangle)):
            the_list.append(triangle[i][y - 1] + triangle[i][y])
        the_list.append(1)
        triangle.append(the_list)

    return triangle
