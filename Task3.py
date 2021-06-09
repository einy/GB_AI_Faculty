import math

n = int(input("Введите число n: "))
num_of_digits = math.ceil(math.log10(n))
n2 = n + n * 10 ** num_of_digits
n3 = n2 + n * 10 ** (2 * num_of_digits)
print(f"Результат: {n+n2+n3}")
