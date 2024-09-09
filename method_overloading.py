# class Demo:
#     def add(self,*args):
#         total = 0
#         for i in args:
#             total = total + i
#         return total
# d = Demo()
# print(d.add(2,3))
# print(d.add(2,3,4))
# print(d.add(3,44,55,66,7))

# class Father:
#     def sleep(self):
#         print("Sleeps from 10:00 PM to 5:00 AM")
#     def eat(self):
#         print("eating")
# class Son(Father):
#     def sleep(self):
#         print("Sleeps from 2:00 PM to 10:00 AM")
# s = Son()
# s.sleep()



# Function decorator
# def mul(func):
#     """This function is a decrator and is used as a decorator to hide a function and can be used when called"""
#     def sum(x,y):
#         print(x+y)
#         func(x,y)
#     return sum

# @mul
# def multi(x,y):
#     print(x*y)
     
# multi(2,5)

# def sqr(x):
#     return x*x
# def fileter_func(a):
#     return a>3
# from functools import reduce
# def sum(x,y):
#     return x+y
# l = [2,4,3,5,6]
# newl = reduce(sum, l)
# # newl = []
# # for item in l:
# #     newl.append(sqr(item))
# print(newl)



marks = [23,45,98,45,34,65,67]
for index, mark in enumerate(marks):
    print(index, mark)
    if index == 3:
        print("Nice!")
# index = 0
# for mark in marks:
#     print(index, mark)
#     if index == 3:
#         print("Nice!")
#     index += 1