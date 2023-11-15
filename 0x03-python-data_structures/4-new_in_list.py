#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_l = my_list[:]
    if 0 <= idx < len(new_l):
        new_l[idx] = element

    return new_l
