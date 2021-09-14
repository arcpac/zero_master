# Question:
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

# Suppose the following input is supplied to the program:

# Hello world
# Practice makes perfect
# Then, the output should be:

# HELLO WORLD
# PRACTICE MAKES PERFECT

def user_input():
    while True:
        value = input()
        
        if len(value) == 0:
            break
        yield value

        
for line in map(str.upper, user_input()):
    print(line)