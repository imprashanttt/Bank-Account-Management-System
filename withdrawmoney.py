from errorHandling import ErrorFinder
import requests

error = ErrorFinder()


class WithdrawMoney:
    def __init__(self) -> None:
        self.amount = 0

    def withdraw(self, rowNo):

        response = requests.get(
            "https://api.sheety.co/162ce777f84396a7d41f65fbc4caef28/userData/sheet1"
        )
        response = error.errorFinder(response)

        if response.ok:
            data = response.json()["sheet1"][rowNo]
            current_balance = data["currentBalance"]
            ObjectId = data["id"]
            self.amount = int(input("Enter how much amount do you want to Withdraw:- "))
            if self.amount < current_balance:
                current_balance = current_balance - self.amount
                print(
                    f"{data['username']} Amount Is debited Successfully. \nYour current Balance is :- {current_balance}"
                )
            else:
                print("You have not insufficient Amount in your account")

            data_value = {
                "sheet1": {
                    "currentBalance": current_balance,
                    "debit": self.amount,
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
