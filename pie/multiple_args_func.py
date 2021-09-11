def mean(*args):
    return sum(args) / len(args)

print(mean(1,2,3,4,5))

# capitalize all letters in the string using upper()
def foo(*args):
   result = [arg.upper() for arg in args]
   result = sorted(result)
   return result
        
print(foo('args', 'args2', 'aaa'))

# key and value parameters
def foo(**args):
   return args
        
print(foo(a='args', b='args2', c='aaa'))
