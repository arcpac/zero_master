def my_decorator(func):

    def wrap_func(*args, **kwargs):
        print('-------')
        func(*args, **kwargs)
    return wrap_func
    

@my_decorator
def hello(greeting, emoji=':(', address="sdfsd"):
    print(greeting, emoji, address)

name = input("Enter greeting: ")
emoji = input("Enter emoji: ")
hello(name, emoji)


# numbers = [1,42,36,6,7,1,89,3,56,8,2,2,3,71,3]
# duplicates = []

# # print(numbers.count(1))

# for number in numbers:
#    if numbers.count(number) > 1:
#        if number not in duplicates:
#            duplicates.append(number)

# print(duplicates)