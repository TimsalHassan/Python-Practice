class Human:
    def __init__(self, name, age):
        print('Calling init from human class')
        self.name = name
        self.age = age
    def showDetails(self):
        print(f'name: {self.name}, age: {self.age}')
    def eat(self):
        print('I can eat')

class Male(Human):
    def __init__(self, m_name, m_age, location):
        print('Calling init from male class')
        Human.__init__(self, m_name, m_age)
        self.location = location
    def sleep(self):
        print('I can sleep')

class Female(Human):
    def __init__(self, name, age, can_dance):
        print('Calling init from female class')
        super().__init__(name, age)
        self.know_dance = can_dance
    def showDetails_F(self):
        Human.showDetails(self)
        print(f'Know Dancing: {self.know_dance}')
    def work(self):
        print('I can work')

female_1  = Female("Sara", 15, True)
female_1.showDetails_F()
print(female_1.age)
# male_1 = Male("Rahul", 34, "Delhi")
# # male_1.eat()
# print(Male.mro())
