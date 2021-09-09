#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    i = 1
    count = len(argv) - 1

    if len(argv) < 2:
        print("0 arguments.")
    elif len(argv) < 3:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(count))

    for j in argv[i:]:
        print("{:d}: {:s}".format(i, j))
        i += 1
