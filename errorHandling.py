import requests

class ErrorFinder:
    
    def errorFinder(self,response):
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # e.g., 404 Not Found
        except requests.exceptions.ConnectionError as conn_err:
            print(f'Connection error occurred: {conn_err}')
        except requests.exceptions.Timeout as timeout_err:
            print(f'Timeout error occurred: {timeout_err}')
        except requests.exceptions.RequestException as req_err:
            print(f'An error occurred: {req_err}')
        return response