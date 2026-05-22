# In Polymorphism mins one name many use 

# class Human:
#     def show(self):
#         print("This is Human Class Method")
# class Pepol(Human):
    
#     def show(self):
#         print("This is pepol class Method")
# p = Pepol()
# p.show()

#-----------------------------------------------------------------------------------------------------------------------
# In python Three type of Parmition are avlabel 
# (1) Public    :   a
# (2) Protected :  _a
# (3) Privet    : __a
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
# the Public or Protected was same type in pyrhon that was use anywere and any can use.
#-----------------------------------------------------------------------------------------------------------------------
# class Compny:
#     name = "Ford" #Public
#     _car = "Musteng" #Protected
#     def show(self):
#         print(f"The Comny name was : {Compny.name} , Car Was : {Compny._car} ")

# class Type:
#     pass
# c = Compny()
# c.show()
# Compny.name = "BMW" # public
# Compny._car = "M530" #Protected
# c.show()
#-----------------------------------------------------------------------------------------------------------------------


# Protected

# class Compny:
#     __name = "Ford"
#     def show(self):
#         Compny.__name = "jeetes"
#         print(Compny.__name)
    
#         das = ""
#     def sa(self):
#         Compny.__name = Compny.das
#         print(Compny.__name)

# c = Compny()
# c.show()
# Compny.das = "Marchadish"
# c.sa()