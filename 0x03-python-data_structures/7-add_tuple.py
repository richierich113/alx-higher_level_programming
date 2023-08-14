#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    if len(tuple_a) == len(tuple_b) == 2:
        for i in range(2):
            num = tuple_a[i] + tuple_b[i]
            new_tuple = new_tuple + (num,)
        return new_tuple
    elif len(tuple_a) == 2 and len(tuple_b) == 1:
        temp_tuple_b = tuple_b + (0,)
        for i in range(2):
            num = tuple_a[i] + temp_tuple_b[i]
            new_tuple = new_tuple + (num,)
        return new_tuple

    elif len(tuple_a) == 2 and len(tuple_b) == 0:
        temp_tuple_b = tuple_b + (0, 0)
        for i in range(2):
            num = tuple_a[i] + temp_tuple_b[i]
            new_tuple = new_tuple + (num,)
        return new_tuple


# for testing function
if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))
