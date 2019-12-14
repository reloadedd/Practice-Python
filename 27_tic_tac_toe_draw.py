#!/usr/bin/env python3

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


def get_input() -> list:
    """This function prompts the user for his/her move, then returns a list of
     the form [row, col]. The function also check for the validity of the
     input."""

    again = False
    while 1:    # This loop will be interrupted when a valid move is entered
        if again:
            print('Wrong input [!] ', end='')
        move = input('Position (row, column) - without parentheses >>> ')
        move = move.strip()    # Remove all whitespaces from left and right
        move = move.split(',')  # Store the list in the same variable

        if 1 <= int(move[0]) <= 3 and 1 <= int(move[1]) <= 3:
            row = int(move[0]) - 1  # the user enters the position starting
            column = int(move[1]) - 1   # from 1. We don't want that
            move[0] = row
            move[1] = column

            if board[row][column] == 0:
                return move     # valid move
            again = True


def display_board():
    """This function simply displays the game board."""

    for row in board:
        for element in row:
            print(element, ' ', end='')
        print()


def play_game():
    """This function handles the way the game works. It asks for input and then
    writes the input into the game matrix and displays the board."""

    while True:
        print('[Player One]: ', end='')
        player_one = get_input()
        board[player_one[0]][player_one[1]] = 'X'
        display_board()

        print('[Player Two]: ', end='')
        player_two = get_input()
        board[player_two[0]][player_two[1]] = 'O'
        display_board()


if __name__ == '__main__':
    print('''Welcome to Tic Tac Toe Game!
        - You will be prompted for a position in the form of the tuple (row, column).
        - The numbering starts from 1. Think about it as 3x3 matrix.
        - You should enter the position (without parentheses). E.g: 2, 3 which 
        represents the element from the second row and the third column.
        - If you enter a wrong position (any number lower than 1 or greater 
        than 3), you will be prompted again. 
    ''')

    play_game()
