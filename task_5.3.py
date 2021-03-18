# + Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
from statistics import mean

surname = []
salary = []
with open('for_task_5.3.txt', 'r', encoding='utf8') as f_obj:
    for i, line in enumerate(f_obj):
        line = line.split()
        payment = float(line[1])
        salary.append(payment)
        if payment < 20000.00:
            surname.append(line[0])
print(f'Following employees received less than 20,000: {surname}')
print(f'The average salary of employees was: {mean(salary)}')
