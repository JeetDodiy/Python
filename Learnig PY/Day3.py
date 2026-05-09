# for loop with break , continue and else

#----------------------------------------------------------------
#                  break  
# for i in range(1,11):
#     if i == 7:
#         break
#     print(i)

#----------------------------------------------------------------
#                 Continu
# for i in range(1,16):
#     if i == 11:
#         continue
#     print(i)

#----------------------------------------------------------------

#                 else
#in python else statment all so use with for loop where the break statment not in use 
# the else statmet auto maticly called 

# for i in range(1,21):
#     if i == 22:
#         print('break in use')
#         break
#     print(i)
# else:
#     print("Break no in use")

#----------------------------------------------------------------

# a = int(input('Enter a number:- '))
# for i in range(a):
#     print('Hello world!')

#----------------------------------------------------------------

# n = int(input('Enter your number :='))
# for i in range(n):
#     print(i+1)

#----------------------------------------------------------------

# n = int(input('Enter number :-'))
# for i in range(n,0,-1):
#     print(i)

#----------------------------------------------------------------

# n = int(input('Entter one number you want print Table :'))
# for i in range(n,n*10+1,n):
#     print(i)

#----------------------------------------------------------------

# n = int(input("enter a number :"))
# sum = 1
# for i in range(1,n+1):
#     sum = sum * i
#     print(f"{sum}")

#----------------------------------------------------------------

# n = int(input('Enter number to ocheck fact :'))
# for i in range(1, n+1 ):
#     if(n%i == 0):
#         print(i) 

#----------------------------------------------------------------

# n = int(input('Enter number to check fact :'))
# sum = 0
# for i in range(1, n ):
#     if n%i == 0:
#         sum = sum+i
# if n == sum:
#             print(f'this is perfact number {n} sum : {sum}')
# else:
#     print('this not pract number')

#----------------------------------------------------------------

# n = int(input('Enter number to check prime num. :'))
# sum = 0
# for i in range(1, n+1 ):
#     if n%i == 0:
#         sum = sum+1
# if sum == 2 or sum == 1:
#             print(f'this is prime number {n}')
# else:
#     print('this not pract number') 

#----------------------------------------------------------------

# name = input('Enter your name :')
# re = ""
# for i in range(len(name)-1,-1,-1):
#     re = re + name[i]
# print(re)    

#----------------------------------------------------------------

# n = input("Enter your value to check pelidrom :")
# b = ""
# for i in range(len(n)-1,-1,-1):
#     b = b + n[i]
# if n == b:
#     print(f"Your is pelindrom ")
# else:
#     print('Your was not pelindrom')

#----------------------------------------------------------------

# name = input("enter your string :")
# char = 0
# spcahr = 0
# digits = 0
# for i in name:
#     if i.isdigit():
#         digits += 1
#     elif i.isalpha():
#         char += 1
#     else:
#         spcahr += 1
# print(f"your string Digitss count is {digits}\n your string Special char count is {spcahr} \n your string char count is {char} ")    