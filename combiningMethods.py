

### fliter with map

c = map(lambda x: x+x, filter(lambda x:(x>= 4), [2,3,4,5,6]))
print(tuple(c))


d = filter(lambda x:(x>= 4),map(lambda x: x+x, [2,3,4,5,6]))
print(set(d))


### fliter and map with reduce

from functools import reduce

r = reduce(lambda x,y: x+y,map(lambda x: x+x,filter(lambda x:(x>= 4),[2,3,4,5,6,7])))
print(r)
