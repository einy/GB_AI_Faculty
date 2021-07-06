from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @property
    def quantity(self):
        pass

    def __add__(self, other):
        return self.quantity + other.quantity


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def v(self):
        return self.__v

    @v.setter  # используется для проверки/коррекции, вызывается автоматически, когда методу(в виде свойства) присваивается значение
    def v(self, v):
        self.__v = v

    @property
    def quantity(self):
        return self.__v / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def h(self):
        return self.__h

    @h.setter  # используется для проверки/коррекции, вызывается автоматически, когда методу(в виде свойства) присваивается значение
    def h(self, h):
        self.__h = h

    @property
    def quantity(self):
        return 2 * self.h / 100 + 0.3


coat1 = Coat(48)
cost1 = Costume(176)
print(f"Всего расход ткани: {coat1 + cost1}")
