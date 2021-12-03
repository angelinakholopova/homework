#! /usr/bin/env python
# -*- coding: utf-8 -*-
def sum_numbers(string):
    list_numbers = string.split()
    summa = 0
    for i in range(len(list_numbers)):
        if list_numbers[i] != 'q':
            summa += int(list_numbers[i])
        else:
            break
    return summa


s = input('Введите числа, разделенные пробелом: ')
print(sum_numbers(s))
first_sum = sum_numbers(s)
s = input('Введите числа, разделенные пробелом: ')
print(sum_numbers(s) + first_sum)
