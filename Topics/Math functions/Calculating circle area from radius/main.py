# Import the math module to use the value of pi
import math

# Define a function to calculate the area of a circle
def calculate_circle_area(radius):
    # Your code here
    area = math.pi * radius ** 2
    # Return the calculated area rounded to 2 decimal places
    return round(area, 2)

# Read the radius as a float from input
user_radius = float(input())

# Call the function with the radius and print the result
print(calculate_circle_area(user_radius))