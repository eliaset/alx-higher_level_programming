#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)

    if (length == 0):
        my_t = (length, None)
    else:
        my_t = ( length, sentence[0])
    return (my_t)
