from createAccount import CreateAccount
from checkBalance import CheckBalance
from withdrawmoney import WithdrawMoney
from depositAmount import DepositAmount
from deleteAccount import DeleteAccount
from errorHandling import ErrorFinder
import requests
import time







create_account = CreateAccount()
check_balance = CheckBalance()
withdraw_amount = WithdrawMoney()
deposit_money = DepositAmount()
delete_account = DeleteAccount()
error=ErrorFinder()


data:str

response = requests.get(
    "https://api.sheety.co/162ce777f84396a7d41f65fbc4caef28/userData/sheet1"
)
response=error.errorFinder(response)

if response.ok:
    data = response.json()["sheet1"]


def checkAccountNumber():
    account = int(input("Enter Your Account Number:-  "))
    
    for row in range(len(data)):
       
        if account == data[row]["accountNo"]:
            pin=int(input("Please Enter Your 4 digit Security Pin for authentication:-  "))
            if pin == data[row]["securityPin"]:
                    return row
            break
    else:
        print("Your Account No/ Security Pin  is Incorrect.Please Try again Later")
        return -1


ourServices = """\n
                Withdraw(money)\n
                Deposit(money)\n
                Open(account)\n
                Delete(account)\n
                Check(balance)\n
                Exit(Cancel)"""
Open = True
while Open:
    user_choice = input(
        f"Hello Sir 👋 \n Which service do you want to use{ourServices}:-\n"
    ).title()

    if user_choice == "Open":
        print("Please Open Your account By providing these Details:- ")
        create_account.open_account()

    elif user_choice == "Withdraw":
        row = checkAccountNumber()
        
        if row != -1:
            withdraw_amount.withdraw(row)
            time.sleep(2)

    elif user_choice == "Deposit":
        row = checkAccountNumber()
        if row != -1:

            deposit_money.deposit(row)
            time.sleep(2)

    elif user_choice == "Check":
        row = checkAccountNumber()
        if row != -1:

            check_balance.show_balance(row)
            time.sleep(2)

    elif user_choice == "Delete":
        row = checkAccountNumber()
        if row != -1:

            delete_account.deleted_account(row)
            time.sleep(2)
    elif user_choice == "Exit":
        Open = False
        

    else:
        print(
            "You are choosing Wrong Option or typo error Please insert option correctly. "
        )
        time.sleep(2)
