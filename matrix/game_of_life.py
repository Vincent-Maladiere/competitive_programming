"""
According to Wikipedia's article: "The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway
in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state:
live (represented by a 1) or dead (represented by a 0).

Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using
the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by
reproduction.

The next state is created by applying the above rules simultaneously to every cell
in the current state, where births and deaths occur simultaneously.

Given the current state of the m x n grid board, return the next state.
"""
# %%
import pytest


def game_of_life(board):

    m, n = len(board), len(board[0])
    neighbors = [[0] * n for _ in range(m)]

    convolution = []
    for idx in range(-1, 2):
        for jdx in range(-1, 2):
            if not (idx == 0 and jdx == 0):
                convolution.append([idx, jdx])

    for idx in range(m):
        for jdx in range(n):
            for idx_offset, jdx_offset in convolution: 
                idx_prime = idx + idx_offset
                if not (0 <= idx_prime <= m - 1):
                    continue
                jdx_prime = jdx + jdx_offset
                if not (0 <= jdx_prime <= n - 1):
                    continue
                
                neighbors[idx][jdx] += board[idx_prime][jdx_prime]

    for idx in range(m):
        for jdx in range(n):
            
            state = board[idx][jdx]
            n_neigh = neighbors[idx][jdx]

            if state and (n_neigh < 2 or n_neigh > 3):
                state = 0

            elif not state and n_neigh == 3:
                state = 1

            board[idx][jdx] = state


# %%
@pytest.mark.parametrize("board, expected", [
    (
        [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
        [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
    ),
    (
        [[1, 1], [1, 0]],
        [[1, 1], [1, 1]],
    ),
    (
        [[1]],
        [[0]],
    ),
])
def test_suite(board, expected):
    game_of_life(board)
    assert board == expected