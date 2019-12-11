#!/usr/bin/env python3


def create_line(columns: int) -> None:
    """This function draws a line full of character "squares"."""

    print(' ---' * columns, sep='')
    print('|   ' * columns, '|', sep='')


def create_board(size: int) -> None:
    """This function creates the board. The board will be a matrix of dimension
    size x size.
    """

    for i in range(size):
        create_line(size)
    # print this here to match the ending dashes
    print(' ---' * size, sep='')


if __name__ == '__main__':
    board_size = int(input('Enter the size of the board >>> '))
    create_board(board_size)
