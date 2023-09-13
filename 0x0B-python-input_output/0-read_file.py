#!/usr/bin/python3
"""module has a function tha t reads a text file"""


def read_file(filename=""):
    """Prints the contents of a UTF8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")


if __name__ == "__main__":
    read_file("my_file_0.txt")
