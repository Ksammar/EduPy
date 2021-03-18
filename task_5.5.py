# + Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать
# сумму чисел в файле и выводить её на экран.
import random
with open('out_task_5.5.txt', 'w', encoding='utf8') as f_w_obg:
    counter = 50
    sum_num = 0
    list_out = []
    for i in range(1, counter):
        rnd_num = random.randint(0, counter)
        list_out.append(f'{rnd_num} ')
        sum_num += rnd_num
    f_w_obg.writelines(list_out)  # помимо читерского способа ниже обычный ;)
print(sum_num)
with open('out_task_5.5.txt', 'r', encoding='utf8') as f_r_obg:
    line = f_r_obg.read().split()
    line = [int(item) for item in line]
    print(sum(line))
