#!/usr/bin/python3

def no_c(my_string):
    for x in my_string:
        if x != "c" and x != "C":
            print("{}".format(x), end='')
