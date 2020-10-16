

### pass by Value: all immutable obj are passed by value
def changeVal(x):
    x += 100



n = 10
print(n)
changeVal(n)
print(n)


### Pass by reference: all mutable obj are passed by reference
print("Example 1")
def changeList_1(l):
    l.append(50)

myList_1 = [10,20,30,40]
print(myList_1)
changeList_1(myList_1)
print(myList_1)

print("Example 2")
def changeList_2(l):
    l = []
    l.append(50)
    print(l)

myList_2 = [10,20,30,40]
print(myList_2)
changeList_2(myList_2)
print(myList_2)
