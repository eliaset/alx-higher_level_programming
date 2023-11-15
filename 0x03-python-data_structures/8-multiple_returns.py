#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)

    if l == 0:
        my_t = (l, None)
    else:
        my_t =  (l, sentence[0])

    return (my_t)
