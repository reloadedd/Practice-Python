#!/usr/bin/env python3


def get_divisors(n):
    d = 1
    while d * d <= n:
        if n % d == 0:
            print(d)
            # If d is a divisor, then number / d is also a divisor
            # But we need to be careful with square numbers
            if d * d < n:
                print(n // d)
        d += 1


if __name__ == '__main__':
    number = int(input("Please enter a number > "))
    get_divisors(number)
