#!/usr/bin/python3
def multiple_returns(sentence):
    my_t = ()
    l = len(sentence)
    if l == 0:
        my_t = 0, None
    else:
        my_t =  l, sentence[0]
    return my_t
