#!/usr/bin/env python3

from bokeh.plotting import figure, show, output_file
from json import load

output = 'plot.html'
json_file = 'info.json'


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
    # where the output should go
    output_file(output)

    # load the json file
    with open(json_file, 'r') as file:
        birthdays = load(file)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    names = [scientist for scientist in birthdays]

    # load our x and y data
    x = [month for month in birthdays]
    y = [int(month_number.split('/')[0]) for month_number in
         birthdays.values()]

    # create a figure
    p = figure(title='Famous scientists and their birthdays',
               x_axis_label="Scientist's name",
               y_axis_label="Scientist's birthday",
               x_range=names,
               y_range=months)

    # create a histogram
    p.circle(x, y, size=25, color='navy', alpha=0.5, line_width=3)

    # render (show) the plot
    show(p)
