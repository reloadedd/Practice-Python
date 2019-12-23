#!/usr/bin/env python3

WORD = 'EVAPORATE'

if __name__ == '__main__':
    guessed = False
    build_word = list('_' * len(WORD))

    print('>>> Welcome to Hangman!')
    print('_ ' * len(WORD))

    while not guessed:
        guess = input('>>> Guess your letter: ')

        if guess in WORD:
            i = 0
            for letter in WORD:
                if guess == letter:
                    if build_word[i] == letter:
                        print('Already guessed. Try another letter.')
                        break
                    else:
                        build_word[i] = letter
                i += 1

            for letter in build_word:
                print(letter, end=' ')
            print()     # Newline

            if '_' not in build_word:
                guessed = True
                print('Hooray! You guessed the word!')
        else:
            print('Incorrect!')
