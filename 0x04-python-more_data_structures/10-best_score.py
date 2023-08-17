#!/usr/bin/python3

# a function that returns a key with the biggest integer value.
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)

    highest_value = max(a_dictionary.values(), default=None)
    for key, value in a_dictionary.items():
        if value == highest_value:
            return (key)
