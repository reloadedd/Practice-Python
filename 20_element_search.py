#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    responseObj = requests.get('https://www.nytimes.com/')
    soup = BeautifulSoup(responseObj.text, 'html.parser')

    filename = input('Write the name of the file in which to write the '
                     'results, please >> ')
    with open(filename, 'w') as results:
        print('The article titles in NYT are the following: ', file=results)
        article_titles = soup.find_all('span')
        index = 0
        for title in article_titles:
            index += 1
            if title.text:
                print('[{0:2}] {1}'.format(index, title.text), file=results)
