#!/usr/bin/python3

"""Module with function which adds 2 integers up
"""


def add_integer(a, b=98):
    """Returns an integer: the addition of a and b
    Args:
        a: first argument
        b: second argument
    Returns:
        int: the addition of a and b
    Raises:
        TypeError: If either or both a or b are not integers or a floats
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))


if __name__ == "__main__":
    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)
