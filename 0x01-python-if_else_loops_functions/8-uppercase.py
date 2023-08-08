#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            cap = ord(c) - 32
        else:
            cap = ord(c)
        print("{:c}".format(cap), end='')
    print(end='\n')
