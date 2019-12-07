#!/usr/bin/env python3

number = int(input("Please enter a number > "))
remainder = number % 2

if remainder:
    print("It's seems that {0} is odd.".format(number))
else:
    print("It's seems that {0} is even.".format(number))

# Check to see if it's multiple of 4
remainder = number % 4
if remainder == 0:
    print("{0} is a multiple of 4, also.".format(number))

num = int(input("Please enter the first number > "))
check = int(input("Please enter the second number > "))
if num % check:
    print("The numbers are not divisible.")
else:
    print("{0} divides {1}".format(check, num))
