from errorHandling import ErrorFinder
import requests


error=ErrorFinder()

class DeleteAccount:
    def __init__(self):
        self.ObjectId: int

    def deleted_account(self, row):
        
            response = requests.get(
                "https://api.sheety.co/162ce777f84396a7d41f65fbc4caef28/userData/sheet1"
            )
            response=error.errorFinder(response)
            if response.ok:
        
                data=response.json()["sheet1"][row]
                ObjectId = data["id"]
                
                response = requests.delete(
                        f"https://api.sheety.co/162ce777f84396a7d41f65fbc4caef28/userData/sheet1/{ObjectId}"
                    )
                response=error.errorFinder(response)
                if response.ok:
                    print(response.text)
                    
                    
                    print(f"{data['username']} account Deleted Successfully")
