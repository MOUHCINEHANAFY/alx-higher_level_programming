#!/usr/bin/python3
"""Solves the N-queens puzzle."""

import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with empty squares."""
    return [[' ' for _ in range(n)] for _ in range(n)]


def is_safe(board, row, col):
    """Check if it's safe to place a queen at the given row and column."""
    n = len(board)

    # Check the left side of the row
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower left diagonal
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_nqueens(board, col, solutions):
    """Recursively solve the N-Queens puzzle."""
    n = len(board)

    if col == n:
        solutions.append([''.join(row) for row in board])
        return

    for row in range(n):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            solve_nqueens(board, col + 1, solutions)
            board[row][col] = ' '


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            raise ValueError
    except ValueError:
        print("N must be an integer greater than or equal to 4")
        sys.exit(1)

    board = init_board(n)
    solutions = []
    solve_nqueens(board, 0, solutions)

    for solution in solutions:
        for row in solution:
            print(row)
        print()


if __name__ == "__main__":
    main()
