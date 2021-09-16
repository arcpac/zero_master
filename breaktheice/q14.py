# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# Suppose the following input is supplied to the program:

# Hello world!
# Then, the output should be:

# UPPER CASE 1
# LOWER CASE 9

sentence = input()

tally = {"upper":0, "lower": 0}

for x in sentence:
    if x.isupper():
        tally["upper"] += 1
    elif x.islower():
        tally["lower"] += 1
    else:
        pass

print("Upper:", tally["upper"])
print("Lower:", tally["lower"])