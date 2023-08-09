#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = list()
    frm_to = len(str) 
    for letter in range(frm_to):
        if letter == n:
            continue
        else:
            str_copy.append(str[letter])
    return "".join(str_copy)
