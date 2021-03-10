# Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def div_numbers(divisible, divisor):
    if abs(divisor) < 1e-15:
        print('division by zero!')
        return None
    else:
        return divisible / divisor


def div_numbers2(divisible, divisor):
    try:
        return divisible / divisor
    finally:
        print('division by zero!!!')  # из С подобных языков так надежнее, чем == 0
        return None


divisible = float(input('insert divisible number '))
divisor = float(input('insert divisor number '))
print(div_numbers(divisible, divisor))
print(div_numbers2(divisible, divisor))
