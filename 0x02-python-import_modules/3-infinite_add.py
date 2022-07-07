#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = 0
    y = len(argv) 
    for x in range(1, y):
        z = int(argv[x])
        total += z
    print("{}".format(total))
