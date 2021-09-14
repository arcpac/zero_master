# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
while True:
    try:
        digit = int(input("Enter digit: "))
        d = dict()
    except ValueError:
        print("Enter a number!")
        continue
    
    for i in range(1, digit + 1):
        d[i] = i * i
    print(d)
