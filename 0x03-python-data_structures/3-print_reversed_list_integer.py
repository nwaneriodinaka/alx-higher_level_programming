#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    for x in range(n, 0, -1):
        print("{}".format(my_list[x-1]))
