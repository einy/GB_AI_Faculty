def my_func(x, y):
    try:
        xx = float(x)
        yy = int(y)
    except ValueError:
        return "ОШИБКА. Ошибка преобразования типов"
    if xx <= 0:
        return "ОШИБКА. Основание должно быть положительным!"
    if yy >= 0:
        return "ОШИБКА. Степень должна быть целой и отрицательной!"
    temp = 1
    for i in range(-yy):
        temp = temp * xx
    return 1 / temp


x = input("Введите основание: ")
y = input("Введите целую отрицательную степень: ")
print(f"Результат возведения в степень: {my_func(x,y)}")
