class Car:
    dirs = ["West", "North", "East", "South", "West", "North"]

    def __init__(self, c, n, d):
        self.speed = 0
        self.color = c
        self.name = n
        self.isPolice = False
        self.direction = d

    def show_speed(self):
        sss = str(self.speed)
        return sss

    def go(self, s):
        self.speed = s

    def stop(self):
        self.speed = 0

    def turn(self, d):
        pos = self.dirs.index(self.direction, 1, len(self.dirs) - 2)
        offset = 1 if d == "Right" else -1
        sss = self.dirs[pos + offset]
        self.direction = sss


class TownCar(Car):
    def show_speed(self):
        sss = str(self.speed) + (". Overspeeding detected!" if self.speed > 60 else "")
        return sss


class WorkCar(Car):
    def show_speed(self):
        sss = str(self.speed) + (". Overspeeding detected!" if self.speed > 40 else "")
        return sss


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, d2):
        super().__init__(d=d2, c="White & Blue", n="Ford Mondeo")
        self.isPolice = True


def show_info(obj):
    print(
        f"{obj.color} car {obj.name} (class: {obj.__class__.__name__}) goes {obj.direction} with the speed {obj.show_speed()}")


tc1 = TownCar("Red", "KIA Rio", "North")
show_info(tc1)
sc1 = SportCar("White", "Jaguar XJ 220", "East")
show_info(sc1)
wc1 = WorkCar("Blue", "Ford Transit", "South")
show_info(wc1)
pc1 = PoliceCar("North")
show_info(pc1)
tc1.go(10)
show_info(tc1)
tc1.turn("Right")
show_info(tc1)
tc1.turn("Left")
show_info(tc1)
tc1.stop()
show_info(tc1)
wc1.go(100)
show_info(wc1)
