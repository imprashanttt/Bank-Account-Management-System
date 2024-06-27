from errorHandling import ErrorFinder

import requests


error=ErrorFinder()



class CheckBalance:
    def __init__(self):

        self.user_pin: int
        self.currentBalance: int

    def show_balance(self, row):
            response = requests.get(
                "https://api.sheety.co/162ce777f84396a7d41f65fbc4caef28/userData/sheet1"
            )
            response=error.errorFinder(response)
            if response.ok:
                data=response.json()["sheet1"][row]
                security_pin = data['securityPin']
                current_balance = data["currentBalance"]
                self.user_pin = security_pin
                self.currentBalance = current_balance
                if self.user_pin == int(input("Enter Your  Security Pin again for your account Security : ")):
                    print(f'{data['username'] }Current Balance is :- {self.currentBalance}')
                else:
                    print("Details Didn't Match with your security Pin")
