#!/usr/bin/env python3

if __name__ == '__main__':
    birthdays = {'Albert Einstein': '03/14/1879',
                 'Benjamin Franklin': '01/17/1706',
                 'Ada Lovelace': '12/10/1815'}

    print('>>> Welcome to the birthday dictionary. We know the birthdays of:')
    for i in birthdays:
        print(i)

    human = input(">>> Who's birthday do you want to look up?\n")
    birthday = birthdays.get(human, None)
    if birthday is None:
        print("We are sorry, but we don't have that person in our dictionary.")
    else:
        print("{}'s birthday is {}".format(human, birthday))
