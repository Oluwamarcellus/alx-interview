#!/usr/bin/env python3
"""
Module containing the pascal's triangle fucntion
"""

def pascal_triangle(n):
    """
    function that returns a list of lists of integers representing
    the Pascal’s triangle of n:
    """

    if n <= 0:
        return []

    arr = []
    for i in range(n+1):
        C = 1
        sub_arr = []
        for j in range(1, i+1):
            sub_arr.append(C)
            C = C * (i - j) // j

        if sub_arr:
            arr.append(sub_arr)

    return arr
