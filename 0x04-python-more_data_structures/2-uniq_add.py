#!/usr/bin/python3

def uniq_add(my_list=[]):
    if len(my_list) == 0:
        return 0

    new_list = [my_list[0]]
    for num in my_list[1:]:
        if num != new_list[-1]:
            new_list.append(num)

    add = sum(new_list)
    return add


if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result:", result)
