#!/usr/bin/python3
def no_c(my_string):
    list_string = list(my_string)
    c = 0
    for i in list_string:
        if i == 'c' or i == 'C':
            list_string[c] = ""
        c += 1

    return "".join(list_string)
