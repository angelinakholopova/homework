#! /usr/bin/env python
# -*- coding: utf-8 -*-
def division(num_1, num_2):
    if num_2 == 0:
        print("Нельзя делить на ноль!")
    else:
        return num_1 / num_2


num1 = int(input("Введите делимое: "))
num2 = int(input("Введите делитель: "))
division(num1, num2)
