"""

def squence_num(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result


squared_list = squence_num([1,2,3,4,5])
print(squared_list)
"""

def squence_num(nums):
    for i in nums:
        yield(i*i)
    

##squared_list = squence_num([1,2,3,4,5])

"""
print(squared_list)
print(next(squared_list))
print(next(squared_list))
print(next(squared_list))
print(next(squared_list))
print(next(squared_list))
print(next(squared_list))
"""

## list comprehension
##squared_list = [x*x for x in [1,2,3,4,5]]

##  generator
squared_list = (x*x for x in [1,2,3,4,5])
for num in squared_list:
    print(num)
