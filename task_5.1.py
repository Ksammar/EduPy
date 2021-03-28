# + Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.

with open('user_data.txt', 'w', encoding='utf8') as f_obj:
    while True:
        any_str = input('Input text: ')
        f_obj.write(any_str + '\n')
        if any_str == '':
            break
