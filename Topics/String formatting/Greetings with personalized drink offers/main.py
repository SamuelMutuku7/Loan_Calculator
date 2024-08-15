# Python code to greet a friend in a unique way
import string

# Function to create a greeting for a friend
def create_greeting(friend_name, favorite_drink):
    # Write your code here to format the string.
    friend_name = string.capwords(friend_name)
    favorite_drink = string.capwords(favorite_drink)
    return f"Hello {friend_name}, I hope you are having a wonderful day! Would you like a glass of {favorite_drink}?"
    # Make sure to capitalize the first letter of both 'friend_name' and 'favorite_drink'. 

# Taking user's input
name_input = input()
drink_input = input()

# Call function and print the greeting
print(create_greeting(name_input, drink_input))