# Make sure your output matches the assignment *exactly*
user_time = int(input())

def screen_time(hours):
    if hours < 2:
        return "That's rare nowadays!"
    elif 2 <= hours < 4:
        return "This seems reasonable"
    else:
        return "Don't forget to take breaks!"

print(screen_time(user_time))