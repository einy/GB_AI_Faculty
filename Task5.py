my_list = [7, 5, 3, 3, 2]
print(f"Исходный список: {my_list}")
x = int(input("Введите целое число для вставки в список: "))
if x <= my_list[len(my_list) - 1]:
    my_list.append(x)
else:
    for i, a in enumerate(my_list):
        if x > a:
            break
    my_list = my_list[:i] + [x] + my_list[i:]
print(f"Список после вставки: {my_list}")
