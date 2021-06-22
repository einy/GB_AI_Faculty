def divide(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        return "ОШИБКА. Второе число не должно быть нулем!"
    return c

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(f"Результат деления первого числа на второе: {divide(a,b)}")
