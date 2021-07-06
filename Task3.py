class Cell():
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return str(self.n)

    def make_order(self, k):
        temp = ""
        for i in range(self.n // k):
            temp += "*" * k + "\n"
        temp += "*" * (self.n % k) + "\n" if self.n % k != 0 else ""
        return temp

    def __add__(self, other):
        return Cell(self.n + other.n)

    def __sub__(self, other):
        if self.n - other.n > 0:
            return Cell(self.n - other.n)
        else:
            print("ОШИБКА: Невозможно произвести вычитание клеток.\n")

    def __mul__(self, other):
        return Cell(self.n * other.n)

    def __truediv__(self, other):
        return Cell(self.n // other.n)


c1 = Cell(14)
c2 = Cell(6)
c3 = c1 + c2
print(f"Результат сложения:\n{c3.make_order(5)}")
c41 = c1 - c2
print(f"Результат вычитания:\n{c41.make_order(5)}")
c42 = c2 - c1
# здесь - генерация сообщения об ошибке
c5 = c1 * c2
print(f"Результат умножения:\n{c5.make_order(5)}")
c6 = c1 / c2
print(f"Результат деления:\n{c6.make_order(5)}")
