

##================= Hidding Data

class MyClass:

    ## class level attributes
    __privateAtt = 10 #Private Attribiute of My Class
    _protectedAtt = 200 #Protected Attribiute of My Class
    publicAtt = 100

    ## public instance level method
    def add(self, increment):
        self.__privateAtt += increment
        self._protectedAtt += increment
        print(self.__privateAtt)
        print(self._protectedAtt)

    def __privateMethod(self):
        print("This is from private method")



class youClass(MyClass):


    def yourMethod(self):
        print(self._protectedAtt)


myObj = MyClass()

myObj_1 = MyClass()
## print(myObj.__privateAtt) This throws an error because __privateAtt is private member
print(myObj.publicAtt)

print(id(myObj._protectedAtt))
print(id(MyClass._protectedAtt))

myObj.add(20)

## myObj.__privateMethod() This throws an error because __privateMethod is private member

"""
print(myObj._protectedAtt)
print(MyClass._protectedAtt)
print(myObj_1._protectedAtt)

print(id(myObj._protectedAtt))
print(id(MyClass._protectedAtt))
print(id(myObj_1._protectedAtt))
"""

## access private member outside of our class
print(myObj._MyClass__privateAtt)
print(MyClass._MyClass__privateAtt)
myObj._MyClass__privateMethod()










