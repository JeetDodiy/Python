import random
import string
import json
from pathlib import Path
class Bank:
    dataBase = 'data.json'
    data = []
    try:
        if Path(dataBase).exists():
            with open(dataBase) as fs:
                data = json.loads(fs.read())
        else:
            print("No existing database found. Starting fresh.")
    except Exception as err:
        print(f"a Error Ocurd : {err}")
    @staticmethod
    def update():
        with open(Bank.dataBase,'w') as fs:
            fs.write(json.dumps(Bank.data))
    @classmethod
    def __accountNumGenerater(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits,k= 3)
        spchar = random.choices("!@#$%^&*",k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def createAccount(self):
        info = {
            "name": input("Insert Your name:"),
            "age": int(input("Enter your Age:")),
            "email": input("Entr Your Email:"),
            "pin":int(input("Eneter Your Pin:")),
            "account_no.": Bank.__accountNumGenerater(),
            "blance": 0
        }
        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("Sorry you can't Open the Acount in Bank")
        else:
            print("Your Account has Bin Created sucsess fuly")
            for i in info:
                print(f" {i} : {info[i]}")
            print("Pliss not doun the account number")
            Bank.data.append(info)
            Bank.update()
    def depositMoney(self):
        accNumber = input("Enter your Bank Account Number:")
        accPin = int(input("Enter your Bank Account Pin:"))
        userData = [i for i in Bank.data if i['account_no.'] == accNumber and i['pin'] == accPin]
        
        if userData == False:
            print("your Account is not in the Bank")
        else:
            ammount = int(input("Enset your Ammouunt for Diposit:"))
            if ammount > 10000 or 0 > ammount:
                print("You can not diposit your mony bicos your ammount is above 10,000 and lover 0")
            else:
                userData[0]['blance'] += ammount
                Bank.update()
                
    def widrow(self):
        accnumber = input("Enter your Account number:")
        pinnum = int(input("enter your Pin:"))
        userdata = [i for i in Bank.data if i['account_no.'] == accnumber and i['pin'] == pinnum]
        if userdata == False:
            print("your account was not in Bank ")
        else:
            ammount = int(input("Enter your Widrol Amount:"))
            if ammount > 10000 or 0> ammount:
                print("your Ammount was above 10,000 or lesthan 0 thats why you can't widrow")
            else:
                if userdata[0]['blance'] < ammount:
                        print(f"you can not Widrow ammount gretar than you Bank balence :{userdata[0]['blance']}")
                else:
                    userdata[0]['blance'] -= ammount
                    print(f'Your Widrow was sacses now your blance was :{userdata[0]['blance']}')
                    Bank.update()
    def Details(self):
        accnumber = input("enter your Account number :")
        accpin = int(input("Enter your Account Pin:"))
        userdata = [i for i in Bank.data if i['account_no.'] == accnumber and i['pin'] == accpin]
        if userdata == False:
            print("Your Bank account was not in Bank")
        else:
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")
                
    def updatedata(self):
        accnumber = input("Enter your Account numebr")
        accpin = int(input("Enter your Account pin:"))
        userdata = [i for i in Bank.data if i['account_no.'] == accnumber and i['pin'] == accpin]
        if userdata == False:
            print("Your account is not in Bank")
        else:
            print("you can't chang the Age , Account number and Blance\n")
            newDiteal = {
                "name" : input("Enter your New name:"),
                "email": input("Enter your New email Id:"),
                "pin" : input("enter your New pin:")
            }
            if newDiteal["name"] == "":
                newDiteal["name"] = userdata[0]['name']
            if newDiteal["email"] == "":
                newDiteal["email"] = userdata[0]['email']
            if newDiteal["pin"] == "":
                newDiteal["pin"] = userdata[0]['pin']
                
            newDiteal["age"] = userdata[0]['age']
            newDiteal["account_no."] = userdata[0]['account_no.']
            newDiteal["blance"] = userdata[0]['blance']
            
            if type(newDiteal["pin"]) == str:
                newDiteal["pin"] = int(newDiteal["pin"])
            for i in newDiteal:
                if newDiteal[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newDiteal[i]
            Bank.update()
            print("Ditails update sucsessfully ")      
    def deletacc(self):
        accnumber = input("Eter your Bank Account numbr :")
        accpin = int(input("Enter your Bank Acount pin"))
        userdata = [i for i in Bank.data if i['account_no.'] == accnumber and i['pin'] == accpin]
        if userdata == False:
            print("your bank Deteail is unavelebal")
        else:
            check = input("Press Y to conform delet Account and Press N to don't delet account:")
            if check == 'n' or check == "N":
                print("Ok You Don't Want to Delet your Accoutn:")
            elif check == "y" or check == "Y":
                print("All write you want to delet your Account:")
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                Bank.update()  
            
            
user = Bank()
print("Press 1 to create acount")
print("Press 2 to Dipositing the money in the Bank")
print("Press 3 to Widrow the money")
print("Press 4 to Details")
print("Press 5 to Update the Details")
print("Press 6 to Delet the Account")
print("Press 7 to Exit")


while True:
    try:
        check = int(input("Enter your choice: "))
        if check == 1:
            user.createAccount()

        if check == 2:
            user.depositMoney()

        if check == 3:
            user.widrow()

        if check == 4:
            user.Details()

        if check == 5:
            user.updatedata()

        if check == 6:
            user.deletacc()
        if check == 7 :
            print("Thank you for visiting the Bank")
            break
    except Exception as err:
        print(f"Error as :{err}")