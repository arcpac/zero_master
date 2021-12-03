# Question:
# Write a program that calculates and prints the value according to the given formula:

# Q = Square root of [(2 _ C _ D)/H]

# Following are the fixed values of C and H:

# C is 50. H is 30.

# D is the variable whose values should be input to your program in a comma-separated sequence.
# For example Let us assume the following comma separated input sequence is given to the program:

# 100,150,180
# The output of the program should be:

# 18,22,24
import math

class myFunc(object):
    def __init__(self):
        self.numbers =[]
        self.my_list = []

    def formula(x):
        c = 50
        h = 30
        result = str(round(math.sqrt((2 * c * x)/h)))
        return result

    def input_nums(self):
        self.numbers = input("Enter numbers: ").split(",")

    def append_to_list(self):
        [self.my_list.append(int(x)) for x in self.numbers]

    def process(self):
        results = [myFunc.formula(x) for x in self.my_list]
        print(", ".join(results))

f = myFunc()
f.input_nums()
f.append_to_list()
f.process()
