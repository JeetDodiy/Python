import  json
from pathlib import Path
class Library1:
    library_Databse = "Library_Databse.json"  
    data = []
    
    try:
        if Path(library_Databse).exists():
            with open(library_Databse) as fs:
                data = json.loads(fs.read())
        else:
            print("The not Existt in data base")
    except Exception  as err:
        print(f"Sumthing is Messing :{err}")
    
    @staticmethod
    def update_Database():
        with open(Library1.library_Databse,'w') as fs:
            fs.write(json.dumps(Library1.data))

    def addbook(self):
        addBook = {
            "book_name" : input("Enter Your Book name:"),
            "book_auther" : input("Entrr Auther Name:"),
            "book_code" : int(input("Entr Book Code:"))
        }
        Library1.data.append(addBook)
        Library1.update_Database() 
        print("All is good")
        
    
    
lb = Library1()  
print("Enter 1 to add Book")
print("Enter 2 to Dain Info of Books")
print("Enter 3 to Update Book")
print("Enter 4 to Delet Book")
print("Enter 5 to Close the Library:")
check = int(input("Enter Your Choice :"))

if check == 1:
    lb.addbook()

    
    