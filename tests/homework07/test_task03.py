from typing import List

import pytest

from homework07.task03 import tic_tac_toe_checker

boards = [
    [["x", "o", "-"], ["o", "x", "-"], ["-", "x", "x"]],
    [["o", "x", "-"], ["x", "o", "-"], ["-", "o", "o"]],
    [["x", "o", "o"], ["o", "x", "x"], ["x", "x", "o"]],
    [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]],
]

outcomes = ["x wins!", "o wins!", "draw!", "unfinished!"]


@pytest.mark.parametrize(("board", "outcome"), zip(boards, outcomes))
def test_tic_tac_toe_checker(board: List[List], outcome: str):
    """Tests the `tic_tac_toe_checker` function.

    Arguments:
        board (List[List]): Tic-Tac-Toe 3x3 board
        outcome (str): Result of a Tic-Tac-Toe game
    """
    assert tic_tac_toe_checker(board) == outcome
