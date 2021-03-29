# + Реализовать класс Road(дорога).
#
# - определить атрибуты: length(длина), width(ширина);
# - значения атрибутов должны передаваться при создании экземпляра класса;
# - атрибуты сделать защищёнными;
# - определить метод расчёта массы асфальта, необходимого для покрытия  всей дороги;
# - использовать формулу: длина * ширина * масса асфальта для покрытия одного кв.метра
#   дороги асфальтом, толщиной в 1 см * число см толщины полотна;
# - проверить работу метода.
#
# Например: 20 м * 5000 м * 25 кг * 5 см = 12500 т.

class Road:
    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)
        self._weight = 25.0

    def weight_of_asphalt_t(self, thickness):
        """
        :param thickness: требуемая толщина асфальта
        :return: вывод требуемой массы в тоннах
        """
        return self._length * self._width * self._weight * float(thickness) / 100.0 / 1000

    def weight_of_asphalt_kg(self, thickness):
        """
        :param thickness: требуемая толщина асфальта
        :return: вывод требуемой массы в килограммах
        """
        return self._length * self._width * self._weight * float(thickness) / 100.0


asphalt_for_road = Road(5000, 20)
print(asphalt_for_road.weight_of_asphalt_t(5), 'ton')
print(asphalt_for_road.weight_of_asphalt_kg(5), 'kg')

