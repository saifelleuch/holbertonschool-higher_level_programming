#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in range(1, len(i)):
            print("{:d}".format(j), "", end="")
        print(i[len(i) - 1])
