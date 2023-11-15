#!/usr/bin/python3
def multiple_returns(sentence):
    my_t = ()
    length = len(sentence)
    if length == 0:
        my_t = 0, None
    else:
        my_t =  length, sentence[0]
    return my_t
