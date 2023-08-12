#!/usr/bin/python3
# a program that imports all functions from the file `calculator_1.py`
# and handles basic operations.
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":

    arg_length = len(sys.argv) - 1
    arg_vals = sys.argv[1:4]

    if arg_length < 3 or arg_length > 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif arg_length == 3:
        a = int(arg_vals[0])
        b = int(arg_vals[2])
        if arg_vals[1] == "+":
            results = add(a, b)
            print(f"{a} + {b} = {results}")
            sys.exit(0)
        elif arg_vals[1] == "-":
            results = sub(a, b)
            print(f"{a} - {b} = {results}")
            sys.exit(0)
        elif arg_vals[1] == "*":
            results = mul(a, b)
            print(f"{a} * {b} = {results}")
            sys.exit(0)
        elif arg_vals[1] == "/":
            results = div(a, b)
            print(f"{a} / {b} = {results}")
            sys.exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
