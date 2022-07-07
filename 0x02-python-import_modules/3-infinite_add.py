#!/usr/bin/python3
if __name__ == "__main__":
    def add(*b):
        total = 0
        for x in b:
            total = total + x
    print("{}".format(add(*b)))
