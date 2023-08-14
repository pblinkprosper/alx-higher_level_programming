#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        length = len(item)
        if length == 0:
            print()
        for i in range(l):
            print("{:d}".format(item[i]), end="\n" if i == length - 1 else " ")
