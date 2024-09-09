# class Human:
#     def __init__(self,num_heart) -> None:
#         print("calling init form human")
#         self.num_eyes = 2
#         self.num_nose = 1
#         self.num_heart = num_heart
#     def eat(self):
#         print('I can eat')
#     def work(self):
#         print('I can work')
# class Male():
#     def __init__(self,name) -> None:
#         print("calling init form male")
#         self.name = name
#     def speak(self):
#         print('Ican speak')
#     def work(self):
#         print('I can code')
# class Boy(Human, Male):
#     def __init__(self,name,heart, language) -> None:
#         Human.__init__(self,heart)
#         Male.__init__(self,name)
#         self.language = language
#     def sleep(self):
#         print("I can sleep")
#     def work(self):
#         print("I can test")
#     def display(self):
#         print(f'Hi, I am {self.name}. I have {self.num_heart} heart,{self.num_eyes} eyes and {self.num_nose} nose. I code in {self.language} language.')

# boy1 = Boy("Ali",1,'python')
# # boy1.work()
# # print(Boy.mro())
# # Male.work(boy1)
# print(boy1.num_eyes)
# print(boy1.num_heart)
# print(boy1.language)
# boy1.display()



def gen(x = 1000):
    yield x

print(list(gen()))