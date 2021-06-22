def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def is_bool(str):
    try:
        bool(str)
        return True
    except ValueError:
        return False


def t(str):
    td = {'i': 'целый', 'f': 'вещественный', 's': 'строковый', 'b': 'логический'}
    return td[str]


def conv(s, t):
    if t == 'i':
        return int(s)
    elif t == 'f':
        return float(s)
    elif t == 'b':
        return bool(s)
    else:
        return s


a = []
print("Этап 1. Формирование списка параметров товара")
i = 1
params = []
while True:
    s = input(f"Введите название параметра №{i} или <ENTER> для прекращения ввода параметров: ")
    if s == "":
        break
    while True:
        s2 = input(f"Введите тип параметра №{i} (i - целый, f - вещественный, s - строка, b - логический): ")
        if s2 not in ("i","f","s","b"):
            print("Повторите ввод.")
        else:
            break
    while True:
        s3 = input(f"Учитывать ли только уникальные значения этого параметра в аналитике? (y/n): ")
        if s3 not in ("y","Y"):
            print("Повторите ввод.")
        else:
            break
    params.append({'name': s, 'type': s2, 'unique': s3 in ('Y', 'y')})
    i += 1
print("\nЭтап 2. Заполнение карточек товаров")
i = 1
while True:
    print(f"Товар №{i}:")
    temp = {}
    for p in params:
        while True:
            s = input(f"Введите значение параметра '{p['name']}' (тип: {t(p['type'])}) товара №{i}: ")
            if (p['type'] == 'i' and not is_int(s)) or (p['type'] == 'f' and not is_float(s)) or (
                    p['type'] == 'b' and not is_bool(s)):
                print("Ошибка типа. Повторите ввод.")
            else:
                break
        temp[p['name']] = conv(s, p['type'])
    a.append((i, temp))
    s = input("Ввести следующий товар (y/n)?: ")
    if not s in ('Y', 'y'):
        break
    i += 1
print("\nЭтап 3. Вывод аналитики")
b = {}
for p in params:
    temp = []
    for x in a:
        if not (p['unique'] and x[1][p['name']] in temp):
            temp.append(x[1][p['name']])
    b[p['name']] = temp
print(b)
