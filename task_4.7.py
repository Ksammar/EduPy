# -*- coding: utf-8 -*-
# Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
from math import factorial as fct
from itertools import count
# from time import time


def fact():
    for el in count(1):
        yield fct(el)


# t0 = time()
print(fact())
j = 0
for i in fact():
    print(i)
    j += 1
    if j > 7:
        break
# t1 = time()
# j = 0
# for i in range(1, 7):
#     print(fct(i))
#     j += 1
#     if j > 5:
#         break
# t2 = time()
# print(f't1 = {t1 - t0}')
# print(f't2 = {t2 - t1}')
