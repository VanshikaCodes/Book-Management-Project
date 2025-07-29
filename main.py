import json
import random
import string
from pathlib import Path

 

class Bank:
    database = 'Bank Mangement Project\data.json'
    data = []
    
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("File not exists")
    except Exception as err:
        print(f"Exception occoured as {err}")


    def __update():
        try:
            with open(Bank.database, "w") as fs:
                json.dump(Bank.data, fs, indent = 4)
                print("Data written to JSON file.")
        except Exception as e:
            print(f"Error updating file: {e}")

    @classmethod 
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits,k = 3)
        spchar = random.choices("#@%^*!$",k = 3)
        id = alpha = num + spchar
        random.shuffle(id)
        return "".join(id)

    def CreateAccount(self):

        info = {
            "name" : input("Enter your name: "),
            "age" : int(input("Enter your age: ")),
            "email" : input("Enter your email: "),
            "pin" : int(input("Enter your pin: ")),
            "accountNo" : Bank.__accountgenerate(),
            "bankBalance" : 0
        }
        if(info['age']<18 or len(str(info["pin"]))!= 4):
            print("You can't create an account")
        else:
            print("Account has been created successfully")
        for i in info:
            print(f"{i} : {info[i]}")

        print("Please note down all your details!")
        Bank.data.append(info)
        Bank.__update()


    def depositMoney(self):
        try:
            accNum = input("Enter your account number: ")
            pinNum = int(input("Enter your pin: "))

            userdata = [i for i in Bank.data if i["accountNo"] == accNum and i["pin"] == pinNum]

            if userdata == False:
                print("Data don't exists")
            else:
                amount = int(input("Enter the amount that you want to submit: "))
                userdata[0]["bankBalance"] += amount
                print("Amount updated successfully!!")
                Bank.__update()
        except Exception as err:
            print(f"Excecption found as {err}")



    def withdrawMoney(self):
        try:
            accNum = input("Enter your account number: ")
            pinNum = int(input("Enter your pin number: "))

            userdata = [i for i in Bank.data if i["accountNo"] == accNum and i["pin"] == pinNum]

            if(userdata == False):
                print("No such data found!")
            else:
                amount = int(input("Enter the amount that you want to withdraw: "))
                if userdata[0]["bankBalance"] > amount:
                    userdata[0]["bankBalance"] -= amount
                    Bank.__update()
                    print("Withdrawl successful!")
                else:
                    print("Amount is greater than the money available")
        except Exception as err:
            print(f"Excecption found as {err}")


    def details(self):
        try:
            accNum = input("Enter your account number: ")
            pinNum = int(input("Enter your pin number: "))

            userdata = [i for i in Bank.data if i["accountNo"] == accNum and i["pin"] == pinNum]

            print("Your details are: \n \n \n")
            if userdata == False:
                print("No such data found!")
            else:
                for index in (userdata[0]):
                    print(f"{index}: {userdata[0][index]}")
        except Exception as err:
            print(f"Excecption found as {err}")


    def updateData(self):
        try:
            accNum = input("Enter your account number: ")
            pinNum = int(input("Enter your pin number: "))

            userdata = [i for i in Bank.data if i["accountNo"] == accNum and i["pin"] == pinNum]
            if userdata == False:
                print("No such data found!")
            else:
                print(user.details())
                print("Press 1 for changing your name")
                print("Press 2 for changing your email")
                print("Press 3 for updating your pin")

                check = int(input("Enter your response: "))

                if check == 1:
                    name = input("Enter the updated name: ")
                    userdata[0]["name"] = name
                    Bank.__update()
                    print("Name changed successfully!")

                if check == 2:
                    email = input("Enter the updated email: ")
                    userdata[0]["email"] = email
                    Bank.__update()
                    print("Email changed successfully!")

                if check == 3:
                    pin = input("Enter the updated pin: ")
                    userdata[0]["pin"] = pin
                    Bank.__update()
                    print("Pin changed successfully!")

        except Exception as err:
            print(f"Excecption found as {err}")

    def Delete(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin aswell "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("sorry no such data exist ")
        else:
            check = input("press y if you actually want to delete the account or press n")
            if check == 'n' or check == "N":
                print("bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("account deleted successfully ")
                Bank.__update()


user = Bank()

print("Press 1 for creating an account")
print("Press 2 for depositing in an account")
print("Press 3 for withdrawing ")
print("Press 4 for Details")
print("Press 5 for Updates in  an account")
print("Press 6 for deleting  an account")

check = int(input("Enter your response: "))

if check == 1:
    user.CreateAccount()

if check == 2:
    user.depositMoney()

if check == 3:
    user.withdrawMoney()

if check == 4:
    user.details()

if check == 5:
    user.updateData()

if check == 6:
    user.Delete()
