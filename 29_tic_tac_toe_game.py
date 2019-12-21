#!/usr/bin/env python3

from sys import exit

BOARD_SIZE = 3
BOARD = [['0', '0', '0'],
         ['0', '0', '0'],
         ['0', '0', '0']]
SCORE = {'player_one': 0, 'player_two': 0}


def create_line(columns: int, line: int) -> None:
    """Draw a line full of character "squares"."""
    print(' -----' * columns, sep='')

    for element in BOARD[line]:
        print(' |  ', sep='', end='')
        print(element, end='')
    print('  |')
    # print()


def display_board(size: int) -> None:
    """Display the game board."""
    for i in range(size):
        create_line(size, i)
    # print this here to match the ending dashes
    print(' -----' * size, sep='')


def get_input() -> list:
    """Prompt the user for his/her move, then returns a list of the form
     [row, col]. The function also check for the validity of the input."""

    while 1:    # This loop will be interrupted when a valid move is entered
        move = input('Position (row, column) - without parentheses >>> ')
        move = move.strip()    # Remove all whitespaces from left and right
        move = move.split(',')  # Store the list in the same variable

        try:
            if 1 <= int(move[0]) <= 3 and 1 <= int(move[1]) <= 3:
                row = int(move[0]) - 1  # the user enters the position starting
                column = int(move[1]) - 1   # from 1. We don't want that
                move[0] = row
                move[1] = column

                if BOARD[row][column] == '0':
                    return move     # valid move
                else:
                    print('[Error] Sorry, but that position is already taken.')
            else:
                print("[Error] The board isn't that large, captain.")
        except ValueError:
            print('[Error] Are you sure those are numbers?')


def check_win() -> str:
    """Check whether any player has won the game."""

    # Check if someone has won - line
    for row in BOARD:
        if (row[0] == row[1] == row[2]) and (row[0] != '0'):
            return row[0]   # Returns 1 or 2, which is the player's number

    # Check if someone has won - column
    for i in range(3):
        if (BOARD[0][i] == BOARD[1][i] == BOARD[2][i]) and \
                (BOARD[0][i] != '0'):
            return BOARD[0][i]  # Returns 1 or, which is the player's number

    # Check if someone has won - principal diagonal
    value = BOARD[0][0]
    win = True
    for i in range(1, 3):
        if BOARD[i][i] != value:
            win = False
            break   # Exit from loop
    if win:
        return value

    # Check if someone has won - secondary diagonal
    if (BOARD[0][2] == BOARD[1][1] == BOARD[2][0]) and (BOARD[0][2] != '0'):
        return BOARD[0][2]  # Returns 1 or 2, which is the player's number
    no_winner = '1'
    for row in BOARD:
        for element in row:
            if element == '0':
                no_winner = '0'

    return no_winner    # Nobody has won or there are moves left


def show_score():
    """Display score."""
    print('=' * 22, 'SCORE', '=' * 22)
    print('[Player One]: ', SCORE['player_one'])
    print('[Player Two]: ', SCORE['player_two'])
    print('=' * 51)


def game_over(winner: str) -> None:
    """Display the winner of the game and then exit."""
    again = ''

    if winner == 'X':
        SCORE['player_one'] += 1
        print('[VICTORY] Hooray! Player One has won the game!')
        show_score()
    elif winner == 'O':
        SCORE['player_two'] += 1
        print('[VICTORY] Hooray! Player Two has won the game!')
        show_score()
    elif winner == '1':
        print('[DRAW] Nobody has won the game!')
        show_score()

    # Bonus
    if winner in ('X', 'O', '1'):
        while again not in ('Y', 'N'):
            again = input('Do you want to play again? [Y/N] >> ').upper()
            if again == 'Y':
                play_game()
            elif again == 'N':
                print('\n{} See ya soon [!] {}'.format('#' * 25, '#' * 25))
                exit(0)


def play_game():
    """Ask for input and then write the input into the game matrix and displays
     the board."""
    global BOARD
    BOARD = [['0', '0', '0'],
             ['0', '0', '0'],
             ['0', '0', '0']]
    display_board(BOARD_SIZE)

    try:
        while True:
            print('[Player One]: ', end='')
            player_one = get_input()
            BOARD[player_one[0]][player_one[1]] = 'X'
            display_board(BOARD_SIZE)
            game_over(check_win())

            print('[Player Two]: ', end='')
            player_two = get_input()
            BOARD[player_two[0]][player_two[1]] = 'O'
            display_board(BOARD_SIZE)
            game_over(check_win())
    except KeyboardInterrupt:
        print('\n{} See ya soon [!] {}'.format('#' * 25, '#' * 25))


if __name__ == '__main__':
    print('''Welcome to Tic Tac Toe Game!
        - You will be prompted for a position in the form of the tuple 
        (row, column).
        - The numbering starts from 1. Think about it as 3x3 matrix.
        - You should enter the position (without parentheses). E.g: 2, 3 which 
        represents the element from the second row and the third column.
        - If you enter a wrong position (any number lower than 1 or greater 
        than 3), you will be prompted again. 
    ''')

    play_game()
