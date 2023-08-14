#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    result = []

    # Populate list_a and list_b with elements from tuple_a and tuple_b
    list_a = list(tuple_a) + [0, 0][:max(0, 2 - len(tuple_a))]
    list_b = list(tuple_b) + [0, 0][:max(0, 2 - len(tuple_b))]

    # Perform element-wise addition
    for i in range(2):
        result.append(list_a[i] + list_b[i])

    return tuple(result)


# for testing function
if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))
