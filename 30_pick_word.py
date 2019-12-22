#!/usr/bin/env python3

from random import choice


def pick_random_word(wordlist: list) -> str:
    """Pick a random number from a list of words."""
    return choice(wordlist)


if __name__ == '__main__':
    with open('sowpods.txt') as sowpods:
        random_word = pick_random_word(sowpods.readlines())
        print('Random word picked:', random_word)
