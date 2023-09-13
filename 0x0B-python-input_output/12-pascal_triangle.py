#!/usr/bin/python3
"""Defines a Pascal's triangle function"""


def pascal_triangle(n):
    """Represents a Pascal's triangle of size n"""

    triangle = []
    for position in range(1, n + 1):
        triangle.append([1] * position)
    for y in range(2, n):
        row = triangle[y]
        prev_row = triangle[y]
        for x in range(1, len(row) - 1):
            row[x] = prev_row[x - 1] + prev_row[x]
    return triangle
