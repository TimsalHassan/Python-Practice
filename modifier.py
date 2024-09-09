class Student:
    def __init__(self, name, rollno, age) -> None:
        self.name = name   # public    no underscore
        self._rollno = rollno  # protected     _  single underscore
        self.__age = age   # private    __  double underscore
    def display(self):
        print(f"Hi myself {self.name} with rollno {self._rollno} from Student class")
class Branch(Student):
    pass
# def showData():
#     b1 = Branch("Ali", 22)
#     print(b1.name)

# # showData()
# s1 = Student("Rahul",24, 28)
# print(s1.name)
# s1.display()
# s1.name = "Kartik"
# print(s1.name)
# s1.display()
# print(s1._Student__age)

 