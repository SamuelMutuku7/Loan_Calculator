first_number = float(input())
second_number = float(input())

def find_quadrant(x_axis, y_axis):
    if x_axis == 0 and y_axis == 0:
        return "It's the origin!"
    elif (x_axis == 0 and y_axis != 0) or (x_axis != 0 and y_axis == 0):
        return "One of the coordinates is equal to zero!"
    elif x_axis > 0 and y_axis > 0:
        return "I"
    elif x_axis < 0 < y_axis:
        return "II"
    elif x_axis < 0 and y_axis < 0:
        return "III"
    else:
        return "IV"

print(find_quadrant(first_number, second_number))
