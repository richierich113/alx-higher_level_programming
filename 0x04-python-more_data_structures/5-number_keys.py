#!/usr/bin/python3

def number_keys(a_dictionary):
    keys_obj = a_dictionary.keys()
    keys_list = list(keys_obj)
    num_of_keys = len(keys_list)
    return num_of_keys


if __name__ == "__main__":
    a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
    nb_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(nb_keys))
