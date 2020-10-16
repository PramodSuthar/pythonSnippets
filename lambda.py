

### lambda is like an anonymous function that has no name

def square(n):
    return n * n


nums = [1,2,3,4,5]

print(list(map(square, nums)))

## lambda lambda_agrs_lis: expression

print(list(map(lambda n: n*n, nums)))


result = lambda x,y: x+y
print("Result is ", result(30,40))
