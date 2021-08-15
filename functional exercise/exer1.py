from functools import reduce

# --------------------------------------------------------------
#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize_item(item):
    return item.capitalize()

print("# 1")
print(list(map(capitalize_item, my_pets)))
# --------------------------------------------------------------
#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

my_numbers.sort()
print("# 2")
print(list(zip(my_strings, my_numbers)))

# --------------------------------------------------------------
#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def more_than_half(item):
    return item > 50

print("# 3")
print(list(filter(more_than_half, scores)))


# --------------------------------------------------------------
#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
print('# 4')
print(my_numbers + scores)
def add(x, item):
    return x + item
    
print(reduce(add, (my_numbers + scores)))
# print(reduce(add, scores))
