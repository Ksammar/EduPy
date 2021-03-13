# Реализовать функцию my_func(), которая принимает
# три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(args):
    return sum(args) - min(args)


numbers = ['first', 'second', 'third']
for i in range(len(numbers)):
    numbers[i] = float(input(f'insert {numbers[i]} number '))
print(my_func(numbers))
