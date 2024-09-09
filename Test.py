# Problem no. 1 :-

# def print_digit(n):
#     while n > 0:
#         digit = n % 10
#         print(digit)
#         n = n // 10
# print_digit(1011)

# Alternate :

# n = int(input("Enter the number: "))
# while n > 0:
#     num = n % 10
#     print(num)
#     n = n // 10

    
# Problem no. 2 :-

# user_input = [ "bcdef", "abcdefg", "bcde", "bcdef"]
# word = {}
# for n in user_input:
#     if n in word:
#         word[n] += 1
#     else:
#         word[n] = 1
# print(len(word.values()))
# print(list(word.values()))


# Problem no. 3 :-

# input_number = int(input("Enter the number: "))
# for num in range(1, input_number):
#     print(str(num)*num)


# Problem no. 4 :-

# sum = input("Enter the number: ")
# count = 1
# for i in range(1,len(sum)):
#     if sum[i] == sum[i-1]:
#         count += 1
#     else:
#         print((count,int(sum[i-1])),end=" ")
#         count = 1
# print((count,int(sum[-1])))


# Problem no. 6 :-

# a = [1,7,-4,12]
# s = 0
# for i in range(0,len(a)):
#     while a[i]>0:
#         s +=a [i]
#         break
# print("the sum is : ",s)

# Problem no. 7 :-

# a = [5,3,4,23,54]
# a.remove(max(a))
# a.remove(min(a))
# s = sum(a)
# print(s)

# Problem no. 8 :-

# def calculate_points(matches):
#     total_points = 0
#     for match in matches:
#         x, y = map(int, match.split(':'))
#         if x > y:
#             total_points += 3
#         elif x == y:
#             total_points += 1
#         elif x < y:
#             total_points += 0
#     return total_points
# matches = ["2:1", "1:3", "4:4", "3:0", "2:2"]
# points = calculate_points(matches)
# print("Total points:", points)

# def cube (x):
#     return x*x*x

# l = [1,2,3,4, 6,4]
# newl = list(map(cube,l))
# print(newl)

# Problem no. 9 :-

# user_input = input("Enter the sentence: ")
# rev = []
# new = user_input.split()
# for n in new:
#     rev.append(n[::-1])
# s = " ".join(rev)
# print(s) 


# Problem no. 10 :-

# word = input("Enter the word: ")
# if len(word) % 2 !=0:
#     print("Middle letter is: ", word[int(len(word)/2)])
# else:
#     print("Middle letters are: ", word[int(len(word)/2)-1],word[int(len(word)/2)])
# Problem no. 11 :-

# strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]
# k = int(input("Enter k : "))
# s = list()
# for n in range(len(strarr) - k+1):
#     r = ''.join(strarr[n:n+k])
#     # print(r)
#     s.append(r)
#     n += 1
# # print (s)
# I = []
# for i in range(len(s)):
#     print(len(s[i]), end = "")
#     I.append(len(s[i]))
# print(max(I),I.index(max(I)))
# max_val_idx = I.index(max(I))
# print(s[max_val_idx])

# Problem no. 12 :-

# sen  = ("is2 Thi1s T4est 3a")
# def sort_string(s):
#     words = s.split()
#     sorted_words = ['' for _ in range(len(words))]
#     for word in words:
#         for char in word:
#             if char.isdigit():
#                 sorted_words[int(char) - 1] = word
#                 break
#     return ' '.join(sorted_words)
# print("The sorted string is: ",sort_string(sen))


# Problem no. 13 :-

# options=["rock","paper","scissor"]
# import random
# c=random.choice(options)
# i=input("Enter ROCK, PAPER or SCISSOR: ")
# print("you:" ,i)
# print("computer:",c)
# if i==c:
#     print('Its a tie')
# elif i=="rock" and c=="paper":
#     print("You lose")
# elif i=="rock" and c=="scissor":
#     print("You won")
# elif i=="paper" and c=="rock":
#     print("You won")
# elif i=="paper" and c=="scissor":
#     print("You lose")
# elif i=="scissor" and c=="rock":
#     print("You lose")
# elif i=="scissor" and c=="paper":
#     print("YOU WON")


# Problem no. 14 :-

# letters = input("Enter the letters: ")
# letter = set(letters)
# new = sorted(letter)
# n = new
# print(n)


# Problem no. 15 :-

# pin = input("Enter the pin: ")
# if (len(pin) == 4 or len(pin) == 6):
#     print("Valid Pin")
# else:
#     print("Invalid Pin")


# Problem no. 16 :-

# s = "camelCasing"
# sp = ""
# for i in s:
#     if i.isupper():
#         sp = sp +" " + i
#     else:
#         sp = sp + i
# print(sp)


# Problem no. 17 :-

# number = input("Enter the number: ")
# p = int(input("Enter power: "))
# power = p
# total = 0
# for i in range(len(number)):
#     total = total + int(number[i]) ** power
#     power += 1
# print("Total: ", total)
# new=total // int(number)
# print(f"Total / number = {total} / {number} = {new}")

# Problem no. 18 :-

# def is_valid_parentheses(s):
#     count = 0
#     for char in s:
#         if char == '(':
#             count += 1
#         else:
#             count -= 1
#     if count == 0:
#         print("true")
#     else:
#         print("false")
# parantheses=input("enter parantheses: ")
# is_valid_parentheses(parantheses)


# Problem no. 19 :-

# def String_fight(fight):
#     left_side = {'w':4,'p':3,'b':2,'s':1,'t':0}
#     right_side = {'m':4,'q':3,'d':2,'z':1,'j':0}
#     left_Side_result = 0
#     right_side_result = 0
#     for char in fight :
#         if char in left_side:
#             left_Side_result += left_side.get(char)
#         elif char in right_side:
#             right_side_result += right_side.get(char)
#         else:
#             print("wrong input :|")
#     if left_Side_result > right_side_result:
#         print("Left side win :)")
#     elif right_side_result > left_Side_result:
#         print("Right side win :)")
#     elif right_side_result == left_Side_result:
#         print("It's a tie!!!!")
#     else:
#         print("Let's fight again")
# inp = input("Enter any alphabat from string: \nm,q,d,z,j for right \nw,p,b,s,t for left \nEnter: ")
# inp = inp.lower()
# String_fight(inp)

