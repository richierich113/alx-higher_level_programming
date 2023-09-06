#!/usr/bin/python3
def magic_string():
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return "BestSchool" * magic_string.count + (", " * (magic_string.count - 1))


if __name__ == "__main__":
    for i in range(10):
        print(magic_string())
