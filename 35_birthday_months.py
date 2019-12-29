#!/usr/bin/env python3

import json
from collections import Counter

filename = 'info.json'


def identify_month_by_number(number: str) -> str:
    """Take the number of the month as a string and return its name."""
    if number == '01':
        return 'January'
    elif number == '02':
        return 'February'
    elif number == '03':
        return 'March'
    elif number == '04':
        return 'April'
    elif number == '05':
        return 'May'
    elif number == '06':
        return 'June'
    elif number == '07':
        return 'July'
    elif number == '08':
        return 'August'
    elif number == '09':
        return 'September'
    elif number == '10':
        return 'October'
    elif number == '11':
        return 'November'
    elif number == '12':
        return 'December'


if __name__ == '__main__':
    with open(filename, 'r') as json_file:
        birthdays = json.load(json_file)
    scientist_months = [month.split('/')[0] for month in birthdays.values()]

    counter = Counter(scientist_months)
    print('{')
    for month in counter:
        print('\t{}: {},'.format(identify_month_by_number(month),
                                 counter[month]))
    print('}')
