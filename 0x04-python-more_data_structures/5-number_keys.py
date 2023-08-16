#!/usr/bin/python3

def number_keys(a_dictionary):
    i = 0
    for item_dict in a_dictionary:
        i += 1
    return i


if __name__ == "__main__":
    a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
    nb_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(nb_keys))
