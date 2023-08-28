#!/usr/bin/python3

def safe_print_integer(value):
    try:
        int_value = int(value)
        print("{:d}".format(int_value))
        return True
    except ValueError as ve:
        print(f"Error: {ve}")
        return False
    except TypeError as te:
        print(f"Error: {te}")
        return False
    except OverflowError as oe:
        print(f"Error: {oe}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


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
