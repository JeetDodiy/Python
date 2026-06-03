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
        print("Book Add sucses fully")
        
    def library_all_book_info(self):
        for i in range(len(Library1.data)):
            print(f"\nBook Number : {i+1}")
            print(f"Book name : {Library1.data[i]["book_name"]}")
            print(f"Book Auther : {Library1.data[i]["book_auther"]}")
            print(f"Book Code : {Library1.data[i]["book_code"]}")
    
    def search_book(self):
        book_Name = input("Enter Book Name for search:")
        book_Info = [i for i in Library1.data if i["book_name"] == book_Name]
        if not book_Info:
            print("Your Book is not in Library")
        else:
            for i in book_Info[0]:
                print(f"\n{i} : {book_Info[0][i]}")
                
    def update_book(self):
        check_book =input("Enter Your book name For update :")
        print("\nYou Can Onliy Update Book auther Name")
        book_info = [i for i in Library1.data if i["book_name"] == check_book]
        if not book_info:
            print("your Book in not in Library")
        else:
            book_Auther = input("Entr New Auther Of book:")
            
            if book_Auther == "":
                book_Auther = book_info[0]["book_auther"]
            else:
                book_info[0]["book_auther"] = book_Auther
                Library1.update_Database()    
                print("Update successfully Update")
            
            
        
        
    
lb = Library1()  
print("Enter 1 to add Book")
print("Enter 2 to All Book Info")
print("Enter 3 to Search Book")
print("Enter 4 to Update Book")
print("Enter 5 to Delet Book")
print("Enter 6 to Close the Library:")
check = int(input("Enter Your Choice :"))

if check == 1:
    lb.addbook()

if check == 2:
    lb.library_all_book_info()

if check == 3:
    lb.search_book()

if check == 4:
    lb.update_book()
    