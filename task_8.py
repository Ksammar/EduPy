"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random
import time
from copy import deepcopy


def loto_generator():
    list_numbers = []
    for i in range(1, 90):
        list_numbers.append(i)
    while True:
        number = random.randint(0, len(list_numbers) - 1)
        res = list_numbers[number]
        list_numbers.remove(res)
        yield res


def number_in_card(num, in_list):
    result = [False, 0, 0]
    for i, el_l in enumerate(in_list):
        for j, el in enumerate(el_l):
            if el == num:
                result[0] = True
                result[1] = i
                result[2] = j
    return result


class LotoCard:
    def __init__(self, name):
        self.__pc_name = ['PC', 'Компьютер', 'Комп', 'Computer', 'Comp']
        self.__main_line = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.type = 0
        if self.__pc_name.count(name) > 0:
            self.type = 1
        self.card = self.__list_filling(self.__main_line)
        self.counter = 0

    @staticmethod
    def __list_filling(in_line):
        main_line = deepcopy(in_line)
        gen_obj = loto_generator()
        for i in range(3):
            counter = 0
            for number in gen_obj:
                if main_line[i][8 if number >= 80 else number // 10] != ' ':
                    continue
                main_line[i][8 if number >= 80 else number // 10] = number
                counter += 1
                if counter > 4:
                    break
        return main_line

class LotoGame:
    def __init__(self, player1, player2):
        if player1.type == 1:
            self.p2 = player1
            self.p1 = player2
        else:
            self.p1 = player1
            self.p2 = player2

    def start(self):
        counter_cub = 90
        gen_obj = loto_generator()
        for number in gen_obj:
            counter_cub -= 1
            if counter_cub > 89:
                break
            print(f'Новый бочонок: {number} (осталось {counter_cub})')
            print('---------- Ваша карточка ---------')
            print('\n'.join('\t'.join(map(str, row)) for row in self.p1.card))
            print('----------------------------------')
            print('------ Карточка компьютера -------')
            print('\n'.join('\t'.join(map(str, row)) for row in self.p2.card))
            print('----------------------------------')
            answer = input('Зачеркнуть цифру? (y/n) \n')
            res_ans = number_in_card(number, self.p1.card)
            if answer == 'y':
                if res_ans[0]:
                    self.p1.card[res_ans[1]][res_ans[2]] = '-'
                    self.p1.counter += 1
                else:
                    print('Вы проиграли!')
                    break
            if answer == 'n':
                if res_ans[0]:
                    print('Вы проиграли!')
                    break
            res_ans = number_in_card(number, self.p2.card)
            if res_ans[0]:
                self.p2.card[res_ans[1]][res_ans[2]] = '-'
                self.p2.counter += 1

            if self.p1.counter > 14 or self.p2.counter > 14:
                break
        if self.p1.counter > 14:
            print('Игрок выиграл!!! \n')
        if self.p2.counter > 14:
            print('Компьютер выиграл!!! \n')

        # print('---------- Ваша карточка ---------')
        # print('\n'.join('\t'.join(map(str, row)) for row in self.p1.card))
        # print('----------------------------------')
        # print('------ Карточка компьютера -------')
        # print('\n'.join('\t'.join(map(str, row)) for row in self.p2.card))
        # print('----------------------------------')



gamer = LotoCard('Игрок')
pc = LotoCard('PC')
game = LotoGame(gamer, pc)
game.start()
# #
# print('\n'.join('\t'.join(map(str, row)) for row in gamer.card))
