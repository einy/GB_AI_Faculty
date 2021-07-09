class Data:
    def __init__(self, my_list):
        self.day, self.month, self.year = my_list

    @staticmethod
    def validate_dmy(obj):
        return obj.day in range(1, 32) and obj.month in [1, 3, 5, 7, 8, 10, 12] or obj.day in range(1,
                                                                                                    31) and obj.month in [
                   4, 6, 9, 11] or obj.day in [28, 29] and obj.month == 2

    @classmethod
    def set_dmy(cls, s):
        my_list = map(int, s.split('-'))
        return cls(my_list)


test = '31-02-2021'
data1 = Data.set_dmy(test)
print(f"Параметры даты {test} корректны" if Data.validate_dmy(data1) else f"Ошибка в параметрах даты {test}")
test = '28-02-2021'
data1 = Data.set_dmy(test)
print(f"Параметры даты {test} корректны" if Data.validate_dmy(data1) else f"Ошибка в параметрах даты {test}")
