def int_func(s):
    return s.capitalize()


s = input("Введите строку: ").split()
for i in range(len(s)):
    print(int_func(s[i]), end="")
    if i != len(s):
        print(" ", end="")
