#!/usr/bin/python3
from sys import argv, exit
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    if len(argv) == 4:
        functions = [('+', add), ('-', sub), ('*', mul), ('/', div)]
        for func in functions:
            if argv[2] == func[0]:
                a = int(argv[1])
                b = int(argv[3])
                print('{:d} {:s} {:d}'.format(
                    a, func[0], b, func[1](a, b)))
                exit()
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    else:
        print('Usage: {:s} <a> <operator> <b>'.format(argv[0]))
        exit(1)
