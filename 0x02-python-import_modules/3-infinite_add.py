#!/usr/bin/python3
# a program that prints the result of the addition of all arguments
from sys import argv

if __name__ == "__main__":

    arg_length = len(argv) - 1
    arg_list = argv[1:]
    add_total = 0

    # if no arg
    if arg_length == 0:
        print(add_total)
    # if one arg
    elif arg_length == 1:
        total = add_total + int(argv[1])
        print("{}".format(total))
    # if multiple args
    else:
        for i in arg_list:
            add_total += int(i)
            print(f"{add_total:d}")
        
