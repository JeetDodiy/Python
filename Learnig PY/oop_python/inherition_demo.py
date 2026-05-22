#-----------------------------------------------------------------------------------------------------------------------
#  In python 4 type of Inherition was use 
# (1) Singal Inherition
# (2) Maltipal Inherition
# (3) Malti leval Inherition
# (4) hairarchical Inherition
#-----------------------------------------------------------------------------------------------------------------------


# class Inherition_Demo:
#     def parent(self):
#         print("this is call as parent class")

#     def parent_con(self,age):
#         print(f"This Parent called Age : {age}")
# class Chaild(Inherition_Demo):
#     def chaild(self):
#         print("this is Chaild method")

# ch = Chaild()
# ch.parent()
# ch.parent_con(45)
# ch.chaild()

# class Compny:
#     def __init__(self,name):
#         self.name = name
#     def show(self):
#         print(f"The Compny Name was :{self.name}")
# class Car_name(Compny):
#     def __init__(self, name,carName):
#         super().__init__(name)
#         self.carName = carName
#     def show(self):
#         print(f"The Car Compny name was : {self.name} , The car Name was : {self.carName}")

# Were one methode overwrite by chaild class the only option to acces perent clss method was crete objecet of perent class
# cm = Compny(name="Toyata")
# cm.show()
# cn = Car_name("honda","HondaCity")
# cn.show()

# Maltiple Inheritation
# class Human:
#     name1 = "jeet"
# class Age:
#     age = "41"
# class Marge(Human,Age):
#     pass

# one = Marge()
# print(one.age,one.name1)

#-----------------------------------------------------------------------------------------------------------------------
##    In maltipal Inheritation Were Two class was Inheritan by one class and Both of tham was ask to sum Value that time, 
##  the chaild only ask one value of oder way like here the First Class was Human was Give in Marge class,
##that was onyl ask the Human class Argument.  
#-----------------------------------------------------------------------------------------------------------------------

# class Human:
#     def __init__(self,name):
#         self.name = name
# class Age:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
# class Marge(Human,Age):
#     pass

# m = Marge("Jeet")

#-----------------------------------------------------------------------------------------------------------------------
## In this Statment The Age Class was First That's Way the Name and Age Both Paremitar was ask by instans
#-----------------------------------------------------------------------------------------------------------------------
# class Marge(Age,Human):
#     pass
# m = Marge("jeet" , 25)

#-----------------------------------------------------------------------------------------------------------------------
## Maltileval Inheritation 
## This type of inheritation use by one class to anethor class aske there acoding value useing Malti leval Inherition 
#-----------------------------------------------------------------------------------------------------------------------
# class Human:
#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender

# class Body(Human):
#     def __init__(self, name, gender,age):
#         super().__init__(name, gender)
#         self.age = age
# class Addres(Body):
#     def __init__(self, name, gender, age,add):
#         super().__init__(name, gender, age)
#         self.add = add

# ad = Addres("jeet","M",28,"Gujrat")
# print(f"Name : {ad.name} , Gender : {ad.gender} , Age :{ad.age} , Addres : {ad.add}")


#-----------------------------------------------------------------------------------------------------------------------
# This Inherition called HairarChikal Inheritaion 
# use for one class constracter use maltipal Class 
#-----------------------------------------------------------------------------------------------------------------------


# class Human:
#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender

# class Body(Human):
#     pass
# class Addres(Human):
#     pass

# bd = Body("Dixit" , "M")
# ad = Addres("jeet","M")
# print(f"Name : {ad.name} , Gender : {ad.gender}")
# print(f"Name : {bd.name} , Gender : {bd.gender}")

#-----------------------------------------------------------------------------------------------------------------------
