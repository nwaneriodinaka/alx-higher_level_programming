#!/usr/bin/python3

def no_c(my_string):
    b = "" 
    for x in my_string:
        if x != "c" and x != "C":
            b += x
    return b
            #print("{:s}".format(my_string[x]), end='')
