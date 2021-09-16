# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.

# Suppose the following input is supplied to the program:

# hello world! 123
# Then, the output should be:

# LETTERS 10
# DIGITS 3

sentence = input()
tally = {"letters": 0, "digits": 0}

for i in sentence:
    if i.isnumeric(): 
        tally["digits"] += 1
    else:
        tally["letters"] += 1

items = tally.items()

for tal in items:
    print(tal)

    # if 'a' <= i and 'z' >= i and 'A' <= i and 'Z' >= i:
    #     print("Hola")
    #     letters += 1
    # else:
    #     print("Oh NO OPH NO NONONONO")
    #     letters += 1
