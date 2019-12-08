#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from pprint import pprint

if __name__ == '__main__':
    r = requests.get('https://www.vanityfair.com/style/society/2014/06/'
                     'monica-lewinsky-humiliation-culture')
    soup = BeautifulSoup(r.text, 'html.parser')
    article = soup.find(class_="grid--item body body__container article__body "
                               "grid-layout__content")
    for item in article.find_all('p'):
        pprint(item.text)
