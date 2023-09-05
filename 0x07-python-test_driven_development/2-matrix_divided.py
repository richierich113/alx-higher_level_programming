#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix.
    Args:
        matrix: a list of lists of integers or floats
        div: a number (integer or float)
    Raises:
        TypeError: If the matrix contains rows of different sizes
         TypeError: If the matrix contains non-numbers
        TypeError: If div is not a number
        ZeroDivisionError: If div is 0
    Returns:
        matrix: resulting matrix after division
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(m_row, list) for m_row in matrix) or
            not all((isinstance(elem, int) or isinstance(elem, float))
                    for elem in [num for m_row in matrix for num in m_row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(m_row) == len(matrix[0]) for m_row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), m_row)) for m_row in matrix])


if __name__ == "__main__":
    matrix = [
    [1, 2, 3],
    [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)
