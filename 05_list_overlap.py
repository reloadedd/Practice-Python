#!/usr/bin/env python3

import random


def return_common_elements(first_list, second_list):
    first_list.extend(second_list)
    new_list = list(set(first_list))
    return new_list


if __name__ == '__main__':
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    common = return_common_elements(a, b)
    print("# Return the common elements of the 2 lists\n", common)

    # Randomly generate 2 lists of random length and test
    list_1 = []
    list_2 = []
    for i in range(random.randint(10, 30)):
        list_1.append(random.randint(1, 10))
        list_2.append(random.randint(1, 100))

    print("# First random list\n", list_1)
    print("# Second random list\n", list_2)
    common = return_common_elements(list_1, list_2)
    print("# Common elements from the 2 randomly generated lists\n", common)

    # One line
    print("# One line\n", list(set(list_1 + list_2)))
