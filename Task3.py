class Worker:
    def __init__(self, n, s, p, w, b):
        dic = {"wage": w, "bonus": b}
        self.name = n
        self.surname = s
        self.position = p
        self._income = dic


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


P_Sample = Position("John", "Doe", "CEO", 300000, 100000)
print(
    f"Full name: {P_Sample.get_full_name()}\nPosition: {P_Sample.position}\nTotal income: {P_Sample.get_total_income()}")
