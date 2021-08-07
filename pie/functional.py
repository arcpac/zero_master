# Zip map, reduce and filter = FUNCTIONAL
my_list = [1,2,3,4]
your_list = (10,11,12)
their_list = (6,7,1)

def mult_by2(item):
    return item*2

def check_odd(item):
    return item % 2 != 0

print(list(map(mult_by2, my_list)))
print(list(filter(check_odd, my_list)))
print(list(zip(my_list, your_list)))
print(list(zip(my_list, your_list, their_list)))