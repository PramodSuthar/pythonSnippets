

"""
The main File fro student Class
"""
from pkts.student import Student


st1 = Student("Marc", "Markos", 1, 1990)
st2 = Student("Lilio", "Maria", 0, 1993)
st3 = Student("David", "Minor", 1, 1995)

st1.displayInfo()
print("***********************")
st2.displayInfo()

print(st1 == st2)
