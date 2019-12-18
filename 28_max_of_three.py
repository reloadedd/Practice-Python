#!/usr/bin/env python3


def max_of_three(first: int, second: int, third: int) -> int:
    """This function returns the maximum number out of three numbers."""

    if first > second:
        if first > third:
            return first
        return third
    else:
        if second > third:
            return second
        return third


if __name__ == '__main__':
    var1 = int(input('Enter a number >> '))
    var2 = int(input('Enter another number >> '))
    var3 = int(input('Enter yet another number >> '))

    print('The largest number is {}'.format(max_of_three(var1, var2, var3)))
