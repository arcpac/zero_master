# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:

numbers = input().split(",")
converted_numbers = []

for number in numbers:
    try:
        converted_numbers.append(int(number))
    except ValueError:
        print("Strings were not converted")
        break
    
print(f'Result: {converted_numbers}')