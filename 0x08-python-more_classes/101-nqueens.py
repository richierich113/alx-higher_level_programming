#!/usr/bin/python3

"""
module for calculation of n-queens problem
"""


class Solution_Board:
    """blueprint class for N queens puzzle
    """
    solutions = []

    def __init__(self, num):
        """instantiator for class for N queens puzzle
        """
        self.num = num

    @property
    def num(self):
        """getter for num which returns num
        """
        return self.__num

    @num.setter
    def num(self, value):
        """setter for num
        Raise:
            TypeError: if num is not an int
        """
        if not isinstance(value, int):
            raise TypeError("num should be an int")
        self.__num = value

def get_n_queens(chess_board, column, num):
    if column >= num:
        Solution_Board.solutions.append(chess_board[:])
        return
    for i in range(0, num):
        if board_safe(chess_board, i, column, num):
            chess_board[i][column] = 1
            get_n_queens(chess_board, column + 1, num)
            chess_board[i][column] = 0

def board_safe(chess_board, row, column, num):
    for i in range(column):
        if chess_board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if chess_board[i][j] == 1:
            return False
    for i, j in zip(range(row, num, 1), range(column, -1, -1)):
        if chess_board[i][j] == 1:
            return False
    return True


if __name__ == "__main__":
    import sys

    args = sys.argv

    if len(args) != 2:
        print("Usage: {} N".format(args[0]))
        sys.exit(1)

    try:
        num = int(args[1])
        if num < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    chess_board = [[0 for _ in range(num)] for _ in range(num)]
    get_n_queens(chess_board, 0, num)

    for solution in Solution_Board.solutions:
        for row in solution:
            print(" ".join(map(str, row)))
        print()
