#!/usr/bin/env python3

import datetime

name = input("Please enter your name here > ")
age = int(input("Please enter your age here > "))

difference = 100 - age
current_year = datetime.datetime.now().year
string = "{0}, the year you will turn 100 will be {1}".format(name, current_year + difference)
print(string)

# Extras
number = int(input("How many times do you want that message to be printed out ? "))
for i in range(number):
    print(string)