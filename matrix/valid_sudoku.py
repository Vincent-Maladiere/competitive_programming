# %%
import pytest
from copy import deepcopy


def is_sudoku_valid(board):

    for idx in range(9):
        seen = []
        for jdx in range(9):
            number = board[idx][jdx]
            if number != ".":
                if not number in seen:
                    seen.append(number)
                else:
                    return False
    
    for jdx in range(9):
        seen = []
        for idx in range(9):
            number = board[idx][jdx]
            print(idx, jdx, number, seen)
            if number != ".":
                if not number in seen:
                    seen.append(number)
                else:
                    return False
    
    for idx in range(3):
        for jdx in range(3):
            seen = []
            for i in range(idx*3, (idx+1)*3):
                for j in range(jdx*3, (jdx+1)*3):
                    number = board[i][j]
                    if number != ".":
                        if not number in seen:
                            seen.append(number)
                        else:
                            return False
    return True

board_1 = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


board_2 = deepcopy(board_1)
board_2[0][0] = "8"

board_3 = deepcopy(board_1)
board_3[0][2] = "6"

# %%

@pytest.mark.parametrize("board, expected", [
    (board_1, True),
    (board_2, False),
    (board_3, False),
])
def test_suite(board, expected):
    assert is_sudoku_valid(board) == expected


# %%

# %%
