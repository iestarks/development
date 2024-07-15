import requests
from requests.auth import HTTPBasicAuth
import getpass

# ServiceNow instance details
instance_url = "https://dev249066.service-now.com"
api_endpoint = "/api/now/table/sys_user"
url = f"{instance_url}{api_endpoint}"

# Authentication details
username = "admin"
# Prompt the user for a password without echoing
password = getpass.getpass("Enter your password: ")

print("Password entered securely.")

# New user details
user_data = {
    "user_name": "Pud",
    "first_name": "Puddy",
    "last_name": "Starks",
    "email": "poptart@gmail.com",
    "password": "Puddypop!",
    # Add any other necessary fields
}

# Make the POST request to create a new user
response = requests.post(url, auth=HTTPBasicAuth(username, password), json=user_data)

# Check the response
if response.status_code == 201:
    print("User created successfully.")
else:
    print(f"Failed to create user. Status code: {response.status_code}, Detail: {response.text}")