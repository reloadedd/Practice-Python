#!/usr/bin/env python3

from string import printable, whitespace
from random import randint


def generate_password(strong: bool = True) -> str:
    password = ''

    if strong:
        length = randint(15, 25)    # Choose a length for the password
        # All printable characters, excluding whitespaces
        chars = list(set(printable) - set(whitespace))
        for i in range(length):
            pick = randint(0, len(chars)) - 1  # Pick a random character
            password += chars[pick]
    else:
        # Credits goes to https://github.com/dwyl/english-words/ for the word
        # list
        index = 0
        div = randint(2, 150000)
        words = randint(2, 5)		# How many words the password should have
        with open('words_alpha.txt') as word_list:
            while words > 0:
                current_word = word_list.readline().strip('\n')
                index += 1
                if index % div == 0:		# if index is divisible by `div`
                    password += current_word
                    password += ' '
                    words -= 1
            password = password[:-1]		# Remove the trailing whitespace

    return password


def main():
    password = generate_password()
    print('[+] Password generated >> {}'.format(password))


if __name__ == '__main__':
    main()
