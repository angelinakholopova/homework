#! /usr/bin/env python
# -*- coding: utf-8 -*-
def int_func(word):
    return word.title()


def str_func(string):
    my_list = string.split()
    for i in range(len(my_list)):
        my_list[i] = int_func(my_list[i])
    string_2 = ' '.join(my_list)
    return string_2


my_word = input('Введите слово: ')
print(int_func(my_word))
my_string = input('Введите несколько слов через пробел: ')
print(str_func(my_string))
