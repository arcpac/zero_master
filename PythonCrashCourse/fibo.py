def fibo(number):
    a = 0
    b = 1
    items = []
    for i in range(number):
        items.append(a)
        temp = a # 0, 1, 1, 2
        a = b # 1, 1, 2, 3
        b = temp + b # 1, 2, 3
    return items

def fibo2(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a # 0, 1, 1, 2
        a = b # 1, 1, 2, 3
        b = temp + b # 1, 2, 3

# for x in fibo2(10):
#     print(x)

from time import time
    
my_list = [x for x in range(1,1000)]

def test():
    l=[]
    for i in range(2000, 3201):
        if (i%7==0) and (i%5!=0):
            l.append(str(i))

    print(','.join(l))
  
test()