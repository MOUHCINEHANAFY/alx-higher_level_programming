#!/usr/bin/python3

def uppercase(str):
    for alpha in str:
        if ord(alpha) in range(97, 123):
            s = ord(alpha) - 32
        else:
            s = ord(alpha)
        print("{:c}".format(s), end='')
    print("")
