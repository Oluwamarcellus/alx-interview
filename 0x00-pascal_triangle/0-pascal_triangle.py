#! /bin/python3

def pascal_triangle(n):
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
