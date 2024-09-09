
class Student():
    def __init__(self, name, rollno, age) -> None:
        self.name = name   # public
        self._rollno = rollno  # protected
        self.__age = age   # private
    def get_age(self):
            return self.__age
    def set_age(self, age):
        if age>35:              
            print("Invaled age given... Age shouild be kesss than 35.")
        else:
            self.__age = age
def display(self):
        print(f"Hi myself {self.name} {self._age} years old with rollno {self._rollno} from Student class")
def displayPrivateData(self):
        self.__display()
class Branch(Student):
    def show(self):
        print(f"My rollno is {self._rollno}")


s1 = Student("Rahul",24, 28)
# print(s1.name)
# s1.display()
# s1.name = "Kartik"
# print(s1.name)
# s1.display()
# print(s1._Student__age)

print(s1.get_age())
s1.set_age(34)
print(s1.get_age())