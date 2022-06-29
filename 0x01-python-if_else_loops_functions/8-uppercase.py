#!/usr/bin/python3
def uppercase(str):
    for x in str:
        x = ord(x)
        if x in range(97, 123):
            print("{}" .format(chr(x - 32)))
        else:
            print("{}" .format(chr(x)), end ='')
