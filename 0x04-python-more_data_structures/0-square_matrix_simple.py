#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = [(list(map((lambda x : x**2), i))) for i in matrix]
    return square
