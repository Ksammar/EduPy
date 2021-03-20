# + Реализовать базовый класс Worker(работник).
#
# - определить атрибуты: name, surname, position(должность), income(доход);
# - последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
#   элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# - создать класс Position(должность) на базе класса Worker;
# - в классе Position  реализовать методы получения полного имени сотрудника(get_full_name)
#   и дохода с учётом премии(get_total_income);
# - проверить работу примера на реальных данных: создать экземпляры класса
# Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income.get('wage') + income.get('bonus')


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income


worker1 = Position('Maxim', 'Shipov', 'Engineer', {'wage': 10000, 'bonus': 1000})
worker2 = Position('Ivan', 'Petrov', 'Technic', {'wage': 5000, 'bonus': 100})
print(worker1.get_full_name())
print(worker1.get_total_income())

print(worker2.get_full_name())
print(worker2.get_total_income())