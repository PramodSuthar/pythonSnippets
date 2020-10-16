


### first Example
print("******** first Example")
grades = [95.5, 98.5, 86, 79, 65]

modifiedGrades = []

for grade in grades:
    modifiedGrades.append(grade + 1.5)



print(grades)
print(modifiedGrades)


modifyGrades = [grade + 2.5 for grade in grades]

print(modifyGrades)


### second Example
print("******** second Example")
nums = [1,2,3,4,5,6,7,8,9,10]
squerdEvenNumbers = []

for num in nums:
    if(num ** 2)%2 == 0:
        squerdEvenNumbers.append(num ** 2)


print(nums)
print(squerdEvenNumbers)


seqEvenNums = [num ** 2 for num in nums if(num ** 2)%2 == 0]
print(seqEvenNums)








