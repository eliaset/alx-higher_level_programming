#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    add = []
    if len(tuple_a) == 0:
        tuple_a += (0, 0)
    elif len(tuple_a) == 1:
        tuple_a += (0,)
    elif len(tuple_a) > 2:
        tuple_a = tuple_a[:2]

    if len(tuple_b) == 0:
        tuple_b += (0, 0)
    elif len(tuple_b) == 1:
        tuple_b += (0,)
    elif len(tuple_b) > 2:
        tuple_b = tuple_b[:2]

    for i in range(2):
        add.append(tuple_a[i] + tuple_b[i])
    return tuple(add)
