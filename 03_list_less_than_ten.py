#!/usr/bin/env python3

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Print all elements that are less than 5
for i in a:
    if i < 5:
        print(i)
print()
# Make a new list with the elements less than 5
new_list = [i for i in a if i < 5]
# Oh, it seems that it's also a one-liner
print(new_list, '\n')

input_number = int(input("Please enter a number > "))
new_list = [i for i in a if i < input_number]
print(new_list)
