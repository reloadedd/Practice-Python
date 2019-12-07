#!/usr/bin/env python3


def generate_fibonacci_sequence(elements_number: int) -> None:
    """Generate the first *n* elements of the fibonacci sequence
    """
    fib1 = 1
    fib2 = 1
    printed_elements = 2

    if elements_number <= 2:
        if elements_number == 1:
            print(fib1)
            return
        print(fib2)
        return

    print(fib1, fib2, end=' ')

    while printed_elements <= elements_number:
        fib3 = fib1 + fib2
        print(fib3, end=' ')
        printed_elements += 1
        fib1 = fib2
        fib2 = fib3
    print('\n')


def main():
    elements_number = int(input("How many elements of the Fibonacci's sequence"
                                " to generate? >>> "))
    generate_fibonacci_sequence(elements_number)


if __name__ == '__main__':
    main()
