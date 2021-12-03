# Question:
# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use init method to construct some parameters


class myFunctions(object):
    def __init__(self):
        self.my_string = ""

    def input_str(self):
        self.my_string = input("Enter string: ")

    def output_str(self):
        print(self.my_string.upper())

function = myFunctions()
function.input_str()
function.output_str()