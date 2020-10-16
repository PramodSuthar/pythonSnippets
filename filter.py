

grades = ['A', 'B', 'F', 'C', 'F', 'A']

## 1- For Loop
filteredGrades = []

for grade in grades:
    if grade != 'F':
        filteredGrades.append(grade)


print(grades)
print(filteredGrades)


## 2- Comprehension method
print([grade for grade in grades if grade != 'F' ])


## 3- Filter method filter(function, iterable)
def removeF(grade):
    return grade != 'F'


result = filter(removeF, grades)
print(list(result))
