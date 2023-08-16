#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Retrieve keys from the dictionary
    keys_obj = a_dictionary.keys()

    # Convert keys view object to a list and sort it
    keys_list = list(keys_obj)
    arranged_keylist = sorted(keys_list)

    # Iterate through sorted keys and print key-value pairs
    for key in arranged_keylist:
        value = a_dictionary[key]
        print(f"{key}: {value}")


if __name__ == "__main__":
    a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level",
                   'ids': [1, 2, 3]}
                       print_sorted_dictionary(a_dictionary)
