#!/usr/bin/python3
"""
This module contains a function text_indentation(text)
"""


def text_indentation(text):
    '''prints a text with 2 new lines after each ".", "?", or ":"
    Args:
        text (str): The string to be printed
    Raises:
        TypeError: If text is not a string
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    empt_string = ""
    characters = ['.', '?', ':']

    for ch in text:
        empt_string += ch
        if ch in characters:
            empt_string += "\n\n"

    print(empt_string, end='')


if __name__ == "__main__":
    text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing \
                     elit. Quonam modo? Utrum igitur tibi litteram videor an \
                     totas paginas commovere? Non autem hoc: igitur ne illud \
                     quidem. Fortasse id optimum, sed ubi illud: Plus semper \
                     voluptatis? Teneo, inquit, finem illi videri nihil \
                     dolere. Transfer idem ad modestiam vel temperantiam, \
                     quae est moderatio cupiditatum rationi oboediens. \
                     Si id dicis, vicimus. Inde sermone vario sex illa a \
                     Dipylo stadia confecimus. Sin aliud quid voles, postea. \
                     Quae animi affectio suum cuique tribuens atque hanc, \
                     quam dico. Utinam quidem dicerent alium alio beatiorem! \
                     Iam ruinas videres""")
