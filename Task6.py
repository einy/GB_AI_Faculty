from itertools import count, cycle

print("Целые числа, начиная с 3, но не больше 10: ")
for i in count(3):
    if i > 10:
        break
    else:
        print(i)
print("Циклический вывод [1, 2, 3, 4, 5], но не больше 11 элементов: ")
my_list = [1, 2, 3, 4, 5]
count = 1
for i in cycle(my_list):
    if count > 11:
        break
    else:
        print(i)
        count += 1
