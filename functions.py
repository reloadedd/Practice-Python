from random import choice


# Used for Hangman series
def pick_random_word() -> str:
    """Pick a random number from a list of words."""
    with open('sowpods.txt') as file:
        wordlist = file.readlines()
        return choice(wordlist)
