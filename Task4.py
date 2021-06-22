a = input("Введите строку: ").split()
for j, b in enumerate(a):
    print(f"Слово № {j+1}: '{b[:10]}'")
