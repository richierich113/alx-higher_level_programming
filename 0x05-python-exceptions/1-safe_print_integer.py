#!/usr/bin/python3

def safe_print_integer(value):
    try:
        int_value = int(value)
        print("{:d}".format(int_value))
        return 0
    except ValueError as ve:
        return 1
    except Exception as e:
        return 1


if __name__ == "__main__":
    value = 89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "School"
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
