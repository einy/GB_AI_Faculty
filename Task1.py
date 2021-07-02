from itertools import cycle
from time import sleep
from os import system, name

ClearScreen = lambda: system('cls' if name == 'nt' else 'clear')


# включить опцию Emulate terminal in output console option в конфигурации скрипта в PyCharm


class TrafficLight:
    lights = [["RED", 7], ["YELLOW", 2], ["GREEN", 5]]

    def Running(self):
        for el in cycle(self.lights):
            __color = el[0]
            print(__color)
            sleep(el[1])
            ClearScreen()


TL_Sample = TrafficLight()
TL_Sample.Running()
