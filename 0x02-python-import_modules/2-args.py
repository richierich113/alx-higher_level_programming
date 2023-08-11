#!/usr/bin/python3
# a program that prints the number of and the list of its arguments.
import sys

if __name__ == "__main__":

    arg_length = len(sys.argv) - 1
    arg_list = sys.argv[1:]

    if arg_length == 0:
        print("0 arguments.")
    elif arg_length == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print(f"{arg_length} arguments:")

        for i in arg_list:
            index = sys.argv.index(i)
            print("{:d}: {}".format(index, sys.argv[i]))
