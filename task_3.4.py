# Программа принимает действительное положительное число x и
# целое отрицательное число y. Выполните возведение числа x в степень y.
# Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
    if x < 0:
        print('not a positive number!')
        return None
    result = 1
    for i in range(abs(y)):
        if y < 0:  # для универсальности функции
            result *= 1/x
        else:
            result *= x
    return result


x = float(input('insert x '))
y = int(input('insert y '))
# print(x ** y)
print(my_func(x, y))
