# + Создать класс TrafficLight(светофор).
# - определить у него один атрибут color(цвет) и метод  running(запуск);
# - атрибут реализовать как приватный;
# - в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# - продолжительность первого состояния(красный) составляет 7 секунд,
#   второго(жёлтый) — 2 секунды, третьего(зелёный) — на ваше усмотрение;
# - переключение между режимами должно осуществляться только в
# указанном порядке(красный, жёлтый, зелёный);
# - проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов. При его
# нарушении выводить соответствующее сообщение и завершать скрипт.
from itertools import cycle
import time


class TrafficLight:
    def __init__(self, start_color='red'):
        self.__color = start_color


    def running(self):
        print('running')
        trafficlight = ['red', 'yellow', 'green', 'yellow']
        traffic_time = {'red': 7, 'yellow': 2, 'green': 5}
        for color in cycle(trafficlight):
            print(time.strftime("%X"), color)
            time.sleep(traffic_time.get(color))


trafficlight = TrafficLight(input('input start color ( \'red\' or \'green\' ): ').lower())
trafficlight.running()
