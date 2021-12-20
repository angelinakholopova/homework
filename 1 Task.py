#! /usr/bin/env python
# -*- coding: utf-8 -*-
def salary():
    working_hours = float(input('Введите количество отработанных часов: '))
    rate = float(input('Введите сумму ставки в час: '))
    bonus = float(input('Введите сумму премии: '))
    return (working_hours * rate) + bonus


print('Заработанная премия = ', salary())
