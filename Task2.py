print("Введите элементы списка. Для окончания ввода вместо очередного элемента сразу же нажмите <ENTER>.")
a = []
while True:
    s = input()
    if s == "":
        break
    else:
        a.append(s)
print("До перестановок: ")
for i in a:
    print(i, end=" ")
print()
for i in range(0, len(a) // 2):
    (a[2 * i], a[2 * i + 1]) = (a[2 * i + 1], a[2 * i])
print("После перестановок: ")
for i in a:
    print(i, end=" ")
