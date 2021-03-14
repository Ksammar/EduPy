# -*- coding: utf-8 -*-
# Реализовать формирование списка, используя функцию range()
# и возможности генератора. В список должны войти чётные
# числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce
out_list = [number for number in range(100, 1001) if number % 2 == 0]
print(out_list)
print(f'Multiplication result: \n {reduce(lambda num1, num2: num1 * num2, out_list)}')
