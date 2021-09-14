# Question:
# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use init method to construct some parameters

class str_grabber():
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter string: ")

    def setUpperCase(self):
        x = self.string.upper()
        print(x)

x = str_grabber()
obj = x.getString()
obj = x.setUpperCase()
