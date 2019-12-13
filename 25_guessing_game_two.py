#!/usr/bin/env python3


def binary_search() -> None:
    left = 0
    right = 100
    guesses = 0

    while left <= right:
        guesses += 1
        middle = (left + right) // 2
        print('It is {} ?'.format(middle))
        guess = input('Your answer (Low/High/Match) >> ')

        if guess.lower() == 'match':
            print('It only took me {} tries to guess the number'.format(
                guesses))
            return
        if guess.lower() == 'high':
            right = middle - 1
        else:
            left = middle + 1


if __name__ == '__main__':
    binary_search()
