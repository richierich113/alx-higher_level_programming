#!/usr/bin/python3
"""module with a function that adds attributes to objects"""


def add_attribute(obj, attrib, value):
    """Add a new attribute to an object if possible
    Raises
        TypeError: if you can't add a new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attrib, value)


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
