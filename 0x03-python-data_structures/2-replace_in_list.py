#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx >= 0:
        if idx > (len(my_list) - 1):
            return my_list

        copy_list = my_list.copy()
        copy_list[idx] = element
        return copy_list
    else:
        return my_list
