with open('text_3.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    enum_obj = enumerate(lines)
    print("Оклады ниже 20 000 рублей имеют следующие сотрудники:")
    sum = 0
    for i, s in enum_obj:
        sal = float(s.split()[1])
        if sal < 20000:
            print(s.split()[0])
        sum += sal
    print(f"Средняя величина окладов сотрудников: {sum/(i+1)} руб.")
