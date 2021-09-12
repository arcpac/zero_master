simple_dict = {
    'a':2,
    'b':3
}

my_dict = {key:value**2 for key,value in simple_dict.items() if value%2==0}
my_dict1 = {num:num*2 for num in [1,2,3,4]}

some_list = ['a', 'b', 'd', 'c', 'a', 'c', 'e', 'f', 'g']

duplicates = []

# FOR LOOP
for x in some_list:
    if some_list.count(x) > 1:
        if x not in duplicates:
            duplicates.append(x)
# print(duplicates)

# COMPREHENSION
duplicates = list(set([num for num in some_list if some_list.count(num) > 1]))
print(duplicates)
