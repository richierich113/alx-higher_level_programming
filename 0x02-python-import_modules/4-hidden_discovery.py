#!/usr/bin/python3
# program that prints all names defined by the compiled module hidden_4.pyc
# that do not start with "__" in alpha order
import hidden_4

if __name__ == "__main__":
    # create empty list to append name to
    final_names = []
    # get the list od names in hidden_4 module and retrieve names as needed
    module_names = dir(hidden_4)
    for name in module_names:
        if name[:2] == "__":
            continue
        final_names.append(name)
    # arrange final names in alpha order in a sorted list and print them
    sorted_names = sorted(final_names)
    for final_name in sorted_names:
        print(final_name)
