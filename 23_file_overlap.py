#!/usr/bin/env python3


def create_list_from_file(filename: str) -> list:
    """This function creates a list of all the numbers from the file given as
    argument to the function. It then returns the list.
    """

    numbers = []
    with open(filename) as file:
        for line in file:
            numbers.append(line.strip())
    return numbers


def compare_lists(list_01: list, list_02: list) -> None:
    """Compare the 2 lists given as arguments to the function."""

    for i in list_01:
        for j in list_02:
            if i == j:
                print('Number {} is overlapping'.format(i))


if __name__ == '__main__':
    happy_numbers = create_list_from_file('happynumbers.txt')
    prime_numbers = create_list_from_file('primenumbers.txt')
    compare_lists(happy_numbers, prime_numbers)
