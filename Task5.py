class Stationery:
    def __init__(self, t):
        self.title = t

    def draw(self):
        print("Это ДЕФОЛТНЫЙ метод отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Это метод отрисовки объекта PEN с наименованием \"{self.title}\"")


class Pencil(Stationery):
    def draw(self):
        print(f"Это метод отрисовки объекта PENCIL с наименованием \"{self.title}\"")


class Handle(Stationery):
    def draw(self):
        print(f"Это метод отрисовки объекта HANDLE с наименованием \"{self.title}\"")


pen1 = Pen("Ручка Parker")
pen1.draw()
pencil1 = Pencil("Карандаш Koh-i-Noor")
pencil1.draw()
handle1 = Handle("Маркер Bic")
handle1.draw()
