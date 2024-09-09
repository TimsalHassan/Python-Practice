# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for i in self.marks:
#             sum += i
#         print("Hi,", self.name, "your avg marks are : ", sum/3)

# s1 = Student("Ali Hassan",[98, 100, 78])
# s1.get_avg()

# class Account:

#     def __init__(self, bal, acc)-> None:
#         self.balance = bal
#         self.account_no = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print(f"Rs. {amount} was debited")
#         print("Total balance ", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print(f"Rs. {amount} was credited")
#         print("Total balance ", self.get_balance())

#     def get_balance(self):
#         return self.balance

# acc1 = Account(10000,12345)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(40000)
# acc1.debit(10000)

# # 
# class Student:
#     def __init__(self, phy, che, maths) -> None:
#         self.phy = phy
#         self.che = che
#         self.maths = maths
#         self.percentage = str((self.phy + self.che + self.maths) /3) + " %"

# s1 = Student(98,87,78)
# print(s1.percentage)



# def groupAnagrams(strs):
#     anagrams = {}
    
#     for word in strs:
#         # Sort the word to form the key
#         sorted_word = ''.join(sorted(word))
#         # Add the word to the corresponding anagram group
#         if sorted_word in anagrams:
#             anagrams[sorted_word].append(word)
#         else:
#             anagrams[sorted_word] = [word]
    
#     # Return the grouped anagrams
#     # return list(anagrams.values())
#     # return anagrams.values()
#     return anagrams

# # Example usage
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(groupAnagrams(strs))





# class  Instructor:
#     def __init__(self,name,address) -> None:
#         self.name = name
#         self.address = address
#         print('Hello')
#     def display(self):
#         print(f'My name is {self.name} and I am from {self.address}')


# instructor_1 = Instructor("Ali","Pakistan")
# instructor_1.display()
# # print(instructor_1)


class Circle:
    pi = 3.14
    def __init__(self,radius) -> None:
        self.radius = radius

    def get_circumference(self):
        return 2 * self.pi * self.radius
    
circe1= Circle(14)
print(circe1.get_circumference())