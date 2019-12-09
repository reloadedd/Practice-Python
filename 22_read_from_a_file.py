#!/usr/bin/env python3

if __name__ == '__main__':
    filename = 'Training_01.txt'

    with open(filename) as sun_pictures:
        categories = {}

        line = sun_pictures.readline()
        while line:
            category_name = line.split('/')[2]

            if category_name not in categories:
                categories[category_name] = 1
            else:
                categories[category_name] += 1

            line = sun_pictures.readline()  # move to the next line

        # print the results
        for key, value in categories.items():
            print('Category [{}] contains {} images.'.format(key, value))
