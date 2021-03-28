# + Создать текстовый файл (не программно),
# сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

from math import factorial as fct

with open('for_task_5.2.txt', 'a', encoding='utf8') as f_obj:
    for i in range(1, 7):
        for j in range(0, i):
            f_obj.write(str(fct(i)) + ' ')
        f_obj.write('\n')
with open('for_task_5.2.txt', 'r', encoding='utf8') as f_obj:
    out_dict = dict({})
    for i, line in enumerate(f_obj, start=1):
        words = len(line.split())
        out_dict.update({f'в строке {i} слов: ': [words]})
for key in out_dict:
    print(key, out_dict[key])
