#!/usr/bin/env python3

from Practice_Python.functions import pick_random_word

WORD = pick_random_word().strip()   # Remove all whitespace

if __name__ == '__main__':
    print(WORD)
    guesses = 0
    build_word = list('_' * len(WORD))

    print('>>> Welcome to Hangman! You have 6 guessed. Good luck!')
    print('_ ' * len(WORD))

    while guesses < 6:
        guess = input('>>> Guess your letter: ').upper()    # Just to make sure
        while len(guess) != 1:
            guess = input('>>> Guess your letter: ').upper()

        if guess in WORD:
            i = 0
            for letter in WORD:
                if guess == letter:
                    if build_word[i] == letter:
                        print('Already guessed. Try another letter.')
                        # guesses -= 1
                        break
                    else:
                        build_word[i] = letter
                i += 1

            print(' '.join(build_word))

            if '_' not in build_word:
                print('Hooray! You guessed the word!')
                break   # End the game
        else:
            print('Incorrect!')
            guesses += 1

        print('Guesses left: ', (6 - guesses))
