# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.             +
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,   +
# а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать. +
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import random
import json


def create_firm_file():
    with open('out_task_5.7.txt', 'w', encoding='utf8') as f_w_obg:
        sequence = ['ООО', 'АО', 'ПАО', 'GmBH', 'AktG']
        for i in range(1, 11):
            line = f'firm{i} {random.choice(sequence)} {random.randint(5000, 20000)} {random.randint(1000, 20000)}\n'
            f_w_obg.write(line)


create_firm_file()
with open('out_task_5.7.txt', 'r', encoding='utf8') as f_r_obg:
    firm_dict = {}
    average_profit = 0
    counter = 0
    for line in f_r_obg:
        line = line.split()
        firm, form, debet, credit = line[:4]
        profit_margin = int(debet) - int(credit)
        if profit_margin > 0:
            average_profit += profit_margin
            counter += 1
        firm_dict.update({firm: [profit_margin]})

average_profit = float(average_profit/counter)
out_list = [firm_dict, {'average_profit': average_profit}]
with open('out_task_5.7.json', 'w', encoding='utf-8') as f_json:
     json.dump(out_list, f_json)

with open('out_task_5.7.json', 'r', encoding='utf-8') as f_json:
     data_loaded = json.load(f_json)

print(data_loaded)

