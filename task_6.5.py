# + Реализовать класс Stationery(канцелярская принадлежность).
#
# - определить в нём атрибут title(название) и метод draw(отрисовка). Метод
# выводит сообщение «Запуск отрисовки»;
# - создать три дочерних класса Pen(ручка), Pencil(карандаш), Handle(маркер);
# - в каждом классе реализовать переопределение метода draw. Для
# каждого класса метод должен выводить уникальное сообщение;
# - создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Ручка', self.title, 'рисует')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш', self.title, 'рисует')


class Handle(Stationery):
    def draw(self):
        print('Маркер', self.title, 'рисует')


pen1 = Pen('Parker')
pen2 = Pen('Nonename')
pencil = Pencil('Koh-i-Noor')
marker = Handle('MARKER')

pen1.draw()
pencil.draw()
marker.draw()
pen2.draw()
