# square
my_list = [1,2,3]

print(list(map(lambda item : item ** 2, my_list)))

a = [(4,6), (-2,1), (8,1), (9,11)]

a.sort(key=lambda x : x[0])

print(a)
