#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if not i:
            print()
            continue
        print("{:d}".format(i[0]), end="")
        for j in i[1:]:
            print(" {:d}".format(j), end="")
        print("")
