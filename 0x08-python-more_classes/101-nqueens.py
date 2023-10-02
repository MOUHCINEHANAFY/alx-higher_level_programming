#!/usr/bin/python3
"""Solves the N-queens puzzle."""
import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at a given position."""
    # Check row on the left
    for i in range(col):
        if board[row][i] == "Q":
            return False

    # Check upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # Check lower diagonal on the left
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    return True


def solve_nqueens(n):
    """Solve the N-queens puzzle using backtracking."""
    def backtrack(row):
        if row == n:
            solutions.append(["".join(row) for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

    board = [["." for _ in range(n)] for _ in range(n)]
    solutions = []
    backtrack(0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        for row in solution:
            print(row)
        print()
