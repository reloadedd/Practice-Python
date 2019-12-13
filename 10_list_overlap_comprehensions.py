#!/usr/bin/env python3

import random

MAX_ELEMENT_VALUE = 100
MAX_ELEMENTS = 20

# Randomly generate two lists

# Noob way

# list_1 = [random.randint(0, MAX_ELEMENT_VALUE) for _ in
# range(random.randint(1, MAX_ELEMENTS))]
# list_2 = [random.randint(0, MAX_ELEMENT_VALUE) for _ in
# range(random.randint(1, MAX_ELEMENTS))]

# Easy way
list_1 = random.sample(range(100), random.randint(1, MAX_ELEMENTS))
list_2 = random.sample(range(100), random.randint(1, MAX_ELEMENTS))

print('First list: ', list_1, '\n', 'Second list: ', list_2, sep='')

commons = list(set([x for x in list_1 for y in list_2 if x == y]))

print('The list that contains only the common elements of both lists is: ',
      commons)
