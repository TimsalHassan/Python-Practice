# class ComplexNumber:
#     def __init__(self,r,i) -> None:
#         self.real = r
#         self.imaginary = i
#     def __add__(self,other):
#         return f"{self.real+other.real} + {self.imaginary+other.imaginary}i"
      
# c1 = ComplexNumber(1,3)
# c2 = ComplexNumber(1,4)
# print(c1+c2)

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False
p1 = Person("Rahul", 34)
p2 = Person("Kartik", 45)
if p1>p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")

