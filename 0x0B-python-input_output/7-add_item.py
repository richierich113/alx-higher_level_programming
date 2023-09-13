#!/usr/bin/python3
"""adds all arguments to a Python list, and then save
them to a file
"""
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


def main():
    """main function
    """
    try:
        new_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        new_list = []

    new_list.extend([sys.argv[i] for i in range(0, len(sys.argv)) if i != 0])
    try:
        save_to_json_file(new_list, 'add_item.json')
    except Exception as e:
        pass


main()
