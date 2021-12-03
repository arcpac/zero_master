# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


# while
# num = int(input("Enter number: "))
# fact = 1

# while num:
    
#     fact = num * fact
#     num = num - 1
# print(fact)

# function
def fact(input_num):
    if input_num == 0:
        return 1
    else:
        return input_num * fact(input_num - 1)

x = input("Enter number: ")

print(fact(int(x)))