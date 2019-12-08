#!/usr/bin/env python3

from random import randint


def get_input() -> int:
    n = int(input('Please enter a 4-digit number >>> '))

    # if the number has more or than 4 digits
    while n > 9999 or n < 1000:
        print("The number entered doesn't have 4 digits.")
        n = int(input('Please enter a 4-digit number >>> '))

    return n


def play_game():
    random_number = randint(1000, 9999)
    random_digits = []      # initialize an empty list
    guesses = 0

    print('[Debug] Random_number >> ', random_number)

    # add all digits into a list and then remove the random number generated
    while random_number:
        random_digits.append(random_number % 10)
        random_number //= 10

    random_digits.reverse()     # preserve the order
    del random_number   # don't need it anymore

    while True:
        bulls = 0
        cows = []
        index = 4
        n = get_input()

        while n:
            digit = n % 10  # get the last digit
            n //= 10     # remove that digit
            index -= 1

            if digit == random_digits[index]:
                cows.append(digit)
            else:
                bulls += random_digits.count(digit)
                if digit in cows:
                    bulls -= 1
        guesses += 1

        if len(cows) == 4:
            print('Congrats, you guessed correctly! It took you just {} '
                  'guesses!'.format(guesses))
            return      # exit, game finished

        print('cows: {}, bulls: {}'.format(len(cows), bulls))


if __name__ == '__main__':
    play_game()
