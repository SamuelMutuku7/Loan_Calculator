# place `import` statement at top of the program
import string

# don't modify this code or the variable may not be available
input_string = input()

# use capwords() here
def capitalize(sentence):
    return string.capwords(sentence)

print(capitalize(input_string))