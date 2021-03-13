# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите число: "))
max_value = number % 10
number = number // 10
while number > max_value:
    if max_value < number % 10:
        max_value = number % 10
    number = number // 10
print(max_value)
