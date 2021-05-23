import time


class TrafficLight:
    def __init__(self):
        self._color = 'красный'

    def runninng(self):
        print('Светофор начал свою работу')
        print(f'Загорелся {self._color} свет')
        time.sleep(7)
        self._color = 'желтый'
        print(f'Загорелся {self._color} свет')
        time.sleep(2)
        self._color = 'зелёный'
        print(f'Загорелся {self._color} свет')
        time.sleep(4)
        return 'Работа светофора закончена'


if __name__ == "__main__":
    first_light = TrafficLight()
    print(first_light.runninng())
    print(first_light._color)
