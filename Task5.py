from random import randint

with open('text_5.txt', 'w', encoding='utf-8') as f:
    checksum = 0
    for _ in range(1000):
        x = randint(0, 100)
        f.write(str(x) + " ")
        checksum += x
    print(f"Сумма числе в файле (при формировании файла): {checksum}")
with open('text_5.txt', 'r', encoding='utf-8') as f:
    ls = (f.readlines()[0]).split()
    print(f"Сумма числе в файле (при чтении из файла): {sum(map(int,ls))}")
