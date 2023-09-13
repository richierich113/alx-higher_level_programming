#!/usr/bin/python3
"""module has a function that appends
a string at the end of a text file
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF8 text file
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)


if __name__ == "__main__":
    nb_characters_added = append_write("file_append.txt", "School is cool!\n")
    print(nb_characters_added)
