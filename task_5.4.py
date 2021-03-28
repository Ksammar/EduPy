# + Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dict_ru_en = {'One': 'один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
# f_w_obg = open('out_task_5.4.txt', 'w')
with open('for_task_5.4.txt', 'r', encoding='utf8') as f_obj:
    for i, line in enumerate(f_obj, start=1):
        line = line.split()
        with open(f'for_task_5.4_{i}.txt', 'w', encoding='utf8') as f_w_obg:
            f_w_obg.write(f'{dict_ru_en.get(line[0])} {line[1]} {line[2]}')


