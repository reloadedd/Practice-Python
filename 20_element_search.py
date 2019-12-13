#!/usr/bin/env python3


def dummy_search(elements: list, n: int) -> bool:
    """Search a number (n) in an ordered list of numbers (elements)
    Returns the True if the element is in the list, otherwise it returns False.
    """
    for i in elements:
        if n == i:
            return True  # We found it
    return False  # Nope, it's not in there


def binary_search(elements: list, n: int) -> bool:
    """Search a number (n) in an ordered list of numbers (elements)
    Returns the True if the element is in the list, otherwise it returns False.
    For accomplishing this task, the function implements binary search method.
    The elements of the list MUST be in increasing order.
    """
    left = 0
    right = len(elements) - 1

    while left <= right:
        middle = (left + right) // 2
        if n == elements[middle]:
            return True  # We found it
        elif n < elements[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return False  # If the execution arrives here, the element it's not in
    # the list


if __name__ == '__main__':
    # The list must be sorted in increasing order for the binary search to work
    the_list = [1, 2, 3, 51, 122, 534, 738, 1337, 9999]
    the_searched_one = 51

    # if dummy_search(the_list, the_searched_one):
    #     print('{} is in the list.'.format(the_searched_one))
    # else:
    #     print('{} is NOT in the list.'.format(the_searched_one))

    if binary_search(the_list, the_searched_one):
        print('{} is in the list.'.format(the_searched_one))
    else:
        print('{} is NOT in the list.'.format(the_searched_one))