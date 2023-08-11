#!/usr/bin/python3
# a program that prints the number of and the list of its arguments.
import sys

if __name__ == "__main__":

    arg_length = len(sys.argv) - 1
    arg_list = sys.argv[1:]

    if arg_length == 0:
        print("0 arguments.".format(arg_length))
    else:
        print(f"{arg_length} arguments:")

        for index, arg_val in enumerate(arg_list, start=1):
            print(f"{index}: {arg_val}")
