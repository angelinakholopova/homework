#! /usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import count, cycle


def count_end():
    start = int(input('Введите начало последовательности: '))
    end = int(input('Введите конец последовательности: '))
    for el in count(start):
        if el > end:
            break
        else:
            print(el)


def cycle_end(my_list):
    c = 0
    for el in cycle(my_list):
        if c > 10:
            break
        else:
            print(el)
            c += 1


new_list = [1, 2, 'my_list', (1, 3), False]
print(count_end())
print(cycle_end(new_list))
