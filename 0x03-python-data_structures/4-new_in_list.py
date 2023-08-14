#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copy_mylist = my_list.copy()
    if idx >= 0:
        if idx > (len(my_list) - 1):
            return copy_mylist

        copy_mylist[idx] = element
        return copy_mylist
    else:
        return copy_mylist
