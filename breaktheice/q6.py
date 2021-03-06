# Question:
# Write a program that calculates and prints the value according to the given formula:

# Q = Square root of [(2 _ C _ D)/H]
# (2*C*D)/H
# Following are the fixed values of C and H:

# C is 50. H is 30.

# D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:

# 100,150,180
# The output of the program should be:

# 18,22,24

from math import sqrt

values = input("Enter values: ").split(",")

def calculate(value):
    c = 50
    h = 30
    result = sqrt((2*c*value)/h)
    return result

result = [calculate(int(value)) for value in values]
result = [round(value) for value in result]
print(result)

