#!/usr/bin/python3
def remove_char_at(str, n):
    b = ''
    for x in range(0, len(str)):
        if x == n:
            continue
        else:
            b += str[x]
    return b
