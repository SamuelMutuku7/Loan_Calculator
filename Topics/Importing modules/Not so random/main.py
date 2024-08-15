# place `import` statement at top of the program
import random

# put your code here
def pickie_ponkie(start, end):
    lucky = random.randint(start, end)
    return lucky

n = pickie_ponkie(-100, 101)