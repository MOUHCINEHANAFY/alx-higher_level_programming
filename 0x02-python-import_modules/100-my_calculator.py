#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    fct = argv[2]

    opertation = {
            "+": add(a, b),
            "-": sub(a, b),
            "*": mul(a, b),
            "/": div(a, b)}

    if fct in opertation.keys():
        print("{:d} {} {:d} = {:d}".format(a, fct, b, opertation[fct]))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
