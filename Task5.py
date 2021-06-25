from functools import reduce


def product(x, y):
    return x * y


my_list = [i for i in range(100, 1001, 2)]
print(reduce(product, my_list))
