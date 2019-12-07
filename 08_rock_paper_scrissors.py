#!/usr/bin/env python3

choices = 'rock', 'paper', 'scissors'
EQUALITY = "Oh, no! There is no winner, it's equality!"
PLAYER_ONE_WINNER = '...And the winner is: ~Player One~'
PLAYER_TWO_WINNER = '...And the winner is: ~Player Two~'

print('''Welcome to the "Rock, Paper and Scissors" Game!
The rules are simple:
    1. Each player chooses what he/she wants from the following list: rock, \
paper or scissors
    2. Rock beats scissors
    3. Scissors beats paper
    4. Paper beats rock
    ''')    # for a newline

try:
    while True:
        player_one = input('Player One [>>>] ')
        while player_one not in choices:
            player_one = input('You can only choose rock, paper or scissors. '
                               'Try again [>>>] ')

        player_two = input('Player Two [>>>] ')
        while player_two not in choices:
            player_two = input('You can only choose rock, paper or scissors. '
                               'Try again [>>>] ')

        if player_one == player_two:    # equality
            print(EQUALITY)
        elif player_one == choices[0]:    # if player one has chosen rock
            if player_two == choices[1]:
                print(PLAYER_TWO_WINNER)
            else:
                print(PLAYER_ONE_WINNER)
        elif player_one == choices[1]:  # if player one has chosen paper
            if player_two == choices[0]:
                print(PLAYER_ONE_WINNER)
            else:
                print(PLAYER_TWO_WINNER)
        else:                           # if player one has chosen scissors
            if player_two == choices[1]:
                print(PLAYER_ONE_WINNER)
            else:
                print(PLAYER_TWO_WINNER)

        play_again = input('Do you want to play again? Player One [>>>] ')
        if play_again not in ['y', 'Y', 'yes']:
            break
        play_again = input('Do you want to play again? Player Two [>>>] ')
        if play_again not in ['y', 'Y', 'yes']:
            break
except KeyboardInterrupt:
    print('\nSee you soon!')
