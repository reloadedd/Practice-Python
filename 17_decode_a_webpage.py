#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

responseObj = requests.get('https://www.nytimes.com/')
soup = BeautifulSoup(responseObj.text, 'html.parser')

print('The article titles in NYT are the following: ')
article_titles = soup.find_all('span')
index = 0
for title in article_titles:
    index += 1
    if title.text:
        print('[{0:2}] {1}'.format(index, title.text))
