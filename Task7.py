def factorial(x):
    prod = 1
    i = 1
    while i <= x:
        yield prod
        i = i + 1
        prod = prod * i


print("Факториалы чисел от 1 до 5:")
for i in factorial(5):
    print(i)
