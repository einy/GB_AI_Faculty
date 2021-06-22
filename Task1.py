my_list = [3, 3.14, "строка", True, None, [5, 6, [7, 8]], tuple("строковая_константа"), set('множество'),
           dict(Имя='Иван', Фамилия='Петров')]
for i, a in enumerate(my_list):
    aname = str(type(a)).split("'")[1]
    print(f"{i}-й элемент списка имеет тип {aname} и значение {a} ")
    if aname in ("list", "tuple", "set", "dict"):
        print("Это элемент списочного типа -> выводим его элементы:")
        if aname == "dict":
            for key, value in a.items():
                print(f"    Ключ: {key}, значение: {value}")
        else:
            for j, b in enumerate(a):
                print(f"    Номер элемента: {j}, значение: {b} ")
