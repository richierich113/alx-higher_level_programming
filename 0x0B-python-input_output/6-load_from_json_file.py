#!/usr/bin/python3
"""module has a function for loading data from .json files
"""
import json


def load_from_json_file(filename):
    """a function that creates an Object from a JSON file
    """
    with open(filename, encoding='utf-8') as myFile:
        return (json.loads(myFile.read()))
