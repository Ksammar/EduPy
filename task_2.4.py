# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

input_str = input('Введите массив слов: ')
input_mas = input_str.split(" ")
counter = 0
while counter < len(input_mas):
    print(f'{counter + 1}. {input_mas[counter][0:10:]}')
    counter += 1