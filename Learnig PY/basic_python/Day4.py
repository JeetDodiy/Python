#While loop Stamant 
# a = 1
# while a <= 10:
#     print(a)
#     a = a + 1

# a = 567
# while a > 0:
#     print(a % 10)
#     a = a //10

#---------------------------------------------------------------------------------------

#print Revars value
# a = int(input('enter number :-'))
# rev = 0
# while a > 0:
#     rev = rev * 10  + a % 10
#     a = a //10
# print(rev)

#---------------------------------------------------------------------------------------

#check pelibrom number 
# a = int(input('Enter number for check Pelinbrom number :-'))
# b = a
# rev = 0
# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10
# if rev == b:
#     print(f'your number is pelindrom :{b} : {rev}')
# else:
#     print(f'your number is not pelindrom :{b} : {rev}')

#---------------------------------------------------------------------------------------

#Choos random number
# import random
# import os
# gess = int(input("Enter randum gess number beetwen 1 to 10:"))
# rean = random.randint(1,10)
# while True:
#     if gess == rean:
#         print("your are write ")
#         break
#     else:
#         print("GAME OVER!")
#         # Safe prank effect
#     os.system("cls")  # clears screen on Windows
    
#     print("""
#     *********************************
#     *   SYSTEM FAILURE DETECTED!    *
#     *********************************
#     """)

#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

# New Chapter 
# Functions

#---------------------------------------------------------------------------------------

# def sum(a,b):
#     print(f"The sum was :{a+b}")
# sum(10,12) 
# def info(name,age):
#     print(f"Your name was :{name} and yoour age is :{age}")
# a = input('enter your name:')
# b = int(input('enter your age:'))
# info(a,b)

#---------------------------------------------------------------------------------------

#check pelindrom
# def checkPali(a):
#     rev = ""
#     for i in range(len(a)-1,-1,-1):
#         rev = rev + a[i]
#     if rev == a:
#         print("this name was pelindrom")
#     else:
#         print("this name was not pelindrom")
# name = input("Ente name for check pelindrom:")
# checkPali(name)

# #Starting arry
# a = 12 ,45, 45, 84
# print(type(a))