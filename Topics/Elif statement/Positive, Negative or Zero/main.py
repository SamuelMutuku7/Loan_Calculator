user_integer = int(input())

def polarity(number):
    if number < 0:
        return "negative"
    elif number > 0:
        return "positive"
    else:
        return "zero"

print(polarity(user_integer))

