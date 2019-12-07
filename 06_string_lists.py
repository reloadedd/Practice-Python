#!/usr/bin/env python3

string = list(input("Please enter a string > "))

if string == string[::-1]:
    print("Palindrome.")
else:
    print("Not palindrome.")
