# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

in_time = int(input('Введите время в секундах: '))
print(f'{in_time//3600}:{(in_time%3600)//60}:{(in_time%60)}')