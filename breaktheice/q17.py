# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:

# D 300
# D 300
# W 200
# D 100
# Then, the output should be:

# 500

from fractions import Fraction

sugar = Fraction('2.5')
scale = Fraction(5/8)

result = sugar * scale
print(Fraction(result))
print(Fraction(25/16))