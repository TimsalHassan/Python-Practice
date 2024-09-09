class Duck:
    def swim(self):
        print("I am a Duck and I can swim")
    def speaks(self):
        print("Quack Quack")
class Cat:
    def swim(self):
        print("I am a Cat and I can swim")
    def speaks(self):
        print("Meow Meow")
class Person:
    def speaks(self):
        print("blah blah blah")
class Demo:
    def display(self, obj):
        obj.swim()
        obj.speaks()
        print("Information dispalyed")

d = Duck()
cat = Cat()
p = Person()
demo = Demo()
demo.display(d)
demo.display(cat)
demo.display(p)





