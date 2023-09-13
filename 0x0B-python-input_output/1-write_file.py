#!/usr/bin/python3
"""module has a function that writes to a file"""


def write_file(filename="", text=""):
    """Writes to a UTF8 text file(UTF8)
    """
    with open(filename, "w", encoding="utf-8") as file:
        return (file.write(text))


if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool\n")
    print(nb_characters)
