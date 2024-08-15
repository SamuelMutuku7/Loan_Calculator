first_integer = int(input())
second_integer = int(input())


def possible_moves(column, row):
    count = 0
    if (column, row) == (1, 8) or (column, row) == (8, 1) or (column, row) == (1, 1) or (column, row) == (8, 8):
        count += 3
    elif 2 <= column <= 7 and 2 <= row <= 7:
        count += 8
    else:
        count += 5
    return count

print(possible_moves(first_integer, second_integer))