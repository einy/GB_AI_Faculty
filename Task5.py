def supersum():
    global sum
    s = input("Введите числа, разделенные пробелом. Спецсимвол, заканчивающий суммирование - '!': ").split()
    i = 0
    while (i < len(s)) and (s[i] != "!"):
        sum += int(s[i])
        i += 1
    print(f"Текущая сумма: {sum}")
    return i == len(s)


sum = 0
while supersum():
    pass
