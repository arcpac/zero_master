# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints:
# Consider use range(#begin, #end) method.

bucket = []
for number in range(2000, 3200):
    if (number % 7 == 0) and (number % 5 != 0):
        bucket.append(str(number))

print(', '.join(bucket))

