#! /usr/bin/env python
# -*- coding: utf-8 -*-
def my_func(x, y):
    if x > 0 > y:
        return x ** y
    else:
        return 'Функция не определена!'


num1 = float(input('Введите действительное положительное число: '))
num2 = int(input('Введите целое отрицательное число: '))
print(my_func(num1, num2))
