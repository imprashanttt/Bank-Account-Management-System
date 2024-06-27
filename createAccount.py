from errorHandling import ErrorFinder

import random
import requests



error=ErrorFinder()

URL = "https://api.sheety.co/162ce777f84396a7d41f65fbc4caef28/userData/sheet1"

HEADER = {"Content-Type": "application/json"}


class CreateAccount:
    def __init__(self):
        self.name: str
        self.accountType: str
        self.aadhar_number: int
        self.pan_number: str
        self.current_balance = 500
        self.accountNumber: self.accountNumber = random.randint(
            2345948484848, 5234983883838
        )
        self.pin = random.randint(1000, 9999)

    def open_account(self):
        self.name = input("Enter your name:- ")
        self.accountType = input(
            "Enter Which Account do you want to open(Saving/Current):- "
        ).title()
        self.aadhar_number = input("Enter your Aadhar number:- ")
        self.pan_number = input("Enter your Pan card number:- ")
        self.print_data()

    def print_data(self):
        print(
            f"Your Account Is opened Here is Your Account Details:- \n ..........Prashant Co-Operative Bank..........\n "
        )
        print(f"Account Number:-  {self.accountNumber}\nTransaction_Pin:-  {self.pin}")
        print(
            f"Personal Details That you Provided:- \n Name:- {self.name}\n Account Type:- {self.accountType}\n Aadhar Number:- {self.aadhar_number}\n Pan card:- {self.pan_number}"
        )
        self.SaveData()

    def SaveData(self):
        from depositAmount import DepositAmount
        from withdrawmoney import WithdrawMoney

        debitAmount = WithdrawMoney()
        creditAmount = DepositAmount()

        data = {
            "sheet1": {
                "username": self.name,
                "accountNo": self.accountNumber,
                "aadharNo": self.aadhar_number,
                "panNo": self.pan_number,
                "securityPin": self.pin,
                "currentBalance": self.current_balance,
                "debit": debitAmount.amount,
                "credit": creditAmount.amount,
                "accountType": self.accountType,
            }
        }
        
            
        response = requests.post(URL, json=data, headers=HEADER)
        response=error.errorFinder(response=response)
        if response.ok:
            print(response.text)
