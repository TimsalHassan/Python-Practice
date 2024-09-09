class Human:
    def __init__(self, num_heart) -> None:
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart
    def eat(self):
        print('Ican eat')
    def work(self):
        print('Ican work')
class Male(Human):
    def __init__(self, name, heart) -> None:
        super().__init__(heart)
        self.name = name
    def walk(self):
        print('I can Walk')
    def work(self):
        super().work()
        print('I can code')
    def display(self):
        print(f'Hi, I am {self.name} and I have {self.num_heart} heart.')


male1 = Male('Hassan', 1)
# male1.walk()
# male1.work()
print(male1.num_eyes)
print(male1.name)
print(male1.num_heart)
male1.display()