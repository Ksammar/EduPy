# + Реализуйте базовый класс Car.
#
# - у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).А
#   также методы: go, stop, turn(direction), которые должны сообщать, что
#   машина поехала, остановилась, повернула(куда);
# - опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# - добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# - для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60(TownCar)
# и 40(WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат.Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed=0, color='white', name='car'):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        # self.speed = 10
        print(self.name, 'go,', 'his speed', self.speed)

    def stop(self):
        self.speed = 0
        print(self.name, 'stop,', 'his speed', self.speed)

    def fast_quickly(self):
        self.speed += 50
        print(self.name, 'speed up,', 'his speed', self.speed)

    def quickly(self):
        self.speed += 10
        print(self.name, ' speed up,', 'his speed', self.speed)

    def fast_slower(self):
        self.speed -= 50
        print(self.name, ' speed down,', 'his speed', self.speed)

    def slower(self):
        self.speed -= 10
        print(self.name, ' speed down,', 'his speed', self.speed)

    def turn(self, direction):
        print(self.name, ' go to ', direction)

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(self.name, 'Overspeed, slow down!')
        else:
            print(self.name, 'your speed is OK')
        return self.speed


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(self.name, 'Overspeed, slow down!')
        else:
            print(self.name, 'your speed is OK')
        return self.speed


class PoliceCar(Car):
    pass
    # def __init__(self):
    #     self.is_police = True


auto1 = TownCar(45, 'green', 'forester')
auto2 = WorkCar(33, 'yellow', 'snow_plow')
auto1.show_speed()
auto2.show_speed()
auto1.go()
auto2.go()
auto1.turn('left')
auto1.fast_quickly()
auto1.quickly()
auto1.show_speed()

auto2.turn('left')
auto2.fast_quickly()
auto2.turn('forward')
auto2.show_speed()

auto1.fast_slower()
auto1.show_speed()
auto2.slower()
auto2.show_speed()
auto2.fast_slower()
auto2.show_speed()
auto1.stop()
auto2.stop()
auto1.show_speed()
auto2.show_speed()
