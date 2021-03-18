# -*- coding: utf-8 -*-
# Реализовать скрипт, в котором должна быть предусмотрена
# функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений
# необходимо запускать скрипт с параметрами.
from sys import argv


def salary(pay, hours, bonus):
        return pay * hours + bonus


hours, pay, bonus = argv[1:4]
try:
    print(salary(float(pay), float(hours), float(bonus)))
except ValueError:
    print('One of element is\'n number')
