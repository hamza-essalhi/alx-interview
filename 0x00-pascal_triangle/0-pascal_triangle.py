#!/usr/bin/python3
"""Pascal"""


def pascal_triangle(n):
    """function to generate Pascal's triangle"""
    if n <= 0:
        return []

    pascal_triangle = []

    for i in range(n):
        new_row = [0] * (i + 1)
        new_row[0] = 1
        new_row[len(new_row) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(new_row):
                a = pascal_triangle[i - 1][j]
                b = pascal_triangle[i - 1][j - 1]
                new_row[j] = a + b

        pascal_triangle.append(new_row)

    return pascal_triangle
