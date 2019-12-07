#!/usr/bin/env python3

import random

number = random.randint(1, 9)
guesses = 0

user_input = input('Enter a number (between 1 and 9) [>>>] ')
while user_input != 'exit':
    if int(user_input) < number:
        print('Too low!')
    elif int(user_input) > number:
        print('Too high!')
    else:
        print("Yep, you've guessed it!")
        break

    guesses += 1
    user_input = input('Enter a number (between 1 and 9) [>>>] ')

print("Counting up, you've took {} guesses.".format(guesses))
