#!/usr/bin/env python3


def remove_duplicates(the_list: list) -> list:
    """This function takes a list and then returns another list containing the
    elements of the original list, but without duplicates.
    """
    return list(set(the_list))


def remove_duplicates_2nd(the_list: list) -> list:
    """This function takes a list and then returns another list containing the
    elements of the original list, but without duplicates. It accomplishes this
    by constructing a new list using a for loop.
    """
    new_list = []

    for i in the_list:
        if i not in new_list:
            new_list.append(i)

    return new_list


def main():
    # list_1 = random.sample(range(100), random.randint(1, 15))
    list_1 = [2, 32, 123, 54, 2, 439, 123, 7]
    list_3 = remove_duplicates_2nd(list_1)

    print('Initial list: ', list_1, '\n', 'Initial list without duplicates: ',
          list_3, sep='')


if __name__ == '__main__':
    main()
