n = int(input("Введите целое положительное число: "))
dmax = 0
while (n > 0):
    d = n % 10
    if d > dmax:
        dmax = d
    n = n // 10
print(f"Набольшая цифра в этом числе: {dmax}")
