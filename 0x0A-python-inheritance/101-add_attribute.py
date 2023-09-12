#!/usr/bin/python3
"""module with a function that adds attributes to objects"""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if possible
    Raises
        TypeError: if you can't add a new attribute
    """
    builtins = (str, int, complex, bool, float, list,
                tuple, dict, set, frozenset, type, object)
    for _type in builtins:
        if type(obj) is _type:
            raise TypeError("can't add new attribute")

    object.__setattr__(obj, name, value)


if __name__ == "__main__":
    class MyClass():
        pass

    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
