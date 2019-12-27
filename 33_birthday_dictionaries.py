#!/usr/bin/env python3

import json

filename = "info.json"


def write_birthday(data: dict) -> None:
    """Write birthday of a scientist to a json file on the disk."""
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


def add_another(data: dict) -> None:
    """Ask the user for a scientist's birthday and write changes to disk."""
    choice = input('Do you want to add another birthday? [Y/N] >>> ').upper()

    if choice == 'Y':
        name = input("Scientist's name >>> ")
        birthday = input("Scientist's birthday (mm/dd/yyyy) >>> ")
        data[name] = birthday
        write_birthday(data)


if __name__ == '__main__':
    with open(filename, 'r') as file:
        info = json.load(file)

    print('>>> Welcome to the birthday dictionary. We know the birthdays of:')
    for i in info:
        print(i)

    human = input(">>> Who's birthday do you want to look up?\n")
    birthday = info.get(human, None)
    if birthday is None:
        print("We are sorry, but we don't have that person in our dictionary.")
    else:
        print("{}'s birthday is {}".format(human, birthday))

    add_another(info)
