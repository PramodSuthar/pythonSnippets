


#### ================== Overloading Operator

class Vector:

    def __init__(self, a , b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Vactor: {(self.a, self.b)}"

    def __add__(self, other):
        return Vector(self.a + other.a,self.b + other.b)


v1 = Vector(2,10)
v2 = Vector(20,100)

print(v1)
print(v2)
print(v1 + v2)
