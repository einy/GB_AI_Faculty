from sys import argv

if len(argv) != 4:
    print("ОШИБКА. Ожидается 3 аргумента командной строки!")
    exit(255)
try:
    (x, y, z) = map(float, [argv[1], argv[2], argv[3]])
except:
    print("ОШИБКА. Данные должны быть вещественными числами!")
    exit(255)
print(f"Результат расчета: {x*y+z}")
