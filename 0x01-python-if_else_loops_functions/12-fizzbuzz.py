#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if (x % 3 == 0 and x % 5 == 0):
            print("{}" .format('fizzbuzz '), end='')
        elif (x % 3 == 0):
            print("{}" .format('fizz '), end='')
        elif (x % 5 == 0):
            print("{}" .format('buzz '), end='')
        else:
            print("{}" "{}" .format(x, ' '), end='')
