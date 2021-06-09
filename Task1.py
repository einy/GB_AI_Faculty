#ver2
while True:
    s = input("Введите целое число: ")
    if s.isdigit() or s[0]=="-" and s[1:].isdigit():
        break
    print("Это было не целое число! Попробуйте снова.")

while True:
    s = input("Введите вещественное число: ")
    try:
        float(s)
        print("Это было вещественное число, спасибо!")
        break
    except ValueError:
        print("Это было не вещественное число! Попробуйте снова.")