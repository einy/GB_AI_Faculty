class DivByZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


num = input("Enter a number to divide 1 to: ")
try:
    num = int(num)
    if num == 0:
        raise DivByZeroError("ERROR: You cannot divide by zero!")
    result = 1 / num
except (ZeroDivisionError, DivByZeroError) as err:
    print(err)
else:
    print(result)
