# def decorate(func):
#     def wrapper():
#         print("Hii this is wrrepar")
#         func()
#         print("hii this is with function")
#     return wrapper

# @decorate
# def samosu():
#     print("this is function")

# samosu()

# Argument withh decorate
# def decorate(func):
#     def wrapper(a,b):
#         print("This is Befor Sum")
#         func(a,b)
#         print("This is after sum")
#     return wrapper

# @decorate
# def sum(a,b):
#     print(f"the sum of A and B was : {a + b}")

# sum(45,45)

#-----------------------------------------------------------------------------------------------------------------------
#  in Pyhton sum key words are difrent and Very use full like args

# def sum(a,b):
#     print(f"The sum of A and B was : {a+b}")
# sum(10,20)

#-----------------------------------------------------------------------------------------------------------------------
# this function we re pre difine the argument Number like A or B here only Two arguments the use of args we hane infainit arguments
# Like this we have n number of argumwnts
#-----------------------------------------------------------------------------------------------------------------------

# def sum(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
        
#     print(f" the sum is :{sum}")

# sum(454,54,45,45,45,45)
#-----------------------------------------------------------------------------------------------------------------------
