#!/usr/bin/env python3


def check_win(board: list) -> int:
    """This function takes a board in form of a matrix aka a list of a list and
    checks whether any player has won the game."""

    # Check if someone has won - line
    for row in board:
        if (row[0] == row[1] == row[2]) and (row[0] != 0):
            return row[0]   # Returns 1 or 2, which is the player's number

    # Check if someone has won - column
    for i in range(3):
        if (board[0][i] == board[1][i] == board[2][i]) and (board[0][i] != 0):
            return board[0][i]  # Returns 1 or, which is the player's number

    # Check if someone has won - principal diagonal
    value = board[0][0]
    win = True
    for i in range(1, 3):
        if board[i][i] != value:
            win = False
            break   # Exit from loop
    if win:
        return value

    # Check if someone has won - secondary diagonal
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] != 0):
        return board[0][2]  # Returns 1 or 2, which is the player's number
    return 0    # Nobody has won


if __name__ == '__main__':
    also_no_winner = [[1, 2, 0],
                      [2, 1, 0],
                      [2, 1, 0]]

    print(check_win(also_no_winner))
