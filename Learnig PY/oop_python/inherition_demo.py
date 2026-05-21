class Inherition_Demo:
    def parent(self):
        print("this is call as parent class")

    def parent_con(self,age):
        print(f"This Parent called Age : {age}")
class Chaild(Inherition_Demo):
    def chaild(self):
        print("this is Chaild method")

ch = Chaild()
ch.parent()
ch.parent_con(45)
ch.chaild()