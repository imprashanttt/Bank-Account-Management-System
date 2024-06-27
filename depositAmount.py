from errorHandling import ErrorFinder

import requests


error = ErrorFinder()


class DepositAmount:
    def __init__(self) -> None:
        self.amount = 0

    def deposit(self, row):

        response = requests.get(
            "https://api.sheety.co/162ce777f84396a7d41f65fbc4caef28/userData/sheet1"
        )
        response = error.errorFinder(response)
        if response.ok:
            data = response.json()["sheet1"][row]
            current_balance = data["currentBalance"]
            ObjectId = data["id"]

            self.amount = int(input("Enter how much amount do you want to deposit:- "))
            current_balance = current_balance + self.amount
            print(
                f"Your Amount Is Credited Successfully. \nYour current Balance is :- {current_balance}"
            )

            data_value = {
                "sheet1": {
                    "currentBalance": current_balance,
                    "credit": self.amount,
                }
            }

            Header = {"Content-Type": "application/json"}

            response = requests.put(
                f"https://api.sheety.co/162ce777f84396a7d41f65fbc4caef28/userData/sheet1/{ObjectId}",
                json=data_value,
                headers=Header,
            )

            response = error.errorFinder(response)

            if response.ok:
                print(response.text)
