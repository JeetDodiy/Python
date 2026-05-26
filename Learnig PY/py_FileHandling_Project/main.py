from pathlib import Path
import os
def checktheFile():
    path = Path('')
    item = list(path.rglob('*'))
    for i, item in enumerate(item):
        print(f"{i+1} : {item}")

def createFile():
    try:
        checktheFile()
        name = input("Enter your file name:")
        p = Path(name)
        with open(p,'w') as fs :
            data = input("Eter your Text")
            fs.write(data)
        print("your file was Created")
    except Exception as err:
        print(f'Error has : {err}')


def readFile():
    try:
        checktheFile()
        name = input("Enert your chois :")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("Read secsfuly")
        else:
            print("your file not exist")
    except Exception as err:
        print(f"your Error : {err}")

def updateFile():
    checktheFile()
    try:
        name = input("enset ypur file name for update:")
        p = Path(name)
        if p.exists and p.is_file:
            print("Enterr 1 to update file name:")
            print("Enterr 2 to Overwrite file:")
            print("Enterr 3 to  Apend sum text to file:")
            choics = int(input("Enter your chois:"))
            if choics == 1:
                name2 = input("Enter your New name for File:")
                p2 = Path(name2)
                p.rename(p2)
            if choics == 2:
                with open(p,'w') as fs:
                    data = input("Entr your Data:")
                    fs.write(data)
            if choics == 3:
                with open(p,'a') as fs:
                    data = input(" Add the Data in file:")
                    fs.write(data)
    except Exception as err:
        print(f"Exception is :{err}")

def deletFile():
    checktheFile()
    try:
        name = input("Enter file name for Delet file: ")
        p = Path(name)
        if p.exists and p.is_file:
            os.remove(p)
        print("file Dilet scsefuliy")
    except Exception as err:
        print(f"Your Exption is :{err}")

for i in range(10):
    print("Enter 1 to create File :")
    print("Enter 2 to read File :")
    print("Enter 3 to Update File :")
    print("Enter 4 to Delete File :")
    check = int(input("Enter the number: "))

    if check == 1:
        createFile()
    if check == 2:
        readFile()
    if check == 3:
        updateFile()
    if check == 4:
        deletFile()