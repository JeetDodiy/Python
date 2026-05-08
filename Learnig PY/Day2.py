# In python three type of if statments are here 
# (1) if
# (2) if - else
# (3) if - elif - else (ledar if)

#if - else Statement

# a = 10
# b = 20
# if a == 10:
#     print("a is 10")

# if a  < b:
#     print("a is less than b")
# else:
#     print("B less than a")

# if - elif - else Statement

# if a == 1000:
#     print("a is 1000")
# elif a < b:
#     print("a is less than b")
# else:
#     print("B less than a")

#----------------------------------------------------------------

# using user input to check qundition    

# a = int(input("Enter your number : "))
# if a == 0:
#     print(f"Your number is zero {a}")
# elif a % 2 == 0:
#     print(f"Your number is even {a}")
# else:
#     print(f"Your number is odd {a}")

#----------------------------------------------------------------

# Accept two number from user and wich is greter and print that number 
# a = int(input("Enter your First number : "))
# b = int(input("Enter your second number : "))
# if a > b:
#     print(f" Your First number is greater {a}")

# elif a==b:
#     print(f"Your number are same {a} and {b}")
# else:
#     print(f"Your second number is greater {b}")

#----------------------------------------------------------------

# Accept Gender and replay with SIR or MAM

# gendar = input("Enter your Gendar in M or F : ")

# if gendar == "M" or gendar == "m":
#     print("Hii SIR")
# elif gendar == "F" or gendar == "f":
#     print("Hii MAM")
# else:
#     print("Invalid Gendar")

#----------------------------------------------------------------


# Accept Name and Age to check vote elegibilty or not

# name = input("Eneter oyurr name :- ")
# age = int(input("Ente your Age :- "))
# if age >= 18:
#     print(f"You are {name} Elegibal to vote now you are {age}")

# else:
#      print(f"you are {name} not elegibal for voting your age is {age} you were your age is 18 you can give vote")

#----------------------------------------------------------------

# Accept year and check that was leep year or not

# year = int(input("Enter your Year :-"))
# if year%100 == 0 and year%400 == 0:
#     print(f"Your given year {year} Was Senchuriy year")
# elif year%100 == 0 and year%4 == 0:
#     print(f"your year was leep year {year}")
# else:
#     print(f"your year was normal year {year}")

#----------------------------------------------------------------

#accept temperature and check cool,good,hot,Very hot,on fire

# temperature = int(input("eter your ctiy temperature :-"))

# if temperature >= 0 and temperature < 10:
#     print(f"your city temperature was cool {temperature}")
# elif temperature >=10 and temperature < 20:
#     print(f"your city temperature was good {temperature}")
# elif temperature >=20 and temperature < 30:
#     print(f"your city temperature was hot {temperature}")  
# elif temperature >=30 and temperature < 40:
#     print(f"your city temperature was very Hot {temperature}")      
# else:
#     print(f"your city temperature is on fire {temperature}")      

#----------------------------------------------------------------
#----------------------------------------------------------------

#Loop Statemant in PY two type of looping statment 
# (1st) For loop
# (2sd) while loop

#(1st) for loop

#----------------------------------------------------------------

# range(Starting point , Ending Point (n-1) , Steps like 1,-1)

# for i in range(1,11,1):
#     print(i)

#----------------------------------------------------------------

#print ting negative number
# for i in range(5,-5,-1):
#     print(i)

#----------------------------------------------------------------

#normal table 
# for i in range(1,11,1):
#     print(f"53 * {i} = {i*53}")

#----------------------------------------------------------------

#table 12 in PY
# for i in range(12,121,12):
#     print(i)

#----------------------------------------------------------------

#Create table using user input
# num = int(input("insert table number you want :- "))
# for i in range(num , num*10+1,num):
#     print(i)

#----------------------------------------------------------------

#cut to
# name = "Dodiya jeet k."
# for i in range(len(name)):
#     print(name[i])