import math

first_integer = int(input())
second_integer = int(input())

def calculate_logarithm(x, y):
    if y <= 0 or y == 1:
        return math.log(x)
    else:
        return math.log(x, y)

result = calculate_logarithm(first_integer, second_integer)
print(round(result, 2))
