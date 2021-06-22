def my_func(x1, x2, x3):
    temp = [x1, x2, x3]
    temp.remove(min(temp))
    return sum(temp)


print(my_func(2, 2, 2))
