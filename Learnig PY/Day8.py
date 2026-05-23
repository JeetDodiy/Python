#-----------------------------------------------------------------------------------------------------------------------

#dist get method 
a = {10:12,20:"jeet",30:45,45:True,48:20}

# b = a.get(48)
# print(b)

# b = a.items()
# print(b)

# b = a.pop(20)
# print(b)

# b = a.popitem(20)
# print(b)

# b = {60:12,25:30,20:20,30:28}

# c = b|a
# print(c)

# sum = 0
# for i in b:
#     sum = sum + b[i]

# print(sum)

#-----------------------------------------------------------------------------------------------------------------------

# create List counter using dict

# a = [1,1,2,3,2,5,5,6,3,3,2,1,4,4,4,5,6]
# dict = {}
# for i in a:
#     if i in dict.keys():
#         dict[i] += 1
#     else:
# dict.keys() not in dict the dict was create ne key and add 1 using this itrection
#         dict[i] = 1
# print(dict)

#-----------------------------------------------------------------------------------------------------------------------

# sum of two dict 

# a = {10:20,20:30,30:45,50:33,45:55}
# b = {30:20,58:22,85:20,50:20,89:52}

# for i in b :
#     if i in a.keys():
#         a[i] += b[i]
#     else:
#         a[i] = b[i]
# print(a)
#-----------------------------------------------------------------------------------------------------------------------

#Exception hanling

# a =10
# b = int(input("Enter number :"))
# print(a/b)

# -------------------------------------------------------IPM------------------------------------------
#                                                                                                    |
#Where use in put 0 the code was clased end give error called :ZeroDivisionError: division by zero   |
# This is called Excption and using try and except block we handel this type of error                |
#                                                                                                    |
# ----------------------------------------------------------------------------------------------------

# this way to we except the error for manualy 
# a =10
# b = int(input("Enter number :"))
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("You can not divaid by Zero")
# print("vary good")
#-----------------------------------------------------------------------------------------------------------------------

# this type system autoamaticly cach the error
# a =10
# b = input("Enter number :")
# try:
#     print(a/b)
# except Exception as err:
#     print(f"you have error :{err}")
# print("vary good")