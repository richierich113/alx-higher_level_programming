#!/usr/bin/python3

def element_at(my_list, idx):
    if idx >= 0:
        if idx > (len(my_list) - 1):
            return None
        query = my_list[idx]
        return query
    else:
        return None
