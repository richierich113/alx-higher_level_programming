#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # retrieve keys from dictionary
    keys_obj = a_dictionary.keys()
    # cast it to a list and arrange them in alpha order using sorted func.
    keys_list = list(keys_obj)
    arranged_keylist = sorted(keys_list)

    for key in arranged_keylist:
        # for each key, get its value and print the key-value pair
        # on separate lines
        value = a_dictionary[key]
        print(f"{key}: {value}")


if __name__ == "__main__":
    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
    print_sorted_dictionary(a_dictionary)
