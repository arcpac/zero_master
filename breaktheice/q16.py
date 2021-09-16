# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:

# 1,2,3,4,5,6,7,8,9

# Then, the output should be:
# 1,9,25,49,81

# seq = input().split(",")

# for x in seq:
#     if x.isnumeric():
#         x = int(x)
#         if x % 2 == 1:
#             print(x**2)
#     else:
#         print("Alphabet are not allowed idiot!")
#         break

mylist = [str(int(i)**2) for i in input().split(',') if int(i) % 2]

print(", ".join(mylist))