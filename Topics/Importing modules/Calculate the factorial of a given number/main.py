# Import the required module
import math

# Input the number
n = int(input())

# Use the factorial function from the math module to calculate the factorial
def calculate_factorial(number):
    return math.factorial(number)

print(calculate_factorial(n))