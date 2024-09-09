class Human:
    def __init__(self, num_heart):
        print('Calling init from human class')
        self.eyes = 2
        self.heart = num_heart
    def eat(self):
        print('I can eat')
    def work(self):
        print('I can work')
class Male(Human):
    def __init__(self, name):
        print('Calling init from male class')
        self.name = name
    def sleep(self):
        print('I can sleep whole day')
class Boy(Male):
    def __init__(self, heart, name, can_dance):
        print('Calling int from boy class')
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.know_dancing = can_dance
    def work(self):
        # Human.work(self)
        super().work()
        print('I can code')
boy1 = Boy(1,'Rahul', True)
print(boy1.name)
print(boy1.know_dancing)
# print(Boy.mro())
