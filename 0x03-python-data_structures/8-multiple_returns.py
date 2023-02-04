#!/usr/bin/python3
def multiple_returns(sentence):
    output = (len(sentence),sentence[0] if len(sentence) > 0 else None)
    return output
