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
            
user = Bank()
print("Press 1 to create acount")
print("Press 2 to Dipositing the money in the Bank")
print("Press 3 to Widrow the money")
print("Press 4 to Details")
print("Press 5 to Update the Details")
print("Press 6 to Delet the Account")

check = int(input("Enter your choice: "))
if check == 1:
    user.createAccount()
