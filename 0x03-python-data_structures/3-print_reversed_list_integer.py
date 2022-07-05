#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        n = len(my_list)
        for x in range(n,):
            i = my_list.pop()
            print("{:d}".format(i))
