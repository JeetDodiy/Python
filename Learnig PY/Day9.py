# the error not acurs else block run automaticly
# a =10
# b = int(input("Enter number :"))
# try:
#     print(a/b)
# except Exception as err:
#     print(f"you have error :{err}")
# else:
#     print("good Boy")
# print("vary good")

#the Finlly block all ways run no mmater what. the try block throw the error and except the error 
# a =10
# b = int(input("Enter number :"))
# try:
#     print(a/b)
# except Exception as err:
#     print(f"you have error :{err}")
# else:
#     print("good Boy")
# finally:
#     print("I run no mater what")
# print("vary good")

# raise Error 
# we create on Exption Error using raise function
# try:
#     age = int(input("Eter your Age :"))
#     if age < 10 or age > 18:
#         raise ValueError("you not in in boys grup")
#     else:
#         print("yaa boy in the grup")
# except Exception as err:
#     print(f"boy Error aavel he:{err}")
# print("OHO Boy grup not exist")

#---------------------File handling-----------------------------------------------
# In python File handling have 4 type of mode 
# (1) r = REad mode this only use to read file and the deflot mde of opne was 'r'
# (2) w = Write mode this mode can create a new file and over write the curent file
# (3) a = Apend mode this mode also create a new file and add new tex in olde file
# (4) x =       mode this mode use to only create file 
#----------------------------------------------------------------------------------

# Open File [r mode]
# p = open(r"E:\jeetPython\Learnig PY\Day1.py")
# print(p.read())

# w = open("create_file_w.tex",'w')
# w.write("The file ceate by W mode")
# w.close()

# w = open("create_file_w.tex",'w')
# w.write("Rewrite the fil using W mode")
# w.close()

# create file and addthe text usig the apend mode
# a = open("create_file_a.tex",'a')
# a.write(' halelu ua hii this')
# a.close()

# a = open("create_file_a.tex",'a')
# a.write(' ,Add tex usinf A mode')
# a.close()

# create file using  x mode
# x = open("create_file_x.tex",'x')
# x.close()

#----------------------------------------------------------------------------------

