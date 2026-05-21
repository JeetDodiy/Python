class Constructor_Demo:
    # The __init__ method acts as a constructor and calld as 
    # Bunder method
    #  the init use as class constractor 
    def __init__(self,add):
        self.add = add
    def cons(self,name,age,number):
        print(f"name : {name} , Age : {age} , Number : {number}, Addres : {self.add}")


co = Constructor_Demo("Rajkot")
co.cons("Jeet", 18, 454585977)