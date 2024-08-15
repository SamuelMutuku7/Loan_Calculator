# Read two integers from the user input
a = int(input())
b = int(input())
numbers = []
divisible_by_3 = []

for i in range(a, b + 1):
    numbers.append(i)
    if i % 3 == 0:
        divisible_by_3.append(i)

average = sum(divisible_by_3) / len(divisible_by_3)
print(average)

