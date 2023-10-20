"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""


from typing import List


def is_winner(line: List) -> bool:
    """Returns `True` if all elements in the list are equal, `False` otherwise.

    Arguments:
        line (List): list elements

    Returns:
        bool: `True` if all elements in the list are equal, `False` otherwise
    """
    return len(set(line)) == 1


def tic_tac_toe_checker(board: List[List]) -> str:
    """Returns the result of a Tic-Tac-Toe game.

    Arguments:
        board (List[List]): Tic-Tac-Toe 3x3 board

    Returns:
        str: `x wins!`, if there is `x` winner,
            `o wins!`, if there is `o` winner,
            `draw!`, if there is a draw,
            `unfinished!`, if board is unfinished
    """
    for i, xline in enumerate(board):
        yline = [line[i] for line in board]
        if any(map(is_winner, (xline, yline))):
            return "{} wins!".format(xline[i])

    xdiag = [line[i] for i, line in enumerate(board)]
    ydiag = [line[i] for i, line in enumerate(reversed(board))]

    if any(map(is_winner, (xdiag, ydiag))):
        return "{} wins!".format(xdiag[1])

    if any("-" in line for line in board):
        return "unfinished!"

    return "draw!"
