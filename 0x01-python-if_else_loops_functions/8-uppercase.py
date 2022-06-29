#!/usr/bin/python3
def uppercase(str):
    for x in str:
        x = ord(x)
        if x in range(97, 123):
            x -= 32
        print("{}" .format(chr(x)), end ='')
    print()
