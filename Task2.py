class Road:
    def __init__(self, l, w):
        self._length = l
        self._width = w
        self._sqm = 25
        self._thickness = 5

    def Calculate(self):
        return self._length * self._width * self._sqm * self._thickness


Road_Sample = Road(20, 5000)
print(Road_Sample.Calculate())
