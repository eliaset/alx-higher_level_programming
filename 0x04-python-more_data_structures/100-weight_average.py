#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    den = 0
    if not my_list:
        return 0
    for i in my_list:
        sum += i[0] * i[1]
        den += i[1]
    return sum/den
