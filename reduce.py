

from functools import reduce

### reduce(function, iterable)
def myFunc(x,y):
    return x+y

def yourFunc(x,y):
    return x*y


myList = [1,2,3,4,5,6,7,8]

print(reduce(myFunc, myList))
print(reduce(yourFunc, myList))
