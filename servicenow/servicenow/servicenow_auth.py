import requests
from requests.auth import HTTPBasicAuth
import getpass


instance = "https://dev249066.service-now.com/api/now/table/incident" 
username = "admin"  # Use your own username
password = "dv0%KokS1*DV"  # Use your own password

# def service_auth():
#     # Attempt to authenticate to the ServiceNow instance
#     response = requests.get(instance, auth=HTTPBasicAuth(username, password))
    
#     # Check if the authentication was successful
#     if response.status_code == 200:
#         print("Authentication successful!")
#     else:
#         print(f"Authentication failed! Status code: {response.status_code}")
    
#     return response

# # Call the function
# response = service_auth()

# # Prompt the user for a password without echoing
# # password = getpass.getpass("Enter your password: ")
# #print("Password entered securely.")


