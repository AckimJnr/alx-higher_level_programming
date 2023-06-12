#!/usr/bin/python3

def multiple_returns(sentence):
    str_len = len(sentence)

    if str_len == 0:
        data = str_len, None
    else:
        data = str_len, sentence[0]
    return data
